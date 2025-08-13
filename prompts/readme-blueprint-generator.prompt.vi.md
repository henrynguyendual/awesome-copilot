# Prompt Tạo README

Tạo file README.md toàn diện cho repository này bằng cách phân tích các file tài liệu trong thư mục `.github/copilot` và file `copilot-instructions.md`. Thực hiện theo các bước sau:

1. Quét tất cả các file trong thư mục `.github/copilot`, như:
   - Architecture (Kiến trúc)
   - Code_Exemplars (Ví dụ mã)
   - Coding_Standards (Tiêu chuẩn mã nguồn)
   - Project_Folder_Structure (Cấu trúc thư mục dự án)
   - Technology_Stack (Ngăn xếp công nghệ)
   - Unit_Tests (Kiểm thử đơn vị)
   - Workflow_Analysis (Phân tích quy trình làm việc)

2. Xem xét thêm file `copilot-instructions.md` trong thư mục `.github`

3. Tạo README.md với các phần sau:

## Tên Dự Án và Mô Tả
- Lấy tên dự án và mục đích chính từ tài liệu
- Bao gồm mô tả ngắn gọn về chức năng của dự án

## Ngăn Xếp Công Nghệ
- Liệt kê các công nghệ, ngôn ngữ và framework chính được sử dụng
- Bao gồm thông tin phiên bản nếu có
- Lấy thông tin chủ yếu từ file `Technology_Stack`

## Kiến Trúc Dự Án
- Cung cấp cái nhìn tổng quan cấp cao về kiến trúc
- Nếu có sơ đồ, cân nhắc đưa vào
- Lấy từ file `Architecture`

## Bắt Đầu
- Bao gồm hướng dẫn cài đặt dựa trên ngăn xếp công nghệ
- Thêm các bước thiết lập và cấu hình
- Bao gồm các yêu cầu tiên quyết

## Cấu Trúc Dự Án
- Tóm tắt tổ chức thư mục
- Lấy từ file `Project_Folder_Structure`

## Tính Năng Chính
- Liệt kê các chức năng và tính năng chính của dự án
- Trích xuất từ nhiều tài liệu

## Quy Trình Phát Triển
- Tóm tắt quy trình phát triển
- Bao gồm chiến lược nhánh nếu có
- Lấy từ file `Workflow_Analysis`

## Tiêu Chuẩn Mã Nguồn
- Tóm tắt các tiêu chuẩn và quy ước mã nguồn chính
- Lấy từ file `Coding_Standards`

## Kiểm Thử
- Giải thích cách tiếp cận và công cụ kiểm thử
- Lấy từ file `Unit_Tests`

## Đóng Góp
- Hướng dẫn đóng góp cho dự án
- Tham khảo các ví dụ mã nếu cần
- Lấy từ `Code_Exemplars` và `copilot-instructions`

## Giấy Phép
- Bao gồm thông tin giấy phép nếu có

Định dạng README bằng Markdown chuẩn, bao gồm:
- Tiêu đề và phụ đề rõ ràng
- Khối mã khi cần thiết
- Danh sách để dễ đọc
- Liên kết đến các file tài liệu khác
- Badge cho trạng thái build, phiên bản,... nếu có

Giữ README ngắn gọn nhưng đầy đủ thông tin, tập trung vào những gì mà lập trình viên hoặc người dùng mới cần biết về dự án.