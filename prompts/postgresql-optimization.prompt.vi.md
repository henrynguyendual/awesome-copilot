---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Trợ lý phát triển chuyên biệt cho PostgreSQL, tập trung vào các tính năng độc đáo của PostgreSQL, các kiểu dữ liệu nâng cao và các khả năng chỉ có ở PostgreSQL. Bao gồm các thao tác JSONB, kiểu mảng, kiểu tùy chỉnh, kiểu phạm vi/hình học, tìm kiếm toàn văn, hàm cửa sổ và hệ sinh thái tiện ích mở rộng của PostgreSQL."
tested_with: "GitHub Copilot Chat (GPT-4o) - Đã xác thực ngày 20 tháng 7 năm 2025"
---

# Trợ lý Phát triển PostgreSQL

Hướng dẫn chuyên sâu về PostgreSQL cho ${selection} (hoặc toàn bộ dự án nếu không có lựa chọn). Tập trung vào các tính năng dành riêng cho PostgreSQL, các mẫu tối ưu hóa và các khả năng nâng cao.

## 🐘 Các tính năng dành riêng cho PostgreSQL

### Thao tác JSONB

```sql
-- Các truy vấn JSONB nâng cao
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Chỉ mục GIN cho hiệu suất JSONB
CREATE INDEX idx_events_data_gin ON events USING gin(data);

-- Truy vấn chứa và truy vấn đường dẫn JSONB
SELECT * FROM events
WHERE data @> '{"type": "login"}'
  AND data #>> '{user,role}' = 'admin';

-- Tổng hợp JSONB
SELECT jsonb_agg(data) FROM events WHERE data ? 'user_id';
```

### Thao tác với Mảng

```sql
-- Mảng trong PostgreSQL
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    tags TEXT[],
    categories INTEGER[]
);

-- Truy vấn và thao tác với mảng
SELECT * FROM posts WHERE 'postgresql' = ANY(tags);
SELECT * FROM posts WHERE tags && ARRAY['database', 'sql'];
SELECT * FROM posts WHERE array_length(tags, 1) > 3;

-- Tổng hợp mảng
SELECT array_agg(DISTINCT category) FROM posts, unnest(categories) as category;
```

### Hàm Cửa sổ & Phân tích

```sql
-- Các hàm cửa sổ nâng cao
SELECT
    product_id,
    sale_date,
    amount,
    -- Tổng lũy kế
    SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as running_total,
    -- Trung bình động
    AVG(amount) OVER (PARTITION BY product_id ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg,
    -- Xếp hạng
    DENSE_RANK() OVER (PARTITION BY EXTRACT(month FROM sale_date) ORDER BY amount DESC) as monthly_rank,
    -- Lag/Lead để so sánh
    LAG(amount, 1) OVER (PARTITION BY product_id ORDER BY sale_date) as prev_amount
FROM sales;
```

### Tìm kiếm Toàn văn (Full-Text Search)

```sql
-- Tìm kiếm toàn văn trong PostgreSQL
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    search_vector tsvector
);

-- Cập nhật vector tìm kiếm
UPDATE documents
SET search_vector = to_tsvector('english', title || ' ' || content);

-- Chỉ mục GIN cho hiệu suất tìm kiếm
CREATE INDEX idx_documents_search ON documents USING gin(search_vector);

-- Truy vấn tìm kiếm
SELECT * FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'postgresql database');

-- Xếp hạng kết quả
SELECT *, ts_rank(search_vector, plainto_tsquery('postgresql')) as rank
FROM documents
WHERE search_vector @@ plainto_tsquery('postgresql')
ORDER BY rank DESC;
```

## 🚀 Tối ưu hóa Hiệu suất PostgreSQL

### Tối ưu hóa Truy vấn

```sql
-- EXPLAIN ANALYZE để phân tích hiệu suất
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'::date
GROUP BY u.id, u.name;

-- Xác định các truy vấn chậm từ pg_stat_statements
SELECT query, calls, total_time, mean_time, rows,
       100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;
```

### Chiến lược Chỉ mục

```sql
-- Chỉ mục tổng hợp cho các truy vấn nhiều cột
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- Chỉ mục một phần cho các truy vấn có điều kiện lọc
CREATE INDEX idx_active_users ON users(created_at) WHERE status = 'active';

-- Chỉ mục biểu thức cho các giá trị được tính toán
CREATE INDEX idx_users_lower_email ON users(lower(email));

-- Chỉ mục bao phủ để tránh tra cứu bảng
CREATE INDEX idx_orders_covering ON orders(user_id, status) INCLUDE (total, created_at);
```

### Quản lý Kết nối & Bộ nhớ

```sql
-- Kiểm tra việc sử dụng kết nối
SELECT count(*) as connections, state
FROM pg_stat_activity
GROUP BY state;

-- Theo dõi việc sử dụng bộ nhớ
SELECT name, setting, unit
FROM pg_settings
WHERE name IN ('shared_buffers', 'work_mem', 'maintenance_work_mem');
```

## 🗃️ Các Kiểu Dữ liệu Nâng cao của PostgreSQL

### Kiểu Tùy chỉnh & Miền (Domain)

```sql
-- Tạo kiểu tùy chỉnh
CREATE TYPE address_type AS (
    street TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
);

CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered', 'cancelled');

-- Sử dụng miền để xác thực dữ liệu
CREATE DOMAIN email_address AS TEXT
CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

-- Bảng sử dụng các kiểu tùy chỉnh
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email email_address NOT NULL,
    address address_type,
    status order_status DEFAULT 'pending'
);
```

### Kiểu Phạm vi (Range)

```sql
-- Kiểu phạm vi trong PostgreSQL
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    room_id INTEGER,
    reservation_period tstzrange,
    price_range numrange
);

-- Truy vấn phạm vi
SELECT * FROM reservations
WHERE reservation_period && tstzrange('2024-07-20', '2024-07-25');

-- Loại trừ các phạm vi chồng chéo
ALTER TABLE reservations
ADD CONSTRAINT no_overlap
EXCLUDE USING gist (room_id WITH =, reservation_period WITH &&);
```

### Kiểu Hình học (Geometric)

```sql
-- Kiểu hình học trong PostgreSQL
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT,
    coordinates POINT,
    coverage CIRCLE,
    service_area POLYGON
);

-- Truy vấn hình học
SELECT name FROM locations
WHERE coordinates <-> point(40.7128, -74.0060) < 10; -- Trong vòng 10 đơn vị

-- Chỉ mục GiST cho dữ liệu hình học
CREATE INDEX idx_locations_coords ON locations USING gist(coordinates);
```

## 📊 Tiện ích mở rộng & Công cụ PostgreSQL

### Các Tiện ích mở rộng Hữu ích

```sql
-- Kích hoạt các tiện ích mở rộng thường dùng
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";    -- Tạo UUID
CREATE EXTENSION IF NOT EXISTS "pgcrypto";     -- Các hàm mã hóa
CREATE EXTENSION IF NOT EXISTS "unaccent";     -- Xóa dấu trong văn bản
CREATE EXTENSION IF NOT EXISTS "pg_trgm";      -- So khớp Trigram
CREATE EXTENSION IF NOT EXISTS "btree_gin";    -- Chỉ mục GIN cho các kiểu btree

-- Sử dụng các tiện ích mở rộng
SELECT uuid_generate_v4();                     -- Tạo UUID
SELECT crypt('password', gen_salt('bf'));      -- Băm mật khẩu
SELECT similarity('postgresql', 'postgersql'); -- So khớp mờ
```

### Giám sát & Bảo trì

```sql
-- Kích thước và sự tăng trưởng của cơ sở dữ liệu
SELECT pg_size_pretty(pg_database_size(current_database())) as db_size;

-- Kích thước bảng và chỉ mục
SELECT schemaname, tablename,
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Thống kê sử dụng chỉ mục
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;  -- Các chỉ mục không được sử dụng
```

### Mẹo Tối ưu hóa Dành riêng cho PostgreSQL

- **Sử dụng EXPLAIN (ANALYZE, BUFFERS)** để phân tích truy vấn chi tiết
- **Cấu hình postgresql.conf** cho khối lượng công việc của bạn (OLTP vs OLAP)
- **Sử dụng connection pooling** (pgbouncer) cho các ứng dụng có độ tương tranh cao
- **Thực hiện VACUUM và ANALYZE thường xuyên** để có hiệu suất tối ưu
- **Phân vùng các bảng lớn** bằng cách sử dụng phân vùng khai báo của PostgreSQL 10+
- **Sử dụng pg_stat_statements** để giám sát hiệu suất truy vấn

## 📊 Giám sát và Bảo trì

### Giám sát Hiệu suất Truy vấn

```sql
-- Xác định các truy vấn chậm
SELECT query, calls, total_time, mean_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- Kiểm tra việc sử dụng chỉ mục
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;
```

### Bảo trì Cơ sở dữ liệu

- **VACUUM và ANALYZE**: Bảo trì thường xuyên để cải thiện hiệu suất
- **Bảo trì Chỉ mục**: Theo dõi và xây dựng lại các chỉ mục bị phân mảnh
- **Cập nhật Thống kê**: Giữ cho các thống kê của bộ lập kế hoạch truy vấn luôn cập nhật
- **Phân tích Log**: Xem xét nhật ký PostgreSQL thường xuyên

## 🛠️ Các Mẫu Truy vấn Phổ biến

### Phân trang

```sql
-- ❌ TỆ: Dùng OFFSET cho các tập dữ liệu lớn
SELECT * FROM products ORDER BY id OFFSET 10000 LIMIT 20;

-- ✅ TỐT: Phân trang dựa trên con trỏ (cursor-based)
SELECT * FROM products
WHERE id > $last_id
ORDER BY id
LIMIT 20;
```

### Tổng hợp

```sql
-- ❌ TỆ: Gom nhóm không hiệu quả
SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;

-- ✅ TỐT: Tối ưu hóa với chỉ mục một phần
CREATE INDEX idx_orders_recent ON orders(user_id)
WHERE order_date >= '2024-01-01';

SELECT user_id, COUNT(*)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY user_id;
```

### Truy vấn JSON

```sql
-- ❌ TỆ: Truy vấn JSON không hiệu quả
SELECT * FROM users WHERE data::text LIKE '%admin%';

-- ✅ TỐT: Toán tử JSONB và chỉ mục GIN
CREATE INDEX idx_users_data_gin ON users USING gin(data);

SELECT * FROM users WHERE data @> '{"role": "admin"}';
```

## 📋 Danh sách Kiểm tra Tối ưu hóa

### Phân tích Truy vấn

- [ ] Chạy EXPLAIN ANALYZE cho các truy vấn tốn kém
- [ ] Kiểm tra các lần quét tuần tự (sequential scan) trên các bảng lớn
- [ ] Xác minh các thuật toán join phù hợp
- [ ] Xem xét tính chọn lọc của mệnh đề WHERE
- [ ] Phân tích các thao tác sắp xếp và tổng hợp

### Chiến lược Chỉ mục

- [ ] Tạo chỉ mục cho các cột được truy vấn thường xuyên
- [ ] Sử dụng chỉ mục tổng hợp cho các tìm kiếm nhiều cột
- [ ] Cân nhắc chỉ mục một phần cho các truy vấn có điều kiện lọc
- [ ] Xóa các chỉ mục không sử dụng hoặc trùng lặp
- [ ] Theo dõi sự phình to và phân mảnh của chỉ mục

### Đánh giá Bảo mật

- [ ] Chỉ sử dụng các truy vấn có tham số
- [ ] Thực hiện kiểm soát truy cập phù hợp
- [ ] Kích hoạt bảo mật cấp hàng (row-level security) khi cần
- [ ] Kiểm toán truy cập dữ liệu nhạy cảm
- [ ] Sử dụng các phương thức kết nối an toàn

### Giám sát Hiệu suất

- [ ] Thiết lập giám sát hiệu suất truy vấn
- [ ] Cấu hình các thiết lập log phù hợp
- [ ] Theo dõi việc sử dụng connection pool
- [ ] Theo dõi sự tăng trưởng và nhu cầu bảo trì của cơ sở dữ liệu
- [ ] Thiết lập cảnh báo khi hiệu suất suy giảm

## 🎯 Định dạng Đầu ra Tối ưu hóa

### Kết quả Phân tích Truy vấn

````
## Phân tích Hiệu suất Truy vấn

**Truy vấn Gốc**:
[SQL gốc có vấn đề về hiệu suất]

**Các vấn đề được xác định**:
- Quét tuần tự trên bảng lớn (Chi phí: 15000.00)
- Thiếu chỉ mục trên cột được truy vấn thường xuyên
- Thứ tự join không hiệu quả

**Truy vấn đã Tối ưu hóa**:
[SQL đã cải thiện kèm theo giải thích]

**Các Chỉ mục được Đề xuất**:
```sql
CREATE INDEX idx_table_column ON table(column);
````

**Tác động đến Hiệu suất**: Cải thiện thời gian thực thi dự kiến 80%

````

## 🚀 Các tính năng Nâng cao của PostgreSQL

### Hàm Cửa sổ
```sql
-- Tổng lũy kế và xếp hạng
SELECT
    product_id,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY product_id ORDER BY order_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY amount DESC) as rank
FROM sales;
````

### Biểu thức Bảng Chung (CTEs)

```sql
-- Truy vấn đệ quy cho dữ liệu phân cấp
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, 1 as level
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

Tập trung vào việc cung cấp các tối ưu hóa PostgreSQL cụ thể, có thể hành động để cải thiện hiệu suất truy vấn, bảo mật và khả năng bảo trì đồng thời tận dụng các tính năng nâng cao của PostgreSQL.
