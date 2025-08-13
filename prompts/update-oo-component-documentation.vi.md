---
chế_độ: 'agent'
mô_tả: 'Cập nhật tài liệu thành phần hướng đối tượng hiện có theo các tiêu chuẩn thực hành tốt nhất của ngành và tiêu chuẩn tài liệu kiến trúc.'
công_cụ: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# Cập nhật Tài liệu Thành phần Hướng Đối tượng Chuẩn

Cập nhật file tài liệu hiện có tại: `${file}` bằng cách phân tích mã nguồn thành phần tương ứng.

Trích xuất đường dẫn thành phần từ phần front matter của tài liệu hiện có (`component_path`) hoặc suy ra từ nội dung tài liệu. Phân tích việc triển khai thành phần hiện tại và cập nhật tài liệu cho phù hợp.

**Tiêu chuẩn Tài liệu:**

- DOC-001: Tuân theo các mức tài liệu của mô hình C4 (Ngữ cảnh, Container, Thành phần, Mã)
- DOC-002: Căn chỉnh với mẫu tài liệu kiến trúc phần mềm Arc42
- DOC-003: Tuân thủ tiêu chuẩn IEEE 1016 về Mô tả Thiết kế Phần mềm
- DOC-004: Sử dụng nguyên tắc Tài liệu Agile (chỉ ghi lại những gì cần thiết và có giá trị)
- DOC-005: Nhắm đến đối tượng chính là các lập trình viên và người bảo trì

**Hướng dẫn Phân tích:**

- ANA-001: Đọc tài liệu hiện có để hiểu ngữ cảnh và cấu trúc thành phần
- ANA-002: Xác định đường dẫn thành phần từ front matter hoặc nội dung
- ANA-003: Kiểm tra mã nguồn hiện tại để tìm cấu trúc lớp và kế thừa
- ANA-004: So sánh tài liệu hiện tại với triển khai hiện tại
- ANA-005: Xác định mẫu thiết kế và thay đổi kiến trúc
- ANA-006: Cập nhật API công khai, interface và phụ thuộc
- ANA-007: Nhận diện mẫu tạo lập/cấu trúc/hành vi mới hoặc thay đổi
- ANA-008: Cập nhật tham số, kiểu trả về và ngoại lệ của phương thức
- ANA-009: Đánh giá lại hiệu năng, bảo mật, độ tin cậy, khả năng bảo trì
- ANA-010: Cập nhật mô hình tích hợp và luồng dữ liệu

**Tối ưu theo Ngôn ngữ:**

- LNG-001: **C#/.NET** - async/await, dependency injection, cấu hình, giải phóng tài nguyên
- LNG-002: **Java** - Spring framework, annotation, xử lý ngoại lệ, đóng gói
- LNG-003: **TypeScript/JavaScript** - module, async pattern, type, npm
- LNG-004: **Python** - package, virtual environment, type hint, testing

**Chiến lược Cập nhật:**

- UPD-001: Giữ nguyên cấu trúc và định dạng tài liệu hiện có
- UPD-002: Cập nhật trường `last_updated` sang ngày hiện tại
- UPD-003: Duy trì lịch sử phiên bản nếu có
- UPD-004: Thêm mục mới nếu thành phần được mở rộng đáng kể
- UPD-005: Đánh dấu tính năng đã ngừng hỗ trợ hoặc thay đổi phá vỡ tương thích
- UPD-006: Cập nhật ví dụ để phản ánh API hiện tại
- UPD-007: Làm mới danh sách phụ thuộc và phiên bản
- UPD-008: Cập nhật sơ đồ mermaid để phản ánh kiến trúc hiện tại

**Xử lý Lỗi:**

- ERR-001: File tài liệu không tồn tại - hướng dẫn vị trí file
- ERR-002: Không tìm thấy đường dẫn thành phần trong tài liệu - yêu cầu làm rõ
- ERR-003: Mã nguồn đã di chuyển - đề xuất đường dẫn mới
- ERR-004: Thay đổi kiến trúc lớn - nêu rõ thay đổi phá vỡ tương thích
- ERR-005: Không đủ quyền truy cập mã nguồn - ghi nhận giới hạn

**Định dạng Kết quả:**

Cập nhật file Markdown hiện có, giữ nguyên cấu trúc và làm mới nội dung phù hợp với triển khai hiện tại. Bảo toàn định dạng, thứ bậc tiêu đề và cách tổ chức.

**Cấu trúc Tài liệu Yêu cầu:**

Cập nhật tài liệu hiện có theo cùng mẫu, đảm bảo tất cả phần phản ánh triển khai hiện tại:

```md
---
title: [Tên thành phần] - Tài liệu Kỹ thuật
component_path: [Đường dẫn thành phần hiện tại]
version: [Phiên bản mới nếu có]
date_created: [Ngày tạo ban đầu - giữ nguyên]
last_updated: [YYYY-MM-DD - cập nhật ngày hiện tại]
owner: [Giữ nguyên hoặc cập nhật nếu thay đổi]
tags: [Cập nhật thẻ nếu cần]
---

# Tài liệu [Tên thành phần]

[Cập nhật phần giới thiệu để phản ánh mục đích và khả năng hiện tại]

## 1. Tổng quan Thành phần

### Mục đích/Trách nhiệm
- OVR-001: Cập nhật trách nhiệm chính
- OVR-002: Làm mới phạm vi (chức năng bao gồm/loại trừ)
- OVR-003: Cập nhật ngữ cảnh hệ thống và mối quan hệ

## 2. Kiến trúc

- ARC-001: Cập nhật mẫu thiết kế (Repository, Factory, Observer, …)
- ARC-002: Làm mới phụ thuộc nội/ngoại bộ với mục đích hiện tại
- ARC-003: Cập nhật tương tác và mối quan hệ
- ARC-004: Cập nhật sơ đồ UML (class, sequence, component)
- ARC-005: Làm mới sơ đồ mermaid mô tả cấu trúc, mối quan hệ, phụ thuộc

### Sơ đồ Cấu trúc và Phụ thuộc Thành phần

Cập nhật sơ đồ mermaid thể hiện:
- **Cấu trúc thành phần** - Lớp, interface và mối quan hệ
- **Phụ thuộc nội bộ** - Cách thành phần tương tác trong hệ thống
- **Phụ thuộc bên ngoài** - Thư viện, dịch vụ, DB, API
- **Luồng dữ liệu** - Hướng phụ thuộc và tương tác
- **Kế thừa/thành phần** - Hệ thống phân cấp và quan hệ thành phần

```mermaid
[Cập nhật sơ đồ cho phù hợp kiến trúc hiện tại]
```

## 3. Tài liệu Interface

- INT-001: Cập nhật tất cả interface công khai và cách sử dụng hiện tại
- INT-002: Làm mới bảng tham chiếu phương thức/thuộc tính
- INT-003: Cập nhật cơ chế event/callback/thông báo

| Phương thức/Thuộc tính | Mục đích | Tham số | Kiểu trả về | Ghi chú |
|------------------------|----------|---------|-------------|--------|
| [Cập nhật API] | | | | |

## 4. Chi tiết Triển khai

- IMP-001: Cập nhật lớp triển khai chính và trách nhiệm
- IMP-002: Làm mới yêu cầu cấu hình và khởi tạo
- IMP-003: Cập nhật thuật toán và logic chính
- IMP-004: Cập nhật đặc điểm hiệu năng và nút thắt

## 5. Ví dụ Sử dụng

### Sử dụng cơ bản

```csharp
// Cập nhật ví dụ sử dụng cơ bản theo API hiện tại
```

### Sử dụng nâng cao

```csharp
// Cập nhật cấu hình nâng cao theo triển khai hiện tại
```

- USE-001: Cập nhật ví dụ cơ bản
- USE-002: Làm mới cấu hình nâng cao
- USE-003: Cập nhật best practice

## 6. Thuộc tính Chất lượng

- QUA-001: Cập nhật bảo mật (auth, data protection)
- QUA-002: Làm mới hiệu năng (scalability, resource usage)
- QUA-003: Cập nhật độ tin cậy (error handling, recovery)
- QUA-004: Làm mới khả năng bảo trì (standards, testing)
- QUA-005: Cập nhật khả năng mở rộng (extension points)

## 7. Thông tin Tham khảo

- REF-001: Cập nhật phụ thuộc với phiên bản và mục đích
- REF-002: Làm mới tùy chọn cấu hình
- REF-003: Cập nhật hướng dẫn test và mock
- REF-004: Làm mới phần khắc phục sự cố
- REF-005: Cập nhật liên kết tài liệu liên quan
- REF-006: Thêm lịch sử thay đổi và ghi chú di trú
```
