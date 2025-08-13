# Thực hành tốt nhất với Entity Framework Core

Mục tiêu của bạn là giúp tôi tuân thủ các thực hành tốt nhất khi làm việc với Entity Framework Core.

## Thiết kế Data Context

- Giữ các lớp DbContext tập trung và mạch lạc
- Sử dụng constructor injection cho cấu hình tùy chọn
- Ghi đè OnModelCreating để cấu hình bằng Fluent API
- Tách cấu hình entity bằng IEntityTypeConfiguration
- Cân nhắc sử dụng mẫu DbContextFactory cho ứng dụng console hoặc kiểm thử

## Thiết kế Entity

- Sử dụng khóa chính có ý nghĩa (xem xét khóa tự nhiên vs khóa thay thế)
- Triển khai mối quan hệ đúng (một-một, một-nhiều, nhiều-nhiều)
- Sử dụng data annotation hoặc Fluent API cho ràng buộc và xác thực
- Triển khai thuộc tính điều hướng hợp lý
- Cân nhắc sử dụng owned entity type cho value object

## Hiệu năng

- Sử dụng AsNoTracking() cho các truy vấn chỉ đọc
- Phân trang cho tập kết quả lớn với Skip() và Take()
- Sử dụng Include() để eager load dữ liệu liên quan khi cần
- Cân nhắc dùng projection (Select) để chỉ lấy trường cần thiết
- Sử dụng truy vấn biên dịch sẵn (compiled queries) cho truy vấn chạy thường xuyên
- Tránh vấn đề N+1 query bằng cách include dữ liệu liên quan hợp lý

## Migrations

- Tạo migration nhỏ, tập trung
- Đặt tên migration có tính mô tả
- Kiểm tra script SQL của migration trước khi áp dụng lên production
- Cân nhắc sử dụng migration bundle khi triển khai
- Thêm dữ liệu seed qua migration khi phù hợp

## Truy vấn

- Sử dụng IQueryable một cách hợp lý và hiểu rõ khi nào truy vấn thực thi
- Ưu tiên LINQ strongly-typed hơn SQL thuần
- Sử dụng toán tử truy vấn phù hợp (Where, OrderBy, GroupBy)
- Cân nhắc sử dụng hàm database cho các thao tác phức tạp
- Triển khai mẫu specification cho truy vấn tái sử dụng

## Theo dõi thay đổi & Lưu dữ liệu

- Sử dụng chiến lược theo dõi thay đổi phù hợp
- Gom các lệnh SaveChanges() lại
- Triển khai kiểm soát đồng bộ (concurrency control) cho ứng dụng nhiều người dùng
- Cân nhắc dùng transaction cho nhiều thao tác
- Sử dụng vòng đời DbContext phù hợp (scoped cho web app)

## Bảo mật

- Tránh SQL injection bằng truy vấn có tham số
- Triển khai phân quyền truy cập dữ liệu hợp lý
- Cẩn thận khi dùng SQL thuần
- Cân nhắc mã hóa dữ liệu nhạy cảm
- Sử dụng migration để quản lý quyền người dùng DB

## Kiểm thử

- Sử dụng provider in-memory cho unit test
- Tạo context kiểm thử riêng với SQLite cho integration test
- Mock DbContext và DbSet cho unit test thuần
- Kiểm thử migration trong môi trường cô lập
- Cân nhắc snapshot testing cho thay đổi mô hình
