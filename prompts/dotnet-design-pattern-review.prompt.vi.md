---
mode: "agent"
description: "Đánh giá mã C#/.NET về việc triển khai mẫu thiết kế và đề xuất các cải tiến."
---

# Đánh giá Mẫu thiết kế .NET/C#

Đánh giá mã C#/.NET trong ${selection} về việc triển khai mẫu thiết kế và đề xuất các cải tiến cho giải pháp/dự án. Không thực hiện bất kỳ thay đổi nào đối với mã, chỉ cung cấp một bài đánh giá.

## Các Mẫu thiết kế Bắt buộc

- **Command Pattern**: Các lớp cơ sở generic (`CommandHandler<TOptions>`), interface `ICommandHandler<TOptions>`, kế thừa `CommandHandlerOptions`, các phương thức tĩnh `SetupCommand(IHost host)`
- **Factory Pattern**: Tích hợp service provider để tạo đối tượng phức tạp
- **Dependency Injection**: Cú pháp primary constructor, kiểm tra null bằng `ArgumentNullException`, trừu tượng hóa qua interface, vòng đời dịch vụ phù hợp
- **Repository Pattern**: Các interface truy cập dữ liệu bất đồng bộ, trừu tượng hóa provider cho các kết nối
- **Provider Pattern**: Trừu tượng hóa dịch vụ bên ngoài (cơ sở dữ liệu, AI), hợp đồng rõ ràng, xử lý cấu hình
- **Resource Pattern**: ResourceManager cho các thông điệp đã được bản địa hóa, các tệp .resx riêng biệt (LogMessages, ErrorMessages)

## Danh sách kiểm tra Đánh giá

- **Mẫu thiết kế**: Xác định các mẫu được sử dụng. Các mẫu Command Handler, Factory, Provider và Repository có được triển khai đúng cách không? Có thiếu các mẫu hữu ích nào không?
- **Kiến trúc**: Có tuân theo quy ước không gian tên (`{Core|Console|App|Service}.{Feature}`)? Có sự tách biệt phù hợp giữa các dự án Core/Console không? Có dạng mô-đun và dễ đọc không?
- **Thực hành tốt nhất của .NET**: Primary constructor, async/await với kiểu trả về là Task, sử dụng ResourceManager, ghi log có cấu trúc, cấu hình được định kiểu mạnh?
- **Mẫu GoF**: Các mẫu Command, Factory, Template Method, Strategy có được triển khai đúng cách không?
- **Nguyên tắc SOLID**: Có vi phạm các nguyên tắc Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion không?
- **Hiệu suất**: Sử dụng async/await đúng cách, giải phóng tài nguyên, ConfigureAwait(false), cơ hội xử lý song song?
- **Khả năng bảo trì**: Tách biệt rõ ràng các mối quan tâm, xử lý lỗi nhất quán, sử dụng cấu hình đúng cách?
- **Khả năng kiểm thử**: Các phụ thuộc được trừu tượng hóa qua interface, các thành phần có thể mock, khả năng kiểm thử bất đồng bộ, tương thích với mẫu AAA?
- **Bảo mật**: Xác thực đầu vào, xử lý thông tin xác thực an toàn, truy vấn có tham số, xử lý ngoại lệ an toàn?
- **Tài liệu**: Tài liệu XML cho các API công khai, mô tả tham số/giá trị trả về, tổ chức tệp tài nguyên?
- **Độ rõ ràng của mã**: Tên có ý nghĩa phản ánh các khái niệm miền, mục đích rõ ràng thông qua các mẫu, cấu trúc tự giải thích?
- **Mã sạch**: Phong cách nhất quán, kích thước phương thức/lớp phù hợp, độ phức tạp tối thiểu, loại bỏ sự trùng lặp?

## Các lĩnh vực cần tập trung cải tiến

- **Command Handlers**: Xác thực trong lớp cơ sở, xử lý lỗi nhất quán, quản lý tài nguyên đúng cách
- **Factories**: Cấu hình phụ thuộc, tích hợp service provider, các mẫu giải phóng tài nguyên (disposal patterns)
- **Providers**: Quản lý kết nối, các mẫu bất đồng bộ, xử lý ngoại lệ và ghi log
- **Cấu hình**: Data annotations, các thuộc tính xác thực, xử lý giá trị nhạy cảm một cách an toàn
- **Tích hợp AI/ML**: Các mẫu Semantic Kernel, xử lý đầu ra có cấu trúc, cấu hình mô hình

Cung cấp các đề xuất cụ thể, có thể hành động để cải tiến phù hợp với kiến trúc của dự án và các phương pháp thực hành tốt
