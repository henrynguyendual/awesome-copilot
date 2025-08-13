---
chế độ: 'agent'
mô tả: 'Cập nhật một phần trong file markdown với mục lục/bảng liệt kê các file từ một thư mục được chỉ định.'
công_cụ: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# Cập nhật Mục lục File Markdown

Cập nhật file markdown `${file}` với mục lục/bảng liệt kê các file từ thư mục `${input:folder}`.

## Quy trình

1. **Quét**: Đọc file markdown đích `${file}` để hiểu cấu trúc hiện tại
2. **Khám phá**: Liệt kê tất cả các file trong thư mục `${input:folder}` phù hợp với mẫu `${input:pattern}`
3. **Phân tích**: Xác định xem có phần bảng/mục lục hiện tại cần cập nhật hay tạo mới
4. **Cấu trúc**: Tạo bảng/danh sách phù hợp dựa trên loại file và nội dung hiện có
5. **Cập nhật**: Thay thế phần hiện có hoặc thêm phần mới với mục lục file
6. **Xác minh**: Đảm bảo cú pháp markdown hợp lệ và định dạng đồng nhất

## Phân tích File

Với mỗi file tìm được, trích xuất:

- **Tên**: Tên file có hoặc không kèm phần mở rộng tuỳ ngữ cảnh
- **Loại**: Phần mở rộng và loại (ví dụ: `.md`, `.js`, `.py`)
- **Mô tả**: Dòng comment đầu tiên, tiêu đề, hoặc mục đích suy đoán
- **Kích thước**: Dung lượng file (tùy chọn)
- **Chỉnh sửa lần cuối**: Ngày chỉnh sửa gần nhất (tùy chọn)

## Tuỳ chọn Cấu trúc Bảng

Chọn định dạng dựa trên loại file và nội dung hiện có:

### Tuỳ chọn 1: Danh sách đơn giản

```markdown
## Các file trong ${folder}

- [tênfile.ext](path/to/tênfile.ext) - Mô tả
- [tênfile2.ext](path/to/tênfile2.ext) - Mô tả
```

### Tuỳ chọn 2: Bảng chi tiết

| File | Loại | Mô tả |
|------|------|-------|
| [tênfile.ext](path/to/tênfile.ext) | Phần mở rộng | Mô tả |
| [tênfile2.ext](path/to/tênfile2.ext) | Phần mở rộng | Mô tả |

### Tuỳ chọn 3: Phân loại theo nhóm

Nhóm file theo loại/danh mục với từng phần hoặc bảng con riêng.

## Chiến lược Cập nhật

- 🔄 **Cập nhật hiện có**: Nếu đã có bảng/mục lục thì thay thế nội dung, giữ nguyên cấu trúc
- ➕ **Thêm mới**: Nếu chưa có thì tạo phần mới với định dạng phù hợp nhất
- 📋 **Giữ nguyên**: Duy trì định dạng và cấu trúc markdown hiện tại
- 🔗 **Liên kết**: Sử dụng đường dẫn tương đối cho liên kết tới file trong repository

## Xác định Phần

Tìm các phần hiện có theo các mẫu:

- Tiêu đề chứa: "index", "files", "contents", "directory", "list"
- Bảng với các cột liên quan đến file
- Danh sách có liên kết file
- Comment HTML đánh dấu phần mục lục file

## Yêu cầu

- Giữ nguyên cấu trúc và định dạng markdown
- Sử dụng đường dẫn tương đối
- Bao gồm mô tả file nếu có
- Sắp xếp file theo thứ tự ABC mặc định
- Xử lý ký tự đặc biệt trong tên file
- Đảm bảo cú pháp markdown hợp lệ
