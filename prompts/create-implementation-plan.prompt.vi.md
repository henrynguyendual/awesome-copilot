# Tạo Kế Hoạch Triển Khai

## Chỉ Thị Chính

Mục tiêu là tạo file kế hoạch triển khai mới cho `${input:PlanPurpose}`. Đầu ra phải có thể đọc bởi máy, xác định được, và có cấu trúc để thực hiện tự động bởi hệ thống AI hoặc con người.

## Ngữ Cảnh Thực Thi

Prompt này được thiết kế cho giao tiếp AI-to-AI và xử lý tự động. Tất cả hướng dẫn phải được diễn giải đúng nguyên văn và thực hiện hệ thống, không cần diễn giải hay làm rõ từ con người.

## Yêu Cầu Cốt Lõi

- Sinh kế hoạch triển khai có thể thực thi hoàn toàn bởi AI hoặc con người
- Ngôn ngữ xác định, không mơ hồ
- Cấu trúc nội dung để phân tích và thực thi tự động
- Tự chứa đầy đủ ngữ cảnh, không phụ thuộc bên ngoài

## Yêu Cầu Cấu Trúc Kế Hoạch

Kế hoạch phải gồm các giai đoạn riêng biệt, độc lập, có nhiệm vụ cụ thể. Mỗi giai đoạn phải có thể xử lý độc lập trừ khi nêu rõ phụ thuộc.

## Kiến Trúc Giai Đoạn

- Mỗi giai đoạn phải có tiêu chí hoàn thành đo được
- Nhiệm vụ có thể chạy song song trừ khi có phụ thuộc
- Mô tả nhiệm vụ phải chỉ rõ file, hàm, chi tiết triển khai
- Không yêu cầu diễn giải hoặc quyết định của con người

## Tiêu Chuẩn Triển Khai Tối Ưu Cho AI

- Ngôn ngữ rõ ràng, không mơ hồ
- Cấu trúc dạng bảng, danh sách, dữ liệu có định dạng
- Chỉ rõ file, dòng code, hằng số, biến cấu hình
- Đặt tên có tiền tố chuẩn (REQ-, TASK-, ...)
- Tiêu chí xác thực có thể kiểm tra tự động

## Quy Tắc Lưu File

- Lưu trong thư mục `/plan/`
- Đặt tên: `[mục đích]-[thành phần]-[phiên bản].md`
- Tiền tố mục đích: `upgrade|refactor|feature|data|infrastructure|process|architecture|design`

## Cấu Trúc Mẫu Bắt Buộc

File phải theo mẫu chuẩn đã cho, bao gồm đầy đủ các mục từ phần đầu (front matter) đến phần liên kết tài liệu.

## Quy Tắc Trạng Thái

Trạng thái phải rõ ràng: `Completed`, `In progress`, `Planned`, `Deprecated`, hoặc `On Hold` và được hiển thị bằng badge.

```md
---
goal: [Tiêu đề ngắn gọn mô tả mục tiêu kế hoạch]
version: [Tùy chọn: ví dụ 1.0, ngày]
date_created: [YYYY-MM-DD]
last_updated: [Tùy chọn]
owner: [Tùy chọn]
status: 'Completed'|'In progress'|'Planned'|'Deprecated'|'On Hold'
tags: [Tùy chọn: danh sách thẻ]
---

# Giới Thiệu

![Status: <status>](https://img.shields.io/badge/status-<status>-<status_color>)

[Mô tả ngắn gọn mục tiêu kế hoạch.]

## 1. Yêu Cầu & Ràng Buộc

- **REQ-001**: ...
- **SEC-001**: ...
- **CON-001**: ...

## 2. Các Bước Triển Khai

### Giai Đoạn 1

- GOAL-001: ...

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | ... | ✅ | ... |

### Giai Đoạn 2

...

## 3. Các Phương Án

- **ALT-001**: ...
- **ALT-002**: ...

## 4. Phụ Thuộc

- **DEP-001**: ...

## 5. File

- **FILE-001**: ...

## 6. Kiểm Thử

- **TEST-001**: ...

## 7. Rủi Ro & Giả Định

- **RISK-001**: ...
- **ASSUMPTION-001**: ...

## 8. Tài Liệu Liên Quan

[Link ...]
```