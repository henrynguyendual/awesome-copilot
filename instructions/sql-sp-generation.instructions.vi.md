---
description: "Hướng dẫn tạo câu lệnh SQL và stored procedure"
applyTo: "**/*.sql"
---

# Phát triển SQL

## Tạo lược đồ cơ sở dữ liệu

- tất cả tên bảng phải ở dạng số ít
- tất cả tên cột phải ở dạng số ít
- tất cả các bảng phải có một cột khóa chính tên là `id`
- tất cả các bảng phải có một cột tên là `created_at` để lưu dấu thời gian tạo
- tất cả các bảng phải có một cột tên là `updated_at` để lưu dấu thời gian cập nhật lần cuối

## Thiết kế lược đồ cơ sở dữ liệu

- tất cả các bảng phải có một ràng buộc khóa chính
- tất cả các ràng buộc khóa ngoại phải có tên
- tất cả các ràng buộc khóa ngoại phải được định nghĩa nội tuyến (inline)
- tất cả các ràng buộc khóa ngoại phải có tùy chọn `ON DELETE CASCADE`
- tất cả các ràng buộc khóa ngoại phải có tùy chọn `ON UPDATE CASCADE`
- tất cả các ràng buộc khóa ngoại phải tham chiếu đến khóa chính của bảng cha

## Phong cách viết mã SQL

- sử dụng chữ hoa cho các từ khóa SQL (SELECT, FROM, WHERE)
- sử dụng thụt lề nhất quán cho các truy vấn và điều kiện lồng nhau
- bao gồm các bình luận để giải thích logic phức tạp
- chia các truy vấn dài thành nhiều dòng để dễ đọc
- sắp xếp các mệnh đề một cách nhất quán (SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY)

## Cấu trúc truy vấn SQL

- sử dụng tên cột rõ ràng trong câu lệnh SELECT thay vì SELECT \*
- chỉ định rõ tên cột với tên bảng hoặc bí danh khi sử dụng nhiều bảng
- hạn chế sử dụng truy vấn con khi có thể sử dụng join
- bao gồm các mệnh đề LIMIT/TOP để giới hạn tập kết quả
- sử dụng chỉ mục (indexing) thích hợp cho các cột thường được truy vấn
- tránh sử dụng hàm trên các cột đã được đánh chỉ mục trong mệnh đề WHERE

## Quy ước đặt tên Stored Procedure

- thêm tiền tố 'usp\_' vào trước tên stored procedure
- sử dụng kiểu PascalCase cho tên stored procedure
- sử dụng tên mô tả để chỉ ra mục đích (ví dụ: usp_GetCustomerOrders)
- bao gồm danh từ số nhiều khi trả về nhiều bản ghi (ví dụ: usp_GetProducts)
- bao gồm danh từ số ít khi trả về một bản ghi (ví dụ: usp_GetProduct)

## Xử lý tham số

- thêm tiền tố '@' vào trước tham số
- sử dụng kiểu camelCase cho tên tham số
- cung cấp giá trị mặc định cho các tham số tùy chọn
- xác thực giá trị tham số trước khi sử dụng
- ghi lại tài liệu cho các tham số bằng bình luận
- sắp xếp các tham số một cách nhất quán (bắt buộc trước, tùy chọn sau)

## Cấu trúc Stored Procedure

- bao gồm khối bình luận ở đầu với mô tả, tham số và giá trị trả về
- trả về mã/thông báo lỗi được tiêu chuẩn hóa
- trả về tập kết quả với thứ tự cột nhất quán
- sử dụng tham số OUTPUT để trả về thông tin trạng thái
- thêm tiền tố 'tmp\_' vào trước các bảng tạm

## Các phương pháp bảo mật SQL tốt nhất

- tham số hóa tất cả các truy vấn để ngăn chặn SQL injection
- sử dụng các câu lệnh đã được chuẩn bị (prepared statements) khi thực thi SQL động
- tránh nhúng thông tin xác thực vào trong các kịch bản SQL
- triển khai xử lý lỗi phù hợp mà không để lộ chi tiết hệ thống
- tránh sử dụng SQL động bên trong các stored procedure

## Quản lý giao dịch (Transaction)

- bắt đầu và cam kết (commit) giao dịch một cách rõ ràng
- sử dụng các mức cô lập (isolation levels) phù hợp dựa trên yêu cầu
- tránh các giao dịch chạy dài gây khóa bảng
- sử dụng xử lý hàng loạt (batch processing) cho các hoạt động dữ liệu lớn
- bao gồm SET NOCOUNT ON cho các stored procedure
