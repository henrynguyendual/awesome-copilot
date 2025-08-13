---
applyTo: "**/*.Tests.ps1"
description: "Các phương pháp hay nhất để kiểm thử PowerShell Pester dựa trên quy ước của Pester v5"
---

# Hướng dẫn Kiểm thử PowerShell Pester v5

Hướng dẫn này cung cấp các chỉ dẫn cụ thể cho PowerShell để tạo các bài kiểm thử tự động bằng mô-đun PowerShell Pester v5. Hãy tuân theo các hướng dẫn phát triển cmdlet PowerShell trong [powershell.instructions.md](./powershell.instructions.md) để biết các phương pháp hay nhất về viết kịch bản PowerShell nói chung.

## Đặt tên và Cấu trúc Tệp

- **Quy ước Tệp:** Sử dụng mẫu đặt tên `*.Tests.ps1`
- **Vị trí:** Đặt các tệp kiểm thử bên cạnh mã nguồn được kiểm thử hoặc trong các thư mục dành riêng cho kiểm thử
- **Mẫu Import:** Sử dụng `BeforeAll { . $PSScriptRoot/FunctionName.ps1 }` để nhập các hàm cần kiểm thử
- **Không có mã trực tiếp:** Đặt TẤT CẢ mã nguồn bên trong các khối Pester (`BeforeAll`, `Describe`, `Context`, `It`, v.v.)

## Cấu trúc Phân cấp của Bài kiểm thử

```powershell
BeforeAll { # Nhập các hàm cần kiểm thử }
Describe 'TênHàm' {
    Context 'Khi có điều kiện' {
        BeforeAll { # Thiết lập cho context }
        It 'Nên có hành vi' { # Bài kiểm thử riêng lẻ }
        AfterAll { # Dọn dẹp cho context }
    }
}
```

## Các Từ khóa Cốt lõi

- **`Describe`**: Nhóm cấp cao nhất, thường được đặt tên theo hàm đang được kiểm thử
- **`Context`**: Nhóm con trong `Describe` cho các kịch bản cụ thể
- **`It`**: Các trường hợp kiểm thử riêng lẻ, sử dụng tên mô tả
- **`Should`**: Từ khóa khẳng định để xác thực kiểm thử
- **`BeforeAll/AfterAll`**: Thiết lập/dọn dẹp một lần cho mỗi khối
- **`BeforeEach/AfterEach`**: Thiết lập/dọn dẹp trước/sau mỗi bài kiểm thử

## Thiết lập và Dọn dẹp (Setup and Teardown)

- **`BeforeAll`**: Chạy một lần khi bắt đầu khối chứa nó, sử dụng cho các hoạt động tốn kém
- **`BeforeEach`**: Chạy trước mỗi `It` trong khối, sử dụng để thiết lập riêng cho từng bài kiểm thử
- **`AfterEach`**: Chạy sau mỗi `It`, được đảm bảo chạy ngay cả khi bài kiểm thử thất bại
- **`AfterAll`**: Chạy một lần khi kết thúc khối, sử dụng để dọn dẹp
- **Phạm vi Biến**: Các biến trong `BeforeAll` có sẵn cho các khối con (chỉ đọc), `BeforeEach/It/AfterEach` chia sẻ cùng một phạm vi

## Khẳng định (Assertions - Should)

- **So sánh Cơ bản**: `-Be`, `-BeExactly`, `-Not -Be`
- **Tập hợp (Collections)**: `-Contain`, `-BeIn`, `-HaveCount`
- **Số**: `-BeGreaterThan`, `-BeLessThan`, `-BeGreaterOrEqual`
- **Chuỗi**: `-Match`, `-Like`, `-BeNullOrEmpty`
- **Kiểu dữ liệu**: `-BeOfType`, `-BeTrue`, `-BeFalse`
- **Tệp**: `-Exist`, `-FileContentMatch`
- **Ngoại lệ (Exceptions)**: `-Throw`, `-Not -Throw`

## Mocking (Tạo đối tượng giả)

- **`Mock TênLệnh { KhốiMã }`**: Thay thế hành vi của lệnh
- **`-ParameterFilter`**: Chỉ mock khi các tham số khớp với điều kiện
- **`-Verifiable`**: Đánh dấu mock là cần được xác minh
- **`Should -Invoke`**: Xác minh mock đã được gọi một số lần cụ thể
- **`Should -InvokeVerifiable`**: Xác minh tất cả các mock có thể xác minh đã được gọi
- **Phạm vi**: Mock mặc định có phạm vi trong khối chứa nó

```powershell
Mock Get-Service { @{ Status = 'Running' } } -ParameterFilter { $Name -eq 'TestService' }
Should -Invoke Get-Service -Exactly 1 -ParameterFilter { $Name -eq 'TestService' }
```

## Các Trường hợp Kiểm thử (Test Cases - Data-Driven Tests)

Sử dụng `-TestCases` hoặc `-ForEach` cho các bài kiểm thử được tham số hóa:

```powershell
It 'Nên trả về <Expected> cho <Input>' -TestCases @(
    @{ Input = 'value1'; Expected = 'result1' }
    @{ Input = 'value2'; Expected = 'result2' }
) {
    Get-Function $Input | Should -Be $Expected
}
```

## Kiểm thử dựa trên Dữ liệu (Data-Driven Tests)

- **`-ForEach`**: Có sẵn trên `Describe`, `Context`, và `It` để tạo nhiều bài kiểm thử từ dữ liệu
- **`-TestCases`**: Bí danh cho `-ForEach` trên các khối `It` (để tương thích ngược)
- **Dữ liệu Hashtable**: Mỗi mục định nghĩa các biến có sẵn trong bài kiểm thử (ví dụ: `@{ Name = 'value'; Expected = 'result' }`)
- **Dữ liệu Mảng**: Sử dụng biến `$_` cho mục hiện tại
- **Mẫu (Templates)**: Sử dụng `<tênbiến>` trong tên bài kiểm thử để mở rộng động

```powershell
# Cách tiếp cận Hashtable
It 'Trả về <Expected> cho <Name>' -ForEach @(
    @{ Name = 'test1'; Expected = 'result1' }
    @{ Name = 'test2'; Expected = 'result2' }
) { Get-Function $Name | Should -Be $Expected }

# Cách tiếp cận Mảng
It 'Chứa <_>' -ForEach 'item1', 'item2' { Get-Collection | Should -Contain $_ }
```

## Thẻ (Tags)

- **Có sẵn trên**: các khối `Describe`, `Context`, và `It`
- **Lọc**: Sử dụng `-TagFilter` và `-ExcludeTagFilter` với `Invoke-Pester`
- **Ký tự đại diện (Wildcards)**: Thẻ hỗ trợ ký tự đại diện kiểu `-like` để lọc linh hoạt

```powershell
Describe 'Function' -Tag 'Unit' {
    It 'Nên hoạt động' -Tag 'Fast', 'Stable' { }
    It 'Nên chạy chậm' -Tag 'Slow', 'Integration' { }
}

# Chỉ chạy các bài kiểm thử đơn vị (unit test) nhanh
Invoke-Pester -TagFilter 'Unit' -ExcludeTagFilter 'Slow'
```

## Bỏ qua (Skip)

- **`-Skip`**: Có sẵn trên `Describe`, `Context`, và `It` để bỏ qua các bài kiểm thử
- **Có điều kiện**: Sử dụng `-Skip:$condition` để bỏ qua một cách linh động
- **Bỏ qua lúc chạy**: Sử dụng `Set-ItResult -Skipped` trong quá trình thực thi kiểm thử (thiết lập/dọn dẹp vẫn chạy)

```powershell
It 'Nên hoạt động trên Windows' -Skip:(-not $IsWindows) { }
Context 'Kiểm thử tích hợp' -Skip { }
```

## Xử lý Lỗi

- **Tiếp tục khi có lỗi**: Sử dụng `Should.ErrorAction = 'Continue'` để thu thập nhiều lỗi
- **Dừng khi có lỗi nghiêm trọng**: Sử dụng `-ErrorAction Stop` cho các điều kiện tiên quyết
- **Kiểm thử Ngoại lệ**: Sử dụng `{ Code } | Should -Throw` để kiểm thử ngoại lệ

## Các Phương pháp Hay nhất (Best Practices)

- **Tên Mô tả**: Sử dụng các mô tả kiểm thử rõ ràng giải thích hành vi
- **Mô hình AAA**: Arrange (sắp xếp), Act (hành động), Assert (khẳng định)
- **Kiểm thử Độc lập**: Mỗi bài kiểm thử phải độc lập với nhau
- **Tránh Bí danh**: Sử dụng tên cmdlet đầy đủ (`Where-Object` không phải `?`)
- **Trách nhiệm Đơn lẻ**: Một khẳng định cho mỗi bài kiểm thử khi có thể
- **Tổ chức Tệp Kiểm thử**: Nhóm các bài kiểm thử liên quan trong các khối `Context`. Các khối `Context` có thể được lồng vào nhau.

## Mẫu Kiểm thử Ví dụ

```powershell
BeforeAll {
    . $PSScriptRoot/Get-UserInfo.ps1
}

Describe 'Get-UserInfo' {
    Context 'Khi người dùng tồn tại' {
        BeforeAll {
            Mock Get-ADUser { @{ Name = 'TestUser'; Enabled = $true } }
        }

        It 'Nên trả về đối tượng người dùng' {
            $result = Get-UserInfo -Username 'TestUser'
            $result | Should -Not -BeNullOrEmpty
            $result.Name | Should -Be 'TestUser'
        }

        It 'Nên gọi Get-ADUser một lần' {
            Get-UserInfo -Username 'TestUser'
            Should -Invoke Get-ADUser -Exactly 1
        }
    }

    Context 'Khi người dùng không tồn tại' {
        BeforeAll {
            Mock Get-ADUser { throw "User not found" }
        }

        It 'Nên ném ra ngoại lệ' {
            { Get-UserInfo -Username 'NonExistent' } | Should -Throw "*not found*"
        }
    }
}
```

## Cấu hình

Cấu hình được định nghĩa **bên ngoài** các tệp kiểm thử khi gọi `Invoke-Pester` để kiểm soát hành vi thực thi.

```powershell
# Tạo cấu hình (Pester 5.2+)
$config = New-PesterConfiguration
$config.Run.Path = './Tests'
$config.Output.Verbosity = 'Detailed'
$config.TestResult.Enabled = $true
$config.TestResult.OutputFormat = 'NUnitXml'
$config.Should.ErrorAction = 'Continue'
Invoke-Pester -Configuration $config
```

**Các mục chính**: Run (Path, Exit), Filter (Tag, ExcludeTag), Output (Verbosity), TestResult (Enabled, OutputFormat), CodeCoverage (Enabled, Path), Should (ErrorAction), Debug
