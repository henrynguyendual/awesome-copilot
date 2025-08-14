---
description: "Prompt tạo README.md thông minh, phân tích cấu trúc tài liệu dự án và tạo tài liệu toàn diện cho repository. Quét các tệp trong thư mục .github/copilot và tệp copilot-instructions.md để trích xuất thông tin dự án, ngăn xếp công nghệ, kiến trúc, quy trình phát triển, tiêu chuẩn viết mã và các phương pháp kiểm thử, đồng thời tạo tài liệu markdown có cấu trúc tốt với định dạng phù hợp, tham chiếu chéo và nội dung tập trung vào nhà phát triển."
---

# Prompt Tạo README

Tạo một tệp README.md toàn diện cho repository này bằng cách phân tích các tệp tài liệu trong thư mục .github/copilot và tệp copilot-instructions.md. Hãy làm theo các bước sau:

1. Quét tất cả các tệp trong thư mục .github/copilot, như:

   - Architecture (Kiến trúc)
   - Code_Exemplars (Mã nguồn mẫu)
   - Coding_Standards (Tiêu chuẩn viết mã)
   - Project_Folder_Structure (Cấu trúc thư mục dự án)
   - Technology_Stack (Ngăn xếp công nghệ)
   - Unit_Tests (Kiểm thử đơn vị)
   - Workflow_Analysis (Phân tích quy trình làm việc)

2. Cũng xem lại tệp copilot-instructions.md trong thư mục .github

3. Tạo một tệp README.md với các phần sau:

## Tên và Mô tả Dự án

- Trích xuất tên dự án và mục đích chính từ tài liệu
- Bao gồm một mô tả ngắn gọn về những gì dự án làm

## Ngăn xếp Công nghệ

- Liệt kê các công nghệ, ngôn ngữ và framework chính được sử dụng
- Bao gồm thông tin phiên bản khi có sẵn
- Lấy thông tin này chủ yếu từ tệp Technology_Stack

## Kiến trúc Dự án

- Cung cấp một cái nhìn tổng quan cấp cao về kiến trúc
- Cân nhắc bao gồm một sơ đồ đơn giản nếu được mô tả trong tài liệu
- Lấy nguồn từ tệp Architecture

## Bắt đầu

- Bao gồm hướng dẫn cài đặt dựa trên ngăn xếp công nghệ
- Thêm các bước thiết lập và cấu hình
- Bao gồm mọi điều kiện tiên quyết

## Cấu trúc Dự án

- Tổng quan ngắn gọn về tổ chức thư mục
- Lấy nguồn từ tệp Project_Folder_Structure

## Các tính năng chính

- Liệt kê các chức năng và tính năng chính của dự án
- Trích xuất từ các tệp tài liệu khác nhau

## Quy trình Phát triển

- Tóm tắt quy trình phát triển
- Bao gồm thông tin về chiến lược phân nhánh nếu có
- Lấy nguồn từ tệp Workflow_Analysis

## Tiêu chuẩn Viết mã

- Tóm tắt các tiêu chuẩn và quy ước viết mã chính
- Lấy nguồn từ tệp Coding_Standards

## Kiểm thử

- Giải thích phương pháp và công cụ kiểm thử
- Lấy nguồn từ tệp Unit_Tests

## Đóng góp

- Hướng dẫn đóng góp cho dự án
- Tham khảo bất kỳ mã nguồn mẫu nào để được hướng dẫn
- Lấy nguồn từ tệp Code_Exemplars và copilot-instructions

## Giấy phép

- Bao gồm thông tin giấy phép nếu có

Định dạng README bằng Markdown phù hợp, bao gồm:

- Các tiêu đề và tiêu đề phụ rõ ràng
- Các khối mã ở những nơi thích hợp
- Danh sách để dễ đọc hơn
- Liên kết đến các tệp tài liệu khác
- Huy hiệu cho trạng thái bản dựng, phiên bản, v.v. nếu có thông tin

Giữ cho README ngắn gọn nhưng đầy đủ thông tin, tập trung vào những gì các nhà phát triển hoặc người dùng mới cần biết về dự
