# Trợ Lý Review Mã PostgreSQL

Chuyên gia review mã PostgreSQL cho ${selection} (hoặc toàn bộ dự án nếu không có lựa chọn). Tập trung vào các thực tiễn tốt nhất, các anti-pattern và tiêu chuẩn chất lượng đặc thù của PostgreSQL.

## 🎯 Các Lĩnh Vực Review Đặc Thù PostgreSQL

### Thực Tiễn Tốt Nhất với JSONB
```sql
-- ❌ SAI: Sử dụng JSONB kém hiệu quả
SELECT * FROM orders WHERE data->>'status' = 'shipped';  -- Không hỗ trợ index

-- ✅ ĐÚNG: Truy vấn JSONB có thể lập chỉ mục
CREATE INDEX idx_orders_status ON orders USING gin((data->'status'));
SELECT * FROM orders WHERE data @> '{"status": "shipped"}';

-- ❌ SAI: Lồng dữ liệu quá sâu mà không cân nhắc
UPDATE orders SET data = data || '{"shipping":{"tracking":{"number":"123"}}}';

-- ✅ ĐÚNG: JSONB có cấu trúc và được kiểm tra
ALTER TABLE orders ADD CONSTRAINT valid_status 
CHECK (data->>'status' IN ('pending', 'shipped', 'delivered'));
```

### Review Các Phép Toán với Array
```sql
-- ❌ SAI: Thao tác array kém hiệu quả
SELECT * FROM products WHERE 'electronics' = ANY(categories);  -- Không có index

-- ✅ ĐÚNG: Truy vấn array với chỉ mục GIN
CREATE INDEX idx_products_categories ON products USING gin(categories);
SELECT * FROM products WHERE categories @> ARRAY['electronics'];

-- ❌ SAI: Nối mảng trong vòng lặp (inefficient)

-- ✅ ĐÚNG: Thao tác mảng hàng loạt
UPDATE products SET categories = categories || ARRAY['new_category']
WHERE id IN (SELECT id FROM products WHERE condition);
```

### Review Thiết Kế Schema PostgreSQL
```sql
-- ❌ SAI: Không tận dụng tính năng PostgreSQL
CREATE TABLE users (
    id INTEGER,
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- ✅ ĐÚNG: Schema tối ưu cho PostgreSQL
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL,  -- Email không phân biệt hoa thường
    created_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Thêm chỉ mục GIN cho metadata
CREATE INDEX idx_users_metadata ON users USING gin(metadata);
```

### Kiểu Dữ Liệu Tùy Chỉnh và Domain
```sql
-- ❌ SAI: Dùng kiểu dữ liệu chung chung
CREATE TABLE transactions (
    amount DECIMAL(10,2),
    currency VARCHAR(3),
    status VARCHAR(20)
);

-- ✅ ĐÚNG: Kiểu dữ liệu tùy chỉnh của PostgreSQL
CREATE TYPE currency_code AS ENUM ('USD', 'EUR', 'GBP', 'JPY');
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');
CREATE DOMAIN positive_amount AS DECIMAL(10,2) CHECK (VALUE > 0);

CREATE TABLE transactions (
    amount positive_amount NOT NULL,
    currency currency_code NOT NULL,
    status transaction_status DEFAULT 'pending'
);
```

## 🔍 Anti-Pattern Đặc Thù PostgreSQL

### Anti-Pattern Hiệu Năng
- **Không dùng index đặc thù PostgreSQL**: Không dùng GIN/GiST cho kiểu dữ liệu phù hợp
- **Dùng JSONB sai cách**: Xem JSONB như chuỗi
- **Bỏ qua toán tử array**: Dùng thao tác array kém hiệu quả
- **Chọn partition key không hợp lý**

### Vấn Đề Thiết Kế Schema
- **Không dùng ENUM** cho giá trị giới hạn
- **Bỏ qua CHECK constraint**
- **Dùng sai kiểu dữ liệu**: VARCHAR thay vì TEXT/CITEXT
- **JSONB không có cấu trúc**

### Vấn Đề Hàm & Trigger
```sql
-- ❌ SAI: Trigger không tối ưu
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();  -- Nên dùng TIMESTAMPTZ
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ✅ ĐÚNG: Trigger tối ưu
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_modified_time_trigger
    BEFORE UPDATE ON table_name
    FOR EACH ROW
    WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE FUNCTION update_modified_time();
```

## 📊 Review Việc Sử Dụng Extension PostgreSQL
```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- UUID
SELECT uuid_generate_v4();

-- Hash mật khẩu
SELECT crypt('password', gen_salt('bf'));

-- So khớp mờ
SELECT word_similarity('postgres', 'postgre');
```

## 🛡️ Review Bảo Mật PostgreSQL

### Row Level Security (RLS)
```sql
ALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_data_policy ON sensitive_data
    FOR ALL TO application_role
    USING (user_id = current_setting('app.current_user_id')::INTEGER);
```

### Quản Lý Quyền
```sql
-- ❌ SAI: Cấp quyền quá rộng
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;

-- ✅ ĐÚNG: Cấp quyền chi tiết
GRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;
GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;
```

## 🎯 Checklist Chất Lượng Mã PostgreSQL

### Thiết Kế Schema
- [ ] Dùng kiểu dữ liệu PostgreSQL thích hợp (CITEXT, JSONB, array)
- [ ] Dùng ENUM cho giá trị cố định
- [ ] Có CHECK constraint
- [ ] Dùng TIMESTAMPTZ
- [ ] Định nghĩa domain tùy chỉnh

### Hiệu Năng
- [ ] Dùng đúng loại index
- [ ] Truy vấn JSONB tối ưu
- [ ] Thao tác array hiệu quả
- [ ] Dùng window function và CTE hợp lý

### Tận Dụng Tính Năng PostgreSQL
- [ ] Dùng extension hợp lý
- [ ] Dùng stored procedure khi cần
- [ ] Tận dụng SQL nâng cao
- [ ] Kỹ thuật tối ưu hóa
- [ ] Xử lý lỗi tốt

### Bảo Mật & Tuân Thủ
- [ ] Có RLS khi cần
- [ ] Quản lý role & quyền hợp lý
- [ ] Dùng hàm mã hóa tích hợp
- [ ] Có audit trail

## 📝 Hướng Dẫn Review PostgreSQL

1. **Tối ưu kiểu dữ liệu**
2. **Chiến lược index hợp lý**
3. **Cấu trúc JSONB rõ ràng**
4. **Hàm PL/pgSQL tối ưu**
5. **Dùng extension phù hợp**
6. **Tận dụng tính năng nâng cao**
7. **Bảo mật đúng chuẩn**