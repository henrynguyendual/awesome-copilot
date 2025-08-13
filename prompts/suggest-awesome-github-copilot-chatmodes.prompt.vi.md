---
mode: 'agent'
description: 'Gợi ý các tệp chatmode GitHub Copilot liên quan từ kho awesome-copilot dựa trên ngữ cảnh của kho hiện tại và lịch sử trò chuyện, tránh trùng lặp với các chatmode hiện có trong kho này.'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'github']
---

# Gợi Ý Chatmode GitHub Copilot Tuyệt Vời

Phân tích ngữ cảnh kho hiện tại và gợi ý các tệp chatmode liên quan từ [kho awesome-copilot](https://github.com/github/awesome-copilot/tree/main/chatmodes) chưa có sẵn trong kho này.

## Quy Trình

1. **Lấy Danh Sách Chatmode Có Sẵn**: Trích xuất danh sách và mô tả chatmode từ [thư mục chatmodes của awesome-copilot](https://github.com/github/awesome-copilot/tree/main/chatmodes)
2. **Quét Chatmode Cục Bộ**: Tìm các tệp chatmode hiện có trong thư mục `.github/chatmodes/`
3. **Trích Xuất Mô Tả**: Đọc front matter từ các tệp chatmode cục bộ để lấy mô tả
4. **Phân Tích Ngữ Cảnh**: Xem xét lịch sử trò chuyện, tệp kho và nhu cầu hiện tại của dự án
5. **So Sánh Các Tệp Đã Có**: Kiểm tra các chatmode đã có trong kho này
6. **Đối Chiếu Mức Liên Quan**: So sánh các chatmode có sẵn với nhu cầu và mô hình sử dụng
7. **Trình Bày Tùy Chọn**: Hiển thị chatmode phù hợp kèm mô tả, lý do đề xuất và trạng thái hiện có
8. **Xác Thực**: Đảm bảo chatmode đề xuất mang lại giá trị bổ sung chưa được bao phủ
9. **Kết Quả**: Cung cấp bảng so sánh giữa chatmode awesome-copilot và chatmode cục bộ
10. **Bước Tiếp Theo**: Nếu có đề xuất, hướng dẫn cách thêm vào repo hoặc thực hiện tự động nếu người dùng đồng ý

## Tiêu Chí Phân Tích Ngữ Cảnh

🔍 **Mẫu Dự Án**:
- Ngôn ngữ lập trình sử dụng (.cs, .js, .py, v.v.)
- Framework (ASP.NET, React, Azure, v.v.)
- Loại dự án (web app, API, thư viện, công cụ)
- Nhu cầu tài liệu (README, specs, ADR)

🗨️ **Ngữ Cảnh Trò Chuyện**:
- Chủ đề và vấn đề gần đây
- Tính năng yêu cầu hoặc cần triển khai
- Mẫu review code
- Quy trình phát triển

## Định Dạng Kết Quả

Hiển thị kết quả trong bảng so sánh chatmode awesome-copilot với chatmode cục bộ:

| Chatmode Awesome-Copilot | Mô Tả | Đã Cài | Chatmode Cục Bộ Tương Tự | Lý Do Đề Xuất |
|---------------------------|-------|-------|--------------------------|---------------|
| [code-reviewer.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/code-reviewer.chatmode.md) | Chatmode review code chuyên dụng | ❌ Không | Không có | Giúp cải thiện quy trình review code |
| [architect.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/architect.chatmode.md) | Hướng dẫn kiến trúc phần mềm | ✅ Có | azure_principal_architect.chatmode.md | Đã được bao phủ bởi chatmode kiến trúc hiện có |
| [debugging-expert.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/debugging-expert.chatmode.md) | Chatmode hỗ trợ debug | ❌ Không | Không có | Cải thiện khả năng xử lý lỗi cho nhóm dev |

## Quy Trình Tìm Chatmode Cục Bộ

1. Liệt kê tất cả tệp `*.chatmode.md` trong `.github/chatmodes/`
2. Đọc front matter để trích mô tả
3. Tạo danh sách chatmode hiện có
4. So sánh để tránh đề xuất trùng lặp

## Yêu Cầu

- Dùng `githubRepo` để lấy nội dung thư mục chatmodes từ kho awesome-copilot
- Quét hệ thống file cục bộ để tìm chatmode trong `.github/chatmodes/`
- Đọc YAML front matter để lấy mô tả
- So sánh với chatmode đã có để tránh trùng
- Tập trung vào các khoảng trống chưa có chatmode bao phủ
- Đảm bảo phù hợp với mục tiêu dự án
- Cung cấp lý do rõ ràng cho từng đề xuất
- Kèm liên kết đến cả chatmode awesome-copilot và chatmode cục bộ tương tự
- Không thêm thông tin ngoài bảng và phân tích

## Tham Chiếu Biểu Tượng

- ✅ Đã cài trong repo
- ❌ Chưa cài trong repo