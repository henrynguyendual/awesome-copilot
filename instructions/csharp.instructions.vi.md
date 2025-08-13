---
description: "Hướng dẫn xây dựng ứng dụng C#"
applyTo: "**/*.cs"
---

# Phát triển C#

## Hướng dẫn C#

- Luôn sử dụng phiên bản C# mới nhất, hiện tại là các tính năng của C# 13.
- Viết bình luận rõ ràng và ngắn gọn cho mỗi hàm.

## Hướng dẫn chung

- Chỉ đưa ra các đề xuất có độ tin cậy cao khi xem xét các thay đổi về mã.
- Viết mã với các phương pháp bảo trì tốt, bao gồm các bình luận về lý do tại sao một số quyết định thiết kế được đưa ra.
- Xử lý các trường hợp đặc biệt và viết xử lý ngoại lệ rõ ràng.
- Đối với các thư viện hoặc phụ thuộc bên ngoài, hãy đề cập đến cách sử dụng và mục đích của chúng trong các bình luận.

## Quy ước đặt tên

- Tuân theo PascalCase cho tên thành phần, tên phương thức và các thành viên công khai.
- Sử dụng camelCase cho các trường riêng tư và biến cục bộ.
- Thêm tiền tố "I" vào tên giao diện (ví dụ: IUserService).

## Định dạng

- Áp dụng kiểu định dạng mã được xác định trong `.editorconfig`.
- Ưu tiên khai báo không gian tên trong phạm vi tệp và các chỉ thị `using` trên một dòng.
- Chèn một dòng mới trước dấu ngoặc nhọn mở của bất kỳ khối mã nào (ví dụ: sau `if`, `for`, `while`, `foreach`, `using`, `try`, v.v.).
- Đảm bảo rằng câu lệnh `return` cuối cùng của một phương thức nằm trên một dòng riêng.
- Sử dụng đối sánh mẫu và biểu thức `switch` bất cứ khi nào có thể.
- Sử dụng `nameof` thay vì chuỗi ký tự khi tham chiếu đến tên thành viên.
- Đảm bảo rằng các bình luận tài liệu XML được tạo cho bất kỳ API công khai nào. Khi có thể, hãy bao gồm tài liệu `<example>` và `<code>` trong các bình luận.

## Thiết lập và cấu trúc dự án

- Hướng dẫn người dùng tạo một dự án .NET mới với các mẫu thích hợp.
- Giải thích mục đích của từng tệp và thư mục được tạo để xây dựng sự hiểu biết về cấu trúc dự án.
- Minh họa cách tổ chức mã bằng cách sử dụng các thư mục tính năng hoặc các nguyên tắc thiết kế theo miền.
- Hiển thị sự phân tách hợp lý các mối quan tâm với các lớp mô hình, dịch vụ và truy cập dữ liệu.
- Giải thích Program.cs và hệ thống cấu hình trong ASP.NET Core 9 bao gồm các cài đặt dành riêng cho môi trường.

## Kiểu tham chiếu có thể rỗng (Nullable Reference Types)

- Khai báo các biến không thể rỗng và kiểm tra `null` tại các điểm vào.
- Luôn sử dụng `is null` hoặc `is not null` thay vì `== null` hoặc `!= null`.
- Tin tưởng vào các chú thích null của C# và không thêm các kiểm tra null khi hệ thống kiểu cho biết một giá trị không thể là null.

## Mẫu truy cập dữ liệu

- Hướng dẫn triển khai lớp truy cập dữ liệu bằng Entity Framework Core.
- Giải thích các tùy chọn khác nhau (SQL Server, SQLite, In-Memory) cho phát triển và sản xuất.
- Minh họa việc triển khai mẫu repository và khi nào nó có lợi.
- Hướng dẫn cách triển khai di chuyển cơ sở dữ liệu và gieo dữ liệu.
- Giải thích các mẫu truy vấn hiệu quả để tránh các vấn đề về hiệu suất phổ biến.

## Xác thực và Ủy quyền

- Hướng dẫn người dùng triển khai xác thực bằng mã thông báo JWT Bearer.
- Giải thích các khái niệm OAuth 2.0 và OpenID Connect liên quan đến ASP.NET Core.
- Hướng dẫn cách triển khai ủy quyền dựa trên vai trò và dựa trên chính sách.
- Minh họa việc tích hợp với Microsoft Entra ID (trước đây là Azure AD).
- Giải thích cách bảo mật cả API dựa trên bộ điều khiển và API tối giản một cách nhất quán.

## Xác thực và Xử lý lỗi

- Hướng dẫn triển khai xác thực mô hình bằng cách sử dụng chú thích dữ liệu và FluentValidation.
- Giải thích quy trình xác thực và cách tùy chỉnh các phản hồi xác thực.
- Minh họa một chiến lược xử lý ngoại lệ toàn cục bằng cách sử dụng middleware.
- Hướng dẫn cách tạo các phản hồi lỗi nhất quán trên toàn bộ API.
- Giải thích việc triển khai chi tiết sự cố (RFC 7807) cho các phản hồi lỗi được tiêu chuẩn hóa.

## Phiên bản và Tài liệu API

- Hướng dẫn người dùng triển khai và giải thích các chiến lược phiên bản API.
- Minh họa việc triển khai Swagger/OpenAPI với tài liệu phù hợp.
- Hướng dẫn cách lập tài liệu cho các điểm cuối, tham số, phản hồi và xác thực.
- Giải thích việc tạo phiên bản trong cả API dựa trên bộ điều khiển và API tối giản.
- Hướng dẫn người dùng tạo tài liệu API có ý nghĩa giúp ích cho người tiêu dùng.

## Ghi nhật ký và Giám sát

- Hướng dẫn triển khai ghi nhật ký có cấu trúc bằng Serilog hoặc các nhà cung cấp khác.
- Giải thích các cấp độ ghi nhật ký và khi nào nên sử dụng mỗi cấp độ.
- Minh họa việc tích hợp với Application Insights để thu thập dữ liệu đo từ xa.
- Hướng dẫn cách triển khai dữ liệu đo từ xa tùy chỉnh và ID tương quan để theo dõi yêu cầu.
- Giải thích cách giám sát hiệu suất, lỗi và các mẫu sử dụng API.

## Kiểm thử

- Luôn bao gồm các trường hợp kiểm thử cho các đường dẫn quan trọng của ứng dụng.
- Hướng dẫn người dùng tạo các bài kiểm thử đơn vị.
- Không đưa ra các bình luận "Act", "Arrange" hoặc "Assert".
- Sao chép kiểu hiện có trong các tệp lân cận cho tên phương thức kiểm thử và cách viết hoa.
- Giải thích các phương pháp kiểm thử tích hợp cho các điểm cuối API.
- Minh họa cách giả lập các phụ thuộc để kiểm thử hiệu quả.
- Hướng dẫn cách kiểm thử logic xác thực và ủy quyền.
- Giải thích các nguyên tắc phát triển dựa trên kiểm thử được áp dụng cho phát triển API.

## Tối ưu hóa hiệu suất

- Hướng dẫn người dùng triển khai các chiến lược bộ nhớ đệm (trong bộ nhớ, phân tán, bộ nhớ đệm phản hồi).
- Giải thích các mẫu lập trình không đồng bộ và tại sao chúng quan trọng đối với hiệu suất API.
- Minh họa việc phân trang, lọc và sắp xếp cho các tập dữ liệu lớn.
- Hướng dẫn cách triển khai nén và các tối ưu hóa hiệu suất khác.
- Giải thích cách đo lường và đánh giá hiệu suất API.

## Triển khai và DevOps

- Hướng dẫn người dùng đóng gói API của họ bằng cách sử dụng hỗ trợ container tích hợp sẵn của .NET (`dotnet publish --os linux --arch x64 -p:PublishProfile=DefaultContainer`).
- Giải thích sự khác biệt giữa việc tạo Dockerfile thủ công và các tính năng xuất bản container của .NET.
- Giải thích các quy trình CI/CD cho các ứng dụng .NET.
- Minh họa việc triển khai lên Azure App Service, Azure Container Apps hoặc các tùy chọn lưu trữ khác.
- Hướng dẫn cách triển khai kiểm tra tình trạng và thăm dò sẵn sàng.
- Giải thích các cấu hình dành riêng cho môi trường cho các giai đoạn triển
