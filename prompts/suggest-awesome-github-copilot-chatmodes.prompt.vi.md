---
mode: "agent"
description: "Đề xuất các tệp chatmode GitHub Copilot phù hợp từ kho lưu trữ awesome-copilot dựa trên ngữ cảnh kho lưu trữ hiện tại và lịch sử trò chuyện, tránh trùng lặp với các chatmode hiện có trong kho lưu trữ này."
tools: ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
---

# Đề xuất các Chatmode Tuyệt vời của GitHub Copilot

Phân tích ngữ cảnh kho lưu trữ hiện tại và đề xuất các tệp chatmode phù hợp từ [kho lưu trữ awesome-copilot của GitHub](https://github.com/github/awesome-copilot/tree/main/chatmodes) mà chưa có sẵn trong kho lưu trữ này.

## Quy trình

1.  **Tải các Chatmode có sẵn**: Trích xuất danh sách và mô tả các chatmode từ [thư mục chatmodes của awesome-copilot](https://github.com/github/awesome-copilot/tree/main/chatmodes)
2.  **Quét các Chatmode cục bộ**: Khám phá các tệp chatmode hiện có trong thư mục `.github/chatmodes/`
3.  **Trích xuất Mô tả**: Đọc phần front matter từ các tệp chatmode cục bộ để lấy mô tả
4.  **Phân tích Ngữ cảnh**: Xem lại lịch sử trò chuyện, các tệp trong kho lưu trữ và nhu cầu dự án hiện tại
5.  **So sánh với cái hiện có**: Kiểm tra so với các chatmode đã có sẵn trong kho lưu trữ này
6.  **Đối chiếu sự phù hợp**: So sánh các chatmode có sẵn với các mẫu và yêu cầu đã xác định
7.  **Trình bày các lựa chọn**: Hiển thị các chatmode phù hợp kèm theo mô tả, lý do và trạng thái sẵn có
8.  **Xác thực**: Đảm bảo các chatmode được đề xuất sẽ bổ sung giá trị mà các chatmode hiện có chưa bao gồm
9.  **Đầu ra**: Cung cấp bảng có cấu trúc với các đề xuất, mô tả và liên kết đến cả chatmode của awesome-copilot và các chatmode cục bộ tương tự
10. **Các bước tiếp theo**: Nếu có bất kỳ đề xuất nào được đưa ra, hãy cung cấp hướng dẫn mà GitHub Copilot có thể làm theo để thêm các chatmode được đề xuất vào kho lưu trữ bằng cách tải tệp xuống thư mục chatmodes. Đề nghị thực hiện việc này tự động nếu người dùng xác nhận.

## Tiêu chí Phân tích Ngữ cảnh

🔍 **Các mẫu trong Kho lưu trữ**:

- Các ngôn ngữ lập trình được sử dụng (.cs, .js, .py, v.v.)
- Các chỉ báo về framework (ASP.NET, React, Azure, v.v.)
- Các loại dự án (ứng dụng web, API, thư viện, công cụ)
- Nhu cầu về tài liệu (README, specs, ADRs)

🗨️ **Ngữ cảnh Lịch sử Trò chuyện**:

- Các cuộc thảo luận và vấn đề gần đây
- Các yêu cầu tính năng hoặc nhu cầu triển khai
- Các mẫu đánh giá mã nguồn (code review)
- Yêu cầu về quy trình phát triển

## Định dạng Đầu ra

Hiển thị kết quả phân tích trong bảng có cấu trúc so sánh các chatmode của awesome-copilot với các chatmode hiện có trong kho lưu trữ:

| Chatmode của Awesome-Copilot                                                                                               | Mô tả                                     | Đã cài đặt | Chatmode cục bộ tương tự              | Lý do đề xuất                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------- | ------------------------------------- | ---------------------------------------------------------------------------- |
| [code-reviewer.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/code-reviewer.chatmode.md)       | Chatmode chuyên dụng để đánh giá mã nguồn | ❌ Không   | Không có                              | Sẽ nâng cao quy trình phát triển với sự hỗ trợ đánh giá mã nguồn chuyên dụng |
| [architect.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/architect.chatmode.md)               | Hướng dẫn về kiến trúc phần mềm           | ✅ Có      | azure_principal_architect.chatmode.md | Đã được bao gồm bởi các chatmode kiến trúc hiện có                           |
| [debugging-expert.chatmode.md](https://github.com/github/awesome-copilot/blob/main/chatmodes/debugging-expert.chatmode.md) | Chatmode hỗ trợ gỡ lỗi                    | ❌ Không   | Không có                              | Có thể cải thiện hiệu quả khắc phục sự cố cho nhóm phát triển                |

## Quy trình Khám phá Chatmode Cục bộ

1.  Liệt kê tất cả các tệp `*.chatmode.md` trong thư mục `.github/chatmodes/`
2.  Đối với mỗi tệp được phát hiện, đọc phần front matter để trích xuất `description`
3.  Xây dựng một danh sách đầy đủ các chatmode hiện có
4.  Sử dụng danh sách này để tránh đề xuất các bản sao

## Yêu cầu

- Sử dụng công cụ `githubRepo` để lấy nội dung từ thư mục chatmodes của kho lưu trữ awesome-copilot
- Quét hệ thống tệp cục bộ để tìm các chatmode hiện có trong thư mục `.github/chatmodes/`
- Đọc phần front matter YAML từ các tệp chatmode cục bộ để trích xuất mô tả
- So sánh với các chatmode hiện có trong kho lưu trữ này để tránh trùng lặp
- Tập trung vào những khoảng trống trong phạm vi của thư viện chatmode hiện tại
- Xác thực rằng các chatmode được đề xuất phù hợp với mục đích và tiêu chuẩn của kho lưu trữ
- Cung cấp lý do rõ ràng cho mỗi đề xuất
- Bao gồm các liên kết đến cả chatmode của awesome-copilot và các chatmode cục bộ tương tự
- Không cung cấp bất kỳ thông tin hoặc ngữ cảnh bổ sung nào ngoài bảng và phân tích

## Tham chiếu Biểu tượng

- ✅ Đã được cài đặt trong kho lưu trữ
- ❌ Chưa được cài đặt trong kho lưu
