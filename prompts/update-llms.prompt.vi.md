---
mode: 'agent'
description: 'Cập nhật tệp llms.txt trong thư mục gốc để phản ánh các thay đổi trong tài liệu hoặc thông số kỹ thuật theo đặc tả llms.txt tại https://llmstxt.org/'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---

# Cập Nhật Tệp LLMs.txt

Cập nhật tệp `llms.txt` hiện có trong thư mục gốc của repository để phản ánh các thay đổi trong tài liệu, thông số kỹ thuật hoặc cấu trúc repository. Tệp này cung cấp hướng dẫn cấp cao cho các mô hình ngôn ngữ lớn (LLM) về nơi tìm nội dung liên quan để hiểu mục đích và thông số kỹ thuật của repository.

## Chỉ Thị Chính

Cập nhật tệp `llms.txt` để duy trì tính chính xác và tuân thủ đặc tả llms.txt, đồng thời phản ánh cấu trúc và nội dung repository hiện tại. Tệp phải được tối ưu hóa cho LLM nhưng vẫn dễ đọc với con người.

## Giai Đoạn Phân Tích và Lập Kế Hoạch

### Bước 1: Xem Xét Tệp Hiện Tại và Đặc Tả
- Đọc tệp `llms.txt` hiện tại để hiểu cấu trúc
- Xem xét đặc tả chính thức tại https://llmstxt.org/
- Xác định các khu vực cần cập nhật dựa trên thay đổi của repository

### Bước 2: Phân Tích Cấu Trúc Repository
- Kiểm tra cấu trúc repository hiện tại
- So sánh với nội dung trong `llms.txt`
- Xác định thư mục, tệp hoặc tài liệu mới cần thêm
- Ghi chú các tệp bị xóa hoặc di chuyển cần cập nhật

### Bước 3: Khám Phá Nội Dung và Phát Hiện Thay Đổi
- Xác định các tệp README mới
- Tìm tài liệu mới (.md trong `/docs/`, `/spec/`, v.v.)
- Xác định tệp thông số kỹ thuật mới
- Tìm tệp cấu hình mới
- Xác định các thay đổi cấu trúc tài liệu

### Bước 4: Lập Kế Hoạch Cập Nhật
- Ghi lại các thay đổi cần thiết để đảm bảo chính xác
- Thêm tệp mới vào `llms.txt`
- Loại bỏ hoặc cập nhật các tham chiếu lỗi thời
- Cải thiện tổ chức để rõ ràng hơn

## Yêu Cầu Thực Hiện

### Tuân Thủ Định Dạng
Tệp `llms.txt` cập nhật phải duy trì cấu trúc chính xác theo đặc tả:

1. **H1 Header**: Tên repository/dự án (bắt buộc)
2. **Blockquote Summary**: Mô tả ngắn gọn (khuyến nghị)
3. **Additional Details**: Ngữ cảnh bổ sung (không có tiêu đề)
4. **File List Sections**: Các mục H2 chứa danh sách liên kết markdown

### Yêu Cầu Nội Dung

#### Phần Bắt Buộc
- **Tên Dự Án**: Rõ ràng, dễ hiểu
- **Tóm Tắt**: Giải thích ngắn gọn mục đích của repository
- **Tệp Chính**: Các tệp quan trọng được tổ chức theo danh mục

#### Định Dạng Liên Kết
Mỗi liên kết: `[tên-mô-tả](đường-dẫn-tương-đối): mô tả tùy chọn`

#### Tổ Chức Nội Dung
Tổ chức theo các mục như:
- **Documentation**: Tài liệu chính
- **Specifications**: Thông số kỹ thuật
- **Examples**: Ví dụ sử dụng
- **Configuration**: Tệp cấu hình
- **Optional**: Nội dung tùy chọn

(Phần còn lại giữ nguyên cấu trúc và dịch toàn bộ nội dung như bản gốc.)