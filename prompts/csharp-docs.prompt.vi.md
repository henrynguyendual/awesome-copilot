---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Đảm bảo rằng các kiểu C# được ghi lại bằng nhận xét XML và tuân theo các phương pháp hay nhất để tạo tài liệu."
---

# Các quy tắc tốt nhất về tài liệu C#

- Các thành viên public nên được ghi lại bằng nhận xét XML.
- Khuyến khích ghi lại tài liệu cho các thành viên internal, đặc biệt nếu chúng phức tạp hoặc không tự giải thích được.
- Sử dụng `<summary>` để mô tả phương thức. Đây nên là một cái nhìn tổng quan ngắn gọn về những gì phương thức thực hiện.
- Sử dụng `<param>` cho các tham số của phương thức.
- Sử dụng `<returns>` cho các giá trị trả về của phương thức.
- Sử dụng `<remarks>` để cung cấp thông tin bổ sung, có thể bao gồm chi tiết triển khai, ghi chú sử dụng hoặc bất kỳ ngữ cảnh liên quan nào khác.
- Sử dụng `<example>` cho các ví dụ về cách sử dụng thành viên.
- Sử dụng `<exception>` để ghi lại các ngoại lệ được ném ra bởi các phương thức.
- Sử dụng `<see>` và `<seealso>` để tham chiếu đến các kiểu hoặc thành viên khác.
- Sử dụng `<inheritdoc/>` để kế thừa tài liệu từ các lớp cơ sở hoặc giao diện.
  - Trừ khi có thay đổi lớn về hành vi, trong trường hợp đó bạn nên ghi lại những điểm khác biệt.
- Sử dụng `<typeparam>` cho các tham số kiểu trong các kiểu hoặc phương thức generic.
- Sử dụng `<typeparamref>` để tham chiếu đến các tham số kiểu trong tài liệu.
- Sử dụng `<c>` cho các đoạn mã nội tuyến.
- Sử dụng `<code>` cho các khối mã.
- Sử dụng `<see langword>` cho các từ khóa dành riêng cho ngôn ngữ như `null`, `true`, `false`, `int`, `bool
