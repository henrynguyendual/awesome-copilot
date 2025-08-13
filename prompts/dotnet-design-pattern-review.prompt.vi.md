# Đánh giá Mẫu thiết kế .NET/C#

Đánh giá mã C#/.NET trong ${selection} về việc triển khai các mẫu thiết kế và đề xuất cải tiến cho giải pháp/dự án. Không thay đổi mã, chỉ cung cấp đánh giá.

## Các mẫu thiết kế yêu cầu

- **Command Pattern**: Các lớp cơ sở generic (`CommandHandler<TOptions>`), interface `ICommandHandler<TOptions>`, kế thừa `CommandHandlerOptions`, phương thức tĩnh `SetupCommand(IHost host)`
- **Factory Pattern**: Tích hợp dịch vụ tạo đối tượng phức tạp với service provider
- **Dependency Injection**: Cú pháp constructor chính, kiểm tra null với `ArgumentNullException`, trừu tượng hóa qua interface, vòng đời service phù hợp
- **Repository Pattern**: Interface truy xuất dữ liệu bất đồng bộ, trừu tượng hóa kết nối
- **Provider Pattern**: Trừu tượng hóa dịch vụ bên ngoài (cơ sở dữ liệu, AI), hợp đồng rõ ràng, xử lý cấu hình
- **Resource Pattern**: Sử dụng ResourceManager cho thông điệp đa ngôn ngữ, tách riêng file .resx (LogMessages, ErrorMessages)

## Checklist đánh giá

- **Mẫu thiết kế**: Xác định mẫu đã sử dụng. Các mẫu Command Handler, Factory, Provider, Repository có được triển khai đúng? Có thiếu mẫu hữu ích nào không?
- **Kiến trúc**: Tuân thủ quy tắc namespace (`{Core|Console|App|Service}.{Feature}`)? Phân tách đúng giữa Core/Console? Mô-đun hóa và dễ đọc?
- **Thực hành tốt .NET**: Constructor chính, async/await trả về Task, dùng ResourceManager, logging có cấu trúc, cấu hình kiểu mạnh?
- **Mẫu GoF**: Command, Factory, Template Method, Strategy có được triển khai đúng?
- **Nguyên tắc SOLID**: Có vi phạm SRP, OCP, LSP, ISP, DIP?
- **Hiệu năng**: Sử dụng async/await hợp lý, giải phóng tài nguyên, ConfigureAwait(false), tận dụng xử lý song song?
- **Dễ bảo trì**: Phân tách trách nhiệm rõ ràng, xử lý lỗi nhất quán, cấu hình hợp lý?
- **Khả năng kiểm thử**: Phụ thuộc được trừu tượng hóa qua interface, có thể mock, hỗ trợ kiểm thử async, tuân thủ AAA?
- **Bảo mật**: Xác thực đầu vào, bảo mật thông tin nhạy cảm, truy vấn có tham số, xử lý ngoại lệ an toàn?
- **Tài liệu**: XML doc cho API public, mô tả tham số/giá trị trả về, tổ chức file resource hợp lý?
- **Độ rõ ràng**: Tên biến/hàm phản ánh đúng domain, ý đồ rõ qua mẫu thiết kế, cấu trúc dễ hiểu?
- **Clean Code**: Phong cách nhất quán, kích thước phương thức/lớp hợp lý, độ phức tạp tối thiểu, loại bỏ trùng lặp?

## Các điểm cải tiến nên tập trung

- **Command Handlers**: Xác thực trong lớp cơ sở, xử lý lỗi nhất quán, quản lý tài nguyên hợp lý
- **Factories**: Cấu hình dependency, tích hợp service provider, pattern dispose hợp lý
- **Providers**: Quản lý kết nối, async pattern, xử lý ngoại lệ và logging
- **Cấu hình**: Data annotation, attribute xác thực, bảo mật giá trị nhạy cảm
- **Tích hợp AI/ML**: Semantic Kernel pattern, xử lý output có cấu trúc, cấu hình mô hình
