---
mode: "agent"
description: "Tạo một GitHub Issue cho yêu cầu tính năng từ tệp đặc tả sử dụng mẫu feature_request.yml."
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# Tạo GitHub Issue từ Tệp Đặc tả

Tạo GitHub Issue cho tệp đặc tả tại `${file}`.

## Quy trình

1. Phân tích tệp đặc tả để trích xuất các yêu cầu
2. Kiểm tra các issue hiện có bằng `search_issues`
3. Tạo issue mới bằng `create_issue` hoặc cập nhật issue hiện có bằng `update_issue`
4. Sử dụng mẫu `feature_request.yml` (sử dụng mẫu mặc định nếu không có)

## Yêu cầu

- Một issue duy nhất cho toàn bộ bản đặc tả
- Tiêu đề rõ ràng xác định bản đặc tả
- Chỉ bao gồm các thay đổi được yêu cầu bởi bản đặc tả
- Xác minh với các issue hiện có trước khi tạo

## Nội dung Issue

- Tiêu đề: Tên tính năng từ bản đặc tả
- Mô tả: Tuyên bố vấn đề, giải pháp đề xuất và bối cảnh
- Nhãn: feature,
