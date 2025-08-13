---
description: "Các mẫu thành phần và ứng dụng .NET MAUI"
applyTo: "**/*.xaml, **/*.cs"
---

# .NET MAUI

## Phong cách và cấu trúc mã .NET MAUI

- Viết mã .NET MAUI và C# hiệu quả và theo đặc ngữ.
- Tuân thủ các quy ước của .NET và .NET MAUI.
- Ưu tiên các hàm nội tuyến cho các thành phần nhỏ hơn nhưng tách logic phức tạp vào các lớp code-behind hoặc dịch vụ.
- Nên sử dụng async/await ở những nơi thích hợp để đảm bảo các hoạt động UI không bị chặn.

## Quy ước đặt tên

- Sử dụng PascalCase cho tên thành phần, tên phương thức và các thành viên công khai.
- Sử dụng camelCase cho các trường riêng tư và biến cục bộ.
- Thêm tiền tố "I" cho tên interface (ví dụ: IUserService).

## Hướng dẫn cụ thể cho .NET MAUI và .NET

- Tận dụng các tính năng tích hợp sẵn của .NET MAUI cho vòng đời thành phần (ví dụ: OnAppearing, OnDisappearing).
- Sử dụng liên kết dữ liệu (data binding) một cách hiệu quả với {Binding}.
- Cấu trúc các thành phần và dịch vụ .NET MAUI theo nguyên tắc Tách biệt các mối quan tâm (Separation of Concerns).
- Luôn sử dụng phiên bản C# mới nhất, hiện tại là các tính năng của C# 13 như record types, pattern matching và global usings.

## Xử lý lỗi và xác thực

- Triển khai xử lý lỗi phù hợp cho các trang .NET MAUI và các lệnh gọi API.
- Sử dụng ghi log để theo dõi lỗi ở backend và xem xét việc ghi lại các lỗi ở cấp độ UI trong MAUI bằng các công cụ như Logger của MAUI Community Toolkit.
- Triển khai xác thực trong các biểu mẫu bằng FluentValidation hoặc DataAnnotations.

## Tối ưu hóa API và hiệu suất MAUI

- Tận dụng các tính năng tích hợp sẵn của MAUI cho vòng đời thành phần (ví dụ: OnAppearing, OnDisappearing).
- Sử dụng các phương thức bất đồng bộ (async/await) cho các lệnh gọi API hoặc các hành động UI có thể chặn luồng chính.
- Tối ưu hóa các thành phần MAUI bằng cách giảm các lần render không cần thiết và sử dụng OnPropertyChanged() một cách hiệu quả.
- Giảm thiểu cây render thành phần bằng cách tránh render lại khi không cần thiết, sử dụng BatchBegin() và BatchCommit() ở những nơi thích hợp.

## Chiến lược lưu trữ đệm (Caching)

- Triển khai lưu trữ đệm trong bộ nhớ (in-memory caching) cho dữ liệu được sử dụng thường xuyên, đặc biệt cho các ứng dụng MAUI. Sử dụng IMemoryCache cho các giải pháp lưu trữ đệm nhẹ.
- Xem xét các chiến lược Distributed Cache (như Redis hoặc SQL Server Cache) cho các ứng dụng lớn hơn cần trạng thái được chia sẻ giữa nhiều người dùng hoặc máy khách.
- Lưu trữ đệm các lệnh gọi API bằng cách lưu trữ các phản hồi để tránh các lệnh gọi dư thừa khi dữ liệu ít có khả năng thay đổi, từ đó cải thiện trải nghiệm người dùng.

## Thư viện quản lý trạng thái

- Sử dụng dependency injection và .NET MAUI Community Toolkit để chia sẻ trạng thái giữa các thành phần.

## Thiết kế và tích hợp API

- Sử dụng HttpClient hoặc các dịch vụ phù hợp khác để giao tiếp với các API bên ngoài hoặc backend của riêng bạn.
- Triển khai xử lý lỗi cho các lệnh gọi API bằng try-catch và cung cấp phản hồi phù hợp cho người dùng trong UI.

## Kiểm thử và gỡ lỗi

- Kiểm thử các thành phần và dịch vụ bằng xUnit, NUnit hoặc MSTest.
- Sử dụng Moq hoặc NSubstitute để tạo mock các dependency trong quá trình kiểm thử.

## Bảo mật và xác thực

- Triển khai Xác thực và Ủy quyền trong ứng dụng MAUI khi cần thiết bằng cách sử dụng OAuth hoặc JWT token để xác thực API.
- Sử dụng HTTPS cho tất cả các giao tiếp web và đảm bảo các chính sách CORS phù hợp được triển khai.

## Tài liệu API và Swagger

- Sử dụng Swagger/OpenAPI để làm tài liệu cho các dịch vụ API backend của bạn.
- Đảm bảo có tài liệu XML cho các model và phương thức API để nâng cao tài
