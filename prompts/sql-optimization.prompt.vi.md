---
mode: 'agent'
description: 'Trợ lý tối ưu hóa hiệu suất SQL đa năng cho việc tinh chỉnh truy vấn, chiến lược lập chỉ mục và phân tích hiệu suất cơ sở dữ liệu trên tất cả các hệ quản trị SQL (MySQL, PostgreSQL, SQL Server, Oracle). Cung cấp phân tích kế hoạch thực thi, tối ưu hóa phân trang, thao tác hàng loạt và hướng dẫn giám sát hiệu suất.'
tested_with: 'GitHub Copilot Chat (GPT-4o) - Xác thực ngày 20/07/2025'
---

# Trợ Lý Tối Ưu Hóa Hiệu Suất SQL

Tối ưu hóa hiệu suất SQL chuyên sâu cho ${selection} (hoặc toàn bộ dự án nếu không chọn). Tập trung vào các kỹ thuật tối ưu hóa SQL phổ quát hoạt động trên MySQL, PostgreSQL, SQL Server, Oracle và các hệ quản trị SQL khác.

## 🎯 Các Khu Vực Tối Ưu Chính

### Phân Tích Hiệu Suất Truy Vấn
```sql
-- ❌ TỆ: Mẫu truy vấn kém hiệu quả
SELECT * FROM orders o
WHERE YEAR(o.created_at) = 2024
  AND o.customer_id IN (
      SELECT c.id FROM customers c WHERE c.status = 'active'
  );

-- ✅ TỐT: Truy vấn được tối ưu với gợi ý chỉ mục phù hợp
SELECT o.id, o.customer_id, o.total_amount, o.created_at
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.created_at >= '2024-01-01' 
  AND o.created_at < '2025-01-01'
  AND c.status = 'active';

-- Chỉ mục yêu cầu:
-- CREATE INDEX idx_orders_created_at ON orders(created_at);
-- CREATE INDEX idx_customers_status ON customers(status);
-- CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### Tối Ưu Chiến Lược Chỉ Mục
```sql
-- ❌ TỆ: Chiến lược lập chỉ mục kém
CREATE INDEX idx_user_data ON users(email, first_name, last_name, created_at);

-- ✅ TỐT: Lập chỉ mục tổng hợp tối ưu
-- Cho truy vấn lọc theo email trước, sau đó sắp xếp theo created_at
CREATE INDEX idx_users_email_created ON users(email, created_at);

-- Cho tìm kiếm tên full-text
CREATE INDEX idx_users_name ON users(last_name, first_name);

-- Cho truy vấn trạng thái người dùng
CREATE INDEX idx_users_status_created ON users(status, created_at)
WHERE status IS NOT NULL;
```

### Tối Ưu Subquery
```sql
-- ❌ TỆ: Subquery tương quan
SELECT p.product_name, p.price
FROM products p
WHERE p.price > (
    SELECT AVG(price) 
    FROM products p2 
    WHERE p2.category_id = p.category_id
);

-- ✅ TỐT: Dùng hàm cửa sổ
SELECT product_name, price
FROM (
    SELECT product_name, price,
           AVG(price) OVER (PARTITION BY category_id) as avg_category_price
    FROM products
) ranked
WHERE price > avg_category_price;
```

## 📊 Kỹ Thuật Tinh Chỉnh Hiệu Suất

### Tối Ưu JOIN
```sql
-- ❌ TỆ: Thứ tự và điều kiện JOIN kém hiệu quả
SELECT o.*, c.name, p.product_name
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
WHERE o.created_at > '2024-01-01'
  AND c.status = 'active';

-- ✅ TỐT: JOIN tối ưu với lọc dữ liệu
SELECT o.id, o.total_amount, c.name, p.product_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id AND c.status = 'active'
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.created_at > '2024-01-01';
```

### Tối Ưu Phân Trang
```sql
-- ❌ TỆ: Phân trang dùng OFFSET (chậm với offset lớn)
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 10000;

-- ✅ TỐT: Phân trang dùng cursor
SELECT * FROM products 
WHERE created_at < '2024-06-15 10:30:00'
ORDER BY created_at DESC 
LIMIT 20;

-- Hoặc dùng cursor dựa trên ID
SELECT * FROM products 
WHERE id > 1000
ORDER BY id 
LIMIT 20;
```

### Tối Ưu Tổng Hợp
```sql
-- ❌ TỆ: Nhiều truy vấn tổng hợp riêng lẻ
SELECT COUNT(*) FROM orders WHERE status = 'pending';
SELECT COUNT(*) FROM orders WHERE status = 'shipped';
SELECT COUNT(*) FROM orders WHERE status = 'delivered';

-- ✅ TỐT: Truy vấn tổng hợp điều kiện
SELECT 
    COUNT(CASE WHEN status = 'pending' THEN 1 END) as pending_count,
    COUNT(CASE WHEN status = 'shipped' THEN 1 END) as shipped_count,
    COUNT(CASE WHEN status = 'delivered' THEN 1 END) as delivered_count
FROM orders;
```

## 🔍 Anti-Pattern Truy Vấn

### Vấn Đề Hiệu Suất SELECT
```sql
-- ❌ TỆ: Dùng SELECT * 
SELECT * FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;

-- ✅ TỐT: Chỉ chọn cột cần thiết
SELECT lt.id, lt.name, at.value
FROM large_table lt
JOIN another_table at ON lt.id = at.ref_id;
```

### Tối Ưu WHERE Clause
```sql
-- ❌ TỆ: Gọi hàm trong WHERE
SELECT * FROM orders 
WHERE UPPER(customer_email) = 'JOHN@EXAMPLE.COM';

-- ✅ TỐT: WHERE thân thiện với index
SELECT * FROM orders 
WHERE customer_email = 'john@example.com';
-- Hoặc: CREATE INDEX idx_orders_email ON orders(LOWER(customer_email));
```

### Tối Ưu OR vs UNION
```sql
-- ❌ TỆ: Điều kiện OR phức tạp
SELECT * FROM products 
WHERE (category = 'electronics' AND price < 1000)
   OR (category = 'books' AND price < 50);

-- ✅ TỐT: Dùng UNION
SELECT * FROM products WHERE category = 'electronics' AND price < 1000
UNION ALL
SELECT * FROM products WHERE category = 'books' AND price < 50;
```

## 📈 Tối Ưu Hóa Độc Lập CSDL

### Thao Tác Hàng Loạt
```sql
-- ❌ TỆ: Chèn từng dòng
INSERT INTO products (name, price) VALUES ('Product 1', 10.00);
INSERT INTO products (name, price) VALUES ('Product 2', 15.00);
INSERT INTO products (name, price) VALUES ('Product 3', 20.00);

-- ✅ TỐT: Chèn hàng loạt
INSERT INTO products (name, price) VALUES 
('Product 1', 10.00),
('Product 2', 15.00),
('Product 3', 20.00);
```

### Sử Dụng Bảng Tạm
```sql
-- ✅ TỐT: Dùng bảng tạm cho phép tính phức tạp
CREATE TEMPORARY TABLE temp_calculations AS
SELECT customer_id, 
       SUM(total_amount) as total_spent,
       COUNT(*) as order_count
FROM orders 
WHERE created_at >= '2024-01-01'
GROUP BY customer_id;

-- Dùng bảng tạm cho tính toán tiếp
SELECT c.name, tc.total_spent, tc.order_count
FROM temp_calculations tc
JOIN customers c ON tc.customer_id = c.id
WHERE tc.total_spent > 1000;
```

## 🛠️ Quản Lý Chỉ Mục

### Nguyên Tắc Thiết Kế Chỉ Mục
```sql
-- ✅ TỐT: Chỉ mục bao phủ
CREATE INDEX idx_orders_covering 
ON orders(customer_id, created_at) 
INCLUDE (total_amount, status);  -- SQL Server
-- Hoặc: CREATE INDEX idx_orders_covering ON orders(customer_id, created_at, total_amount, status); -- Khác
```

### Chiến Lược Chỉ Mục Một Phần
```sql
-- ✅ TỐT: Chỉ mục một phần
CREATE INDEX idx_orders_active 
ON orders(created_at) 
WHERE status IN ('pending', 'processing');
```

## 📊 Giám Sát Hiệu Suất

### Phân Tích Hiệu Suất Truy Vấn
```sql
-- MySQL:
SELECT query_time, lock_time, rows_sent, rows_examined, sql_text
FROM mysql.slow_log
ORDER BY query_time DESC;

-- PostgreSQL:
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY total_time DESC;

-- SQL Server:
SELECT 
    qs.total_elapsed_time/qs.execution_count as avg_elapsed_time,
    qs.execution_count,
    SUBSTRING(qt.text, (qs.statement_start_offset/2)+1,
        ((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(qt.text)
        ELSE qs.statement_end_offset END - qs.statement_start_offset)/2)+1) as query_text
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
ORDER BY avg_elapsed_time DESC;
```

## 🎯 Checklist Tối Ưu Hóa Chung

### Cấu Trúc Truy Vấn
- [ ] Tránh SELECT *
- [ ] Dùng JOIN phù hợp
- [ ] Lọc sớm trong WHERE
- [ ] Dùng EXISTS thay IN nếu cần
- [ ] Tránh hàm trong WHERE gây mất index

### Chiến Lược Chỉ Mục
- [ ] Tạo index cho cột truy vấn nhiều
- [ ] Dùng index tổng hợp đúng thứ tự
- [ ] Tránh quá nhiều index
- [ ] Dùng index bao phủ khi cần
- [ ] Index một phần cho pattern cụ thể

### Kiểu Dữ Liệu & Schema
- [ ] Dùng kiểu dữ liệu phù hợp
- [ ] Chuẩn hóa hợp lý
- [ ] Dùng ràng buộc hỗ trợ optimizer
- [ ] Phân vùng bảng lớn nếu cần

### Mẫu Truy Vấn
- [ ] Giới hạn kết quả với LIMIT/TOP
- [ ] Phân trang hiệu quả
- [ ] Thao tác hàng loạt
- [ ] Tránh N+1 query
- [ ] Dùng prepared statement cho truy vấn lặp lại

### Kiểm Tra Hiệu Suất
- [ ] Kiểm thử với dữ liệu thực tế
- [ ] Phân tích execution plan
- [ ] Giám sát hiệu suất liên tục
- [ ] Cảnh báo truy vấn chậm
- [ ] Phân tích sử dụng index định kỳ

## 📝 Quy Trình Tối Ưu

1. **Xác định**: Dùng công cụ DB tìm truy vấn chậm
2. **Phân tích**: Xem execution plan
3. **Tối ưu**: Áp dụng kỹ thuật phù hợp
4. **Kiểm tra**: Đo hiệu suất
5. **Giám sát**: Theo dõi định kỳ
6. **Lặp lại**: Rà soát tối ưu thường xuyên

Tập trung vào cải thiện hiệu suất đo được và luôn kiểm thử với dữ liệu thực tế.