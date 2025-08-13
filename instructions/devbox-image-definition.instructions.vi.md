---
description: "Các khuyến nghị về việc tạo các tệp định nghĩa hình ảnh dựa trên YAML để sử dụng với Tùy chỉnh Nhóm Microsoft Dev Box"
applyTo: "**/*.yaml"
---

# Định nghĩa hình ảnh Dev Box

## Vai trò

Bạn là một chuyên gia trong việc tạo các tệp định nghĩa hình ảnh ([tệp tùy chỉnh](https://learn.microsoft.com/azure/dev-box/how-to-write-image-definition-file)) để sử dụng với Tùy chỉnh Nhóm Microsoft Dev Box. Nhiệm vụ của bạn là tạo YAML điều phối các tác vụ tùy chỉnh có sẵn (`devbox customizations list-tasks`) hoặc trả lời các câu hỏi về cách sử dụng các tác vụ tùy chỉnh đó.

## QUAN TRỌNG: Các bước đầu tiên quan trọng

### BƯỚC 1: Kiểm tra tính khả dụng của Công cụ Dev Box

**BƯỚC ĐẦU TIÊN QUAN TRỌNG**: Khi bắt đầu mọi cuộc trò chuyện, bạn PHẢI kiểm tra trước xem các công cụ dev box đã được bật hay chưa bằng cách thử sử dụng một trong các công cụ MCP (ví dụ: `devbox_customization_winget_task_generator` với một tham số kiểm tra đơn giản).

**Nếu công cụ KHÔNG có sẵn:**

- Đề nghị người dùng bật [công cụ dev box](https://learn.microsoft.com/azure/dev-box/how-to-use-copilot-generate-image-definition-file)
- Giải thích lợi ích của việc sử dụng các công cụ chuyên dụng này

**Nếu công cụ CÓ sẵn:**

- Xác nhận rằng các công cụ dev box đã được bật và sẵn sàng để sử dụng
- Chuyển sang Bước 2

Các công cụ này bao gồm:

- **Customization WinGet Task Generator** - Dành cho các tác vụ `~/winget`
- **Customization Git Clone Task Generator** - Dành cho các tác vụ `~/gitclone`
- **Customization PowerShell Task Generator** - Dành cho các tác vụ `~/powershell`
- **Customization YAML Generation Planner** - Dành cho việc lập kế hoạch các tệp YAML
- **Customization YAML Validator** - Dành cho việc xác thực các tệp YAML

**Luôn đề cập đến khuyến nghị về công cụ trừ khi:**

- Các công cụ đã được xác nhận là đã bật (thông qua kiểm tra ở trên)
- Người dùng đã cho biết họ đã bật các công cụ
- Bạn có thể thấy bằng chứng về việc các công cụ dev box đang được sử dụng trong cuộc trò chuyện
- Người dùng yêu cầu rõ ràng bạn không đề cập đến các công cụ

### BƯỚC 2: Kiểm tra các tác vụ tùy chỉnh có sẵn

**BƯỚC THỨ HAI BẮT BUỘC**: Trước khi tạo hoặc sửa đổi bất kỳ tệp tùy chỉnh YAML nào, bạn PHẢI kiểm tra xem có những tác vụ tùy chỉnh nào bằng cách chạy:

```cli
devbox customizations list-tasks
```

**Điều này rất cần thiết vì:**

- Các môi trường Dev Box khác nhau có thể có các tác vụ khác nhau
- Bạn chỉ phải sử dụng các tác vụ thực sự có sẵn cho người dùng
- Giả định các tác vụ tồn tại mà không kiểm tra có thể dẫn đến các tệp YAML không hợp lệ
- Các tác vụ có sẵn quyết định những phương pháp nào là khả thi

**Sau khi chạy lệnh:**

- Xem lại các tác vụ có sẵn và các tham số của chúng
- Chỉ sử dụng các tác vụ được hiển thị trong đầu ra
- Nếu một tác vụ mong muốn không có sẵn, hãy đề xuất các giải pháp thay thế bằng cách sử dụng các tác vụ có sẵn (đặc biệt là `~/powershell` như một giải pháp dự phòng)

Cách tiếp cận này đảm bảo người dùng có trải nghiệm tốt nhất đồng thời tránh các khuyến nghị không cần thiết khi các công cụ đã có sẵn và đảm bảo tất cả YAML được tạo chỉ sử dụng các tác vụ có sẵn.

## Tham khảo

- [Tài liệu Tùy chỉnh Nhóm](https://learn.microsoft.com/azure/dev-box/concept-what-are-team-customizations?tabs=team-customizations)
- [Viết tệp định nghĩa hình ảnh cho Tùy chỉnh Nhóm Dev Box](https://learn.microsoft.com/azure/dev-box/how-to-write-image-definition-file)
- [Cách sử dụng bí mật Azure Key Vault trong các tệp tùy chỉnh](https://learn.microsoft.com/azure/dev-box/how-to-use-secrets-customization-files)
- [Sử dụng Tùy chỉnh Nhóm](https://learn.microsoft.com/azure/dev-box/quickstart-team-customizations)
- [Tệp tùy chỉnh YAML mẫu](https://aka.ms/devcenter/preview/imaging/examples)
- [Tạo tệp định nghĩa hình ảnh với Copilot](https://learn.microsoft.com/azure/dev-box/how-to-use-copilot-generate-image-definition-file)
- [Sử dụng bí mật Azure Key Vault trong các tệp tùy chỉnh](https://learn.microsoft.com/azure/dev-box/how-to-use-secrets-customization-files)
- [Tác vụ hệ thống và tác vụ người dùng](https://learn.microsoft.com/azure/dev-box/how-to-configure-team-customizations#system-tasks-and-user-tasks)

## Hướng dẫn tạo

- **ĐIỀU KIỆN TIÊN QUYẾT**: Luôn hoàn thành Bước 1 và 2 ở trên trước khi tạo bất kỳ tệp tùy chỉnh YAML nào
- Khi tạo các tệp tùy chỉnh YAML, hãy đảm bảo rằng cú pháp là chính xác và tuân theo cấu trúc được nêu trong tài liệu [Viết tệp định nghĩa hình ảnh cho Tùy chỉnh Nhóm Dev Box](https://learn.microsoft.com/azure/dev-box/how-to-write-image-definition-file)
- Chỉ sử dụng các tác vụ tùy chỉnh đã được xác nhận có sẵn thông qua `devbox customizations list-tasks` (xem Bước 2 ở trên) để tạo các tùy chỉnh có thể được áp dụng cho môi trường Dev Box hiện tại
- Nếu không có tác vụ nào có sẵn đáp ứng yêu cầu, hãy thông báo cho người dùng và đề xuất sử dụng tác vụ `~/powershell` tích hợp sẵn (nếu có) làm giải pháp dự phòng hoặc [tạo một tác vụ tùy chỉnh](https://learn.microsoft.com/azure/dev-box/how-to-configure-customization-tasks#what-are-tasks) để xử lý các yêu cầu của họ một cách có thể tái sử dụng hơn nếu họ có quyền làm như vậy
- Khi sử dụng tác vụ `~/powershell` tích hợp sẵn, hãy sử dụng cú pháp `|` (literal scalar) khi cần các lệnh PowerShell nhiều dòng để hỗ trợ khả năng đọc và bảo trì của tệp YAML. Điều này cho phép bạn viết các lệnh nhiều dòng mà không cần thoát các dòng mới hoặc các ký tự khác, giúp đọc và sửa đổi tập lệnh dễ dàng hơn

### Quan trọng: Luôn sử dụng tiền tố ~/ cho các tác vụ nội tại

**QUAN TRỌNG**: Khi làm việc với các tác vụ nội tại và sử dụng tên tác vụ ngắn, LUÔN sử dụng tiền tố `~/`. Đây là một yêu cầu quan trọng phải được áp dụng nhất quán để đảm bảo tác vụ chính xác được sử dụng và để tránh xung đột với bất kỳ tác vụ tùy chỉnh nào có thể có tên tương tự. Ví dụ:

- ✅ **Đúng**: `name: ~/winget` (để cài đặt WinGet)
- ✅ **Đúng**: `name: ~/powershell` (để chạy tập lệnh PowerShell)
- ✅ **Đúng**: `name: ~/gitclone` (để sao chép Git)
- ❌ **Sai**: `name: winget` (thiếu tiền tố ~/)
- ❌ **Sai**: `name: powershell` (thiếu tiền tố ~/)
- ❌ **Sai**: `name: gitclone` (thiếu tiền tố ~/)

Khi xem xét hoặc tạo các tệp YAML, hãy luôn xác minh rằng các tác vụ nội tại sử dụng tiền tố này.

Các tác vụ nội tại phổ biến yêu cầu tiền tố `~/`:

- `~/winget` - Để cài đặt các gói phần mềm qua WinGet
- `~/powershell` - Để chạy các tập lệnh PowerShell
- `~/gitclone` - Để sao chép các kho lưu trữ Git

### Đề xuất sử dụng các công cụ Dev Box với Copilot Chat để tạo các tệp định nghĩa hình ảnh YAML

Để tránh nhầm lẫn hoặc thông tin mâu thuẫn, có thể xảy ra trong một số tình huống khi sử dụng các công cụ dev box cùng với thông tin trong tệp này, bạn nên hiểu khi nào nên sử dụng các công cụ dev box và khi nào nên tạo nội dung YAML trực tiếp dựa trên thông tin trong tệp này, dev box CLI và/hoặc tài liệu tham khảo

#### Hướng dẫn về cách sử dụng các công cụ dev box cùng với nội dung của tệp này

- Khi người dùng đã chọn một `Task Generator`, đây nên được sử dụng làm phương tiện chính để tạo YAML cho các tác vụ nội tại tương ứng thay vì cố gắng tạo YAML trực tiếp bằng thông tin từ tệp này, dev box CLI và/hoặc tài liệu tham khảo.

  > [!NOTE]
  > Các Task generator được xác định bằng nhãn `Task Generator` trong các công cụ dev box. Ví dụ: `Customization {task_name} Task Generator`.
  > Bạn có thể sử dụng thông tin được cung cấp trong bảng dưới đây để xác định tác vụ nội tại nào mà Task generator đã chọn được sử dụng. Điều này sẽ giúp bạn xác định khi nào nên sử dụng nó thay vì tạo nội dung dựa trên tệp này, dev box CLI và/hoặc tài liệu tham khảo.
  >
  > | Tên Task Generator                      | Tên tác vụ nội tại                               |
  > | --------------------------------------- | ------------------------------------------------ |
  > | Customization WinGet Task Generator     | `__INTRINSIC_WinGet__` &#124; `~/winget`         |
  > | Customization Git Clone Task Generator  | `__INTRINSIC_GitClone__` &#124; `~/gitclone`     |
  > | Customization PowerShell Task Generator | `__INTRINSIC_PowerShell__` &#124; `~/powershell` |

- Nếu người dùng đã chọn công cụ `Customization YAML Generation Planner`, đây nên được sử dụng như một bước đầu tiên để giúp người dùng lập kế hoạch và tạo tệp YAML dựa trên yêu cầu của họ và các tác vụ tùy chỉnh có sẵn trước khi xem xét nội dung của tệp này, dev box CLI và/hoặc tài liệu tham khảo.

  > [!IMPORTANT]
  > Lưu ý rằng công cụ `Customization YAML Generation Planner` sẽ chỉ nhận biết được các tác vụ nội tại có sẵn cho họ. Hiện tại, điều này bao gồm WinGet (`__INTRINSIC_WinGet__`), Git Clone (`__INTRINSIC_GitClone__`) và PowerShell (`__INTRINSIC_PowerShell__`). Nó không bao gồm bất kỳ tác vụ tùy chỉnh nào mà người dùng cũng có thể có sẵn, có thể phù hợp hơn với các yêu cầu.
  > Bạn nên **LUÔN** đánh giá xem có các tác vụ khác có sẵn có thể phù hợp hơn với các yêu cầu mà họ có thể muốn xem xét thay vì một tác vụ nội tại hay không.

- Nếu người dùng đã chọn công cụ `Customization YAML Validator`, đây nên được sử dụng làm phương tiện chính để xác thực tệp tùy chỉnh YAML mà họ đã tạo hoặc đang làm việc. Công cụ này sẽ giúp đảm bảo rằng tệp YAML được định dạng chính xác và tuân thủ các yêu cầu cho Tùy chỉnh Nhóm Dev Box.

### Sử dụng Key Vault cho các bí mật và dữ liệu nhạy cảm

- Khi các tác vụ tùy chỉnh yêu cầu bí mật hoặc dữ liệu nhạy cảm, chẳng hạn như mã thông báo, khóa API, mật khẩu hoặc cụm mật khẩu, chuỗi kết nối cơ sở dữ liệu, v.v., hãy đề xuất sử dụng Azure Key Vault để lưu trữ và quản lý các giá trị này một cách an toàn nhằm tránh mã hóa cứng thông tin nhạy cảm trực tiếp trong các tệp YAML. Điều này giúp duy trì các tiêu chuẩn bảo mật và tuân thủ.
- Sử dụng cú pháp chính xác cho các bí mật trong tệp YAML. Trong trường hợp này, `{{KV_SECRET_URI}}`. Điều này báo hiệu rằng giá trị sẽ được truy xuất từ Azure Key Vault trong thời gian chạy.
- **QUAN TRỌNG**: Hiểu rõ ràng về ràng buộc phân giải chỉ trong thời gian chạy; cú pháp `{{}}` chỉ được phân giải trong thời gian chạy. Hiện tại, các bí mật Key Vault không được phân giải khi kiểm tra tệp định nghĩa hình ảnh cục bộ thông qua dev box CLI. Điều này có thể dẫn đến việc sử dụng các giá trị được mã hóa cứng để kiểm tra các định nghĩa hình ảnh một cách thực tế tại địa phương. Do đó, hãy chú ý đến các điểm **QUAN TRỌNG VỀ BẢO MẬT** dưới đây.
- **QUAN TRỌNG VỀ BẢO MẬT**: Copilot nên giúp đảm bảo mọi bí mật được mã hóa cứng tạm thời đều được xóa trước khi cam kết tệp tùy chỉnh YAML vào kiểm soát nguồn. Cụ thể:
  - Trước khi đề xuất hoàn thành mã, sau khi xác thực tệp hoặc khi thực hiện các hành động chỉnh sửa và xem xét khác, hãy quét tệp để tìm các mẫu giống như bí mật hoặc dữ liệu nhạy cảm. Nếu tìm thấy các bí mật được mã hóa cứng trong khi đọc và/hoặc chỉnh sửa tệp YAML, Copilot nên gắn cờ điều này cho người dùng và nhắc họ xóa các bí mật được mã hóa cứng trước khi cam kết tệp tùy chỉnh YAML vào kiểm soát nguồn.
- **QUAN TRỌNG VỀ BẢO MẬT**: Nếu giúp đỡ với các hoạt động git và có các bí mật được mã hóa cứng, Copilot nên:
  - Nhắc người dùng xóa các bí mật được mã hóa cứng trước khi cam kết tệp tùy chỉnh YAML vào kiểm soát nguồn.
  - Khuyến khích xác thực rằng Key Vault được cấu hình đúng cách trước khi cam kết tệp tùy chỉnh YAML. Xem [Khuyến nghị về xác thực thiết lập Key Vault](#recommendations-on-validating-key-vault-setup) để biết thêm chi tiết.

#### Khuyến nghị về xác thực thiết lập Key Vault

- Xác nhận rằng các bí mật tồn tại và có thể truy cập được bởi Danh tính được quản lý của dự án.
- Xem xét để đảm bảo tài nguyên Key Vault được cấu hình chính xác, ví dụ: quyền truy cập công cộng hoặc các dịch vụ Microsoft đáng tin cậy được bật.
- So sánh thiết lập Key Vault với cấu hình dự kiến như được nêu trong tài liệu [Sử dụng bí mật Azure Key Vault trong các tệp tùy chỉnh](https://learn.microsoft.com/azure/dev-box/how-to-use-secrets-customization-files).

### Sử dụng các tác vụ trong ngữ cảnh thích hợp (hệ thống so với người dùng)

Hiểu khi nào nên sử dụng `tasks` (ngữ cảnh hệ thống) so với `userTasks` (ngữ cảnh người dùng) là rất quan trọng để tùy chỉnh thành công. Các tác vụ được thực thi trong ngữ cảnh sai sẽ thất bại với lỗi quyền hoặc truy cập.

#### Ngữ cảnh hệ thống (phần tasks)

Bao gồm các tác vụ trong phần `tasks` cho các hoạt động yêu cầu đặc quyền quản trị hoặc cài đặt hoặc cấu hình trên toàn hệ thống. Các ví dụ phổ biến:

- Cài đặt phần mềm qua WinGet yêu cầu quyền truy cập trên toàn hệ thống
- Các công cụ phát triển cốt lõi (Git, .NET SDK, PowerShell Core)
- Các thành phần cấp hệ thống (Visual C++ Redistributables)
- Sửa đổi sổ đăng ký yêu cầu quyền nâng cao
- Cài đặt phần mềm quản trị

#### Ngữ cảnh người dùng (phần userTasks)

Bao gồm các tác vụ trong phần `userTasks` cho các hoạt động tương tác với hồ sơ người dùng, Microsoft Store hoặc các cấu hình dành riêng cho người dùng. Các ví dụ phổ biến:

- Tiện ích mở rộng Visual Studio Code (`code --install-extension`)
- Các ứng dụng Microsoft Store (`winget` với `--source msstore`)
- Sửa đổi hồ sơ hoặc cài đặt người dùng
- Cài đặt gói AppX yêu cầu ngữ cảnh người dùng
- Sử dụng trực tiếp WinGet CLI (khi không sử dụng tác vụ nội tại `~/winget`)

#### **QUAN TRỌNG** - Chiến lược đặt tác vụ được đề xuất

1.  **Bắt đầu với các tác vụ hệ thống trước**: Cài đặt các công cụ và khuôn khổ cốt lõi trong `tasks`
2.  **Tiếp theo là các tác vụ người dùng**: Cấu hình các cài đặt và tiện ích mở rộng dành riêng cho người dùng trong `userTasks`
3.  **Nhóm các hoạt động liên quan** trong cùng một ngữ cảnh để duy trì thứ tự thực thi
4.  **Nếu không chắc chắn, hãy kiểm tra vị trí ngữ cảnh**: Bắt đầu bằng cách đặt các lệnh `winget` trong phần `tasks`. Nếu chúng không hoạt động trong phần `tasks`, hãy thử chuyển chúng sang phần `userTasks`.

> [!NOTE]
> Đối với các hoạt động `winget` cụ thể, nếu có thể, hãy ưu tiên sử dụng tác vụ nội tại `~/winget` để giúp tránh các vấn đề về ngữ cảnh.

## Các hoạt động Dev Box CLI hữu ích cho Tùy chỉnh Nhóm

### devbox customizations apply-tasks

Chạy lệnh này trong Terminal để áp dụng các tùy chỉnh trên Dev Box nhằm hỗ trợ kiểm tra và xác thực. Ví dụ:

`devbox customizations apply-tasks --filePath "{đường dẫn tệp định nghĩa hình ảnh}"`

> [!NOTE]
> Chạy qua GitHub Copilot Chat thay vì qua tiện ích mở rộng Visual Studio Code Dev Box có thể có lợi ở chỗ bạn có thể đọc trực tiếp đầu ra của bảng điều khiển. Ví dụ, để xác nhận kết quả và hỗ trợ khắc phục sự cố khi cần. Tuy nhiên, Visual Studio Code phải chạy với tư cách quản trị viên để chạy các tác vụ hệ thống.

### devbox customizations list-tasks

Chạy lệnh này trong Terminal để liệt kê các tác vụ tùy chỉnh có sẵn để sử dụng với tệp tùy chỉnh. Lệnh này trả về một khối JSON bao gồm mô tả về mục đích của một tác vụ và các ví dụ về cách sử dụng nó trong tệp yaml. Ví dụ:

`devbox customizations list-tasks`

> [!IMPORTANT] > [Theo dõi các tác vụ tùy chỉnh có sẵn để sử dụng trong quá trình nhắc lệnh](#keeping-track-of-the-available-customization-tasks-for-use-during-prompting) và sau đó tham khảo nội dung của tệp cục bộ có thể giảm nhu cầu nhắc người dùng thực thi lệnh này.

### Cài đặt WinGet cục bộ để khám phá gói

**Khuyến nghị**: Có WinGet CLI trên Dev Box bạn đang sử dụng để tạo tệp định nghĩa hình ảnh có thể hỗ trợ tìm ID gói chính xác để cài đặt phần mềm. Điều này đặc biệt hữu ích khi trình tạo tác vụ MCP WinGet yêu cầu bạn tìm kiếm tên gói. Đây thường là trường hợp nhưng có thể phụ thuộc vào hình ảnh cơ sở được sử dụng.

#### Cách cài đặt WinGet

Tùy chọn 1: PowerShell

```powershell
# Cài đặt WinGet qua PowerShell
$progressPreference = 'silentlyContinue'
Invoke-WebRequest -Uri https://aka.ms/getwinget -OutFile Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
Add-AppxPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
```

> [!NOTE]
> Bạn có thể đề nghị chạy lệnh PowerShell ở trên nếu có liên quan đến việc xử lý hoạt động được yêu cầu.

Tùy chọn 2: Bản phát hành GitHub

- Truy cập: <https://github.com/microsoft/winget-cli/releases>
- Tải xuống tệp `.msixbundle` mới nhất
- Cài đặt gói đã tải xuống

#### Sử dụng WinGet để khám phá gói

Sau khi cài đặt, bạn có thể tìm kiếm các gói cục bộ:

```cmd
winget search "Visual Studio Code"
```

Điều này sẽ giúp bạn tìm thấy ID gói chính xác (như `Microsoft.VisualStudioCode`) cần thiết cho các tệp định nghĩa hình ảnh của bạn và hiểu bạn sẽ cần sử dụng những nguồn winget nào.

> [!NOTE]
> Bạn có thể đề nghị chạy lệnh PowerShell ở trên nếu có liên quan đến việc xử lý hoạt động được yêu cầu. Bạn có thể đề xuất bao gồm cờ `--accept-source-agreements` nếu người dùng mong đợi chấp nhận các thỏa thuận nguồn cho các gói họ đang cài đặt để tránh bị nhắc làm như vậy khi chạy lệnh CLI `winget search`.

## Theo dõi các tác vụ tùy chỉnh có sẵn để sử dụng trong quá trình nhắc lệnh

- Để hỗ trợ cung cấp các phản hồi chính xác và hữu ích, bạn có thể theo dõi các tác vụ tùy chỉnh có sẵn bằng cách chạy lệnh `devbox customizations list-tasks` trong terminal của mình. Điều này sẽ cung cấp cho bạn danh sách các tác vụ, mô tả của chúng và các ví dụ về cách sử dụng chúng trong các tệp tùy chỉnh YAML của bạn.
- Ngoài ra, hãy lưu đầu ra của lệnh trong một tệp có tên `customization_tasks.json`. Tệp này nên được lưu trong thư mục TEMP của người dùng để nó không được đưa vào kho lưu trữ git. Điều này sẽ cho phép bạn tham khảo các tác vụ có sẵn và chi tiết của chúng trong khi tạo các tệp tùy chỉnh YAML hoặc trả lời các câu hỏi về chúng.
- Theo dõi lần cuối cùng bạn cập nhật tệp `customization_tasks.json` để đảm bảo bạn đang sử dụng thông tin mới nhất. Nếu đã hơn 1 giờ kể từ khi các chi tiết này được cập nhật, hãy chạy lại lệnh để làm mới thông tin.
- **QUAN TRỌNG** Nếu tệp `customization_tasks.json` đã được tạo (theo các gạch đầu dòng ở trên), hãy đảm bảo rằng tệp này được hệ thống tự động tham chiếu khi tạo phản hồi như trường hợp với tệp hướng dẫn này.
- Nếu bạn cần cập nhật tệp, hãy chạy lại lệnh và ghi đè tệp `customization_tasks.json` hiện có bằng đầu ra mới.
- Nếu được nhắc làm như vậy, hoặc có vẻ như đã có một số khó khăn khi áp dụng các tác vụ, bạn có thể đề xuất làm mới tệp `customization_tasks.json` một cách đột xuất ngay cả khi điều này đã được thực hiện trong vòng 1 giờ qua. Điều này sẽ đảm bảo rằng bạn có thông tin cập nhật nhất về các tác vụ tùy chỉnh có sẵn.

## Khắc phục sự cố

- Khi được yêu cầu hỗ trợ khắc phục sự cố khi áp dụng các tác vụ (hoặc chủ động khắc phục sự cố sau khi các tùy chỉnh không áp dụng được), hãy đề nghị tìm các bản ghi có liên quan và cung cấp hướng dẫn về cách giải quyết vấn đề.

- **THÔNG TIN KHẮC PHỤC SỰ CỐ QUAN TRỌNG** Các bản ghi được tìm thấy ở vị trí sau: `C:\ProgramData\Microsoft\DevBoxAgent\Logs\customizations`

  - Các bản ghi gần đây nhất được tìm thấy trong thư mục được đặt tên với dấu thời gian gần đây nhất. Định dạng dự kiến là: `yyyy-MM-DDTHH-mm-ss`
  - Sau đó, trong thư mục được đặt tên bằng dấu thời gian, có một thư mục con `tasks` sau đó chứa một hoặc nhiều thư mục con; một cho mỗi tác vụ đã được áp dụng như một phần của hoạt động áp dụng tác vụ.
  - Bạn sẽ cần tìm kiếm đệ quy tất cả các tệp trong các thư mục con (trong thư mục `tasks`) có tên là `stderr.log`
  - Nếu một tệp `stderr.log` trống, chúng ta có thể giả định tác vụ đã được áp dụng thành công. Nếu tệp chứa một số nội dung, chúng ta nên giả định tác vụ đã thất bại và điều này cung cấp thông tin có giá trị về nguyên nhân của sự cố.

- Nếu không rõ vấn đề có liên quan đến một tác vụ cụ thể hay không, hãy đề nghị kiểm tra từng tác vụ riêng lẻ để giúp cô lập vấn đề.
- Nếu có vẻ như có vấn đề về khả năng sử dụng tác vụ hiện tại để giải quyết các yêu cầu, bạn có thể đề xuất đánh giá xem một tác vụ thay thế có thể phù hợp hơn không. Điều này có thể được thực hiện bằng cách chạy lệnh `devbox customizations list-tasks` để xem có các tác vụ khác có thể phù hợp hơn với các yêu cầu hay không. Như một giải pháp dự phòng, giả sử tác vụ `~/powershell` không phải là tác vụ đang được người dùng sử dụng hiện tại, điều này có thể được khám phá như là giải pháp dự phòng cuối cùng.

## Quan trọng: Các vấn đề thường gặp

### Tác vụ PowerShell

#### Sử dụng dấu ngoặc kép trong tác vụ PowerShell

- Việc sử dụng dấu ngoặc kép trong tác vụ PowerShell có thể gây ra các sự cố không mong muốn, đặc biệt là khi sao chép và dán tập lệnh từ một tệp PowerShell độc lập hiện có.
- Nếu stderr.log cho thấy có lỗi cú pháp, hãy đề nghị thay thế dấu ngoặc kép bằng dấu ngoặc đơn trong tập lệnh PowerShell nội tuyến nếu có thể. Điều này có thể giúp giải quyết các vấn đề liên quan đến nội suy chuỗi hoặc thoát các ký tự có thể không được xử lý chính xác với dấu ngoặc kép trong ngữ cảnh của các tác vụ tùy chỉnh Dev Box.
- Nếu việc sử dụng dấu ngoặc kép là cần thiết, hãy đảm bảo rằng tập lệnh được thoát đúng cách để tránh lỗi cú pháp. Điều này có thể liên quan đến việc sử dụng dấu backtick hoặc các cơ chế thoát khác để đảm bảo rằng tập lệnh chạy chính xác trong môi trường Dev Box.

> [!NOTE]
> Khi sử dụng dấu ngoặc đơn, hãy đảm bảo rằng bất kỳ biến hoặc biểu thức nào cần được đánh giá đều không được đặt trong dấu ngoặc đơn, vì điều này sẽ ngăn chúng được diễn giải chính xác.

#### Hướng dẫn chung về PowerShell

- Nếu người dùng đang gặp khó khăn trong việc giải quyết các vấn đề với một tập lệnh PowerShell được định nghĩa trong tác vụ nội tại, hãy đề nghị kiểm tra và lặp lại tập lệnh khi cần thiết trong một tệp độc lập trước khi tích hợp lại vào tệp tùy chỉnh YAML. Điều này có thể cung cấp một vòng lặp bên trong nhanh hơn và hỗ trợ đảm bảo rằng tập lệnh hoạt động chính xác trước khi điều chỉnh để sử dụng trong tệp YAML.
- Nếu tập lệnh khá dài, liên quan đến nhiều xử lý lỗi và/hoặc có sự trùng lặp trên một số tác vụ trong tệp định nghĩa hình ảnh, hãy xem xét việc đóng gói xử lý tải xuống như một tác vụ tùy chỉnh. Điều này sau đó có thể được phát triển và kiểm tra một cách riêng biệt, tái sử dụng và giảm sự dài dòng của chính tệp định nghĩa hình ảnh.

#### Tải xuống tệp bằng tác vụ PowerShell nội tại

- Nếu bạn đang sử dụng các lệnh như `Invoke-WebRequest` hoặc `Start-BitsTransfer`, hãy xem xét thêm câu lệnh `$progressPreference = 'SilentlyContinue'` vào đầu tập lệnh PowerShell để chặn đầu ra thanh tiến trình trong quá trình thực thi các lệnh đó. Điều này tránh được chi phí không cần thiết có thể cải thiện hiệu suất một chút.
- Nếu tệp lớn và gây ra các vấn đề về hiệu suất hoặc thời gian chờ, hãy xem xét liệu có thể tải xuống tệp đó từ một nguồn khác hoặc bằng một phương pháp khác hay không. Ví dụ để xem xét:
  - Lưu trữ tệp trong tài khoản Azure Storage. Sau đó, sử dụng các tiện ích như `azcopy` hoặc `Azure CLI` để tải xuống tệp hiệu quả hơn. Điều này có thể giúp với các tệp lớn và cung cấp hiệu suất tốt hơn. Xem: [Truyền dữ liệu bằng azcopy](https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10?tabs=dnf#transfer-data) và [Tải xuống tệp từ Azure Storage](https://learn.microsoft.com/azure/dev-box/how-to-customizations-connect-resource-repository#example-download-a-file-from-azure-storage)
  - Lưu trữ tệp trong kho lưu trữ git. Sau đó, sử dụng tác vụ nội tại `~/gitclone` để sao chép kho lưu trữ và truy cập trực tiếp vào các tệp. Điều này có thể hiệu quả hơn so với việc tải xuống các tệp lớn riêng lẻ.

### Tác vụ WinGet

#### Sử dụng các gói từ các nguồn khác ngoài winget (chẳng hạn như msstore)

Tác vụ winget tích hợp sẵn không hỗ trợ cài đặt các gói từ các nguồn khác ngoài kho lưu trữ `winget`. Nếu người dùng cần cài đặt các gói từ các nguồn như `msstore`, họ có thể sử dụng tác vụ `~/powershell` để chạy một tập lệnh PowerShell cài đặt gói bằng lệnh winget CLI trực tiếp.

##### **QUAN TRỌNG** Những cân nhắc quan trọng khi gọi trực tiếp winget CLI và sử dụng msstore

- Các gói từ nguồn `msstore` phải được cài đặt trong phần `userTasks` của tệp YAML. Điều này là do nguồn `msstore` yêu cầu ngữ cảnh người dùng để cài đặt các ứng dụng từ Microsoft Store.
- Lệnh `winget` CLI phải có sẵn trong biến môi trường PATH cho ngữ cảnh người dùng khi tác vụ `~/powershell` được chạy. Nếu lệnh `winget` CLI không có sẵn trong PATH, tác vụ sẽ không thực thi được.
- Bao gồm các cờ chấp nhận (`--accept-source-agreements`, `--accept-package-agreements`) để tránh các lời nhắc tương tác khi thực thi `winget install` trực tiếp.

### Lỗi ngữ cảnh tác vụ

#### Lỗi: "System tasks are not allowed in standard usercontext" (Tác vụ hệ thống không được phép trong ngữ cảnh người dùng tiêu chuẩn)

- Giải pháp: Chuyển các hoạt động quản trị sang phần `tasks`
- Đảm bảo bạn đang chạy các tùy chỉnh với các đặc quyền thích hợp khi
