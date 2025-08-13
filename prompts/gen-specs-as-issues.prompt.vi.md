# Trợ lý Quản lý Sản phẩm: Xác định và Đặc tả Tính năng

Quy trình này hướng dẫn bạn tiếp cận có hệ thống để xác định tính năng còn thiếu, ưu tiên chúng và tạo đặc tả chi tiết để triển khai.

## 1. Giai đoạn Hiểu Dự án

- Xem cấu trúc dự án để hiểu cách tổ chức
- Đọc README.md và tài liệu khác để nắm chức năng cốt lõi
- Xác định trạng thái triển khai hiện tại bằng cách xem:
  - Điểm vào chính (CLI, API, UI, ...)
  - Module lõi và chức năng
  - Test để hiểu hành vi mong đợi
  - Mã placeholder

**Câu hỏi gợi ý:**
- Mục đích chính của dự án là gì?
- Giải quyết vấn đề gì cho người dùng?
- Có mẫu nào trong triển khai hiện tại?
- Tài liệu có đề cập tính năng chưa hoàn thiện không?

## 2. Giai đoạn Phân tích Khoảng trống

- So sánh khả năng được tài liệu hóa với triển khai thực tế
- Xác định mã placeholder chưa có chức năng thực
- Tìm tính năng được đề cập nhưng thiếu triển khai
- Xem hành trình người dùng để tìm bước hỏng hoặc thiếu
- Tập trung vào chức năng cốt lõi trước

**Kết quả:**
- Danh sách 5-7 tính năng tiềm năng bị thiếu
- Mỗi tính năng ghi:
  - Trạng thái hiện tại
  - Tham chiếu tài liệu
  - Ảnh hưởng nếu thiếu

## 3. Giai đoạn Ưu tiên

- Cho điểm mỗi khoảng trống:

**Thang điểm (1-5):**
- Ảnh hưởng người dùng: Bao nhiêu người hưởng lợi?
- Phù hợp chiến lược: Có khớp mục tiêu chính?
- Khả thi triển khai: Độ phức tạp kỹ thuật?
- Nhu cầu tài nguyên: Nỗ lực phát triển?
- Mức rủi ro: Ảnh hưởng tiêu cực?

**Độ ưu tiên = (Ảnh hưởng × Phù hợp) / (Nỗ lực × Rủi ro)**

**Kết quả:**
- 3 tính năng ưu tiên cao nhất
- Mỗi tính năng có:
  - Tên
  - Trạng thái
  - Ảnh hưởng nếu không triển khai
  - Phụ thuộc vào tính năng khác

## 4. Giai đoạn Xây dựng Đặc tả

- Mỗi tính năng ưu tiên viết đặc tả chi tiết nhưng gọn:
  - Ưu tiên đơn giản
  - MVP trước
  - Tối ưu trải nghiệm dev
  - Thân thiện triển khai

**Mỗi đặc tả gồm:**
1. **Tổng quan & Phạm vi**
   - Giải quyết vấn đề gì?
   - Bao gồm & loại trừ gì?

2. **Yêu cầu kỹ thuật**
   - Chức năng cốt lõi
   - Giao diện người dùng (API, UI, CLI,...)
   - Điểm tích hợp

3. **Kế hoạch triển khai**
   - File/module tạo hoặc chỉnh
   - Ví dụ code minh họa
   - Cấu trúc dữ liệu & interface

4. **Tiêu chí chấp nhận**
   - Khi nào coi là xong?
   - Chức năng cụ thể phải hoạt động?
   - Test cần pass?

## 5. Giai đoạn Tạo Issue GitHub

- Mỗi đặc tả thành 1 issue GitHub:
  - Tiêu đề rõ ràng
  - Nội dung đặc tả chi tiết
  - Label phù hợp (enhancement, high-priority,...)
  - Nhắc đến triết lý MVP

**Mẫu issue:**

# [Tên tính năng]

## Tổng quan
[Mô tả ngắn về tính năng]

## Phạm vi
[Phạm vi bao gồm & loại trừ]

## Yêu cầu kỹ thuật
[Yêu cầu kỹ thuật cụ thể]

## Kế hoạch triển khai
[Cách tiếp cận, ví dụ code]

## Tiêu chí chấp nhận
[Danh sách yêu cầu để coi là hoàn tất]

## Ưu tiên
[Lý do ưu tiên]

## Phụ thuộc
- **Chặn:** [Danh sách issue bị chặn]
- **Bị chặn bởi:** [Danh sách issue phụ thuộc]

## Quy mô triển khai
- **Ước tính effort:** [Nhỏ/Vừa/Lớn]
- **Sub-issues:** [Liên kết sub-issues]

## 5.5 Tối ưu phân phối công việc

- **Phân tích độc lập**
  - Xác định thành phần độc lập
  - Refactor đặc tả để tối đa luồng độc lập
  - Tạo ranh giới rõ giữa phần phụ thuộc

- **Sơ đồ phụ thuộc**
  - Thiết lập issue cha-con khi cần
  - Ghi rõ "blocked by" và "blocks"

- **Cân bằng khối lượng**
  - Chia nhỏ đặc tả lớn thành sub-issues
  - Mỗi sub-issue 1-3 ngày dev
  - Tiêu chí chấp nhận riêng cho từng sub-issue

**Hướng dẫn:**
- Dùng cú pháp liên kết issue GitHub
- Label trạng thái phụ thuộc
- Thêm ước tính effort để hỗ trợ lập sprint

## 6. Giai đoạn Rà soát Cuối

- Tóm tắt đặc tả đã tạo
- Nêu phụ thuộc giữa tính năng
- Đề xuất thứ tự triển khai
- Lưu ý rủi ro và thách thức

Nguyên tắc xuyên suốt:
- Ưu tiên đơn giản
- Bắt đầu với MVP
- Tối ưu trải nghiệm dev
- Xây nền tảng mở rộng được
- Xem xét cộng đồng và đóng góp mã nguồn mở
