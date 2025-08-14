---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "runCommands"]
description: "Nhận các phương pháp hay nhất cho Entity Framework Core"
---

# Các phương pháp hay nhất cho Entity Framework Core

Mục tiêu của bạn là giúp tôi tuân theo các phương pháp hay nhất khi làm việc với Entity Framework Core.

## Thiết kế Data Context

- Giữ cho các lớp DbContext tập trung và gắn kết.
- Sử dụng constructor injection để truyền các tùy chọn cấu hình.
- Ghi đè (override) `OnModelCreating` để cấu hình bằng Fluent API.
- Tách biệt các cấu hình entity bằng cách sử dụng `IEntityTypeConfiguration`.
- Cân nhắc sử dụng mẫu `DbContextFactory` cho các ứng dụng console hoặc kiểm thử.

## Thiết kế Entity

- Sử dụng khóa chính có ý nghĩa (cân nhắc giữa khóa tự nhiên và khóa thay thế).
- Triển khai các mối quan hệ phù hợp (một-một, một-nhiều, nhiều-nhiều).
- Sử dụng data annotations hoặc fluent API cho các ràng buộc và xác thực.
- Triển khai các thuộc tính điều hướng (navigational properties) phù hợp.
- Cân nhắc sử dụng các kiểu thực thể sở hữu (owned entity types) cho các đối tượng giá trị (value objects).

## Hiệu năng

- Sử dụng `AsNoTracking()` cho các truy vấn chỉ đọc.
- Triển khai phân trang cho các tập kết quả lớn bằng `Skip()` và `Take()`.
- Sử dụng `Include()` để tải trước (eager load) các entity liên quan khi cần thiết.
- Cân nhắc sử dụng phép chiếu (projection) với `Select` để chỉ lấy các trường cần thiết.
- Sử dụng các truy vấn đã biên dịch (compiled queries) cho các truy vấn được thực thi thường xuyên.
- Tránh vấn đề truy vấn N+1 bằng cách include dữ liệu liên quan một cách hợp lý.

## Migrations (Di chuyển cơ sở dữ liệu)

- Tạo các migration nhỏ, tập trung.
- Đặt tên migration một cách mô tả.
- Kiểm tra các script SQL của migration trước khi áp dụng cho môi trường production.
- Cân nhắc sử dụng các gói migration (migration bundles) để triển khai.
- Thêm dữ liệu khởi tạo (data seeding) thông qua migration khi thích hợp.

## Truy vấn

- Sử dụng `IQueryable` một cách thận trọng và hiểu khi nào các truy vấn được thực thi.
- Ưu tiên các truy vấn LINQ có kiểu dữ liệu mạnh (strongly-typed) hơn là SQL thô.
- Sử dụng các toán tử truy vấn phù hợp (`Where`, `OrderBy`, `GroupBy`).
- Cân nhắc sử dụng các hàm của cơ sở dữ liệu cho các hoạt động phức tạp.
- Triển khai mẫu specifications cho các truy vấn có thể tái sử dụng.

## Theo dõi thay đổi & Lưu

- Sử dụng các chiến lược theo dõi thay đổi phù hợp.
- Gộp các lệnh gọi `SaveChanges()` thành lô.
- Triển khai kiểm soát đồng thời (concurrency control) cho các kịch bản nhiều người dùng.
- Cân nhắc sử dụng transaction cho nhiều hoạt động.
- Sử dụng vòng đời DbContext phù hợp (scoped cho ứng dụng web).

## Bảo mật

- Tránh SQL injection bằng cách sử dụng các truy vấn tham số hóa.
- Triển khai các quyền truy cập dữ liệu phù hợp.
- Cẩn thận với các truy vấn SQL thô.
- Cân nhắc mã hóa dữ liệu cho thông tin nhạy cảm.
- Sử dụng migration để quản lý quyền người dùng cơ sở dữ liệu.

## Kiểm thử

- Sử dụng nhà cung cấp cơ sở dữ liệu trong bộ nhớ (in-memory) cho unit test.
- Tạo các context kiểm thử riêng biệt với SQLite cho integration test.
- Mock `DbContext` và `DbSet` cho các unit test thuần túy.
- Kiểm thử migration trong các môi trường cô lập.
- Cân nhắc kiểm thử ảnh chụp nhanh (snapshot testing) cho các thay đổi của model.

Khi xem xét mã EF Core của tôi, hãy xác định các vấn đề và đề xuất các cải tiến tuân theo những phương pháp hay nhất
