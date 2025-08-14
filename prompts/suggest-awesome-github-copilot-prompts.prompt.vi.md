---
mode: "agent"
description: "Đề xuất các tệp prompt GitHub Copilot có liên quan từ kho lưu trữ awesome-copilot dựa trên ngữ cảnh kho lưu trữ hiện tại và lịch sử trò chuyện, tránh trùng lặp với các prompt đã có trong kho lưu trữ này."
tools: ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
---

# Đề xuất các Prompt GitHub Copilot Tuyệt vời

Phân tích ngữ cảnh kho lưu trữ hiện tại và đề xuất các tệp prompt có liên quan từ [kho lưu trữ GitHub awesome-copilot](https://github.com/github/awesome-copilot/tree/main/prompts) chưa có sẵn trong kho lưu trữ này.

## Quy trình

1.  **Tải các Prompt có sẵn**: Trích xuất danh sách prompt và mô tả từ [README của awesome-copilot](https://github.com/github/awesome-copilot/blob/main/README.md)
2.  **Quét các Prompt cục bộ**: Khám phá các tệp prompt hiện có trong thư mục `.github/prompts/`
3.  **Trích xuất Mô tả**: Đọc phần front matter từ các tệp prompt cục bộ để lấy mô tả
4.  **Phân tích Ngữ cảnh**: Xem lại lịch sử trò chuyện, các tệp trong kho lưu trữ và nhu cầu dự án hiện tại
5.  **So sánh Hiện có**: Kiểm tra với các prompt đã có sẵn trong kho lưu trữ này
6.  **Đối chiếu Mức độ liên quan**: So sánh các prompt có sẵn với các mẫu và yêu cầu đã xác định
7.  **Trình bày Lựa chọn**: Hiển thị các prompt có liên quan kèm theo mô tả, lý do và trạng thái sẵn có
8.  **Xác thực**: Đảm bảo các prompt được đề xuất sẽ mang lại giá trị mới mà các prompt hiện có chưa bao gồm
9.  **Đầu ra**: Cung cấp bảng có cấu trúc với các đề xuất, mô tả và liên kết đến cả prompt của awesome-copilot và các prompt cục bộ tương tự
10. **Các bước tiếp theo**: Nếu có bất kỳ đề xuất nào được đưa ra, hãy cung cấp hướng dẫn mà GitHub Copilot có thể làm theo để thêm các prompt được đề xuất vào kho lưu trữ bằng cách tải tệp xuống thư mục prompts. Đề nghị thực hiện việc này tự động nếu người dùng xác nhận.

## Tiêu chí Phân tích Ngữ cảnh

🔍 **Các mẫu trong Kho lưu trữ**:

- Ngôn ngữ lập trình được sử dụng (.cs, .js, .py, v.v.)
- Các chỉ báo về framework (ASP.NET, React, Azure, v.v.)
- Các loại dự án (ứng dụng web, API, thư viện, công cụ)
- Nhu cầu về tài liệu (README, specs, ADRs)

🗨️ **Ngữ cảnh Lịch sử Trò chuyện**:

- Các cuộc thảo luận và vấn đề gần đây
- Các yêu cầu tính năng hoặc nhu cầu triển khai
- Các mẫu đánh giá mã (code review)
- Yêu cầu về quy trình phát triển

## Định dạng Đầu ra

Hiển thị kết quả phân tích trong bảng có cấu trúc so sánh các prompt của awesome-copilot với các prompt hiện có trong kho lưu trữ:

| Prompt Awesome-Copilot                                                                           | Mô tả                          | Đã cài đặt | Prompt cục bộ tương tự                      | Lý do đề xuất                                                                       |
| ------------------------------------------------------------------------------------------------ | ------------------------------ | ---------- | ------------------------------------------- | ----------------------------------------------------------------------------------- |
| [code-review.md](https://github.com/github/awesome-copilot/blob/main/prompts/code-review.md)     | Các prompt đánh giá mã tự động | ❌ Không   | Không có                                    | Sẽ cải thiện quy trình phát triển với các quy trình đánh giá mã được tiêu chuẩn hóa |
| [documentation.md](https://github.com/github/awesome-copilot/blob/main/prompts/documentation.md) | Tạo tài liệu dự án             | ✅ Có      | create_oo_component_documentation.prompt.md | Đã được bao gồm bởi các prompt tài liệu hiện có                                     |
| [debugging.md](https://github.com/github/awesome-copilot/blob/main/prompts/debugging.md)         | Các prompt hỗ trợ gỡ lỗi       | ❌ Không   | Không có                                    | Có thể cải thiện hiệu quả khắc phục sự cố cho nhóm phát triển                       |

## Quy trình Khám phá Prompt Cục bộ

1.  Liệt kê tất cả các tệp `*.prompt.md` trong thư mục `.github/prompts/`.
2.  Đối với mỗi tệp được phát hiện, đọc phần front matter để trích xuất `description` (mô tả).
3.  Xây dựng một danh sách đầy đủ các prompt hiện có.
4.  Sử dụng danh sách này để tránh đề xuất các prompt trùng lặp.

## Yêu cầu

- Sử dụng công cụ `githubRepo` để lấy nội dung từ kho lưu trữ awesome-copilot.
- Quét hệ thống tệp cục bộ để tìm các prompt hiện có trong thư mục `.github/prompts/`.
- Đọc phần front matter YAML từ các tệp prompt cục bộ để trích xuất mô tả.
- So sánh với các prompt hiện có trong kho lưu trữ này để tránh trùng lặp.
- Tập trung vào những khoảng trống trong phạm vi của thư viện prompt hiện tại.
- Xác thực rằng các prompt được đề xuất phù hợp với mục đích và tiêu chuẩn của kho lưu trữ.
- Cung cấp lý do rõ ràng cho mỗi đề xuất.
- Bao gồm các liên kết đến cả prompt của awesome-copilot và các prompt cục bộ tương tự.
- Không cung cấp bất kỳ thông tin hoặc ngữ cảnh bổ sung nào ngoài bảng và phân tích.

## Chú thích Biểu tượng

- ✅ Đã được cài đặt trong kho lưu trữ
- ❌ Chưa được cài đặt
