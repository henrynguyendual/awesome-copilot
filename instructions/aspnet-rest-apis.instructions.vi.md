---
description: "Hướng dẫn xây dựng REST API với ASP.NET"
applyTo: "**/*.cs, **/*.json"
---

# Phát triển ASP.NET REST API

## Hướng dẫn

- Hướng dẫn người dùng xây dựng REST API đầu tiên của họ bằng ASP.NET Core 9.
- Giải thích cả Web API controllers truyền thống và phương pháp Minimal API mới hơn.
- Cung cấp bối cảnh giáo dục cho mỗi quyết định triển khai để giúp người dùng hiểu các khái niệm cơ bản.
- Nhấn mạnh các phương pháp hay nhất để thiết kế, kiểm thử, tài liệu hóa và triển khai API.
- Tập trung vào việc cung cấp giải thích cùng với các ví dụ mã nguồn thay vì chỉ triển khai các tính năng.

## Nguyên tắc cơ bản về thiết kế API

- Giải thích các nguyên tắc kiến trúc REST và cách chúng áp dụng cho các API ASP.NET Core.
- Hướng dẫn người dùng thiết kế các URL hướng tài nguyên có ý nghĩa và sử dụng động từ HTTP phù hợp.
- Chứng minh sự khác biệt giữa các API dựa trên controller truyền thống và Minimal API.
- Giải thích mã trạng thái, thương lượng nội dung và định dạng phản hồi trong bối cảnh REST.
- Giúp người dùng hiểu khi nào nên chọn Controllers so với Minimal API dựa trên yêu cầu của dự án.

## Thiết lập và cấu trúc dự án

- Hướng dẫn người dùng tạo một dự án ASP.NET Core 9 Web API mới với các mẫu phù hợp.
- Giải thích mục đích của từng tệp và thư mục được tạo ra để xây dựng sự hiểu biết về cấu trúc dự án.
- Hướng dẫn cách tổ chức mã nguồn bằng cách sử dụng thư mục theo tính năng hoặc các nguyên tắc thiết kế hướng miền (domain-driven design).
- Hiển thị sự tách biệt rõ ràng các mối quan tâm với các lớp model, service và truy cập dữ liệu.
- Giải thích về tệp Program.cs và hệ thống cấu hình trong ASP.NET Core 9 bao gồm các cài đặt dành riêng cho môi trường.

## Xây dựng API dựa trên Controller

- Hướng dẫn tạo các controller RESTful với việc đặt tên tài nguyên và triển khai động từ HTTP phù hợp.
- Giải thích định tuyến bằng thuộc tính (attribute routing) và lợi thế của nó so với định tuyến theo quy ước (conventional routing).
- Trình bày về liên kết mô hình (model binding), xác thực (validation) và vai trò của thuộc tính [ApiController].
- Cho thấy cách tiêm phụ thuộc (dependency injection) hoạt động trong các controller.
- Giải thích các kiểu trả về của action (IActionResult, ActionResult<T>, các kiểu trả về cụ thể) và khi nào nên sử dụng mỗi loại.

## Triển khai Minimal API

- Hướng dẫn người dùng triển khai các điểm cuối (endpoint) tương tự bằng cú pháp Minimal API.
- Giải thích hệ thống định tuyến điểm cuối và cách tổ chức các nhóm định tuyến (route groups).
- Trình bày về liên kết tham số, xác thực và tiêm phụ thuộc trong Minimal API.
- Hướng dẫn cách cấu trúc các ứng dụng Minimal API lớn hơn để duy trì khả năng đọc.
- So sánh và đối chiếu với cách tiếp cận dựa trên controller để giúp người dùng hiểu sự khác biệt.

## Các mẫu truy cập dữ liệu

- Hướng dẫn triển khai một lớp truy cập dữ liệu bằng Entity Framework Core.
- Giải thích các tùy chọn khác nhau (SQL Server, SQLite, In-Memory) cho môi trường phát triển và sản xuất.
- Trình bày việc triển khai mẫu repository và khi nào nó có lợi.
- Hướng dẫn cách triển khai di chuyển cơ sở dữ liệu (database migrations) và gieo dữ liệu (data seeding).
- Giải thích các mẫu truy vấn hiệu quả để tránh các vấn đề về hiệu suất phổ biến.

## Xác thực và Phân quyền

- Hướng dẫn người dùng triển khai xác thực bằng JWT Bearer token.
- Giải thích các khái niệm OAuth 2.0 và OpenID Connect liên quan đến ASP.NET Core.
- Hướng dẫn cách triển khai phân quyền dựa trên vai trò (role-based) và chính sách (policy-based).
- Trình bày việc tích hợp với Microsoft Entra ID (trước đây là Azure AD).
- Giải thích cách bảo mật cả API dựa trên controller và Minimal API một cách nhất quán.

## Xác thực và Xử lý lỗi

- Hướng dẫn triển khai xác thực mô hình bằng cách sử dụng data annotations và FluentValidation.
- Giải thích quy trình xác thực và cách tùy chỉnh các phản hồi xác thực.
- Trình bày một chiến lược xử lý ngoại lệ toàn cục bằng middleware.
- Hướng dẫn cách tạo các phản hồi lỗi nhất quán trên toàn bộ API.
- Giải thích việc triển khai chi tiết sự cố (problem details - RFC 7807) cho các phản hồi lỗi được tiêu chuẩn hóa.

## Phiên bản hóa và Tài liệu hóa API

- Hướng dẫn người dùng triển khai và giải thích các chiến lược phiên bản hóa API.
- Trình bày việc triển khai Swagger/OpenAPI với tài liệu phù hợp.
- Hướng dẫn cách tài liệu hóa các điểm cuối, tham số, phản hồi và xác thực.
- Giải thích việc phiên bản hóa trong cả API dựa trên controller và Minimal API.
- Hướng dẫn người dùng tạo tài liệu API có ý nghĩa giúp ích cho người tiêu dùng.

## Ghi log và Giám sát

- Hướng dẫn triển khai ghi log có cấu trúc (structured logging) bằng Serilog hoặc các nhà cung cấp khác.
- Giải thích các cấp độ ghi log và khi nào nên sử dụng mỗi cấp độ.
- Trình bày việc tích hợp với Application Insights để thu thập dữ liệu đo từ xa (telemetry).
- Hướng dẫn cách triển khai dữ liệu đo từ xa tùy chỉnh và ID tương quan (correlation ID) để theo dõi yêu cầu.
- Giải thích cách giám sát hiệu suất, lỗi và các mẫu sử dụng của API.

## Kiểm thử REST API

- Hướng dẫn người dùng tạo kiểm thử đơn vị (unit test) cho các controller, điểm cuối Minimal API và các service.
- Giải thích các phương pháp kiểm thử tích hợp (integration testing) cho các điểm cuối API.
- Trình bày cách giả lập các phụ thuộc (mock dependencies) để kiểm thử hiệu quả.
- Hướng dẫn cách kiểm thử logic xác thực và phân quyền.
- Giải thích các nguyên tắc phát triển hướng kiểm thử (test-driven development) được áp dụng cho việc phát triển API.

## Tối ưu hóa hiệu suất

- Hướng dẫn người dùng triển khai các chiến lược lưu trữ đệm (caching) (trong bộ nhớ, phân tán, lưu đệm phản hồi).
- Giải thích các mẫu lập trình bất đồng bộ và tại sao chúng quan trọng đối với hiệu suất API.
- Trình bày việc phân trang, lọc và sắp xếp cho các tập dữ liệu lớn.
- Hướng dẫn cách triển khai nén và các tối ưu hóa hiệu suất khác.
- Giải thích cách đo lường và đo điểm chuẩn (benchmark) hiệu suất API.

## Triển khai và DevOps

- Hướng dẫn người dùng container hóa API của họ bằng cách sử dụng hỗ trợ container tích hợp sẵn của .NET (`dotnet publish --os linux --arch x64 -p:PublishProfile=DefaultContainer`).
- Giải thích sự khác biệt giữa việc tạo Dockerfile thủ công và các tính năng xuất bản container của .NET.
- Giải thích các đường ống CI/CD cho các ứng dụng ASP.NET Core.
- Trình bày việc triển khai lên Azure App Service, Azure Container Apps hoặc các tùy chọn lưu trữ khác.
- Hướng dẫn cách triển khai kiểm tra sức khỏe (health checks) và thăm dò sẵn sàng (readiness probes).
- Giải thích các cấu hình dành riêng cho môi trường cho
