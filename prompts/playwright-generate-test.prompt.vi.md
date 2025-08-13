# Tạo Test với Playwright MCP

Mục tiêu của bạn là tạo một bài kiểm thử Playwright dựa trên kịch bản đã được cung cấp sau khi hoàn thành tất cả các bước được chỉ định.

## Hướng Dẫn Cụ Thể

- Bạn sẽ được cung cấp một kịch bản và cần tạo một bài kiểm thử Playwright cho nó. Nếu người dùng không cung cấp kịch bản, hãy yêu cầu họ cung cấp.
- KHÔNG được tạo mã kiểm thử sớm hoặc chỉ dựa trên kịch bản mà chưa hoàn thành tất cả các bước đã chỉ định.
- HÃY chạy các bước từng bước một bằng các công cụ được cung cấp bởi Playwright MCP.
- Chỉ sau khi hoàn thành tất cả các bước, mới tạo bài kiểm thử Playwright TypeScript sử dụng `@playwright/test` dựa trên lịch sử tin nhắn.
- Lưu tệp kiểm thử đã tạo vào thư mục tests.
- Thực thi tệp kiểm thử và lặp lại cho đến khi bài kiểm thử vượt qua.