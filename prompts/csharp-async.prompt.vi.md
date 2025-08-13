# Thực Hành Tốt Nhất Cho Lập Trình Bất Đồng Bộ (Async) Trong C#

Mục tiêu của bạn là giúp tôi tuân theo các thực hành tốt nhất khi lập trình bất đồng bộ trong C#.

## Quy Tắc Đặt Tên

- Sử dụng hậu tố 'Async' cho tất cả các phương thức async
- Giữ tên phương thức khớp với phiên bản đồng bộ nếu có (ví dụ: `GetDataAsync()` cho `GetData()`)

## Kiểu Trả Về

- Trả về `Task<T>` khi phương thức trả về giá trị
- Trả về `Task` khi phương thức không trả về giá trị
- Cân nhắc `ValueTask<T>` trong các tình huống yêu cầu hiệu năng cao để giảm cấp phát bộ nhớ
- Tránh trả về `void` cho phương thức async ngoại trừ các event handler

## Xử Lý Ngoại Lệ

- Dùng khối try/catch bao quanh các biểu thức `await`
- Tránh nuốt ngoại lệ trong phương thức async
- Sử dụng `ConfigureAwait(false)` khi thích hợp để tránh deadlock trong code thư viện
- Truyền ngoại lệ bằng `Task.FromException()` thay vì throw trực tiếp trong các phương thức trả về Task async

## Hiệu Năng

- Dùng `Task.WhenAll()` để thực hiện song song nhiều tác vụ
- Dùng `Task.WhenAny()` để triển khai timeout hoặc lấy task hoàn thành đầu tiên
- Tránh sử dụng async/await không cần thiết khi chỉ trả về kết quả từ Task
- Cân nhắc sử dụng CancellationToken cho các tác vụ chạy lâu

## Lỗi Thường Gặp

- Không bao giờ sử dụng `.Wait()`, `.Result` hoặc `.GetAwaiter().GetResult()` trong code async
- Tránh trộn lẫn code đồng bộ và async
- Không tạo phương thức async void (ngoại trừ event handler)
- Luôn `await` các phương thức trả về Task

## Mẫu Triển Khai

- Triển khai pattern async command cho các tác vụ chạy lâu
- Sử dụng async streams (`IAsyncEnumerable<T>`) để xử lý chuỗi dữ liệu bất đồng bộ
- Cân nhắc sử dụng Task-based Asynchronous Pattern (TAP) cho các API public

Khi review code C#, hãy xác định các vấn đề này và đề xuất cải tiến để tuân theo các thực hành tốt nhất này.