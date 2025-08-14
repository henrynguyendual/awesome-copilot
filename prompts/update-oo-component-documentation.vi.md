---
mode: "agent"
description: "Cập nhật tài liệu thành phần hướng đối tượng hiện có theo các tiêu chuẩn thực hành tốt nhất của ngành và tiêu chuẩn tài liệu kiến trúc."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Cập nhật Tài liệu Thành phần Hướng đối tượng Tiêu chuẩn

Cập nhật tệp tài liệu hiện có tại: `${file}` bằng cách phân tích mã thành phần tương ứng.

Trích xuất đường dẫn thành phần từ phần front matter của tài liệu hiện có (trường `component_path`) hoặc suy ra từ nội dung tài liệu. Phân tích việc triển khai thành phần hiện tại và cập nhật tài liệu cho phù hợp.

**Tiêu chuẩn Tài liệu:**

- DOC-001: Tuân theo các cấp độ tài liệu của Mô hình C4 (Bối cảnh, Vùng chứa, Thành phần, Mã nguồn)
- DOC-002: Căn chỉnh theo mẫu tài liệu kiến trúc phần mềm Arc42
- DOC-003: Tuân thủ tiêu chuẩn Mô tả Thiết kế Phần mềm IEEE 1016
- DOC-004: Sử dụng các nguyên tắc Tài liệu Agile (chỉ đủ tài liệu mang lại giá trị)
- DOC-005: Hướng đến đối tượng chính là các nhà phát triển và người bảo trì

**Hướng dẫn Phân tích:**

- ANA-001: Đọc tài liệu hiện có để hiểu bối cảnh và cấu trúc của thành phần
- ANA-002: Xác định đường dẫn thành phần từ front matter hoặc phân tích nội dung
- ANA-003: Kiểm tra các tệp mã nguồn hiện tại để biết cấu trúc lớp và kế thừa
- ANA-004: So sánh tài liệu hiện có với việc triển khai hiện tại
- ANA-005: Xác định các mẫu thiết kế và thay đổi kiến trúc
- ANA-006: Cập nhật các API công khai, giao diện và các phụ thuộc
- ANA-007: Nhận diện các mẫu tạo/cấu trúc/hành vi mới/thay đổi
- ANA-008: Cập nhật tham số phương thức, giá trị trả về, các ngoại lệ
- ANA-009: Đánh giá lại hiệu suất, bảo mật, độ tin cậy, khả năng bảo trì
- ANA-010: Cập nhật các mẫu tích hợp và luồng dữ liệu

**Tối ưu hóa theo Ngôn ngữ Cụ thể:**

- LNG-001: **C#/.NET** - async/await, dependency injection, cấu hình, giải phóng tài nguyên (disposal)
- LNG-002: **Java** - Spring framework, annotations, xử lý ngoại lệ, đóng gói
- LNG-003: **TypeScript/JavaScript** - modules, các mẫu async, types, npm
- LNG-004: **Python** - packages, môi trường ảo, gợi ý kiểu (type hints), kiểm thử

**Chiến lược Cập nhật:**

- UPD-001: Giữ nguyên cấu trúc và định dạng tài liệu hiện có
- UPD-002: Cập nhật trường `last_updated` thành ngày hiện tại
- UPD-003: Duy trì lịch sử phiên bản trong front matter nếu có
- UPD-004: Thêm các phần mới nếu thành phần đã mở rộng đáng kể
- UPD-005: Đánh dấu các tính năng không còn được dùng hoặc các thay đổi đột phá
- UPD-006: Cập nhật các ví dụ để phản ánh API hiện tại
- UPD-007: Làm mới danh sách phụ thuộc và phiên bản
- UPD-008: Cập nhật các sơ đồ mermaid để phản ánh kiến trúc hiện tại

**Xử lý Lỗi:**

- ERR-001: Tệp tài liệu không tồn tại - cung cấp hướng dẫn về vị trí tệp
- ERR-002: Không tìm thấy đường dẫn thành phần trong tài liệu - yêu cầu làm rõ
- ERR-003: Mã nguồn đã được di chuyển - đề xuất các đường dẫn được cập nhật
- ERR-004: Thay đổi kiến trúc lớn - nêu bật các thay đổi đột phá
- ERR-005: Không đủ quyền truy cập vào mã nguồn - ghi lại các hạn chế

**Định dạng Đầu ra:**

Cập nhật tệp Markdown hiện có, duy trì cấu trúc của nó trong khi làm mới nội dung để khớp với việc triển khai hiện tại. Giữ nguyên định dạng, hệ thống tiêu đề và các quyết định tổ chức hiện có.

**Cấu trúc Tài liệu Bắt buộc:**

Cập nhật tài liệu hiện có theo cùng một cấu trúc mẫu, đảm bảo tất cả các phần phản ánh việc triển khai hiện tại:

````md
---
title: [Tên Thành phần] - Tài liệu Kỹ thuật
component_path: [Đường dẫn thành phần hiện tại]
version: [Phiên bản được cập nhật nếu có]
date_created: [Ngày tạo ban đầu - giữ nguyên]
last_updated: [YYYY-MM-DD - cập nhật thành ngày hiện tại]
owner: [Giữ nguyên người sở hữu hiện tại hoặc cập nhật nếu thay đổi]
tags: [Cập nhật các thẻ nếu cần dựa trên chức năng hiện tại]
---

# Tài liệu [Tên Thành phần]

[Cập nhật phần giới thiệu để phản ánh mục đích và khả năng của thành phần hiện tại]

## 1. Tổng quan về Thành phần

### Mục đích/Trách nhiệm

- OVR-001: Cập nhật trách nhiệm chính của thành phần
- OVR-002: Làm mới phạm vi (chức năng bao gồm/không bao gồm)
- OVR-003: Cập nhật bối cảnh hệ thống và các mối quan hệ

## 2. Phần Kiến trúc

- ARC-001: Cập nhật các mẫu thiết kế được sử dụng (Repository, Factory, Observer, v.v.)
- ARC-002: Làm mới các phụ thuộc nội bộ và bên ngoài với mục đích hiện tại
- ARC-003: Cập nhật các tương tác và mối quan hệ của thành phần
- ARC-004: Cập nhật các sơ đồ trực quan (lớp UML, tuần tự, thành phần)
- ARC-005: Làm mới sơ đồ mermaid hiển thị cấu trúc, mối quan hệ và các phụ thuộc của thành phần hiện tại

### Sơ đồ Cấu trúc và Phụ thuộc của Thành phần

Cập nhật sơ đồ mermaid để hiển thị hiện tại:

- **Cấu trúc thành phần** - Các lớp, giao diện hiện tại và mối quan hệ của chúng
- **Phụ thuộc nội bộ** - Cách các thành phần hiện tương tác trong hệ thống
- **Phụ thuộc bên ngoài** - Các thư viện, dịch vụ, cơ sở dữ liệu, API bên ngoài hiện tại
- **Luồng dữ liệu** - Hướng hiện tại của các phụ thuộc và tương tác
- **Kế thừa/Hợp thành** - Hệ thống phân cấp lớp và mối quan hệ hợp thành hiện tại

```mermaid
[Cập nhật sơ đồ để phản ánh kiến trúc hiện tại]
```

## 3. Tài liệu Giao diện

- INT-001: Cập nhật tất cả các giao diện công khai và các mẫu sử dụng hiện tại
- INT-002: Làm mới bảng tham chiếu phương thức/thuộc tính với API hiện tại
- INT-003: Cập nhật các cơ chế sự kiện/gọi lại/thông báo

| Phương thức/Thuộc tính           | Mục đích | Tham số | Kiểu trả về | Ghi chú sử dụng |
| -------------------------------- | -------- | ------- | ----------- | --------------- |
| [Cập nhật bảng với API hiện tại] |          |         |             |                 |

## 4. Chi tiết Triển khai

- IMP-001: Cập nhật các lớp triển khai chính và trách nhiệm hiện tại
- IMP-002: Làm mới các yêu cầu cấu hình và các mẫu khởi tạo
- IMP-003: Cập nhật các thuật toán chính và logic nghiệp vụ
- IMP-004: Cập nhật các đặc tính hiệu suất và các điểm nghẽn

## 5. Ví dụ Sử dụng

### Sử dụng Cơ bản

```csharp
// Cập nhật ví dụ sử dụng cơ bản theo API hiện tại
```

### Sử dụng Nâng cao

```csharp
// Cập nhật các mẫu cấu hình nâng cao theo triển khai hiện tại
```

- USE-001: Cập nhật các ví dụ sử dụng cơ bản
- USE-002: Làm mới các mẫu cấu hình nâng cao
- USE-003: Cập nhật các phương pháp hay nhất và các mẫu được đề xuất

## 6. Thuộc tính Chất lượng

- QUA-001: Cập nhật bảo mật (xác thực, ủy quyền, bảo vệ dữ liệu)
- QUA-002: Làm mới hiệu suất (đặc tính, khả năng mở rộng, sử dụng tài nguyên)
- QUA-003: Cập nhật độ tin cậy (xử lý lỗi, khả năng chịu lỗi, phục hồi)
- QUA-004: Làm mới khả năng bảo trì (tiêu chuẩn, kiểm thử, tài liệu)
- QUA-005: Cập nhật khả năng mở rộng (các điểm mở rộng, tùy chọn tùy chỉnh)

## 7. Thông tin Tham khảo

- REF-001: Cập nhật các phụ thuộc với phiên bản và mục đích hiện tại
- REF-002: Làm mới tham chiếu các tùy chọn cấu hình
- REF-003: Cập nhật hướng dẫn kiểm thử và thiết lập mock
- REF-004: Làm mới phần khắc phục sự cố (các vấn đề thường gặp, thông báo lỗi)
- REF-005: Cập nhật các liên kết tài liệu liên quan
- REF-006: Thêm lịch sử thay đổi và ghi chú di chuyển cho bản cập nhật này
````
