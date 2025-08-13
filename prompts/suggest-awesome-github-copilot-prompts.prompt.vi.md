---
mode: 'agent'
description: 'Gợi ý các tệp prompt GitHub Copilot liên quan từ kho awesome-copilot dựa trên ngữ cảnh của kho hiện tại và lịch sử trò chuyện, tránh trùng lặp với các prompt hiện có trong kho này.'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'github']
---

# Gợi Ý Prompt GitHub Copilot Tuyệt Vời

Phân tích ngữ cảnh kho hiện tại và gợi ý các tệp prompt liên quan từ [kho awesome-copilot của GitHub](https://github.com/github/awesome-copilot/tree/main/prompts) chưa có sẵn trong kho này.

## Quy Trình

1. **Lấy Danh Sách Prompt Có Sẵn**: Trích xuất danh sách prompt và mô tả từ [README của awesome-copilot](https://github.com/github/awesome-copilot/blob/main/README.md)
2. **Quét Prompt Cục Bộ**: Tìm các tệp prompt hiện có trong thư mục `.github/prompts/`
3. **Trích Xuất Mô Tả**: Đọc phần front matter từ các tệp prompt cục bộ để lấy mô tả
4. **Phân Tích Ngữ Cảnh**: Xem xét lịch sử trò chuyện, các tệp trong kho và nhu cầu hiện tại của dự án
5. **So Sánh Các Prompt Đã Có**: Kiểm tra các prompt đã tồn tại trong kho
6. **Đối Chiếu Mức Liên Quan**: So sánh các prompt có sẵn với nhu cầu và mẫu sử dụng
7. **Trình Bày Tùy Chọn**: Hiển thị prompt phù hợp kèm mô tả, lý do đề xuất và trạng thái hiện có
8. **Xác Thực**: Đảm bảo prompt đề xuất mang lại giá trị bổ sung chưa được bao phủ
9. **Kết Quả**: Cung cấp bảng so sánh giữa prompt awesome-copilot và prompt cục bộ
10. **Bước Tiếp Theo**: Nếu có đề xuất, hướng dẫn cách thêm vào repo hoặc thực hiện tự động nếu người dùng đồng ý

## Tiêu Chí Phân Tích Ngữ Cảnh

🔍 **Mẫu Dự Án**:
- Ngôn ngữ lập trình sử dụng (.cs, .js, .py, v.v.)
- Framework (ASP.NET, React, Azure, v.v.)
- Loại dự án (ứng dụng web, API, thư viện, công cụ)
- Nhu cầu tài liệu (README, specs, ADR)

🗨️ **Ngữ Cảnh Trò Chuyện**:
- Chủ đề và vấn đề gần đây
- Tính năng yêu cầu hoặc cần triển khai
- Mẫu review code
- Quy trình phát triển

## Định Dạng Kết Quả

Hiển thị kết quả trong bảng so sánh prompt awesome-copilot với prompt cục bộ:

| Prompt Awesome-Copilot | Mô Tả | Đã Cài | Prompt Cục Bộ Tương Tự | Lý Do Đề Xuất |
|-------------------------|-------|-------|------------------------|---------------|
| [code-review.md](https://github.com/github/awesome-copilot/blob/main/prompts/code-review.md) | Prompt review code tự động | ❌ Không | Không có | Giúp cải thiện quy trình review code với tiêu chuẩn thống nhất |
| [documentation.md](https://github.com/github/awesome-copilot/blob/main/prompts/documentation.md) | Sinh tài liệu dự án | ✅ Có | create_oo_component_documentation.prompt.md | Đã được bao phủ bởi prompt tài liệu hiện có |
| [debugging.md](https://github.com/github/awesome-copilot/blob/main/prompts/debugging.md) | Prompt hỗ trợ debug | ❌ Không | Không có | Giúp cải thiện hiệu quả xử lý lỗi cho nhóm phát triển |

## Quy Trình Tìm Prompt Cục Bộ

1. Liệt kê tất cả các tệp `*.prompt.md` trong `.github/prompts/`
2. Đọc front matter để trích mô tả
3. Tạo danh sách prompt hiện có
4. So sánh để tránh đề xuất trùng lặp

## Yêu Cầu

- Sử dụng `githubRepo` để lấy nội dung thư mục prompts từ kho awesome-copilot
- Quét hệ thống file cục bộ để tìm prompt trong `.github/prompts/`
- Đọc YAML front matter để lấy mô tả
- So sánh với prompt đã có để tránh trùng
- Tập trung vào các khoảng trống chưa được bao phủ
- Đảm bảo phù hợp với mục tiêu dự án
- Cung cấp lý do rõ ràng cho từng đề xuất
- Kèm liên kết đến cả prompt awesome-copilot và prompt cục bộ tương tự
- Không thêm thông tin ngoài bảng và phân tích

## Tham Chiếu Biểu Tượng

- ✅ Đã cài trong repo
- ❌ Chưa cài trong repo