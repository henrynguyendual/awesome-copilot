---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Trợ lý đánh giá mã SQL toàn diện, thực hiện phân tích bảo mật, khả năng bảo trì và chất lượng mã trên tất cả các cơ sở dữ liệu SQL (MySQL, PostgreSQL, SQL Server, Oracle). Tập trung vào việc ngăn chặn SQL injection, kiểm soát truy cập, tiêu chuẩn mã và phát hiện các anti-pattern. Bổ sung cho lời nhắc tối ưu hóa SQL để bao quát toàn bộ quá trình phát triển."
tested_with: "GitHub Copilot Chat (GPT-4o) - Đã xác thực ngày 20 tháng 7 năm 2025"
---

# Đánh giá Mã SQL

Thực hiện đánh giá mã SQL kỹ lưỡng cho ${selection} (hoặc toàn bộ dự án nếu không có lựa chọn nào) tập trung vào bảo mật, hiệu suất, khả năng bảo trì và các phương pháp hay nhất về cơ sở dữ liệu.

## 🔒 Phân tích Bảo mật

### Ngăn chặn SQL Injection

```sql
-- ❌ NGHIÊM TRỌNG: Lỗ hổng SQL Injection
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ AN TOÀN: Truy vấn tham số hóa
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### Kiểm soát Truy cập & Quyền hạn

- **Nguyên tắc Đặc quyền Tối thiểu**: Cấp các quyền tối thiểu cần thiết
- **Truy cập Dựa trên Vai trò**: Sử dụng vai trò cơ sở dữ liệu thay vì cấp quyền trực tiếp cho người dùng
- **Bảo mật Lược đồ**: Quyền sở hữu và kiểm soát truy cập lược đồ phù hợp
- **Bảo mật Hàm/Thủ tục**: Xem xét quyền DEFINER so với INVOKER

### Bảo vệ Dữ liệu

- **Lộ lọt Dữ liệu Nhạy cảm**: Tránh `SELECT *` trên các bảng có cột nhạy cảm
- **Ghi nhật ký Kiểm toán**: Đảm bảo các hoạt động nhạy cảm được ghi lại
- **Che giấu Dữ liệu**: Sử dụng view hoặc hàm để che giấu dữ liệu nhạy cảm
- **Mã hóa**: Xác minh việc lưu trữ được mã hóa cho dữ liệu nhạy cảm

## ⚡ Tối ưu hóa Hiệu suất

### Phân tích Cấu trúc Truy vấn

```sql
-- ❌ TỆ: Mẫu truy vấn không hiệu quả
SELECT DISTINCT u.*
FROM users u, orders o, products p
WHERE u.id = o.user_id
AND o.product_id = p.id
AND YEAR(o.order_date) = 2024;

-- ✅ TỐT: Cấu trúc đã tối ưu hóa
SELECT u.id, u.name, u.email
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.order_date >= '2024-01-01'
AND o.order_date < '2025-01-01';
```

### Xem xét Chiến lược Chỉ mục

- **Thiếu Chỉ mục**: Xác định các cột cần đánh chỉ mục
- **Thừa Chỉ mục**: Tìm các chỉ mục không sử dụng hoặc dư thừa
- **Chỉ mục Tổng hợp**: Chỉ mục nhiều cột cho các truy vấn phức tạp
- **Bảo trì Chỉ mục**: Kiểm tra các chỉ mục bị phân mảnh hoặc lỗi thời

### Tối ưu hóa Join

- **Các loại Join**: Xác minh các loại join phù hợp (INNER so với LEFT so với EXISTS)
- **Thứ tự Join**: Tối ưu hóa để có tập kết quả nhỏ hơn trước
- **Tích Descartes**: Xác định và sửa các điều kiện join bị thiếu
- **Subquery so với JOIN**: Chọn cách tiếp cận hiệu quả nhất

### Hàm Tổng hợp và Hàm Cửa sổ

```sql
-- ❌ TỆ: Tổng hợp không hiệu quả
SELECT user_id,
       (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o1.user_id) as order_count
FROM orders o1
GROUP BY user_id;

-- ✅ TỐT: Tổng hợp hiệu quả
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id;
```

## 🛠️ Chất lượng Mã & Khả năng Bảo trì

### Phong cách & Định dạng SQL

```sql
-- ❌ TỆ: Định dạng và phong cách kém
select u.id,u.name,o.total from users u left join orders o on u.id=o.user_id where u.status='active' and o.order_date>='2024-01-01';

-- ✅ TỐT: Định dạng sạch sẽ, dễ đọc
SELECT u.id,
       u.name,
       o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
  AND o.order_date >= '2024-01-01';
```

### Quy ước Đặt tên

- **Đặt tên Nhất quán**: Bảng, cột, ràng buộc tuân theo các mẫu nhất quán
- **Tên Mô tả**: Tên rõ ràng, có ý nghĩa cho các đối tượng cơ sở dữ liệu
- **Từ khóa Dành riêng**: Tránh sử dụng các từ khóa dành riêng của cơ sở dữ liệu làm định danh
- **Phân biệt Chữ hoa/Chữ thường**: Sử dụng nhất quán cách viết hoa/thường trong toàn bộ lược đồ

### Xem xét Thiết kế Lược đồ

- **Chuẩn hóa**: Mức độ chuẩn hóa phù hợp (tránh chuẩn hóa quá mức/dưới mức)
- **Kiểu dữ liệu**: Lựa chọn kiểu dữ liệu tối ưu cho lưu trữ và hiệu suất
- **Ràng buộc**: Sử dụng đúng PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL
- **Giá trị Mặc định**: Giá trị mặc định phù hợp cho các cột

## 🗄️ Các Phương pháp Hay nhất cho Từng Cơ sở dữ liệu

### PostgreSQL

```sql
-- Sử dụng JSONB cho dữ liệu JSON
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Chỉ mục GIN cho các truy vấn JSONB
CREATE INDEX idx_events_data ON events USING gin(data);

-- Kiểu mảng cho các cột đa giá trị
CREATE TABLE tags (
    post_id INT,
    tag_names TEXT[]
);
```

### MySQL

```sql
-- Sử dụng các storage engine phù hợp
CREATE TABLE sessions (
    id VARCHAR(128) PRIMARY KEY,
    data TEXT,
    expires TIMESTAMP
) ENGINE=InnoDB;

-- Tối ưu hóa cho InnoDB
ALTER TABLE large_table
ADD INDEX idx_covering (status, created_at, id);
```

### SQL Server

```sql
-- Sử dụng các kiểu dữ liệu phù hợp
CREATE TABLE products (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT GETUTCDATE()
);

-- Chỉ mục Columnstore cho phân tích
CREATE COLUMNSTORE INDEX idx_sales_cs ON sales;
```

### Oracle

```sql
-- Sử dụng sequence để tự động tăng
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE users (
    id NUMBER DEFAULT user_id_seq.NEXTVAL PRIMARY KEY,
    name VARCHAR2(255) NOT NULL
);
```

## 🧪 Kiểm thử & Xác thực

### Kiểm tra Tính toàn vẹn Dữ liệu

```sql
-- Xác minh tính toàn vẹn tham chiếu
SELECT o.user_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- Kiểm tra tính nhất quán của dữ liệu
SELECT COUNT(*) as inconsistent_records
FROM products
WHERE price < 0 OR stock_quantity < 0;
```

### Kiểm thử Hiệu suất

- **Kế hoạch Thực thi**: Xem xét kế hoạch thực thi truy vấn
- **Kiểm thử Tải**: Kiểm thử truy vấn với khối lượng dữ liệu thực tế
- **Kiểm thử Sức chịu đựng**: Xác minh hiệu suất dưới tải đồng thời
- **Kiểm thử Hồi quy**: Đảm bảo các tối ưu hóa không làm hỏng chức năng

## 📊 Các Anti-Pattern Phổ biến

### Vấn đề Truy vấn N+1

```sql
-- ❌ TỆ: N+1 truy vấn trong mã ứng dụng
for user in users:
    orders = query("SELECT * FROM orders WHERE user_id = ?", user.id)

-- ✅ TỐT: Một truy vấn duy nhất đã được tối ưu hóa
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### Lạm dụng DISTINCT

```sql
-- ❌ TỆ: DISTINCT che giấu các vấn đề về join
SELECT DISTINCT u.name
FROM users u, orders o
WHERE u.id = o.user_id;

-- ✅ TỐT: Join đúng cách không cần DISTINCT
SELECT u.name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
```

### Lạm dụng Hàm trong Mệnh đề WHERE

```sql
-- ❌ TỆ: Hàm ngăn cản việc sử dụng chỉ mục
SELECT * FROM orders
WHERE YEAR(order_date) = 2024;

-- ✅ TỐT: Điều kiện khoảng sử dụng chỉ mục
SELECT * FROM orders
WHERE order_date >= '2024-01-01'
  AND order_date < '2025-01-01';
```

## 📋 Danh sách Kiểm tra Đánh giá SQL

### Bảo mật

- [ ] Tất cả đầu vào của người dùng đều được tham số hóa
- [ ] Không xây dựng SQL động bằng cách nối chuỗi
- [ ] Kiểm soát truy cập và quyền hạn phù hợp
- [ ] Dữ liệu nhạy cảm được bảo vệ đúng cách
- [ ] Các vector tấn công SQL injection đã được loại bỏ

### Hiệu suất

- [ ] Có chỉ mục cho các cột thường được truy vấn
- [ ] Không có câu lệnh `SELECT *` không cần thiết
- [ ] Các JOIN được tối ưu hóa và sử dụng các loại phù hợp
- [ ] Mệnh đề WHERE có tính chọn lọc và sử dụng chỉ mục
- [ ] Các truy vấn con được tối ưu hóa hoặc chuyển đổi thành JOIN

### Chất lượng Mã

- [ ] Quy ước đặt tên nhất quán
- [ ] Định dạng và thụt lề đúng cách
- [ ] Chú thích có ý nghĩa cho logic phức tạp
- [ ] Sử dụng các kiểu dữ liệu phù hợp
- [ ] Đã triển khai xử lý lỗi

### Thiết kế Lược đồ

- [ ] Các bảng được chuẩn hóa đúng cách
- [ ] Các ràng buộc đảm bảo tính toàn vẹn dữ liệu
- [ ] Các chỉ mục hỗ trợ các mẫu truy vấn
- [ ] Các mối quan hệ khóa ngoại được xác định
- [ ] Các giá trị mặc định là phù hợp

## 🎯 Định dạng Đầu ra Đánh giá

### Mẫu Vấn đề

````
## [ĐỘ ƯU TIÊN] [DANH MỤC]: [Mô tả ngắn gọn]

**Vị trí**: [Tên Bảng/View/Thủ tục và số dòng nếu có]
**Vấn đề**: [Giải thích chi tiết về vấn đề]
**Rủi ro Bảo mật**: [Nếu có - rủi ro injection, lộ lọt dữ liệu, v.v.]
**Tác động Hiệu suất**: [Chi phí truy vấn, tác động đến thời gian thực thi]
**Khuyến nghị**: [Cách khắc phục cụ thể với ví dụ mã]

**Trước**:
```sql
-- SQL có vấn đề
````

**Sau**:

```sql
-- SQL đã cải thiện
```

**Cải thiện Dự kiến**: [Lợi ích về hiệu suất, lợi ích về bảo mật]

```

### Đánh giá Tóm tắt
- **Điểm Bảo mật**: [1-10] - Bảo vệ chống SQL injection, kiểm soát truy cập
- **Điểm Hiệu suất**: [1-10] - Hiệu quả truy vấn, sử dụng chỉ mục
- **Điểm Khả năng Bảo trì**: [1-10] - Chất lượng mã, tài liệu
- **Điểm Chất lượng Lược đồ**: [1-10] - Mẫu thiết kế, chuẩn hóa

### 3 Hành động Ưu tiên Hàng đầu
1. **[Sửa lỗi Bảo mật Nghiêm trọng]**: Giải quyết các lỗ hổng SQL injection
2. **[Tối ưu hóa Hiệu suất]**: Thêm các chỉ mục còn thiếu hoặc tối ưu hóa truy vấn
3. **[Chất lượng Mã]**: Cải thiện quy ước đặt tên và tài liệu

Tập trung vào việc cung cấp các khuyến nghị có thể hành động, không phụ thuộc vào cơ sở dữ liệu cụ thể, đồng thời nêu bật các tối ưu hóa và phương pháp hay nhất dành riêng cho từng nền tảng.
```
