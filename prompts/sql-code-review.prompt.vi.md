---
mode: 'agent'
description: 'Trợ lý xem xét mã SQL toàn diện, thực hiện phân tích bảo mật, khả năng bảo trì và chất lượng mã trên tất cả các cơ sở dữ liệu SQL (MySQL, PostgreSQL, SQL Server, Oracle). Tập trung vào ngăn chặn SQL injection, kiểm soát truy cập, tiêu chuẩn mã và phát hiện anti-pattern. Bổ sung cho prompt tối ưu hóa SQL để hoàn thiện quá trình phát triển.'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Xác thực ngày 20/07/2025'
---

# Xem Xét Mã SQL

Thực hiện đánh giá kỹ lưỡng mã SQL của ${selection} (hoặc toàn bộ dự án nếu không chọn) tập trung vào bảo mật, hiệu suất, khả năng bảo trì và các thực hành tốt nhất của cơ sở dữ liệu.

## 🔒 Phân Tích Bảo Mật

### Ngăn Chặn SQL Injection
```sql
-- ❌ NGHIÊM TRỌNG: Lỗ hổng SQL Injection
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ AN TOÀN: Truy vấn có tham số
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### Kiểm Soát Truy Cập & Quyền
- **Nguyên tắc quyền tối thiểu**: Chỉ cấp quyền cần thiết
- **Truy cập dựa trên vai trò**: Sử dụng vai trò DB thay vì cấp quyền trực tiếp
- **Bảo mật schema**: Quyền sở hữu và kiểm soát truy cập schema phù hợp
- **Bảo mật hàm/thủ tục**: Kiểm tra quyền DEFINER vs INVOKER

### Bảo Vệ Dữ Liệu
- **Lộ dữ liệu nhạy cảm**: Tránh SELECT * với bảng chứa dữ liệu nhạy cảm
- **Ghi nhật ký kiểm toán**: Ghi log các thao tác nhạy cảm
- **Ẩn dữ liệu**: Sử dụng view/hàm để ẩn dữ liệu
- **Mã hóa**: Đảm bảo lưu trữ mã hóa dữ liệu nhạy cảm

## ⚡ Tối Ưu Hiệu Suất

### Phân Tích Cấu Trúc Truy Vấn
```sql
-- ❌ TỆ: Cấu trúc truy vấn kém hiệu quả
SELECT DISTINCT u.* 
FROM users u, orders o, products p
WHERE u.id = o.user_id 
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ TỐT: Cấu trúc tối ưu
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01' 
AND o.order_date < '2025-01-01';
```

### Chiến Lược Chỉ Mục
- **Thiếu chỉ mục**: Xác định cột cần chỉ mục
- **Thừa chỉ mục**: Xóa chỉ mục không dùng hoặc trùng lặp
- **Chỉ mục tổng hợp**: Multi-column index cho truy vấn phức tạp
- **Bảo trì chỉ mục**: Kiểm tra phân mảnh hoặc lỗi thời

### Tối Ưu JOIN
- **Loại JOIN**: Dùng loại JOIN phù hợp (INNER, LEFT, EXISTS)
- **Thứ tự JOIN**: Ưu tiên bảng kết quả nhỏ trước
- **Cartesian Products**: Sửa lỗi thiếu điều kiện JOIN
- **Subquery vs JOIN**: Chọn phương pháp hiệu quả hơn

### Hàm Tổng Hợp & Cửa Sổ
```sql
-- ❌ TỆ: Tổng hợp kém hiệu quả
SELECT user_id, 
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ TỐT: Tổng hợp hiệu quả
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```

## 🛠️ Chất Lượng & Khả Năng Bảo Trì

### Phong Cách & Định Dạng SQL
```sql
-- ❌ TỆ: Định dạng kém
select u.id,u.name,o.total from users u left join orders o on u.id=o.user_id where u.status='active' and o.order_date>='2024-01-01';

-- ✅ TỐT: Định dạng rõ ràng
SELECT u.id,
       u.name,
       o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
  AND o.order_date >= '2024-01-01';
```

### Quy Ước Đặt Tên
- **Nhất quán**: Tên bảng/cột/ràng buộc theo cùng mẫu
- **Mô tả rõ ràng**: Tên dễ hiểu cho đối tượng DB
- **Tránh từ khóa**: Không dùng từ khóa DB làm tên
- **Phân biệt chữ hoa/thường**: Nhất quán

### Thiết Kế Schema
- **Chuẩn hóa**: Mức chuẩn hóa phù hợp
- **Kiểu dữ liệu**: Chọn kiểu tối ưu
- **Ràng buộc**: Dùng PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL hợp lý
- **Giá trị mặc định**: Phù hợp với cột

## 🗄️ Thực Hành Tốt Theo CSDL

### PostgreSQL
```sql
-- JSONB cho dữ liệu JSON
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- GIN index cho JSONB
CREATE INDEX idx_events_data ON events USING gin(data);
```

### MySQL
```sql
-- Chọn storage engine phù hợp
CREATE TABLE sessions (
    id VARCHAR(128) PRIMARY KEY,
    data TEXT,
    expires TIMESTAMP
) ENGINE=InnoDB;
```

### SQL Server
```sql
-- Kiểu dữ liệu phù hợp
CREATE TABLE products (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT GETUTCDATE()
);
```

### Oracle
```sql
-- Sequence cho auto-increment
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;
```

## 🧪 Kiểm Tra & Xác Thực
- Kiểm tra toàn vẹn dữ liệu
- Xem execution plan
- Load/stress test
- Regression test

## 📊 Anti-Patterns Phổ Biến
- Vấn đề N+1 query
- Lạm dụng DISTINCT
- Dùng hàm trong WHERE làm mất index

## 📋 Checklist Xem Xét SQL
- Bảo mật
- Hiệu suất
- Chất lượng mã
- Thiết kế schema

## 🎯 Định Dạng Kết Quả
- Mẫu báo cáo vấn đề
- Đánh giá tổng thể (Security, Performance, Maintainability, Schema)
- Top 3 hành động ưu tiên