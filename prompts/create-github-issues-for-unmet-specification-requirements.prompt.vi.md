---
mode: "agent"
description: "Tạo GitHub Issues cho các yêu cầu chưa được triển khai từ các tệp đặc tả bằng cách sử dụng mẫu feature_request.yml."
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# Tạo GitHub Issues cho các Yêu cầu Đặc tả Chưa được Đáp ứng

Tạo GitHub Issues cho các yêu cầu chưa được triển khai trong tệp đặc tả tại `${file}`.

## Quy trình

1.  Phân tích tệp đặc tả để trích xuất tất cả các yêu cầu.
2.  Kiểm tra trạng thái triển khai trong codebase cho mỗi yêu cầu.
3.  Tìm kiếm các issue hiện có bằng `search_issues` để tránh trùng lặp.
4.  Tạo issue mới cho mỗi yêu cầu chưa được triển khai bằng `create_issue`.
5.  Sử dụng mẫu `feature_request.yml` (sử dụng mặc định nếu không có).

## Yêu cầu

- Một issue cho mỗi yêu cầu chưa được triển khai từ tệp đặc tả.
- Ánh xạ rõ ràng giữa ID yêu cầu và mô tả.
- Bao gồm hướng dẫn triển khai và tiêu chí chấp nhận.
- Xác minh với các issue hiện có trước khi tạo.

## Nội dung Issue

- Tiêu đề: ID yêu cầu và mô tả ngắn gọn.
- Mô tả: Yêu cầu chi tiết, phương pháp triển khai và ngữ cảnh.
- Nhãn: feature, enhancement (nếu phù hợp).

## Kiểm tra Triển khai

- Tìm kiếm codebase cho các mẫu mã liên quan.
- Kiểm tra các tệp đặc tả liên quan trong thư mục `/spec/`.
- Xác minh yêu cầu không được triển khai
