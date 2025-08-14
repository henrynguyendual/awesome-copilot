---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Nhận các phương pháp hay nhất cho lập trình bất đồng bộ trong C#"
---

# Các phương pháp hay nhất cho Lập trình bất đồng bộ trong C#

Mục tiêu của bạn là giúp tôi tuân theo các phương pháp hay nhất cho lập trình bất đồng bộ trong C#.

## Quy ước đặt tên

- Sử dụng hậu tố 'Async' cho tất cả các phương thức bất đồng bộ
- Tên phương thức phải khớp với các phương thức đồng bộ tương ứng khi có thể (ví dụ: `GetDataAsync()` cho `GetData()`)

## Kiểu trả về

- Trả về `Task<T>` khi phương thức trả về một giá trị
- Trả về `Task` khi phương thức không trả về giá trị
- Cân nhắc `ValueTask<T>` cho các kịch bản yêu cầu hiệu năng cao để giảm việc cấp phát bộ nhớ
- Tránh trả về `void` cho các phương thức bất đồng bộ, ngoại trừ các trình xử lý sự kiện (event handlers)

## Xử lý ngoại lệ (Exception Handling)

- Sử dụng khối try/catch xung quanh các biểu thức `await`
- Tránh "nuốt" ngoại lệ (swallowing exceptions) trong các phương thức bất đồng bộ
- Sử dụng `ConfigureAwait(false)` khi thích hợp để ngăn chặn deadlock trong mã thư viện
- Lan truyền ngoại lệ với `Task.FromException()` thay vì ném (throwing) trong các phương thức trả về `Task` bất đồng bộ

## Hiệu năng

- Sử dụng `Task.WhenAll()` để thực thi song song nhiều tác vụ
- Sử dụng `Task.WhenAny()` để triển khai thời gian chờ (timeouts) hoặc lấy tác vụ hoàn thành đầu tiên
- Tránh sử dụng `async/await` không cần thiết khi chỉ đơn giản là chuyển tiếp kết quả của tác vụ
- Cân nhắc sử dụng cancellation token cho các hoạt động chạy trong thời gian dài

## Những cạm bẫy thường gặp

- Không bao giờ sử dụng `.Wait()`, `.Result`, hoặc `.GetAwaiter().GetResult()` trong mã bất đồng bộ
- Tránh trộn lẫn mã chặn (blocking) và mã bất đồng bộ
- Không tạo các phương thức `async void` (ngoại trừ các trình xử lý sự kiện)
- Luôn `await` các phương thức trả về `Task`

## Các mẫu triển khai (Implementation Patterns)

- Triển khai mẫu lệnh bất đồng bộ (async command pattern) cho các hoạt động chạy trong thời gian dài
- Sử dụng luồng bất đồng bộ (async streams - `IAsyncEnumerable<T>`) để xử lý các chuỗi một cách bất đồng bộ
- Cân nhắc mẫu bất đồng bộ dựa trên tác vụ (task-based asynchronous pattern - TAP) cho các API công khai

Khi xem xét mã C# của tôi, hãy xác định những vấn đề này và đề xuất các cải tiến tuân theo những phương pháp hay nhất
