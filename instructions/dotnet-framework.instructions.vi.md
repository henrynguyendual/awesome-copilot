---
description: "Hướng dẫn làm việc với các dự án .NET Framework. Bao gồm cấu trúc dự án, phiên bản ngôn ngữ C#, quản lý NuGet và các phương pháp hay nhất."
applyTo: "**/*.csproj, **/*.cs"
---

# Phát triển .NET Framework

## Yêu cầu về Build và Biên dịch

- Luôn sử dụng `msbuild /t:rebuild` để build solution hoặc project thay vì `dotnet build`

## Quản lý Tệp Dự án

### Cấu trúc Dự án Kiểu không phải SDK

Các dự án .NET Framework sử dụng định dạng dự án cũ, khác biệt đáng kể so với các dự án kiểu SDK hiện đại:

- **Bao gồm Tệp một cách tường minh**: Tất cả các tệp nguồn mới **PHẢI** được thêm một cách tường minh vào tệp dự án (`.csproj`) bằng cách sử dụng phần tử `<Compile>`

  - Các dự án .NET Framework không tự động bao gồm các tệp trong thư mục như các dự án kiểu SDK
  - Ví dụ: `<Compile Include="Path\To\NewFile.cs" />`

- **Không có Import ngầm định**: Không giống như các dự án kiểu SDK, các dự án .NET Framework không tự động import các không gian tên (namespaces) hoặc assembly phổ biến

- **Cấu hình Build**: Chứa các mục `<PropertyGroup>` tường minh cho các cấu hình Debug/Release

- **Đường dẫn Đầu ra**: Các định nghĩa `<OutputPath>` và `<IntermediateOutputPath>` tường minh

- **Framework Mục tiêu**: Sử dụng `<TargetFrameworkVersion>` thay vì `<TargetFramework>`
  - Ví dụ: `<TargetFrameworkVersion>v4.7.2</TargetFrameworkVersion>`

## Quản lý Gói NuGet

- Việc cài đặt và cập nhật các gói NuGet trong các dự án .NET Framework là một công việc phức tạp, đòi hỏi các thay đổi phối hợp trên nhiều tệp. Do đó, **không cố gắng cài đặt hoặc cập nhật các gói NuGet** trong dự án này.
- Thay vào đó, nếu cần thay đổi các tham chiếu NuGet, hãy yêu cầu người dùng cài đặt hoặc cập nhật các gói NuGet bằng Visual Studio NuGet Package Manager hoặc Visual Studio package manager console.
- Khi đề xuất các gói NuGet, hãy đảm bảo chúng tương thích với .NET Framework hoặc .NET Standard 2.0 (không chỉ .NET Core hoặc .NET 5+).

## Phiên bản Ngôn ngữ C# là 7.3

- Dự án này chỉ giới hạn ở các tính năng của C# 7.3. Vui lòng tránh sử dụng:

### Các tính năng C# 8.0+ (KHÔNG HỖ TRỢ):

- Khai báo using (`using var stream = ...`)
- Câu lệnh Await using (`await using var resource = ...`)
- Biểu thức switch (`variable switch { ... }`)
- Phép gán null-coalescing (`??=`)
- Toán tử range và index (`array[1..^1]`, `array[^1]`)
- Phương thức giao diện mặc định (Default interface methods)
- Thành viên chỉ đọc (Readonly members) trong struct
- Hàm cục bộ tĩnh (Static local functions)
- Kiểu tham chiếu có thể null (`string?`, `#nullable enable`)

### Các tính năng C# 9.0+ (KHÔNG HỖ TRỢ):

- Records (`public record Person(string Name)`)
- Thuộc tính chỉ khởi tạo (Init-only properties) (`{ get; init; }`)
- Chương trình cấp cao nhất (Top-level programs) (chương trình không có phương thức Main)
- Các cải tiến về pattern matching
- Biểu thức new theo kiểu mục tiêu (`List<string> list = new()`)

### Các tính năng C# 10+ (KHÔNG HỖ TRỢ):

- Câu lệnh global using
- Không gian tên phạm vi tệp (File-scoped namespaces)
- Record structs
- Thành viên bắt buộc (Required members)

### Sử dụng thay thế (Tương thích C# 7.3):

- Câu lệnh using truyền thống với dấu ngoặc nhọn
- Câu lệnh switch thay vì biểu thức switch
- Kiểm tra null tường minh thay vì phép gán null-coalescing
- Cắt mảng bằng cách lập chỉ mục thủ công
- Lớp trừu tượng (Abstract classes) hoặc giao diện (interfaces) thay vì phương thức giao diện mặc định

## Lưu ý về Môi trường (môi trường Windows)

- Sử dụng đường dẫn kiểu Windows với dấu gạch chéo ngược (ví dụ: `C:\path\to\file.cs`)
- Sử dụng các lệnh phù hợp với Windows khi đề xuất các thao tác trên terminal
- Xem xét các hành vi cụ thể của Windows khi làm việc với các hoạt động hệ thống tệp

## Các Cạm bẫy và Phương pháp hay nhất phổ biến của .NET Framework

### Mẫu Async/Await

- **ConfigureAwait(false)**: Luôn sử dụng `ConfigureAwait(false)` trong mã thư viện để tránh deadlock:
  ```csharp
  var result = await SomeAsyncMethod().ConfigureAwait(false);
  ```
- **Tránh sync-over-async**: Không sử dụng `.Result` hoặc `.Wait()` hoặc `.GetAwaiter().GetResult()`. Các mẫu sync-over-async này có thể dẫn đến deadlock và hiệu suất kém. Luôn sử dụng `await` cho các lệnh gọi bất đồng bộ.

### Xử lý DateTime

- **Sử dụng DateTimeOffset cho dấu thời gian**: Ưu tiên `DateTimeOffset` hơn `DateTime` cho các điểm thời gian tuyệt đối
- **Chỉ định DateTimeKind**: Khi sử dụng `DateTime`, luôn chỉ định `DateTimeKind.Utc` hoặc `DateTimeKind.Local`
- **Định dạng theo văn hóa**: Sử dụng `CultureInfo.InvariantCulture` để tuần tự hóa/phân tích cú pháp

### Thao tác Chuỗi

- **StringBuilder để nối chuỗi**: Sử dụng `StringBuilder` cho nhiều lần nối chuỗi
- **StringComparison**: Luôn chỉ định `StringComparison` cho các thao tác chuỗi:
  ```csharp
  string.Equals(other, StringComparison.OrdinalIgnoreCase)
  ```

### Quản lý Bộ nhớ

- **Mẫu Dispose**: Triển khai `IDisposable` đúng cách cho các tài nguyên không được quản lý
- **Câu lệnh using**: Luôn bọc các đối tượng `IDisposable` trong câu lệnh using
- **Tránh Large Object Heap (LOH)**: Giữ các đối tượng dưới 85KB để tránh phân bổ LOH

### Cấu hình

- **Sử dụng ConfigurationManager**: Truy cập cài đặt ứng dụng thông qua `ConfigurationManager.AppSettings`
- **Chuỗi kết nối**: Lưu trữ trong mục `<connectionStrings>`, không phải `<appSettings>`
- **Biến đổi (Transformations)**: Sử dụng biến đổi web.config/app.config cho các cài đặt dành riêng cho môi trường

### Xử lý Ngoại lệ

- **Ngoại lệ cụ thể**: Bắt các loại ngoại lệ cụ thể, không phải `Exception` chung
- **Không "nuốt" ngoại lệ**: Luôn ghi log hoặc ném lại ngoại lệ một cách thích hợp
- **Sử dụng using cho tài nguyên disposable**: Đảm bảo dọn dẹp đúng cách ngay cả khi xảy ra ngoại lệ

### Cân nhắc về Hiệu suất

- **Tránh boxing**: Lưu ý về boxing/unboxing với các kiểu giá trị và generics
- **String interning**: Sử dụng `string.Intern()` một cách thận trọng cho các chuỗi được sử dụng thường xuyên
- **Khởi tạo lười (Lazy initialization)**: Sử dụng `Lazy<T>` cho việc tạo đối tượng tốn kém
- **Tránh reflection trong các đường dẫn nóng (hot paths)**: Cache các đối tượng `MethodInfo`, `PropertyInfo` khi có thể
