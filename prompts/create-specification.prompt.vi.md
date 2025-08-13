# Tạo Tài Liệu Đặc Tả

Mục tiêu của bạn là tạo một file đặc tả mới cho `${input:SpecPurpose}`.

File đặc tả phải xác định các yêu cầu, ràng buộc và giao diện của các thành phần giải pháp một cách rõ ràng, không mơ hồ và có cấu trúc để Generative AI có thể sử dụng hiệu quả. Tuân theo các tiêu chuẩn tài liệu đã được thiết lập và đảm bảo nội dung có thể đọc được bởi máy và tự chứa đầy đủ.

## Thực Hành Tốt Nhất Cho Đặc Tả Sẵn Sàng Cho AI

- Sử dụng ngôn ngữ chính xác, rõ ràng, không mơ hồ
- Phân biệt rõ yêu cầu, ràng buộc và khuyến nghị
- Sử dụng định dạng có cấu trúc (heading, danh sách, bảng) để dễ phân tích
- Tránh sử dụng thành ngữ, ẩn dụ hoặc tham chiếu phụ thuộc ngữ cảnh
- Định nghĩa tất cả từ viết tắt và thuật ngữ chuyên ngành
- Bao gồm ví dụ và trường hợp biên khi áp dụng
- Đảm bảo tài liệu tự chứa, không phụ thuộc vào ngữ cảnh bên ngoài

File đặc tả cần được lưu trong thư mục `/spec/` và đặt tên theo quy tắc: `spec-[a-z0-9-]+.md`, bắt đầu bằng mục đích chính (schema, tool, data, infrastructure, process, architecture, hoặc design) và mô tả nội dung.

File phải được định dạng Markdown chuẩn.

## Mẫu Đặc Tả Bắt Buộc

```md
---
title: [Tiêu đề ngắn gọn mô tả nội dung đặc tả]
version: [Tùy chọn: ví dụ 1.0, Ngày]
date_created: [YYYY-MM-DD]
last_updated: [Tùy chọn]
owner: [Tùy chọn: Nhóm/cá nhân chịu trách nhiệm]
tags: [Tùy chọn: danh sách thẻ, ví dụ: `infrastructure`, `process`, `design`, `app`]
---

# Giới Thiệu

[Mô tả ngắn gọn về mục tiêu của đặc tả.]

## 1. Mục Đích & Phạm Vi

[Mô tả rõ ràng mục tiêu và phạm vi áp dụng của đặc tả. Nêu đối tượng sử dụng và giả định.]

## 2. Định Nghĩa

[Liệt kê và định nghĩa tất cả từ viết tắt, thuật ngữ chuyên ngành.]

## 3. Yêu Cầu, Ràng Buộc & Hướng Dẫn

- **REQ-001**: Yêu cầu 1
- **SEC-001**: Yêu cầu bảo mật 1
- **[3 CHỮ]-001**: Yêu cầu khác
- **CON-001**: Ràng buộc 1
- **GUD-001**: Hướng dẫn 1
- **PAT-001**: Mẫu thiết kế 1

## 4. Giao Diện & Hợp Đồng Dữ Liệu

[Mô tả API, giao diện, hợp đồng dữ liệu. Dùng bảng hoặc code block cho schema và ví dụ.]

## 5. Tiêu Chí Chấp Nhận

- **AC-001**: Given [ngữ cảnh], When [hành động], Then [kết quả mong đợi]
- **AC-002**: Hệ thống sẽ [hành vi] khi [điều kiện]
- **AC-003**: [Tiêu chí khác]

## 6. Chiến Lược Kiểm Thử Tự Động

- **Cấp độ kiểm thử**: Unit, Integration, End-to-End
- **Framework**: MSTest, FluentAssertions, Moq (cho .NET)
- **Quản lý dữ liệu test**: [cách tạo và dọn dữ liệu]
- **Tích hợp CI/CD**: [tích hợp kiểm thử tự động vào pipeline GitHub Actions]
- **Yêu cầu bao phủ code**: [mức tối thiểu]
- **Kiểm thử hiệu năng**: [cách thực hiện]

## 7. Lý Do & Bối Cảnh

[Giải thích lý do cho yêu cầu, ràng buộc và hướng dẫn.]

## 8. Phụ Thuộc & Tích Hợp Bên Ngoài

### Hệ thống bên ngoài
- **EXT-001**: [Tên hệ thống] - [Mục đích và cách tích hợp]

### Dịch vụ bên thứ ba
- **SVC-001**: [Tên dịch vụ] - [Khả năng và SLA yêu cầu]

### Phụ thuộc hạ tầng
- **INF-001**: [Thành phần hạ tầng] - [Yêu cầu và ràng buộc]

### Phụ thuộc dữ liệu
- **DAT-001**: [Nguồn dữ liệu ngoài] - [Định dạng, tần suất, yêu cầu truy cập]

### Phụ thuộc nền tảng
- **PLT-001**: [Yêu cầu nền tảng] - [Phiên bản và lý do]

### Yêu cầu tuân thủ
- **COM-001**: [Yêu cầu pháp lý hoặc tuân thủ] - [Ảnh hưởng đến triển khai]

## 9. Ví Dụ & Trường Hợp Biên

```code
// Ví dụ minh họa bao gồm cả trường hợp biên
```

## 10. Tiêu Chí Xác Thực

[Danh sách các tiêu chí hoặc bài test để xác thực việc tuân thủ đặc tả.]

## 11. Đặc Tả Liên Quan / Tài Liệu Tham Khảo

[Link tới đặc tả liên quan]
[Link tới tài liệu bên ngoài]
```