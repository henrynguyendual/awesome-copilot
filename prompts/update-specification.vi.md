---
mode: "agent"
description: "Cập nhật một tệp đặc tả hiện có cho giải pháp, được tối ưu hóa cho việc sử dụng bởi AI Tạo sinh dựa trên các yêu cầu mới hoặc cập nhật cho bất kỳ mã nguồn hiện có nào."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Cập nhật Đặc tả

Mục tiêu của bạn là cập nhật tệp đặc tả hiện có `${file}` dựa trên các yêu cầu mới hoặc cập nhật cho bất kỳ mã nguồn hiện có nào.

Tệp đặc tả phải xác định các yêu cầu, ràng buộc và giao diện cho các thành phần của giải pháp một cách rõ ràng, không mơ hồ và có cấu trúc để các AI Tạo sinh sử dụng hiệu quả. Tuân thủ các tiêu chuẩn tài liệu đã được thiết lập và đảm bảo nội dung có thể đọc được bằng máy và khép kín.

## Các Thực hành Tốt nhất cho Đặc tả Sẵn sàng cho AI

- Sử dụng ngôn ngữ chính xác, rõ ràng và không mơ hồ.
- Phân biệt rõ ràng giữa các yêu cầu, ràng buộc và khuyến nghị.
- Sử dụng định dạng có cấu trúc (tiêu đề, danh sách, bảng) để dễ dàng phân tích cú pháp.
- Tránh các thành ngữ, ẩn dụ hoặc các tham chiếu phụ thuộc vào ngữ cảnh.
- Định nghĩa tất cả các từ viết tắt và thuật ngữ chuyên ngành.
- Bao gồm các ví dụ và trường hợp biên khi có thể.
- Đảm bảo tài liệu là khép kín và không phụ thuộc vào ngữ cảnh bên ngoài.

Đặc tả nên được lưu trong thư mục [/spec/](/spec/) và được đặt tên theo quy ước sau: `[a-z0-9-]+.md`, trong đó tên phải mô tả nội dung của đặc tả và bắt đầu bằng mục đích cấp cao, là một trong các loại sau [lược đồ, công cụ, dữ liệu, cơ sở hạ tầng, quy trình, kiến trúc, hoặc thiết kế].

Tệp đặc tả phải được định dạng bằng Markdown hợp lệ.

Các tệp đặc tả phải tuân theo mẫu dưới đây, đảm bảo rằng tất cả các phần được điền đầy đủ. Phần front matter cho markdown phải được cấu trúc chính xác theo ví dụ sau:

````md
---
title: [Tiêu đề ngắn gọn mô tả trọng tâm của đặc tả]
version: [Tùy chọn: ví dụ: 1.0, Ngày]
date_created: [YYYY-MM-DD]
last_updated: [Tùy chọn: YYYY-MM-DD]
owner: [Tùy chọn: Nhóm/Cá nhân chịu trách nhiệm về đặc tả này]
tags: [Tùy chọn: Danh sách các thẻ hoặc danh mục liên quan, ví dụ: `cơ sở hạ tầng`, `quy trình`, `thiết kế`, `ứng dụng`, v.v.]
---

# Giới thiệu

[Một đoạn giới thiệu ngắn gọn về đặc tả và mục tiêu mà nó dự định đạt được.]

## 1. Mục đích & Phạm vi

[Cung cấp một mô tả rõ ràng, ngắn gọn về mục đích của đặc tả và phạm vi áp dụng của nó. Nêu rõ đối tượng dự kiến và bất kỳ giả định nào.]

## 2. Định nghĩa

[Liệt kê và định nghĩa tất cả các từ viết tắt, chữ viết tắt và thuật ngữ chuyên ngành được sử dụng trong đặc tả này.]

## 3. Yêu cầu, Ràng buộc & Hướng dẫn

[Liệt kê rõ ràng tất cả các yêu cầu, ràng buộc, quy tắc và hướng dẫn. Sử dụng dấu đầu dòng hoặc bảng để rõ ràng.]

- **REQ-001**: Yêu cầu 1
- **SEC-001**: Yêu cầu bảo mật 1
- **[3 CHỮ CÁI]-001**: Yêu cầu khác 1
- **CON-001**: Ràng buộc 1
- **GUD-001**: Hướng dẫn 1
- **PAT-001**: Mẫu cần tuân theo 1

## 4. Giao diện & Hợp đồng Dữ liệu

[Mô tả các giao diện, API, hợp đồng dữ liệu hoặc các điểm tích hợp. Sử dụng bảng hoặc khối mã cho các lược đồ và ví dụ.]

## 5. Tiêu chí Chấp nhận

[Xác định các tiêu chí chấp nhận rõ ràng, có thể kiểm thử cho mỗi yêu cầu, sử dụng định dạng Given-When-Then khi thích hợp.]

- **AC-001**: Cho [ngữ cảnh], Khi [hành động], Thì [kết quả mong đợi]
- **AC-002**: Hệ thống sẽ [hành vi cụ thể] khi [điều kiện]
- **AC-003**: [Các tiêu chí chấp nhận bổ sung khi cần]

## 6. Chiến lược Tự động hóa Kiểm thử

[Xác định phương pháp kiểm thử, các framework và yêu cầu tự động hóa.]

- **Các cấp độ kiểm thử**: Đơn vị, Tích hợp, Đầu cuối (End-to-End)
- **Frameworks**: MSTest, FluentAssertions, Moq (cho các ứng dụng .NET)
- **Quản lý Dữ liệu Kiểm thử**: [phương pháp tạo và dọn dẹp dữ liệu kiểm thử]
- **Tích hợp CI/CD**: [kiểm thử tự động trong các pipeline của GitHub Actions]
- **Yêu cầu về Độ bao phủ**: [ngưỡng độ bao phủ mã tối thiểu]
- **Kiểm thử Hiệu năng**: [phương pháp kiểm thử tải và hiệu năng]

## 7. Lý do & Bối cảnh

[Giải thích lý do đằng sau các yêu cầu, ràng buộc và hướng dẫn. Cung cấp bối cảnh cho các quyết định thiết kế.]

## 8. Phụ thuộc & Tích hợp Bên ngoài

[Xác định các hệ thống, dịch vụ bên ngoài và các phụ thuộc kiến trúc cần thiết cho đặc tả này. Tập trung vào **cái gì** cần thiết thay vì **cách thức** triển khai. Tránh các phiên bản gói hoặc thư viện cụ thể trừ khi chúng đại diện cho các ràng buộc kiến trúc.]

### Hệ thống bên ngoài

- **EXT-001**: [Tên hệ thống bên ngoài] - [Mục đích và loại tích hợp]

### Dịch vụ của bên thứ ba

- **SVC-001**: [Tên dịch vụ] - [Các khả năng cần thiết và yêu cầu SLA]

### Phụ thuộc cơ sở hạ tầng

- **INF-001**: [Thành phần cơ sở hạ tầng] - [Yêu cầu và ràng buộc]

### Phụ thuộc dữ liệu

- **DAT-001**: [Nguồn dữ liệu bên ngoài] - [Định dạng, tần suất và yêu cầu truy cập]

### Phụ thuộc nền tảng công nghệ

- **PLT-001**: [Yêu cầu nền tảng/runtime] - [Ràng buộc phiên bản và lý do]

### Phụ thuộc tuân thủ

- **COM-001**: [Yêu cầu quy định hoặc tuân thủ] - [Tác động đến việc triển khai]

**Lưu ý**: Phần này nên tập trung vào các phụ thuộc kiến trúc và kinh doanh, không phải các triển khai gói cụ thể. Ví dụ, chỉ định "thư viện xác thực OAuth 2.0" thay vì "Microsoft.AspNetCore.Authentication.JwtBearer v6.0.1".

## 9. Ví dụ & Trường hợp Biên

```code
// Đoạn mã hoặc ví dụ dữ liệu minh họa việc áp dụng đúng các hướng dẫn, bao gồm cả các trường hợp biên
```
````

## 10. Tiêu chí Xác thực

[Liệt kê các tiêu chí hoặc bài kiểm tra phải được thỏa mãn để tuân thủ đặc tả này.]

## 11. Đặc tả Liên quan / Đọc thêm

[Liên kết đến đặc tả liên quan 1]
[Liên kết đến tài liệu bên ngoài có liên quan]

```

```
