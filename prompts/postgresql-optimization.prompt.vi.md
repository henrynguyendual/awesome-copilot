# Trợ Lý Phát Triển PostgreSQL

Hướng dẫn chuyên sâu về PostgreSQL cho ${selection} (hoặc toàn bộ dự án nếu không có lựa chọn). Tập trung vào các tính năng đặc thù của PostgreSQL, các mẫu tối ưu hóa và khả năng nâng cao.

## 🚀 Các Tính Năng Đặc Thù PostgreSQL

### Thao Tác JSONB
```sql
-- Truy vấn JSONB nâng cao
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index GIN cho hiệu suất JSONB
CREATE INDEX idx_events_data_gin ON events USING gin(data);

-- Truy vấn chứa và truy vấn theo đường dẫn
SELECT * FROM events 
WHERE data @> '{"type": "login"}'
  AND data #>> '{user,role}' = 'admin';

-- Tổng hợp JSONB
SELECT jsonb_agg(data) FROM events WHERE data ? 'user_id';
```

### Thao Tác Mảng
```sql
-- Mảng trong PostgreSQL
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    tags TEXT[],
    categories INTEGER[]
);

-- Truy vấn và thao tác mảng
SELECT * FROM posts WHERE 'postgresql' = ANY(tags);
SELECT * FROM posts WHERE tags && ARRAY['database', 'sql'];
SELECT * FROM posts WHERE array_length(tags, 1) > 3;

-- Tổng hợp mảng
SELECT array_agg(DISTINCT category) FROM posts, unnest(categories) as category;
```

### Window Functions & Phân Tích
```sql
-- Window functions nâng cao
SELECT 
    product_id,
    sale_date,
    amount,
    SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as running_total,
    AVG(amount) OVER (PARTITION BY product_id ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg,
    DENSE_RANK() OVER (PARTITION BY EXTRACT(month FROM sale_date) ORDER BY amount DESC) as monthly_rank,
    LAG(amount, 1) OVER (PARTITION BY product_id ORDER BY sale_date) as prev_amount
FROM sales;
```

### Tìm Kiếm Toàn Văn
```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    search_vector tsvector
);

UPDATE documents 
SET search_vector = to_tsvector('english', title || ' ' || content);

CREATE INDEX idx_documents_search ON documents USING gin(search_vector);

SELECT * FROM documents 
WHERE search_vector @@ plainto_tsquery('english', 'postgresql database');

SELECT *, ts_rank(search_vector, plainto_tsquery('postgresql')) as rank
FROM documents 
WHERE search_vector @@ plainto_tsquery('postgresql')
ORDER BY rank DESC;
```

## ⚡ Tối Ưu Hiệu Suất PostgreSQL

### Tối Ưu Truy Vấn
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) 
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'::date
GROUP BY u.id, u.name;

SELECT query, calls, total_time, mean_time, rows,
       100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;
```

### Chiến Lược Index
```sql
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);
CREATE INDEX idx_active_users ON users(created_at) WHERE status = 'active';
CREATE INDEX idx_users_lower_email ON users(lower(email));
CREATE INDEX idx_orders_covering ON orders(user_id, status) INCLUDE (total, created_at);
```

### Quản Lý Kết Nối & Bộ Nhớ
```sql
SELECT count(*) as connections, state 
FROM pg_stat_activity 
GROUP BY state;

SELECT name, setting, unit 
FROM pg_settings 
WHERE name IN ('shared_buffers', 'work_mem', 'maintenance_work_mem');
```

## 🗂️ Kiểu Dữ Liệu Nâng Cao

### Kiểu Tùy Chỉnh & Domain
```sql
CREATE TYPE address_type AS (
    street TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
);

CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered', 'cancelled');

CREATE DOMAIN email_address AS TEXT 
CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email email_address NOT NULL,
    address address_type,
    status order_status DEFAULT 'pending'
);
```

### Kiểu Dải (Range Types)
```sql
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    room_id INTEGER,
    reservation_period tstzrange,
    price_range numrange
);

SELECT * FROM reservations 
WHERE reservation_period && tstzrange('2024-07-20', '2024-07-25');

ALTER TABLE reservations 
ADD CONSTRAINT no_overlap 
EXCLUDE USING gist (room_id WITH =, reservation_period WITH &&);
```

### Kiểu Hình Học
```sql
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT,
    coordinates POINT,
    coverage CIRCLE,
    service_area POLYGON
);

SELECT name FROM locations 
WHERE coordinates <-> point(40.7128, -74.0060) < 10;

CREATE INDEX idx_locations_coords ON locations USING gist(coordinates);
```

## 📊 Extension & Công Cụ PostgreSQL

### Extension Hữu Ích
```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "unaccent";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "btree_gin";

SELECT uuid_generate_v4();
SELECT crypt('password', gen_salt('bf'));
SELECT similarity('postgresql', 'postgersql');
```

### Giám Sát & Bảo Trì
```sql
SELECT pg_size_pretty(pg_database_size(current_database())) as db_size;

SELECT schemaname, tablename,
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes 
WHERE idx_scan = 0;
```

### Mẹo Tối Ưu PostgreSQL
- Sử dụng `EXPLAIN (ANALYZE, BUFFERS)`
- Cấu hình `postgresql.conf` cho workload
- Dùng connection pooling (pgbouncer)
- VACUUM và ANALYZE định kỳ
- Partition bảng lớn
- Dùng `pg_stat_statements`

## 📋 Checklist Tối Ưu

- [ ] Kiểm tra truy vấn với EXPLAIN ANALYZE
- [ ] Tạo index hợp lý
- [ ] Loại bỏ index không dùng
- [ ] Giám sát kết nối & hiệu suất
- [ ] Đảm bảo bảo mật & phân quyền