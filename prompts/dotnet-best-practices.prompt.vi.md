# Thực hành tốt nhất với .NET/C#

Nhiệm vụ của bạn là đảm bảo mã .NET/C# trong ${selection} tuân thủ các thực hành tốt nhất dành riêng cho giải pháp/dự án này. Bao gồm:

## Tài liệu & Cấu trúc

- Tạo chú thích tài liệu XML đầy đủ cho tất cả các lớp, interface, phương thức và thuộc tính public
- Bao gồm mô tả tham số và giá trị trả về trong tài liệu XML
- Tuân thủ cấu trúc namespace đã thiết lập: {Core|Console|App|Service}.{Feature}

## Mẫu thiết kế & Kiến trúc

- Sử dụng cú pháp constructor chính cho dependency injection (ví dụ: `public class MyClass(IDependency dependency)`)
- Triển khai mẫu Command Handler với các lớp cơ sở generic (ví dụ: `CommandHandler<TOptions>`)
- Áp dụng nguyên tắc phân tách interface với quy tắc đặt tên rõ ràng (tiền tố 'I' cho interface)
- Sử dụng mẫu Factory cho việc tạo đối tượng phức tạp

## Dependency Injection & Dịch vụ

- Sử dụng constructor injection với kiểm tra null bằng ArgumentNullException
- Đăng ký service với vòng đời phù hợp (Singleton, Scoped, Transient)
- Sử dụng pattern Microsoft.Extensions.DependencyInjection
- Triển khai interface dịch vụ để dễ dàng kiểm thử

## Quản lý tài nguyên & Đa ngôn ngữ

- Sử dụng ResourceManager cho thông điệp và chuỗi lỗi đa ngôn ngữ
- Tách riêng file LogMessages và ErrorMessages
- Truy cập resource qua `_resourceManager.GetString("MessageKey")`

## Mẫu Async/Await

- Sử dụng async/await cho tất cả thao tác I/O và tác vụ chạy lâu
- Trả về Task hoặc Task<T> từ phương thức async
- Sử dụng ConfigureAwait(false) khi phù hợp
- Xử lý ngoại lệ async đúng cách

## Tiêu chuẩn kiểm thử

- Sử dụng MSTest framework với FluentAssertions cho assert
- Tuân thủ mô hình AAA (Arrange, Act, Assert)
- Sử dụng Moq để mock dependency
- Kiểm thử cả trường hợp thành công và thất bại
- Bao gồm kiểm thử xác minh tham số null

## Cấu hình & Cài đặt

- Sử dụng lớp cấu hình kiểu mạnh (strongly-typed) với data annotation
- Triển khai attribute xác thực (Required, NotEmptyOrWhitespace)
- Sử dụng IConfiguration binding cho cài đặt
- Hỗ trợ file cấu hình appsettings.json

## Semantic Kernel & Tích hợp AI

- Sử dụng Microsoft.SemanticKernel cho các thao tác AI
- Triển khai cấu hình kernel và đăng ký dịch vụ đúng cách
- Xử lý cài đặt mô hình AI (ChatCompletion, Embedding, ...)
- Sử dụng mẫu output có cấu trúc để đảm bảo phản hồi AI đáng tin cậy

## Xử lý lỗi & Ghi log

- Sử dụng structured logging với Microsoft.Extensions.Logging
- Bao gồm scoped logging với ngữ cảnh ý nghĩa
- Ném ngoại lệ cụ thể với thông điệp mô tả
- Sử dụng try-catch cho các tình huống lỗi dự kiến

## Hiệu năng & Bảo mật

- Sử dụng tính năng C# 12+ và tối ưu hóa .NET 8 khi có thể
- Thực hiện xác thực và làm sạch dữ liệu đầu vào
- Sử dụng truy vấn có tham số cho thao tác DB
- Tuân thủ nguyên tắc lập trình an toàn cho AI/ML

## Chất lượng mã

- Đảm bảo tuân thủ nguyên tắc SOLID
- Tránh lặp code bằng cách sử dụng lớp cơ sở và tiện ích
- Sử dụng tên biến/hàm có ý nghĩa và phản ánh đúng domain
- Giữ phương thức tập trung và mạch lạc
- Triển khai pattern dispose hợp lý cho tài nguyên
