# Tạo Hồ Sơ Quyết Định Kiến Trúc (ADR)

Tạo tài liệu ADR cho `${input:DecisionTitle}` với định dạng cấu trúc tối ưu cho cả AI và con người đọc.

## Đầu Vào

- **Ngữ cảnh**: `${input:Context}`
- **Quyết định**: `${input:Decision}`
- **Phương án thay thế**: `${input:Alternatives}`
- **Các bên liên quan**: `${input:Stakeholders}`

## Xác Thực Đầu Vào
Nếu bất kỳ thông tin bắt buộc nào không có hoặc không thể xác định từ lịch sử hội thoại, hãy yêu cầu người dùng cung cấp trước khi tạo ADR.

## Yêu Cầu

- Sử dụng ngôn ngữ chính xác, rõ ràng
- Tuân theo định dạng ADR tiêu chuẩn với phần đầu (front matter)
- Bao gồm cả hậu quả tích cực và tiêu cực
- Ghi rõ các phương án thay thế cùng lý do từ chối
- Cấu trúc phù hợp cho việc phân tích máy và tham khảo thủ công
- Sử dụng ký hiệu bullet code (3-4 chữ + 3 số) cho các mục nhiều dòng

File ADR phải được lưu trong thư mục `/docs/adr/` với định dạng tên: `adr-NNNN-[title-slug].md`, trong đó NNNN là số thứ tự 4 chữ số tiếp theo (ví dụ: `adr-0001-database-selection.md`).

## Cấu Trúc Tài Liệu Bắt Buộc

File markdown phải tuân thủ mẫu sau:

```md
---
title: "ADR-NNNN: [Tiêu đề quyết định]"
status: "Proposed"
date: "YYYY-MM-DD"
authors: "[Tên/Chức vụ các bên liên quan]"
tags: ["architecture", "decision"]
supersedes: ""
superseded_by: ""
---

# ADR-NNNN: [Tiêu đề quyết định]

## Trạng Thái

**Proposed** | Accepted | Rejected | Superseded | Deprecated

## Ngữ Cảnh

[Mô tả vấn đề, ràng buộc kỹ thuật, yêu cầu kinh doanh, và các yếu tố môi trường dẫn đến quyết định này.]

## Quyết Định

[Giải pháp được chọn cùng lý do lựa chọn.]

## Hậu Quả

### Tích Cực

- **POS-001**: [Kết quả tích cực và lợi ích]
- **POS-002**: [Cải thiện hiệu năng, bảo trì, khả năng mở rộng]
- **POS-003**: [Phù hợp nguyên tắc kiến trúc]

### Tiêu Cực

- **NEG-001**: [Thỏa hiệp, hạn chế, bất lợi]
- **NEG-002**: [Nợ kỹ thuật hoặc độ phức tạp]
- **NEG-003**: [Rủi ro và thách thức tương lai]

## Các Phương Án Xem Xét

### [Tên phương án 1]

- **ALT-001**: **Mô tả**: [Mô tả kỹ thuật ngắn gọn]
- **ALT-002**: **Lý do từ chối**: [Vì sao không chọn]

### [Tên phương án 2]

- **ALT-003**: **Mô tả**: [Mô tả kỹ thuật ngắn gọn]
- **ALT-004**: **Lý do từ chối**: [Vì sao không chọn]

## Ghi Chú Triển Khai

- **IMP-001**: [Lưu ý triển khai]
- **IMP-002**: [Chiến lược chuyển đổi hoặc triển khai]
- **IMP-003**: [Tiêu chí giám sát và thành công]

## Tham Khảo

- **REF-001**: [ADR liên quan]
- **REF-002**: [Tài liệu bên ngoài]
- **REF-003**: [Tiêu chuẩn hoặc khung tham chiếu]
```