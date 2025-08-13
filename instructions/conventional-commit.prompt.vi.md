---
description: "Prompt và quy trình để tạo thông điệp commit theo quy ước bằng cách sử dụng định dạng XML có cấu trúc. Hướng dẫn người dùng tạo các thông điệp commit được tiêu chuẩn hóa, mang tính mô tả phù hợp với đặc tả Conventional Commits, bao gồm hướng dẫn, ví dụ và xác thực."
tools: ["run_in_terminal", "get_terminal_output"]
---

### Hướng dẫn

```xml
    <description>Tệp này chứa một mẫu prompt để tạo thông điệp commit theo quy ước. Nó cung cấp hướng dẫn, ví dụ và các quy tắc định dạng để giúp người dùng viết các thông điệp commit được tiêu chuẩn hóa, mang tính mô tả theo đặc tả Conventional Commits.</description>
    <note>
```

### Quy trình

**Thực hiện theo các bước sau:**

1.  Chạy `git status` để xem lại các tệp đã thay đổi.
2.  Chạy `git diff` hoặc `git diff --cached` để kiểm tra các thay đổi.
3.  Đưa các thay đổi của bạn vào khu vực chờ (staging) bằng `git add <file>`.
4.  Xây dựng thông điệp commit của bạn bằng cấu trúc XML sau.
5.  Sau khi tạo thông điệp commit, Copilot sẽ tự động chạy lệnh sau trong terminal tích hợp của bạn (không cần xác nhận):

```bash
git commit -m "type(scope): description"
```

6.  Chỉ cần thực thi prompt này và Copilot sẽ xử lý việc commit cho bạn trong terminal.

### Cấu trúc thông điệp Commit

```xml
<commit-message>
    <type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert</type>
    <scope>()</scope>
    <description>Một bản tóm tắt ngắn gọn, mang tính mệnh lệnh về thay đổi</description>
    <body>(tùy chọn: giải thích chi tiết hơn)</body>
    <footer>(tùy chọn: ví dụ: BREAKING CHANGE: chi tiết, hoặc tham chiếu đến issue)</footer>
</commit-message>
```

### Ví dụ

```xml
<examples>
    <example>feat(parser): thêm khả năng phân tích cú pháp mảng</example>
    <example>fix(ui): sửa lỗi căn chỉnh nút</example>
    <example>docs: cập nhật README với hướng dẫn sử dụng</example>
    <example>refactor: cải thiện hiệu suất xử lý dữ liệu</example>
    <example>chore: cập nhật các dependency</example>
    <example>feat!: gửi email khi đăng ký (BREAKING CHANGE: yêu cầu dịch vụ email)</example>
</examples>
```

### Xác thực

```xml
<validation>
    <type>Phải là một trong các loại được phép. Xem <reference>https://www.conventionalcommits.org/en/v1.0.0/#specification</reference></type>
    <scope>Tùy chọn, nhưng được khuyến nghị để rõ ràng.</scope>
    <description>Bắt buộc. Sử dụng thể mệnh lệnh (ví dụ: "thêm", không phải "đã thêm").</description>
    <body>Tùy chọn. Sử dụng cho ngữ cảnh bổ sung.</body>
    <footer>Sử dụng cho các thay đổi đột phá (breaking changes) hoặc tham chiếu đến issue.</footer>
</validation>
```

### Bước cuối cùng

```xml
<final-step>
    <cmd>git commit -m "type(scope): description"</cmd>
    <note>Thay thế bằng thông điệp bạn đã xây dựng. Bao gồm cả body và footer nếu cần.</note>
</final-step>
```
