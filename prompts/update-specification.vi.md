---
chế_độ: 'agent'
mô_tả: 'Cập nhật file đặc tả hiện có của giải pháp, được tối ưu cho Generative AI dựa trên yêu cầu mới hoặc cập nhật của mã nguồn.'
công_cụ: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# Cập nhật Đặc tả

Mục tiêu của bạn là cập nhật file đặc tả `${file}` hiện có dựa trên yêu cầu mới hoặc cập nhật của mã nguồn.

File đặc tả phải xác định yêu cầu, ràng buộc và giao diện cho các thành phần của giải pháp một cách rõ ràng, không mơ hồ, và có cấu trúc để AI Generative dễ sử dụng. Tuân theo các tiêu chuẩn tài liệu đã được thiết lập và đảm bảo nội dung có thể đọc bởi máy và tự chứa.

## Thực hành tốt nhất cho Đặc tả sẵn sàng cho AI

- Sử dụng ngôn ngữ chính xác, rõ ràng và không mơ hồ.
- Phân biệt rõ ràng giữa yêu cầu, ràng buộc và khuyến nghị.
- Sử dụng định dạng có cấu trúc (tiêu đề, danh sách, bảng) để dễ dàng phân tích.
- Tránh dùng thành ngữ, ẩn dụ hoặc tham chiếu phụ thuộc ngữ cảnh.
- Định nghĩa tất cả các từ viết tắt và thuật ngữ chuyên ngành.
- Bao gồm ví dụ và trường hợp biên khi áp dụng.
- Đảm bảo tài liệu tự chứa và không phụ thuộc vào ngữ cảnh bên ngoài.

File đặc tả phải được lưu trong thư mục [/spec/](/spec/) và đặt tên theo quy ước: `[a-z0-9-]+.md`, với phần tên mô tả nội dung và bắt đầu bằng mục đích cấp cao, thuộc một trong các nhóm: [schema, tool, data, infrastructure, process, architecture, design].

File đặc tả phải được định dạng Markdown chuẩn.

Các file đặc tả phải tuân theo mẫu dưới đây, đảm bảo tất cả các phần được điền đầy đủ. Phần front matter phải được cấu trúc chính xác như ví dụ sau:

```md
---
title: [Tiêu đề ngắn gọn mô tả trọng tâm của đặc tả]
version: [Tùy chọn: ví dụ 1.0, Ngày]
date_created: [YYYY-MM-DD]
last_updated: [Tùy chọn: YYYY-MM-DD]
owner: [Tùy chọn: Nhóm/cá nhân chịu trách nhiệm cho đặc tả này]
tags: [Tùy chọn: Danh sách thẻ hoặc danh mục liên quan, ví dụ: `infrastructure`, `process`, `design`, `app`]
---

# Giới thiệu

[Một phần giới thiệu ngắn gọn về đặc tả và mục tiêu của nó.]

## 1. Mục đích & Phạm vi

[Mô tả rõ ràng, ngắn gọn mục đích của đặc tả và phạm vi áp dụng. Xác định đối tượng mục tiêu và giả định.]

## 2. Định nghĩa

[Liệt kê và định nghĩa tất cả từ viết tắt, ký hiệu và thuật ngữ chuyên ngành được sử dụng.]

## 3. Yêu cầu, Ràng buộc & Hướng dẫn

[Liệt kê rõ ràng tất cả yêu cầu, ràng buộc, quy tắc và hướng dẫn. Sử dụng bullet hoặc bảng.]

- **REQ-001**: Yêu cầu 1
- **SEC-001**: Yêu cầu bảo mật 1
- **[3 CHỮ] - 001**: Yêu cầu khác
- **CON-001**: Ràng buộc 1
- **GUD-001**: Hướng dẫn 1
- **PAT-001**: Mẫu cần tuân theo 1

## 4. Giao diện & Hợp đồng Dữ liệu

[Mô tả giao diện, API, hợp đồng dữ liệu hoặc điểm tích hợp. Sử dụng bảng hoặc code block cho schema và ví dụ.]

## 5. Tiêu chí Chấp nhận

[Định nghĩa rõ ràng, có thể kiểm thử tiêu chí chấp nhận cho mỗi yêu cầu, sử dụng định dạng Given-When-Then khi phù hợp.]

- **AC-001**: Given [ngữ cảnh], When [hành động], Then [kết quả mong đợi]
- **AC-002**: Hệ thống sẽ [hành vi cụ thể] khi [điều kiện]
- **AC-003**: [Tiêu chí khác]

## 6. Chiến lược Kiểm thử Tự động

[Xác định cách tiếp cận kiểm thử, framework và yêu cầu tự động hóa.]

- **Cấp độ Kiểm thử**: Unit, Integration, End-to-End
- **Framework**: MSTest, FluentAssertions, Moq (cho .NET)
- **Quản lý Dữ liệu Test**: [cách tạo và dọn dữ liệu test]
- **Tích hợp CI/CD**: [kiểm thử tự động trong GitHub Actions]
- **Yêu cầu Bao phủ Code**: [ngưỡng tối thiểu]
- **Kiểm thử Hiệu năng**: [cách tiếp cận load/performance testing]

## 7. Cơ sở & Ngữ cảnh

[Giải thích lý do của các yêu cầu, ràng buộc và hướng dẫn. Cung cấp ngữ cảnh cho quyết định thiết kế.]

## 8. Phụ thuộc & Tích hợp Bên ngoài

[Xác định hệ thống bên ngoài, dịch vụ và phụ thuộc kiến trúc cần thiết cho đặc tả này. Tập trung vào **cái gì** cần hơn là **cách** thực hiện.]

### Hệ thống Bên ngoài
- **EXT-001**: [Tên hệ thống] - [Mục đích và kiểu tích hợp]

### Dịch vụ Bên thứ Ba
- **SVC-001**: [Tên dịch vụ] - [Khả năng yêu cầu và SLA]

### Phụ thuộc Hạ tầng
- **INF-001**: [Thành phần hạ tầng] - [Yêu cầu và ràng buộc]

### Phụ thuộc Dữ liệu
- **DAT-001**: [Nguồn dữ liệu bên ngoài] - [Định dạng, tần suất, yêu cầu truy cập]

### Phụ thuộc Nền tảng Công nghệ
- **PLT-001**: [Yêu cầu nền tảng/chạy] - [Ràng buộc phiên bản và lý do]

### Phụ thuộc Tuân thủ
- **COM-001**: [Yêu cầu tuân thủ] - [Tác động đến triển khai]

**Lưu ý**: Phần này tập trung vào phụ thuộc kiến trúc và nghiệp vụ, không chỉ định phiên bản gói cụ thể.

## 9. Ví dụ & Trường hợp Biên

```code
// Code hoặc dữ liệu minh họa áp dụng đúng hướng dẫn, bao gồm trường hợp biên
```

## 10. Tiêu chí Xác thực

[Liệt kê tiêu chí hoặc kiểm thử cần đạt để tuân thủ đặc tả này.]

## 11. Đặc tả Liên quan / Tài liệu Tham khảo

[Liên kết đến đặc tả liên quan]
[Liên kết tài liệu ngoài]
```
