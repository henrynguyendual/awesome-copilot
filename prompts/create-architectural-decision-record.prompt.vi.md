---
mode: "agent"
description: "Tạo tài liệu Ghi chép Quyết định Kiến trúc (ADR) cho việc ghi lại quyết định được tối ưu hóa cho AI."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Tạo Ghi chép Quyết định Kiến trúc

Tạo một tài liệu ADR cho `${input:DecisionTitle}` sử dụng định dạng có cấu trúc được tối ưu hóa cho cả AI và con người đọc hiểu.

## Đầu vào

- **Bối cảnh**: `${input:Context}`
- **Quyết định**: `${input:Decision}`
- **Các phương án thay thế**: `${input:Alternatives}`
- **Các bên liên quan**: `${input:Stakeholders}`

## Xác thực Đầu vào

Nếu bất kỳ thông tin đầu vào bắt buộc nào không được cung cấp hoặc không thể xác định từ lịch sử cuộc trò chuyện, hãy yêu cầu người dùng cung cấp thông tin còn thiếu trước khi tiến hành tạo ADR.

## Yêu cầu

- Sử dụng ngôn ngữ chính xác, không mơ hồ
- Tuân theo định dạng ADR chuẩn hóa với phần front matter
- Bao gồm cả hệ quả tích cực và tiêu cực
- Ghi lại các phương án thay thế cùng với lý do từ chối
- Cấu trúc để máy có thể phân tích và con người có thể tham khảo
- Sử dụng các gạch đầu dòng được mã hóa (mã 3-4 chữ cái + số có 3 chữ số) cho các mục có nhiều hạng mục

ADR phải được lưu trong thư mục `/docs/adr/` theo quy ước đặt tên: `adr-NNNN-[tieu-de-slug].md`, trong đó NNNN là số thứ tự 4 chữ số tiếp theo (ví dụ: `adr-0001-lua-chon-co-so-du-lieu.md`).

## Cấu trúc Tài liệu Bắt buộc

Tệp tài liệu phải tuân theo mẫu dưới đây, đảm bảo tất cả các phần được điền đầy đủ. Phần front matter cho markdown phải được cấu trúc chính xác theo ví dụ sau:

```md
---
title: "ADR-NNNN: [Tiêu đề Quyết định]"
status: "Đề xuất"
date: "YYYY-MM-DD"
authors: "[Tên/Vai trò các bên liên quan]"
tags: ["kiến trúc", "quyết định"]
supersedes: ""
superseded_by: ""
---

# ADR-NNNN: [Tiêu đề Quyết định]

## Trạng thái

**Đề xuất** | Chấp nhận | Từ chối | Thay thế | Không dùng nữa

## Bối cảnh

[Tuyên bố vấn đề, các ràng buộc kỹ thuật, yêu cầu kinh doanh và các yếu tố môi trường đòi hỏi quyết định này.]

## Quyết định

[Giải pháp được chọn cùng với lý do lựa chọn rõ ràng.]

## Hệ quả

### Tích cực

- **POS-001**: [Các kết quả có lợi và ưu điểm]
- **POS-002**: [Cải thiện về hiệu suất, khả năng bảo trì, khả năng mở rộng]
- **POS-003**: [Sự phù hợp với các nguyên tắc kiến trúc]

### Tiêu cực

- **NEG-001**: [Các đánh đổi, hạn chế, nhược điểm]
- **NEG-002**: [Nợ kỹ thuật hoặc sự phức tạp được thêm vào]
- **NEG-003**: [Rủi ro và thách thức trong tương lai]

## Các phương án thay thế đã xem xét

### [Tên phương án thay thế 1]

- **ALT-001**: **Mô tả**: [Mô tả kỹ thuật ngắn gọn]
- **ALT-002**: **Lý do từ chối**: [Tại sao phương án này không được chọn]

### [Tên phương án thay thế 2]

- **ALT-003**: **Mô tả**: [Mô tả kỹ thuật ngắn gọn]
- **ALT-004**: **Lý do từ chối**: [Tại sao phương án này không được chọn]

## Ghi chú triển khai

- **IMP-001**: [Các cân nhắc chính khi triển khai]
- **IMP-002**: [Chiến lược di chuyển hoặc triển khai nếu có]
- **IMP-003**: [Tiêu chí giám sát và thành công]

## Tài liệu tham khảo

- **REF-001**: [Các ADR liên quan]
- **REF-002**: [Tài liệu bên ngoài]
- **REF-003**: [Các tiêu chuẩn hoặc
```
