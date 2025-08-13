---
applyTo: "**/*.ps1,**/*.psm1"
description: "Các phương pháp tốt nhất cho cmdlet và kịch bản PowerShell dựa trên hướng dẫn của Microsoft"
---

# Hướng dẫn Phát triển Cmdlet PowerShell

Hướng dẫn này cung cấp các chỉ dẫn cụ thể cho PowerShell để giúp GitHub Copilot tạo ra các kịch bản có tính thành ngữ, an toàn và dễ bảo trì. Nó tuân thủ các hướng dẫn phát triển cmdlet PowerShell của Microsoft.

## Quy ước Đặt tên

- **Định dạng Động từ-Danh từ:**

  - Sử dụng các động từ PowerShell đã được phê duyệt (Get-Verb)
  - Sử dụng danh từ số ít
  - Dùng kiểu PascalCase cho cả động từ và danh từ
  - Tránh các ký tự đặc biệt và khoảng trắng

- **Tên Tham số:**

  - Sử dụng kiểu PascalCase
  - Chọn tên rõ ràng, mang tính mô tả
  - Sử dụng dạng số ít trừ khi luôn là số nhiều
  - Tuân theo các tên chuẩn của PowerShell

- **Tên Biến:**

  - Sử dụng PascalCase cho biến công khai (public)
  - Sử dụng camelCase cho biến riêng tư (private)
  - Tránh viết tắt
  - Sử dụng tên có ý nghĩa

- **Tránh dùng Bí danh (Alias):**
  - Sử dụng tên cmdlet đầy đủ
  - Tránh sử dụng bí danh trong kịch bản (ví dụ: sử dụng `Get-ChildItem` thay vì `gci`)
  - Ghi lại tài liệu cho bất kỳ bí danh tùy chỉnh nào
  - Sử dụng tên tham số đầy đủ

### Ví dụ

```powershell
function Get-UserProfile {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Username,

        [Parameter()]
        [ValidateSet('Basic', 'Detailed')]
        [string]$ProfileType = 'Basic'
    )

    process {
        # Logic xử lý ở đây
    }
}
```

## Thiết kế Tham số

- **Các Tham số Chuẩn:**

  - Sử dụng các tên tham số phổ biến (`Path`, `Name`, `Force`)
  - Tuân theo quy ước của các cmdlet tích hợp sẵn
  - Sử dụng bí danh cho các thuật ngữ chuyên biệt
  - Ghi lại mục đích của tham số

- **Tên Tham số:**

  - Sử dụng dạng số ít trừ khi luôn là số nhiều
  - Chọn tên rõ ràng, mang tính mô tả
  - Tuân theo quy ước của PowerShell
  - Sử dụng định dạng PascalCase

- **Lựa chọn Kiểu dữ liệu:**

  - Sử dụng các kiểu .NET phổ biến
  - Triển khai xác thực phù hợp
  - Cân nhắc `ValidateSet` cho các tùy chọn giới hạn
  - Kích hoạt tính năng tự động hoàn thành (tab completion) khi có thể

- **Tham số Chuyển đổi (Switch Parameters):**
  - Sử dụng `[switch]` cho các cờ boolean
  - Tránh các tham số `$true`/`$false`
  - Mặc định là `$false` khi bị bỏ qua
  - Sử dụng tên hành động rõ ràng

### Ví dụ

```powershell
function Set-ResourceConfiguration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter()]
        [ValidateSet('Dev', 'Test', 'Prod')]
        [string]$Environment = 'Dev',

        [Parameter()]
        [switch]$Force,

        [Parameter()]
        [ValidateNotNullOrEmpty()]
        [string[]]$Tags
    )

    process {
        # Logic xử lý ở đây
    }
}
```

## Pipeline và Đầu ra

- **Đầu vào Pipeline:**

  - Sử dụng `ValueFromPipeline` cho đầu vào đối tượng trực tiếp
  - Sử dụng `ValueFromPipelineByPropertyName` để ánh xạ thuộc tính
  - Triển khai các khối Begin/Process/End để xử lý pipeline
  - Ghi lại các yêu cầu đầu vào của pipeline

- **Đối tượng Đầu ra:**

  - Trả về các đối tượng đa dạng (rich objects), không phải văn bản đã định dạng
  - Sử dụng `PSCustomObject` cho dữ liệu có cấu trúc
  - Tránh `Write-Host` để xuất dữ liệu
  - Cho phép xử lý bởi các cmdlet tiếp theo trong chuỗi

- **Truyền dữ liệu qua Pipeline (Streaming):**

  - Xuất từng đối tượng một
  - Sử dụng khối `process` để truyền dữ liệu
  - Tránh thu thập các mảng lớn
  - Cho phép xử lý ngay lập tức

- **Mẫu PassThru:**
  - Mặc định không có đầu ra cho các cmdlet hành động
  - Triển khai tham số chuyển đổi `-PassThru` để trả về đối tượng
  - Trả về đối tượng đã được sửa đổi/tạo với `-PassThru`
  - Sử dụng verbose/warning để cập nhật trạng thái

### Ví dụ

```powershell
function Update-ResourceStatus {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline, ValueFromPipelineByPropertyName)]
        [string]$Name,

        [Parameter(Mandatory)]
        [ValidateSet('Active', 'Inactive', 'Maintenance')]
        [string]$Status,

        [Parameter()]
        [switch]$PassThru
    )

    begin {
        Write-Verbose "Bắt đầu quá trình cập nhật trạng thái tài nguyên"
        $timestamp = Get-Date
    }

    process {
        # Xử lý từng tài nguyên riêng lẻ
        Write-Verbose "Đang xử lý tài nguyên: $Name"

        $resource = [PSCustomObject]@{
            Name = $Name
            Status = $Status
            LastUpdated = $timestamp
            UpdatedBy = $env:USERNAME
        }

        # Chỉ xuất ra nếu PassThru được chỉ định
        if ($PassThru) {
            Write-Output $resource
        }
    }

    end {
        Write-Verbose "Quá trình cập nhật trạng thái tài nguyên đã hoàn tất"
    }
}
```

## Xử lý Lỗi và An toàn

- **Triển khai ShouldProcess:**

  - Sử dụng `[CmdletBinding(SupportsShouldProcess = $true)]`
  - Đặt mức `ConfirmImpact` phù hợp
  - Gọi `$PSCmdlet.ShouldProcess()` cho các thay đổi hệ thống
  - Sử dụng `ShouldContinue()` cho các xác nhận bổ sung

- **Các Luồng Thông báo:**

  - `Write-Verbose` cho các chi tiết hoạt động với `-Verbose`
  - `Write-Warning` cho các điều kiện cảnh báo
  - `Write-Error` cho các lỗi không kết thúc (non-terminating)
  - `throw` cho các lỗi kết thúc (terminating)
  - Tránh `Write-Host` trừ khi dùng cho văn bản giao diện người dùng

- **Mẫu Xử lý Lỗi:**

  - Sử dụng các khối try/catch để quản lý lỗi
  - Đặt tùy chọn `ErrorAction` phù hợp
  - Trả về các thông báo lỗi có ý nghĩa
  - Sử dụng `ErrorVariable` khi cần
  - Bao gồm xử lý lỗi kết thúc và không kết thúc phù hợp

- **Thiết kế Không tương tác:**
  - Chấp nhận đầu vào qua các tham số
  - Tránh `Read-Host` trong kịch bản
  - Hỗ trợ các kịch bản tự động hóa
  - Ghi lại tài liệu cho tất cả các đầu vào bắt buộc

### Ví dụ

```powershell
function Remove-UserAccount {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [ValidateNotNullOrEmpty()]
        [string]$Username,

        [Parameter()]
        [switch]$Force
    )

    begin {
        Write-Verbose "Bắt đầu quá trình xóa tài khoản người dùng"
        $ErrorActionPreference = 'Stop'
    }

    process {
        try {
            # Xác thực
            if (-not (Test-UserExists -Username $Username)) {
                Write-Error "Không tìm thấy tài khoản người dùng '$Username'"
                return
            }

            # Xác nhận
            $shouldProcessMessage = "Xóa tài khoản người dùng '$Username'"
            if ($Force -or $PSCmdlet.ShouldProcess($Username, $shouldProcessMessage)) {
                Write-Verbose "Đang xóa tài khoản người dùng: $Username"

                # Thao tác chính
                Remove-ADUser -Identity $Username -ErrorAction Stop
                Write-Warning "Tài khoản người dùng '$Username' đã bị xóa"
            }
        }
        catch [Microsoft.ActiveDirectory.Management.ADException] {
            Write-Error "Lỗi Active Directory: $_"
            throw
        }
        catch {
            Write-Error "Lỗi không mong muốn khi xóa tài khoản người dùng: $_"
            throw
        }
    }

    end {
        Write-Verbose "Quá trình xóa tài khoản người dùng đã hoàn tất"
    }
}
```

## Tài liệu và Phong cách

- **Trợ giúp dựa trên Chú thích:** Bao gồm trợ giúp dựa trên chú thích cho bất kỳ hàm hoặc cmdlet nào công khai. Bên trong hàm, thêm một khối chú thích trợ giúp `<# ... #>` với ít nhất:

  - `.SYNOPSIS` Mô tả ngắn gọn
  - `.DESCRIPTION` Giải thích chi tiết
  - `.EXAMPLE` các phần với cách sử dụng thực tế
  - `.PARAMETER` mô tả các tham số
  - `.OUTPUTS` Kiểu đầu ra được trả về
  - `.NOTES` Thông tin bổ sung

- **Định dạng Nhất quán:**

  - Tuân theo phong cách PowerShell nhất quán
  - Sử dụng thụt lề phù hợp (khuyến nghị 4 dấu cách)
  - Dấu ngoặc nhọn mở trên cùng dòng với câu lệnh
  - Dấu ngoặc nhọn đóng trên một dòng mới
  - Sử dụng ngắt dòng sau các toán tử pipeline
  - Dùng PascalCase cho tên hàm và tham số
  - Tránh khoảng trắng không cần thiết

- **Hỗ trợ Pipeline:**

  - Triển khai các khối Begin/Process/End cho các hàm pipeline
  - Sử dụng `ValueFromPipeline` khi thích hợp
  - Hỗ trợ đầu vào pipeline theo tên thuộc tính
  - Trả về các đối tượng phù hợp, không phải văn bản đã định dạng

- **Tránh Bí danh:** Sử dụng tên cmdlet và tham số đầy đủ
  - Tránh sử dụng bí danh trong kịch bản (ví dụ: sử dụng `Get-ChildItem` thay vì `gci`); bí danh có thể chấp nhận được khi sử dụng tương tác trong shell.
  - Sử dụng `Where-Object` thay vì `?` hoặc `where`
  - Sử dụng `ForEach-Object` thay vì `%`
  - Sử dụng `Get-ChildItem` thay vì `ls` hoặc `dir`

## Ví dụ Đầy đủ: Mẫu Cmdlet từ Đầu đến Cuối

```powershell
function New-Resource {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
    param(
        [Parameter(Mandatory = $true,
                   ValueFromPipeline = $true,
                   ValueFromPipelineByPropertyName = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,

        [Parameter()]
        [ValidateSet('Development', 'Production')]
        [string]$Environment = 'Development'
    )

    begin {
        Write-Verbose "Bắt đầu quá trình tạo tài nguyên"
    }

    process {
        try {
            if ($PSCmdlet.ShouldProcess($Name, "Tạo tài nguyên mới")) {
                # Logic tạo tài nguyên ở đây
                Write-Output ([PSCustomObject]@{
                    Name = $Name
                    Environment = $Environment
                    Created = Get-Date
                })
            }
        }
        catch {
            Write-Error "Không thể tạo tài nguyên: $_"
        }
    }

    end {
        Write-Verbose "Hoàn tất quá trình tạo tài nguyên"
    }
}
```
