---
mode: "agent"
description: "Đảm bảo mã .NET/C# đáp ứng các phương pháp hay nhất cho giải pháp/dự án."
---

# Các phương pháp hay nhất cho .NET/C#

Nhiệm vụ của bạn là đảm bảo mã .NET/C# trong ${selection} đáp ứng các phương pháp hay nhất dành riêng cho giải pháp/dự án này. Điều này bao gồm:

## Tài liệu & Cấu trúc

- Tạo các bình luận tài liệu XML toàn diện cho tất cả các lớp, giao diện, phương thức và thuộc tính công khai
- Bao gồm mô tả tham số và mô tả giá trị trả về trong các bình luận XML
- Tuân theo cấu trúc không gian tên đã được thiết lập: {Core|Console|App|Service}.{Feature}

## Mẫu thiết kế & Kiến trúc

- Sử dụng cú pháp hàm tạo chính (primary constructor) để tiêm phụ thuộc (ví dụ: `public class MyClass(IDependency dependency)`)
- Triển khai mẫu Command Handler với các lớp cơ sở generic (ví dụ: `CommandHandler<TOptions>`)
- Sử dụng phân tách giao diện (interface segregation) với quy ước đặt tên rõ ràng (tiền tố 'I' cho các giao diện)
- Tuân theo mẫu Factory để tạo đối tượng phức tạp.

## Tiêm phụ thuộc & Dịch vụ

- Sử dụng tiêm phụ thuộc qua hàm tạo (constructor dependency injection) với kiểm tra null thông qua ArgumentNullException
- Đăng ký các dịch vụ với vòng đời thích hợp (Singleton, Scoped, Transient)
- Sử dụng các mẫu của Microsoft.Extensions.DependencyInjection
- Triển khai các giao diện dịch vụ để có thể kiểm thử

## Quản lý tài nguyên & Bản địa hóa

- Sử dụng ResourceManager cho các thông báo và chuỗi lỗi đã được bản địa hóa
- Tách biệt các tệp tài nguyên LogMessages và ErrorMessages
- Truy cập tài nguyên thông qua `_resourceManager.GetString("MessageKey")`

## Các mẫu Async/Await

- Sử dụng async/await cho tất cả các hoạt động I/O và các tác vụ chạy dài
- Trả về Task hoặc Task<T> từ các phương thức bất đồng bộ
- Sử dụng ConfigureAwait(false) ở những nơi thích hợp
- Xử lý các ngoại lệ bất đồng bộ một cách đúng đắn

## Tiêu chuẩn kiểm thử

- Sử dụng framework MSTest với FluentAssertions để xác nhận
- Tuân theo mẫu AAA (Arrange, Act, Assert)
- Sử dụng Moq để giả lập (mocking) các phụ thuộc
- Kiểm thử cả kịch bản thành công và thất bại
- Bao gồm các bài kiểm thử xác thực tham số null

## Cấu hình & Cài đặt

- Sử dụng các lớp cấu hình được định kiểu mạnh (strongly-typed) với các thuộc tính dữ liệu (data annotations)
- Triển khai các thuộc tính xác thực (Required, NotEmptyOrWhitespace)
- Sử dụng IConfiguration binding cho các cài đặt
- Hỗ trợ các tệp cấu hình appsettings.json

## Tích hợp Semantic Kernel & AI

- Sử dụng Microsoft.SemanticKernel cho các hoạt động AI
- Triển khai cấu hình kernel và đăng ký dịch vụ phù hợp
- Xử lý các cài đặt mô hình AI (ChatCompletion, Embedding, v.v.)
- Sử dụng các mẫu đầu ra có cấu trúc để có phản hồi AI đáng tin cậy

## Xử lý lỗi & Ghi log

- Sử dụng ghi log có cấu trúc với Microsoft.Extensions.Logging
- Bao gồm ghi log theo phạm vi (scoped logging) với ngữ cảnh có ý nghĩa
- Ném ra các ngoại lệ cụ thể với thông báo mô tả rõ ràng
- Sử dụng các khối try-catch cho các kịch bản lỗi có thể lường trước

## Hiệu suất & Bảo mật

- Sử dụng các tính năng của C# 12+ và các tối ưu hóa của .NET 8 ở những nơi có thể áp dụng
- Triển khai xác thực và làm sạch đầu vào đúng cách
- Sử dụng các truy vấn có tham số cho các hoạt động cơ sở dữ liệu
- Tuân thủ các phương pháp lập trình an toàn cho các hoạt động AI/ML

## Chất lượng mã nguồn

- Đảm bảo tuân thủ các nguyên tắc SOLID
- Tránh trùng lặp mã thông qua các lớp cơ sở và các tiện ích
- Sử dụng tên có ý nghĩa phản ánh các khái niệm trong miền nghiệp vụ
- Giữ cho các phương thức tập trung và gắn kết
- Triển khai các mẫu giải phóng tài nguyên (disposal patterns)
