---
mode: "agent"
description: "Cập nhật một phần trong tệp markdown với một chỉ mục/bảng các tệp từ một thư mục được chỉ định."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Cập nhật Chỉ mục Tệp Markdown

Cập nhật tệp markdown `${file}` với một chỉ mục/bảng các tệp từ thư mục `${input:folder}`.

## Quy trình

1.  **Quét**: Đọc tệp markdown đích `${file}` để hiểu cấu trúc hiện có.
2.  **Khám phá**: Liệt kê tất cả các tệp trong thư mục được chỉ định `${input:folder}` khớp với mẫu `${input:pattern}`.
3.  **Phân tích**: Xác định xem có phần bảng/chỉ mục hiện có để cập nhật hay tạo cấu trúc mới.
4.  **Cấu trúc**: Tạo định dạng bảng/danh sách phù hợp dựa trên loại tệp và nội dung hiện có.
5.  **Cập nhật**: Thay thế phần hiện có hoặc thêm phần mới với chỉ mục tệp.
6.  **Xác thực**: Đảm bảo cú pháp markdown hợp lệ và định dạng nhất quán.

## Phân tích Tệp

Đối với mỗi tệp được khám phá, hãy trích xuất:

- **Tên**: Tên tệp có hoặc không có phần mở rộng tùy theo ngữ cảnh.
- **Loại**: Phần mở rộng và danh mục tệp (ví dụ: `.md`, `.js`, `.py`).
- **Mô tả**: Dòng chú thích đầu tiên, tiêu đề hoặc mục đích được suy ra.
- **Kích thước**: Kích thước tệp để tham khảo (tùy chọn).
- **Sửa đổi**: Ngày sửa đổi cuối cùng (tùy chọn).

## Các tùy chọn Cấu trúc Bảng

Chọn định dạng dựa trên loại tệp và nội dung hiện có:

### Tùy chọn 1: Danh sách Đơn giản

```markdown
## Các tệp trong ${folder}

- [tên_tệp.ext](đường_dẫn/đến/tên_tệp.ext) - Mô tả
- [tên_tệp2.ext](đường_dẫn/đến/tên_tệp2.ext) - Mô tả
```

### Tùy chọn 2: Bảng Chi tiết

| Tệp                                        | Loại         | Mô tả |
| ------------------------------------------ | ------------ | ----- |
| [tên_tệp.ext](đường_dẫn/đến/tên_tệp.ext)   | Phần mở rộng | Mô tả |
| [tên_tệp2.ext](đường_dẫn/đến/tên_tệp2.ext) | Phần mở rộng | Mô tả |

### Tùy chọn 3: Các mục được Phân loại

Nhóm các tệp theo loại/danh mục với các phần hoặc bảng con riêng biệt.

## Chiến lược Cập nhật

- 🔄 **Cập nhật hiện có**: Nếu phần bảng/chỉ mục đã tồn tại, hãy thay thế nội dung trong khi vẫn giữ nguyên cấu trúc.
- ➕ **Thêm mới**: Nếu không có phần nào tồn tại, hãy tạo phần mới bằng định dạng phù hợp nhất.
- 📋 **Bảo tồn**: Duy trì định dạng markdown, cấp độ tiêu đề và luồng tài liệu hiện có.
- 🔗 **Liên kết**: Sử dụng đường dẫn tương đối cho các liên kết tệp trong kho lưu trữ.

## Nhận dạng Phần

Tìm kiếm các phần hiện có với các mẫu sau:

- Tiêu đề chứa: "index", "files", "contents", "directory", "list"
- Bảng có các cột liên quan đến tệp
- Danh sách có liên kết tệp
- Chú thích HTML đánh dấu các phần chỉ mục tệp

## Yêu cầu

- Bảo tồn cấu trúc và định dạng markdown hiện có
- Sử dụng đường dẫn tương đối cho các liên kết tệp
- Bao gồm mô tả tệp khi có sẵn
- Sắp xếp các tệp theo thứ tự bảng chữ cái theo mặc định
- Xử lý các ký tự đặc biệt trong tên tệp
- Xác thực tất cả cú pháp markdown
