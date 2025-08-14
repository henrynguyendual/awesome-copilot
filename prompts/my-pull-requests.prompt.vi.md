---
mode: "agent"
tools: ["githubRepo", "github", "get_me", "get_pull_request", "get_pull_request_comments", "get_pull_request_diff", "get_pull_request_files", "get_pull_request_reviews", "get_pull_request_status", "list_pull_requests", "request_copilot_review"]
description: "Liệt kê các pull request của tôi trong kho lưu trữ hiện tại"
---

Tìm kiếm kho lưu trữ hiện tại (sử dụng #githubRepo để biết thông tin kho lưu trữ) và liệt kê bất kỳ pull request nào bạn tìm thấy (sử dụng #list_pull_requests) được giao cho tôi.

Mô tả mục đích và chi tiết của mỗi pull request.

Nếu một PR đang chờ ai đó xem xét, hãy làm nổi bật điều đó trong câu trả lời.

Nếu có bất kỳ lỗi kiểm tra nào trên PR, hãy mô tả chúng và đề xuất các bản sửa lỗi có thể.

Nếu chưa có đánh giá nào được thực hiện bởi Copilot, hãy đề nghị yêu cầu một đánh giá bằng
