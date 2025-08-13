---
description: "Các mẫu component và ứng dụng Blazor"
applyTo: "**/*.razor, **/*.razor.cs, **/*.razor.css"
---

## Phong cách và Cấu trúc Code Blazor

- Viết mã Blazor và C# theo phong cách đặc trưng và hiệu quả.
- Tuân thủ các quy ước của .NET và Blazor.
- Sử dụng Razor Components một cách thích hợp để phát triển giao diện người dùng dựa trên component.
- Ưu tiên các hàm nội tuyến (inline functions) cho các component nhỏ nhưng tách logic phức tạp vào các lớp code-behind hoặc service.
- Nên sử dụng async/await ở những nơi thích hợp để đảm bảo các hoạt động UI không bị chặn.

## Quy ước Đặt tên

- Tuân thủ quy tắc PascalCase cho tên component, tên phương thức và các thành viên public.
- Sử dụng camelCase cho các trường private và biến cục bộ.
- Thêm tiền tố "I" cho tên interface (ví dụ: IUserService).

## Hướng dẫn Cụ thể cho Blazor và .NET

- Tận dụng các tính năng tích hợp sẵn của Blazor cho vòng đời của component (ví dụ: OnInitializedAsync, OnParametersSetAsync).
- Sử dụng data binding một cách hiệu quả với @bind.
- Tận dụng Dependency Injection cho các service trong Blazor.
- Cấu trúc các component và service của Blazor theo nguyên tắc Tách biệt các Mối quan tâm (Separation of Concerns).
- Luôn sử dụng phiên bản C# mới nhất, hiện tại là các tính năng của C# 13 như record types, pattern matching, và global usings.

## Xử lý Lỗi và Xác thực (Validation)

- Triển khai xử lý lỗi phù hợp cho các trang Blazor và các lệnh gọi API.
- Sử dụng ghi log (logging) để theo dõi lỗi ở backend và xem xét việc bắt lỗi ở cấp độ UI trong Blazor bằng các công cụ như ErrorBoundary.
- Triển khai xác thực bằng FluentValidation hoặc DataAnnotations trong các biểu mẫu (forms).

## API Blazor và Tối ưu hóa Hiệu năng

- Tận dụng Blazor server-side hoặc WebAssembly một cách tối ưu dựa trên yêu cầu của dự án.
- Sử dụng các phương thức bất đồng bộ (async/await) cho các lệnh gọi API hoặc các hành động UI có thể chặn luồng chính.
- Tối ưu hóa các component Razor bằng cách giảm các lần render không cần thiết và sử dụng StateHasChanged() một cách hiệu quả.
- Giảm thiểu cây render của component bằng cách tránh render lại khi không cần thiết, sử dụng ShouldRender() ở những nơi thích hợp.
- Sử dụng EventCallbacks để xử lý tương tác người dùng một cách hiệu quả, chỉ truyền dữ liệu tối thiểu khi kích hoạt sự kiện.

## Chiến lược Caching

- Triển khai caching trong bộ nhớ (in-memory caching) cho dữ liệu thường xuyên sử dụng, đặc biệt đối với các ứng dụng Blazor Server. Sử dụng IMemoryCache cho các giải pháp caching nhẹ.
- Đối với Blazor WebAssembly, sử dụng localStorage hoặc sessionStorage để cache trạng thái ứng dụng giữa các phiên làm việc của người dùng.
- Xem xét các chiến lược Distributed Cache (như Redis hoặc SQL Server Cache) cho các ứng dụng lớn cần trạng thái được chia sẻ giữa nhiều người dùng hoặc client.
- Cache các lệnh gọi API bằng cách lưu trữ các phản hồi để tránh các lệnh gọi dư thừa khi dữ liệu ít có khả năng thay đổi, từ đó cải thiện trải nghiệm người dùng.

## Thư viện Quản lý Trạng thái

- Sử dụng Cascading Parameters và EventCallbacks tích hợp sẵn của Blazor để chia sẻ trạng thái cơ bản giữa các component.
- Triển khai các giải pháp quản lý trạng thái nâng cao bằng các thư viện như Fluxor hoặc BlazorState khi ứng dụng trở nên phức tạp hơn.
- Để duy trì trạng thái phía client trong Blazor WebAssembly, hãy xem xét sử dụng Blazored.LocalStorage hoặc Blazored.SessionStorage để duy trì trạng thái sau khi tải lại trang.
- Đối với Blazor server-side, sử dụng Scoped Services và mẫu StateContainer để quản lý trạng thái trong các phiên làm việc của người dùng đồng thời giảm thiểu việc render lại.

## Thiết kế và Tích hợp API

- Sử dụng HttpClient hoặc các dịch vụ phù hợp khác để giao tiếp với các API bên ngoài hoặc backend của riêng bạn.
- Triển khai xử lý lỗi cho các lệnh gọi API bằng try-catch và cung cấp phản hồi phù hợp cho người dùng trong UI.

## Kiểm thử và Gỡ lỗi trong Visual Studio

- Tất cả kiểm thử đơn vị (unit testing) và kiểm thử tích hợp (integration testing) nên được thực hiện trong Visual Studio Enterprise.
- Kiểm thử các component và service của Blazor bằng xUnit, NUnit, hoặc MSTest.
- Sử dụng Moq hoặc NSubstitute để giả lập (mocking) các dependency trong quá trình kiểm thử.
- Gỡ lỗi các vấn đề về UI của Blazor bằng các công cụ dành cho nhà phát triển của trình duyệt và các công cụ gỡ lỗi của Visual Studio cho các vấn đề ở backend và server-side.
- Để phân tích và tối ưu hóa hiệu năng, hãy dựa vào các công cụ chẩn đoán của Visual Studio.

## Bảo mật và Xác thực

- Triển khai Xác thực (Authentication) và Phân quyền (Authorization) trong ứng dụng Blazor khi cần thiết bằng cách sử dụng ASP.NET Identity hoặc JWT token để xác thực API.
- Sử dụng HTTPS cho tất cả các giao tiếp web và đảm bảo các chính sách CORS phù hợp được triển khai.

## Tài liệu API và Swagger

- Sử dụng Swagger/OpenAPI để làm tài liệu cho các dịch vụ API backend của bạn.
- Đảm bảo có tài liệu XML cho các model và phương thức API để
