# Tạo File LLMs.txt từ Cấu Trúc Repository

Tạo file `llms.txt` mới từ đầu trong thư mục gốc của repository theo chuẩn chính thức tại https://llmstxt.org/. File này cung cấp hướng dẫn cấp cao cho các mô hình ngôn ngữ lớn (LLM) về vị trí tìm nội dung liên quan để hiểu mục đích và đặc tả của repository.

## Chỉ Thị Chính

Tạo file `llms.txt` toàn diện giúp LLM hiểu và điều hướng repository hiệu quả. File phải tuân thủ chuẩn `llms.txt` và tối ưu cho LLM nhưng vẫn dễ đọc với con người.

## Giai Đoạn Phân Tích & Lập Kế Hoạch

### Bước 1: Xem xét chuẩn llms.txt

- Đọc kỹ đặc tả tại https://llmstxt.org/
- Nắm rõ cấu trúc và yêu cầu định dạng markdown

### Bước 2: Phân tích cấu trúc repository

- Kiểm tra toàn bộ cấu trúc repository
- Xác định mục đích và phạm vi
- Liệt kê thư mục và file quan trọng

### Bước 3: Khám phá nội dung

- Tìm README
- Tìm tài liệu (`.md` trong `/docs/`, `/spec/`,...)
- Tìm file đặc tả
- Tìm file cấu hình
- Tìm ví dụ và code mẫu

### Bước 4: Lập kế hoạch triển khai

- Tóm tắt mục đích repository
- Liệt kê file chính và phụ
- Xây dựng cấu trúc `llms.txt`

## Yêu Cầu Triển Khai

### Tuân thủ định dạng

1. **H1**: Tên project
2. **Blockquote**: Mô tả ngắn
3. **Thông tin bổ sung**: Không có heading
4. **H2**: Danh sách file liên kết

### Yêu cầu nội dung

- Tên project rõ ràng
- Tóm tắt mục đích
- Liệt kê file quan trọng theo danh mục

### Tiêu chí chọn file

Bao gồm file:
- Giải thích mục đích dự án
- Tài liệu kỹ thuật chính
- Ví dụ sử dụng
- Cấu hình và hướng dẫn cài đặt

Loại trừ file:
- Chỉ chi tiết triển khai
- Thông tin trùng lặp
- Build artifacts hoặc file sinh ra

## Các Bước Thực Hiện

1. Phân tích repository
2. Lập kế hoạch nội dung
3. Tạo file `llms.txt` tuân chuẩn
4. Kiểm tra & xác thực

## Đảm Bảo Chất Lượng

- ✅ Đúng chuẩn định dạng
- ✅ Ngôn ngữ rõ ràng
- ✅ Bao quát file cần thiết
- ✅ Tổ chức hợp lý

## Mẫu Cấu Trúc

```txt
# [Tên Repository]

> [Mô tả ngắn gọn]

## Documentation

- [Main README](README.md): Hướng dẫn chính
- [Contributing Guide](CONTRIBUTING.md): Quy tắc đóng góp

## Specifications

- [Technical Specification](spec/technical-spec.md): Yêu cầu kỹ thuật

## Examples

- [Basic Example](examples/basic-usage.md): Ví dụ cơ bản

## Configuration

- [Setup Guide](docs/setup.md): Hướng dẫn cài đặt

## Optional

- [Architecture Documentation](docs/architecture.md): Tài liệu kiến trúc
```