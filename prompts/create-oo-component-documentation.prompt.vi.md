---
mode: "agent"
description: "Tạo tài liệu toàn diện, được tiêu chuẩn hóa cho các thành phần hướng đối tượng theo các phương pháp hay nhất trong ngành và các tiêu chuẩn tài liệu kiến trúc."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Tạo Tài liệu Chuẩn cho Thành phần Hướng đối tượng

Tạo tài liệu toàn diện cho (các) thành phần hướng đối tượng tại: `${input:ComponentPath}`.

Phân tích thành phần bằng cách kiểm tra mã nguồn trong đường dẫn được cung cấp. Nếu là thư mục, hãy phân tích tất cả các tệp nguồn. Nếu là một tệp đơn, hãy coi đó là thành phần chính và phân tích các tệp liên quan trong cùng thư mục.

## Tiêu chuẩn Tài liệu

- DOC-001: Tuân thủ các cấp độ tài liệu của Mô hình C4 (Bối cảnh, Vùng chứa, Thành phần, Mã nguồn)
- DOC-002: Căn chỉnh theo mẫu tài liệu kiến trúc phần mềm Arc42
- DOC-003: Tuân thủ tiêu chuẩn Mô tả Thiết kế Phần mềm IEEE 1016
- DOC-004: Sử dụng các nguyên tắc Tài liệu Agile (chỉ đủ tài liệu mang lại giá trị)
- DOC-005: Hướng đến đối tượng chính là các nhà phát triển và người bảo trì

## Hướng dẫn Phân tích

- ANA-001: Xác định loại đường dẫn (thư mục hay tệp đơn) và xác định thành phần chính
- ANA-002: Kiểm tra các tệp mã nguồn để tìm cấu trúc lớp và kế thừa
- ANA-003: Xác định các mẫu thiết kế và quyết định kiến trúc
- ANA-004: Ghi lại tài liệu về các API công khai, giao diện và các phụ thuộc
- ANA-005: Nhận diện các mẫu khởi tạo/cấu trúc/hành vi
- ANA-006: Ghi lại tài liệu về các tham số phương thức, giá trị trả về, các ngoại lệ
- ANA-007: Đánh giá hiệu suất, bảo mật, độ tin cậy, khả năng bảo trì
- ANA-008: Suy luận các mẫu tích hợp và luồng dữ liệu

## Tối ưu hóa theo Ngôn ngữ Cụ thể

- LNG-001: **C#/.NET** - async/await, dependency injection, cấu hình, giải phóng tài nguyên (disposal)
- LNG-002: **Java** - Spring framework, annotations, xử lý ngoại lệ, đóng gói
- LNG-003: **TypeScript/JavaScript** - modules, các mẫu async, types, npm
- LNG-004: **Python** - packages, môi trường ảo, gợi ý kiểu, kiểm thử

## Xử lý Lỗi

- ERR-001: Đường dẫn không tồn tại - cung cấp hướng dẫn định dạng đúng
- ERR-002: Không tìm thấy tệp nguồn - đề xuất các vị trí thay thế
- ERR-003: Cấu trúc không rõ ràng - ghi lại các phát hiện và yêu cầu làm rõ
- ERR-004: Các mẫu không chuẩn - ghi lại các phương pháp tiếp cận tùy chỉnh
- ERR-005: Không đủ mã nguồn - tập trung vào thông tin có sẵn, chỉ ra các lỗ hổng

## Định dạng Đầu ra

Tạo tệp Markdown có cấu trúc tốt với hệ thống tiêu đề rõ ràng, các khối mã, bảng, danh sách gạch đầu dòng và định dạng phù hợp để dễ đọc và bảo trì.

## Vị trí Tệp

Tài liệu nên được lưu trong thư mục `/docs/components/` và được đặt tên theo quy ước: `[ten-thanh-phan]-documentation.md`.

## Cấu trúc Tài liệu Bắt buộc

Tệp tài liệu phải tuân theo mẫu dưới đây, đảm bảo tất cả các phần được điền đầy đủ. Phần front matter cho markdown phải được cấu trúc chính xác theo ví dụ sau:

````md
---
title: [Tên Thành phần] - Tài liệu Kỹ thuật
component_path: `${input:ComponentPath}`
version: [Tùy chọn: ví dụ: 1.0, Ngày]
date_created: [YYYY-MM-DD]
last_updated: [Tùy chọn: YYYY-MM-DD]
owner: [Tùy chọn: Nhóm/Cá nhân chịu trách nhiệm về thành phần này]
tags: [Tùy chọn: Danh sách các thẻ hoặc danh mục liên quan, ví dụ: `component`,`service`,`tool`,`infrastructure`,`documentation`,`architecture` v.v.]
---

# Tài liệu [Tên Thành phần]

[Một đoạn giới thiệu ngắn gọn, súc tích về thành phần và mục đích của nó trong hệ thống.]

## 1. Tổng quan về Thành phần

### Mục đích/Trách nhiệm

- OVR-001: Nêu rõ trách nhiệm chính của thành phần
- OVR-002: Xác định phạm vi (chức năng bao gồm/không bao gồm)
- OVR-003: Mô tả bối cảnh hệ thống và các mối quan hệ

## 2. Phần Kiến trúc

- ARC-001: Ghi lại các mẫu thiết kế đã sử dụng (Repository, Factory, Observer, v.v.)
- ARC-002: Liệt kê các phụ thuộc nội bộ và bên ngoài cùng với mục đích của chúng
- ARC-003: Ghi lại các tương tác và mối quan hệ của thành phần
- ARC-004: Bao gồm các sơ đồ trực quan (lớp UML, tuần tự, thành phần)
- ARC-005: Tạo sơ đồ mermaid hiển thị cấu trúc, mối quan hệ và các phụ thuộc của thành phần

### Sơ đồ Cấu trúc và Phụ thuộc của Thành phần

Bao gồm một sơ đồ mermaid toàn diện cho thấy:

- **Cấu trúc thành phần** - Các lớp chính, giao diện và mối quan hệ của chúng
- **Phụ thuộc nội bộ** - Cách các thành phần tương tác trong hệ thống
- **Phụ thuộc bên ngoài** - Các thư viện, dịch vụ, cơ sở dữ liệu, API bên ngoài
- **Luồng dữ liệu** - Hướng của các phụ thuộc và tương tác
- **Kế thừa/Hợp thành** - Hệ thống phân cấp lớp và các mối quan hệ hợp thành

```mermaid
graph TD
    subgraph "Hệ thống Thành phần"
        A[Thành phần Chính] --> B[Dịch vụ Nội bộ]
        A --> C[Repository Nội bộ]
        B --> D[Logic Nghiệp vụ]
        C --> E[Lớp Truy cập Dữ liệu]
    end

    subgraph "Phụ thuộc Bên ngoài"
        F[API Bên ngoài]
        G[Cơ sở dữ liệu]
        H[Thư viện của bên thứ ba]
        I[Dịch vụ Cấu hình]
    end

    A --> F
    E --> G
    B --> H
    A --> I

    classDiagram
        class MainComponent {
            +property: Type
            +method(): ReturnType
            +asyncMethod(): Promise~Type~
        }
        class InternalService {
            +businessOperation(): Result
        }
        class ExternalAPI {
            <<external>>
            +apiCall(): Data
        }

        MainComponent --> InternalService
        MainComponent --> ExternalAPI
```

## 3. Tài liệu Giao diện

- INT-001: Ghi lại tất cả các giao diện công khai và các mẫu sử dụng
- INT-002: Tạo bảng tham chiếu phương thức/thuộc tính
- INT-003: Ghi lại các cơ chế sự kiện/gọi lại/thông báo

| Phương thức/Thuộc tính | Mục đích   | Tham số   | Kiểu trả về | Ghi chú sử dụng |
| ---------------------- | ---------- | --------- | ----------- | --------------- |
| [Tên]                  | [Mục đích] | [Tham số] | [Kiểu]      | [Ghi chú]       |

## 4. Chi tiết Triển khai

- IMP-001: Ghi lại các lớp triển khai chính và trách nhiệm của chúng
- IMP-002: Mô tả các yêu cầu cấu hình và khởi tạo
- IMP-003: Ghi lại các thuật toán chính và logic nghiệp vụ
- IMP-004: Ghi chú các đặc điểm hiệu suất và các điểm nghẽn

## 5. Ví dụ Sử dụng

### Sử dụng Cơ bản

```csharp
// Ví dụ sử dụng cơ bản
var component = new ComponentName();
component.DoSomething();
```

### Sử dụng Nâng cao

```csharp
// Các mẫu cấu hình nâng cao
var options = new ComponentOptions();
var component = ComponentFactory.Create(options);
await component.ProcessAsync(data);
```

- USE-001: Cung cấp các ví dụ sử dụng cơ bản
- USE-002: Hiển thị các mẫu cấu hình nâng cao
- USE-003: Ghi lại các phương pháp hay nhất và các mẫu được đề xuất

## 6. Thuộc tính Chất lượng

- QUA-001: Bảo mật (xác thực, ủy quyền, bảo vệ dữ liệu)
- QUA-002: Hiệu suất (đặc điểm, khả năng mở rộng, sử dụng tài nguyên)
- QUA-003: Độ tin cậy (xử lý lỗi, khả năng chịu lỗi, phục hồi)
- QUA-004: Khả năng bảo trì (tiêu chuẩn, kiểm thử, tài liệu)
- QUA-005: Khả năng mở rộng (các điểm mở rộng, tùy chọn tùy chỉnh)

## 7. Thông tin Tham khảo

- REF-001: Liệt kê các phụ thuộc với phiên bản và mục đích
- REF-002: Tham chiếu đầy đủ các tùy chọn cấu hình
- REF-003: Hướng dẫn kiểm thử và thiết lập mock
- REF-004: Khắc phục sự cố (các vấn đề thường gặp, thông báo lỗi)
- REF-005: Các liên kết tài liệu liên quan
- REF-006: Lịch sử thay đổi và ghi chú di
````
