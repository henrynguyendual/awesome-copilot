---
mode: agent
description: "Khám phá trang web để kiểm thử bằng Playwright MCP"
tools: ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "playwright"]
model: "Claude Sonnet 4"
---

# Khám phá Trang web để Kiểm thử

Mục tiêu của bạn là khám phá trang web và xác định các chức năng chính.

## Hướng dẫn Cụ thể

1.  Điều hướng đến URL được cung cấp bằng Playwright MCP Server. Nếu không có URL nào được cung cấp, hãy yêu cầu người dùng cung cấp.
2.  Xác định và tương tác với 3-5 tính năng cốt lõi hoặc luồng người dùng.
3.  Ghi lại các tương tác của người dùng, các yếu tố giao diện người dùng có liên quan (và bộ định vị của chúng), và các kết quả mong đợi.
4.  Đóng ngữ cảnh trình duyệt sau khi hoàn thành.
5.  Cung cấp một bản tóm tắt ngắn gọn về những phát hiện của bạn.
6.  Đề xuất và tạo các trường hợp kiểm thử dựa trên quá trình khám
