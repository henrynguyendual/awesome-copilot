---
mode: agent
description: "Tạo một bài kiểm thử Playwright dựa trên một kịch bản sử dụng Playwright MCP"
tools: ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "playwright"]
model: "Claude Sonnet 4"
---

# Tạo bài kiểm thử với Playwright MCP

Mục tiêu của bạn là tạo một bài kiểm thử Playwright dựa trên kịch bản được cung cấp sau khi hoàn thành tất cả các bước đã quy định.

## Hướng dẫn cụ thể

- Bạn được cung cấp một kịch bản và bạn cần tạo một bài kiểm thử playwright cho nó. Nếu người dùng không cung cấp kịch bản, bạn sẽ yêu cầu họ cung cấp.
- KHÔNG tạo mã kiểm thử sớm hoặc chỉ dựa trên kịch bản mà không hoàn thành tất cả các bước đã quy định.
- HÃY chạy từng bước một bằng các công cụ do Playwright MCP cung cấp.
- Chỉ sau khi tất cả các bước hoàn tất, hãy tạo ra một bài kiểm thử Playwright TypeScript sử dụng `@playwright/test` dựa trên lịch sử tin nhắn.
- Lưu tệp kiểm thử đã tạo vào thư mục `tests`.
- Thực thi tệp kiểm thử và lặp lại cho đến khi bài kiểm thử thành
