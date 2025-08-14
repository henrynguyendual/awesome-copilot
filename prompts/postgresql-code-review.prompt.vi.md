---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Trợ lý đánh giá code dành riêng cho PostgreSQL, tập trung vào các phương pháp hay nhất, các anti-pattern và các tiêu chuẩn chất lượng độc đáo của PostgreSQL. Bao gồm các hoạt động JSONB, sử dụng mảng, các kiểu tùy chỉnh, thiết kế schema, tối ưu hóa hàm và các tính năng bảo mật độc quyền của PostgreSQL như Row Level Security (RLS)."
tested_with: "GitHub Copilot Chat (GPT-4o) - Đã xác thực ngày 20 tháng 7 năm 2025"
---

# Trợ lý Đánh giá Code PostgreSQL

Đánh giá code PostgreSQL chuyên sâu cho ${selection} (hoặc toàn bộ dự án nếu không có lựa chọn). Tập trung vào các phương pháp hay nhất, các mẫu anti-pattern và các tiêu chuẩn chất lượng dành riêng cho PostgreSQL.

## 🎯 Các Lĩnh vực Đánh giá Dành riêng cho PostgreSQL

### Các Phương pháp Tốt nhất cho JSONB

```sql
-- ❌ TỆ: Sử dụng JSONB không hiệu quả
SELECT * FROM orders WHERE data->>'status' = 'shipped';  -- Không hỗ trợ index

-- ✅ TỐT: Truy vấn JSONB có thể đánh index
CREATE INDEX idx_orders_status ON orders USING gin((data->'status'));
SELECT * FROM orders WHERE data @> '{"status": "shipped"}';

-- ❌ TỆ: Lồng sâu không cân nhắc
UPDATE orders SET data = data || '{"shipping":{"tracking":{"number":"123"}}}';

-- ✅ TỐT: JSONB có cấu trúc với xác thực
ALTER TABLE orders ADD CONSTRAINT valid_status
CHECK (data->>'status' IN ('pending', 'shipped', 'delivered'));
```

### Đánh giá Thao tác Mảng

```sql
-- ❌ TỆ: Thao tác mảng không hiệu quả
SELECT * FROM products WHERE 'electronics' = ANY(categories);  -- Không có index

-- ✅ TỐT: Truy vấn mảng được đánh index GIN
CREATE INDEX idx_products_categories ON products USING gin(categories);
SELECT * FROM products WHERE categories @> ARRAY['electronics'];

-- ❌ TỆ: Nối mảng trong vòng lặp
-- Điều này sẽ không hiệu quả trong một hàm/thủ tục

-- ✅ TỐT: Thao tác mảng hàng loạt
UPDATE products SET categories = categories || ARRAY['new_category']
WHERE id IN (SELECT id FROM products WHERE condition);
```

### Đánh giá Thiết kế Schema PostgreSQL

```sql
-- ❌ TỆ: Không sử dụng các tính năng của PostgreSQL
CREATE TABLE users (
    id INTEGER,
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- ✅ TỐT: Schema được tối ưu hóa cho PostgreSQL
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL,  -- Email không phân biệt chữ hoa/thường
    created_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Thêm index GIN cho JSONB để truy vấn metadata
CREATE INDEX idx_users_metadata ON users USING gin(metadata);
```

### Các Kiểu và Domain Tùy chỉnh

```sql
-- ❌ TỆ: Sử dụng kiểu chung cho dữ liệu cụ thể
CREATE TABLE transactions (
    amount DECIMAL(10,2),
    currency VARCHAR(3),
    status VARCHAR(20)
);

-- ✅ TỐT: Các kiểu tùy chỉnh của PostgreSQL
CREATE TYPE currency_code AS ENUM ('USD', 'EUR', 'GBP', 'JPY');
CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'failed', 'cancelled');
CREATE DOMAIN positive_amount AS DECIMAL(10,2) CHECK (VALUE > 0);

CREATE TABLE transactions (
    amount positive_amount NOT NULL,
    currency currency_code NOT NULL,
    status transaction_status DEFAULT 'pending'
);
```

## 🔍 Các Anti-Pattern Dành riêng cho PostgreSQL

### Các Anti-Pattern về Hiệu năng

- **Tránh các index đặc thù của PostgreSQL**: Không sử dụng GIN/GiST cho các kiểu dữ liệu phù hợp
- **Sử dụng sai JSONB**: Coi JSONB như một trường chuỗi đơn giản
- **Bỏ qua các toán tử mảng**: Sử dụng các thao tác mảng không hiệu quả
- **Lựa chọn khóa phân vùng kém**: Không tận dụng hiệu quả việc phân vùng của PostgreSQL

### Các Vấn đề về Thiết kế Schema

- **Không sử dụng kiểu ENUM**: Sử dụng VARCHAR cho các bộ giá trị giới hạn
- **Bỏ qua các ràng buộc**: Thiếu ràng buộc CHECK để xác thực dữ liệu
- **Sai kiểu dữ liệu**: Sử dụng VARCHAR thay vì TEXT hoặc CITEXT
- **Thiếu cấu trúc JSONB**: JSONB không có cấu trúc mà không có xác thực

### Các Vấn đề về Hàm và Trigger

```sql
-- ❌ TỆ: Hàm trigger không hiệu quả
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();  -- Nên sử dụng TIMESTAMPTZ
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ✅ TỐT: Hàm trigger được tối ưu hóa
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Đặt trigger chỉ kích hoạt khi cần thiết
CREATE TRIGGER update_modified_time_trigger
    BEFORE UPDATE ON table_name
    FOR EACH ROW
    WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE FUNCTION update_modified_time();
```

## 📊 Đánh giá Việc sử dụng Extension của PostgreSQL

### Các Phương pháp Tốt nhất về Extension

```sql
-- ✅ Kiểm tra xem extension có tồn tại không trước khi tạo
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- ✅ Sử dụng extension một cách thích hợp
-- Tạo UUID
SELECT uuid_generate_v4();

-- Băm mật khẩu
SELECT crypt('password', gen_salt('bf'));

-- So khớp văn bản mờ
SELECT word_similarity('postgres', 'postgre');
```

## 🛡️ Đánh giá Bảo mật PostgreSQL

### Bảo mật Cấp độ Hàng (Row Level Security - RLS)

```sql
-- ✅ TỐT: Triển khai RLS
ALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_data_policy ON sensitive_data
    FOR ALL TO application_role
    USING (user_id = current_setting('app.current_user_id')::INTEGER);
```

### Quản lý Đặc quyền

```sql
-- ❌ TỆ: Phân quyền quá rộng
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;

-- ✅ TỐT: Phân quyền chi tiết
GRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;
GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;
```

## 🎯 Danh sách Kiểm tra Chất lượng Code PostgreSQL

### Thiết kế Schema

- [ ] Sử dụng các kiểu dữ liệu phù hợp của PostgreSQL (CITEXT, JSONB, mảng)
- [ ] Tận dụng các kiểu ENUM cho các giá trị bị ràng buộc
- [ ] Triển khai các ràng buộc CHECK phù hợp
- [ ] Sử dụng TIMESTAMPTZ thay vì TIMESTAMP
- [ ] Định nghĩa các domain tùy chỉnh cho các ràng buộc có thể tái sử dụng

### Các Cân nhắc về Hiệu năng

- [ ] Các loại index phù hợp (GIN cho JSONB/mảng, GiST cho các khoảng)
- [ ] Các truy vấn JSONB sử dụng toán tử chứa (@>, ?)
- [ ] Các thao tác mảng sử dụng các toán tử đặc thù của PostgreSQL
- [ ] Sử dụng đúng các hàm cửa sổ và CTE
- [ ] Sử dụng hiệu quả các hàm đặc thù của PostgreSQL

### Tận dụng các Tính năng của PostgreSQL

- [ ] Sử dụng các extension khi thích hợp
- [ ] Triển khai các thủ tục lưu trữ trong PL/pgSQL khi có lợi
- [ ] Tận dụng các tính năng SQL nâng cao của PostgreSQL
- [ ] Sử dụng các kỹ thuật tối ưu hóa đặc thù của PostgreSQL
- [ ] Triển khai xử lý lỗi phù hợp trong các hàm

### Bảo mật và Tuân thủ

- [ ] Triển khai Bảo mật Cấp độ Hàng (RLS) khi cần thiết
- [ ] Quản lý vai trò và đặc quyền phù hợp
- [ ] Sử dụng các hàm mã hóa tích hợp sẵn của PostgreSQL
- [ ] Triển khai các dấu vết kiểm toán với các tính năng của PostgreSQL

## 📝 Hướng dẫn Đánh giá Dành riêng cho PostgreSQL

1.  **Tối ưu hóa Kiểu dữ liệu**: Đảm bảo các kiểu đặc thù của PostgreSQL được sử dụng một cách thích hợp
2.  **Chiến lược Index**: Xem xét các loại index và đảm bảo các index đặc thù của PostgreSQL được sử dụng
3.  **Cấu trúc JSONB**: Xác thực thiết kế schema và các mẫu truy vấn JSONB
4.  **Chất lượng Hàm**: Xem xét các hàm PL/pgSQL về hiệu quả và các phương pháp hay nhất
5.  **Sử dụng Extension**: Xác minh việc sử dụng các extension của PostgreSQL một cách thích hợp
6.  **Các Tính năng Hiệu năng**: Kiểm tra việc sử dụng các tính năng nâng cao của PostgreSQL
7.  **Triển khai Bảo mật**: Xem xét các tính năng bảo mật đặc thù của PostgreSQL

Tập trung vào các khả năng độc đáo của PostgreSQL và đảm bảo code tận dụng những gì làm cho PostgreSQL trở nên đặc biệt thay vì coi nó như một cơ sở dữ liệu SQL thông
