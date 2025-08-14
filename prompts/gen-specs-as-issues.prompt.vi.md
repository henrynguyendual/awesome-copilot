---
description: "Quy trình này hướng dẫn bạn qua một phương pháp có hệ thống để xác định các tính năng còn thiếu, ưu tiên chúng và tạo ra các đặc tả chi tiết để triển khai."
---

# Trợ lý Quản lý Sản phẩm: Xác định và Đặc tả Tính năng

Quy trình này hướng dẫn bạn qua một phương pháp có hệ thống để xác định các tính năng còn thiếu, ưu tiên chúng và tạo ra các đặc tả chi tiết để triển khai.

## 1. Giai đoạn Tìm hiểu Dự án

- Xem xét cấu trúc dự án để hiểu cách tổ chức của nó
- Đọc tệp README.md và các tệp tài liệu khác để hiểu chức năng cốt lõi của dự án
- Xác định trạng thái triển khai hiện tại bằng cách kiểm tra:
  - Các điểm truy cập chính (CLI, API, UI, v.v.)
  - Các mô-đun cốt lõi và chức năng của chúng
  - Các bài kiểm thử (tests) để hiểu hành vi mong đợi
  - Bất kỳ phần triển khai giữ chỗ nào (placeholder)

**Câu hỏi hướng dẫn:**

- Mục đích chính của dự án này là gì?
- Nó giải quyết những vấn đề gì của người dùng?
- Có những khuôn mẫu nào tồn tại trong việc triển khai hiện tại?
- Những tính năng nào được đề cập trong tài liệu nhưng chưa được triển khai đầy đủ?

## 2. Giai đoạn Phân tích Lỗ hổng

- So sánh các khả năng được ghi trong tài liệu CHỈ với việc triển khai thực tế
- Xác định mã "giữ chỗ" (placeholder) thiếu chức năng thực sự
- Tìm kiếm các tính năng được đề cập trong tài liệu nhưng thiếu sự triển khai mạnh mẽ
- Xem xét hành trình của người dùng và xác định các bước bị hỏng hoặc còn thiếu
- Tập trung vào chức năng cốt lõi trước (không phải các tính năng "có thì tốt")

**Kết quả cần tạo:**

- Tạo một danh sách các tính năng tiềm năng còn thiếu (5-7 mục)
- Đối với mỗi tính năng, ghi chú:
  - Trạng thái triển khai hiện tại
  - Các tham chiếu trong tài liệu
  - Tác động đến trải nghiệm người dùng nếu thiếu

## 3. Giai đoạn Ưu tiên hóa

- Gán điểm cho mỗi lỗ hổng được xác định:

**Ma trận chấm điểm (thang điểm 1-5):**

- Tác động đến Người dùng: Có bao nhiêu người dùng được hưởng lợi?
- Phù hợp với Chiến lược: Có phù hợp với sứ mệnh cốt lõi không?
- Tính khả thi về Triển khai: Độ phức tạp kỹ thuật?
- Yêu cầu về Nguồn lực: Nỗ lực phát triển cần thiết?
- Mức độ Rủi ro: Các tác động tiêu cực tiềm ẩn?

**Độ ưu tiên = (Tác động đến Người dùng × Phù hợp với Chiến lược) / (Nỗ lực Triển khai × Mức độ Rủi ro)**

**Kết quả cần tạo:**

- Trình bày 3 tính năng còn thiếu có độ ưu tiên cao nhất dựa trên điểm số
- Đối với mỗi tính năng, cung cấp:
  - Tên tính năng
  - Trạng thái hiện tại
  - Tác động nếu không được triển khai
  - Các phụ thuộc vào các tính năng khác

## 4. Giai đoạn Xây dựng Đặc tả

- Đối với mỗi tính năng được ưu tiên, hãy phát triển một đặc tả chi tiết nhưng thực tế:
  - Bắt đầu với triết lý: đơn giản hơn phức tạp
  - Tập trung vào chức năng MVP (Sản phẩm Khả dụng Tối thiểu) trước tiên
  - Xem xét trải nghiệm của nhà phát triển
  - Giữ cho đặc tả thân thiện với việc triển khai

**Đối với Mỗi Đặc tả Tính năng:**

1.  **Tổng quan & Phạm vi**

    - Nó giải quyết vấn đề gì?
    - Bao gồm những gì và loại trừ rõ ràng những gì?

2.  **Yêu cầu Kỹ thuật**

    - Chức năng cốt lõi cần thiết
    - Các giao diện người dùng (API, UI, CLI, v.v.)
    - Các điểm tích hợp với mã hiện có

3.  **Kế hoạch Triển khai**

    - Các mô-đun/tệp chính cần tạo hoặc sửa đổi
    - Các ví dụ mã đơn giản cho thấy phương pháp tiếp cận
    - Cấu trúc dữ liệu và giao diện rõ ràng

4.  **Tiêu chí Chấp nhận**
    - Làm thế nào chúng ta biết khi nào nó hoàn thành?
    - Chức năng cụ thể nào phải hoạt động?
    - Những bài kiểm thử nào phải vượt qua?

## 5. Giai đoạn Tạo Issue trên GitHub

- Đối với mỗi đặc tả, tạo một issue trên GitHub:
  - Tiêu đề rõ ràng, mô tả
  - Đặc tả toàn diện trong phần thân
  - Các nhãn phù hợp (enhancement, high-priority, v.v.)
  - Đề cập rõ ràng triết lý MVP khi có liên quan

**Cấu trúc Mẫu Issue:**

# [Tên Tính năng]

## Tổng quan

[Mô tả ngắn gọn về tính năng và mục đích của nó]

## Phạm vi

[Bao gồm những gì và loại trừ rõ ràng những gì]

## Yêu cầu Kỹ thuật

[Các nhu cầu và ràng buộc kỹ thuật cụ thể]

## Kế hoạch Triển khai

[Phương pháp tiếp cận từng bước với các ví dụ mã đơn giản]

## Tiêu chí Chấp nhận

[Danh sách rõ ràng các yêu cầu để coi tính năng là hoàn chỉnh]

## Độ ưu tiên

[Lý giải cho việc ưu tiên]

## Các phụ thuộc

- **Chặn (Blocks):** [Danh sách các issue bị chặn bởi issue này]
- **Bị chặn bởi (Blocked by):** [Danh sách các issue mà issue này phụ thuộc vào]

## Quy mô Triển khai

- **Nỗ lực ước tính:** [Nhỏ/Trung bình/Lớn]
- **Các issue con:** [Liên kết đến các issue con nếu đây là issue cha]

## 5.5 Tối ưu hóa Phân bổ Công việc

- **Phân tích tính Độc lập**

  - Xem xét từng đặc tả để xác định các thành phần thực sự độc lập
  - Tái cấu trúc các đặc tả để tối đa hóa các luồng công việc độc lập
  - Tạo ra ranh giới rõ ràng giữa các thành phần phụ thuộc lẫn nhau

- **Sơ đồ hóa Phụ thuộc**

  - Đối với các tính năng có các phụ thuộc không thể tránh khỏi, thiết lập hệ thống phân cấp issue rõ ràng
  - Tạo các issue cha cho tính năng tổng thể với các issue con cho các thành phần
  - Ghi lại rõ ràng các mối quan hệ "bị chặn bởi" và "chặn"

- **Cân bằng Khối lượng Công việc**
  - Chia nhỏ các đặc tả lớn thành các issue con nhỏ hơn, dễ quản lý
  - Đảm bảo mỗi issue con đại diện cho 1-3 ngày làm việc của nhà phát triển
  - Bao gồm các tiêu chí chấp nhận cụ thể cho từng issue con

**Hướng dẫn Triển khai:**

- Sử dụng cú pháp liên kết issue của GitHub để tạo các mối quan hệ rõ ràng
- Thêm các nhãn để chỉ ra trạng thái phụ thuộc (ví dụ: "blocked", "prerequisite")
- Bao gồm độ phức tạp/nỗ lực ước tính cho mỗi issue để hỗ trợ lập kế hoạch sprint

## 6. Giai đoạn Đánh giá Cuối cùng

- Tóm tắt tất cả các đặc tả đã tạo
- Nêu bật các phụ thuộc triển khai giữa các tính năng
- Đề xuất một thứ tự triển khai hợp lý
- Ghi chú bất kỳ thách thức hoặc cân nhắc tiềm năng nào

Hãy nhớ trong suốt quá trình này:

- Ưu tiên sự đơn giản hơn sự phức tạp
- Bắt đầu với các triển khai khả dụng tối thiểu có thể hoạt động
- Tập trung vào trải nghiệm của nhà phát triển
- Xây dựng một nền tảng có thể mở rộng sau này
- Xem xét cộng đồng mã nguồn mở và mô hình đóng góp

Việc thể hiện phương pháp tiếp cận của chúng ta qua quy trình này sẽ giúp duy trì tính nhất quán trong cách các tính năng được đặc tả và ưu tiên, đảm bảo rằng các dự án phần mềm phát triển một cách có suy nghĩ và lấy người dùng
