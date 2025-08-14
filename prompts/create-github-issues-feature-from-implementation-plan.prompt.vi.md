---
mode: "agent"
description: "Tạo GitHub Issues từ các giai đoạn của kế hoạch triển khai bằng cách sử dụng các mẫu feature_request.yml hoặc chore_request.yml."
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# Tạo GitHub Issue từ Kế hoạch Triển khai

Tạo GitHub Issues cho kế hoạch triển khai tại `${file}`.

## Quy trình

1. Phân tích tệp kế hoạch để xác định các giai đoạn
2. Kiểm tra các issue hiện có bằng `search_issues`
3. Tạo issue mới cho mỗi giai đoạn bằng `create_issue` hoặc cập nhật issue hiện có bằng `update_issue`
4. Sử dụng các mẫu `feature_request.yml` hoặc `chore_request.yml` (sử dụng mẫu mặc định nếu không có)

## Yêu cầu

- Một issue cho mỗi giai đoạn triển khai
- Tiêu đề và mô tả rõ ràng, có cấu trúc
- Chỉ bao gồm các thay đổi được yêu cầu bởi kế hoạch
- Xác minh với các issue hiện có trước khi tạo

## Nội dung Issue

- Tiêu đề: Tên giai đoạn từ kế hoạch triển khai
- Mô tả: Chi tiết giai đoạn, yêu cầu và bối cảnh
- Nhãn: Phù hợp với loại issue (tính
