---
description: "Hướng dẫn cho GitHub Copilot để viết bình luận nhằm đạt được code tự giải thích với ít bình luận hơn. Các ví dụ bằng JavaScript nhưng nó sẽ hoạt động trên bất kỳ ngôn ngữ nào có bình luận."
applyTo: "**"
---

# Hướng dẫn Viết Bình luận cho Code Tự giải thích

## Nguyên tắc Cốt lõi

**Viết code tự nó nói lên ý nghĩa. Chỉ bình luận khi cần thiết để giải thích TẠI SAO, không phải CÁI GÌ.**
Hầu hết thời gian chúng ta không cần bình luận.

## Nguyên tắc Viết Bình luận

### ❌ TRÁNH Các loại Bình luận này

**Bình luận Hiển nhiên**

```javascript
// Tệ: Diễn tả điều hiển nhiên
let counter = 0; // Khởi tạo biến đếm bằng không
counter++; // Tăng biến đếm lên một
```

**Bình luận Thừa thãi**

```javascript
// Tệ: Bình luận lặp lại code
function getUserName() {
  return user.name; // Trả về tên của người dùng
}
```

**Bình luận Lỗi thời**

```javascript
// Tệ: Bình luận không khớp với code
// Tính thuế với tỷ lệ 5%
const tax = price * 0.08; // Thực tế là 8%
```

### ✅ NÊN VIẾT Các loại Bình luận này

**Logic Nghiệp vụ Phức tạp**

```javascript
// Tốt: Giải thích TẠI SAO lại có phép tính cụ thể này
// Áp dụng các bậc thuế lũy tiến: 10% cho đến 10k, 20% cho phần trên
const tax = calculateProgressiveTax(income, [0.1, 0.2], [10000]);
```

**Thuật toán Không hiển nhiên**

```javascript
// Tốt: Giải thích lựa chọn thuật toán
// Sử dụng Floyd-Warshall cho bài toán đường đi ngắn nhất giữa tất cả các cặp đỉnh
// vì chúng ta cần khoảng cách giữa tất cả các nút
for (let k = 0; k < vertices; k++) {
  for (let i = 0; i < vertices; i++) {
    for (let j = 0; j < vertices; j++) {
      // ... phần triển khai
    }
  }
}
```

**Biểu thức Chính quy (Regex)**

```javascript
// Tốt: Giải thích biểu thức regex khớp với cái gì
// Khớp với định dạng email: username@domain.extension
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

**Các Ràng buộc hoặc Lưu ý của API**

```javascript
// Tốt: Giải thích ràng buộc từ bên ngoài
// Giới hạn tỷ lệ của API GitHub: 5000 yêu cầu/giờ cho người dùng đã xác thực
await rateLimiter.wait();
const response = await fetch(githubApiUrl);
```

## Khung Quyết định

Trước khi viết một bình luận, hãy tự hỏi:

1.  **Code đã tự giải thích chưa?** → Không cần bình luận
2.  **Tên biến/hàm tốt hơn có loại bỏ được nhu cầu bình luận không?** → Tái cấu trúc (refactor) thay vì bình luận
3.  **Bình luận này giải thích TẠI SAO, không phải CÁI GÌ?** → Bình luận tốt
4.  **Điều này có giúp ích cho những người bảo trì trong tương lai không?** → Bình luận tốt

## Các Trường hợp Đặc biệt cho Bình luận

### API Công khai (Public API)

```javascript
/**
 * Tính lãi kép bằng công thức tiêu chuẩn.
 *
 * @param {number} principal - Số tiền gốc ban đầu
 * @param {number} rate - Lãi suất hàng năm (dưới dạng số thập phân, ví dụ: 0.05 cho 5%)
 * @param {number} time - Khoảng thời gian tính bằng năm
 * @param {number} compoundFrequency - Số lần ghép lãi mỗi năm (mặc định: 1)
 * @returns {number} Số tiền cuối cùng sau khi tính lãi kép
 */
function calculateCompoundInterest(principal, rate, time, compoundFrequency = 1) {
  // ... phần triển khai
}
```

### Cấu hình và Hằng số

```javascript
// Tốt: Giải thích nguồn gốc hoặc lý do
const MAX_RETRIES = 3; // Dựa trên các nghiên cứu về độ tin cậy của mạng
const API_TIMEOUT = 5000; // Thời gian chờ của AWS Lambda là 15 giây, để lại khoảng đệm
```

### Chú thích (Annotations)

```javascript
// TODO: Thay thế bằng xác thực người dùng phù hợp sau khi xem xét bảo mật
// FIXME: Rò rỉ bộ nhớ trong môi trường production - cần điều tra việc quản lý kết nối
// HACK: Giải pháp tạm thời cho lỗi trong thư viện v2.1.0 - xóa sau khi nâng cấp
// NOTE: Việc triển khai này giả định múi giờ UTC cho tất cả các tính toán
// WARNING: Hàm này sửa đổi mảng gốc thay vì tạo một bản sao
// PERF: Cân nhắc lưu vào bộ đệm kết quả này nếu được gọi thường xuyên trong các đoạn code nóng
// SECURITY: Xác thực đầu vào để ngăn chặn SQL injection trước khi sử dụng trong truy vấn
// BUG: Lỗi trường hợp biên khi mảng rỗng - cần điều tra
// REFACTOR: Tách logic này ra thành hàm tiện ích riêng để tái sử dụng
// DEPRECATED: Sử dụng newApiFunction() thay thế - hàm này sẽ bị xóa trong v3.0
```

## Các Mẫu Xấu cần Tránh

### Bình luận cho Code Chết

```javascript
// Tệ: Đừng bình luận mã nguồn không dùng nữa
// const oldFunction = () => { ... };
const newFunction = () => { ... };
```

### Bình luận Nhật ký Thay đổi

```javascript
// Tệ: Đừng duy trì lịch sử thay đổi trong bình luận
// Sửa đổi bởi John vào ngày 15-01-2023
// Sửa lỗi được báo cáo bởi Sarah vào ngày 03-02-2023
function processData() {
  // ... phần triển khai
}
```

### Bình luận Phân cách

```javascript
// Tệ: Đừng sử dụng các bình luận trang trí
//=====================================
// CÁC HÀM TIỆN ÍCH
//=====================================
```

## Danh sách Kiểm tra Chất lượng

Trước khi commit, hãy đảm bảo các bình luận của bạn:

- [ ] Giải thích TẠI SAO, không phải CÁI GÌ
- [ ] Đúng ngữ pháp và rõ ràng
- [ ] Vẫn chính xác khi code phát triển
- [ ] Thêm giá trị thực sự vào việc hiểu code
- [ ] Được đặt ở vị trí thích hợp (phía trên đoạn code mà chúng mô tả)
- [ ] Sử dụng chính tả đúng và ngôn ngữ chuyên nghiệp

## Tóm tắt

Hãy nhớ rằng: \*\*Bình luận tốt nhất là bình luận bạn không cần phải viết vì code đã tự tài liệu
