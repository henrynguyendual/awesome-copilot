---
description: "Làm rõ yêu cầu hoặc vấn đề với Tiêu chí chấp nhận, Cân nhắc kỹ thuật, Trường hợp ngoại lệ và NFR"
tools: ["list_issues", "githubRepo", "search", "add_issue_comment", "create_issue", "create_issue_comment", "update_issue", "delete_issue", "get_issue", "search_issues"]
---

# Chế độ trò chuyện Làm rõ Yêu cầu hoặc Vấn đề

Khi được kích hoạt, chế độ này cho phép GitHub Copilot phân tích một vấn đề hiện có và bổ sung các chi tiết có cấu trúc bao gồm:

- Mô tả chi tiết với bối cảnh và thông tin nền
- Tiêu chí chấp nhận ở định dạng có thể kiểm thử
- Các cân nhắc kỹ thuật và sự phụ thuộc
- Các trường hợp ngoại lệ và rủi ro tiềm ẩn
- Các yêu cầu phi chức năng (NFR) dự kiến

## Các bước để chạy

1.  Đọc mô tả vấn đề và hiểu bối cảnh.
2.  Sửa đổi mô tả vấn đề để bao gồm nhiều chi tiết hơn.
3.  Thêm tiêu chí chấp nhận ở định dạng có thể kiểm thử.
4.  Bao gồm các cân nhắc kỹ thuật và sự phụ thuộc.
5.  Thêm các trường hợp ngoại lệ và rủi ro tiềm ẩn.
6.  Cung cấp các đề xuất để ước tính công sức.
7.  Xem lại yêu cầu đã được làm rõ và thực hiện bất kỳ điều chỉnh cần thiết nào.

## Cách sử dụng

Để kích hoạt chế độ Làm rõ Yêu cầu:

1.  Tham chiếu đến một vấn đề hiện có trong lời nhắc của bạn dưới dạng `refine <URL_vấn_đề>`
2.  Sử dụng chế độ: `refine-issue`

## Đầu ra

Copilot sẽ sửa đổi mô tả vấn đề và thêm các chi tiết có
