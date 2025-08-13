# Thực hành tốt nhất khi viết tài liệu C#

- Các thành viên public nên được viết tài liệu bằng XML comments.
- Khuyến khích viết tài liệu cho cả các thành viên internal, đặc biệt nếu chúng phức tạp hoặc không tự giải thích được.
- Sử dụng `<summary>` để mô tả phương thức. Phần này nên là tóm tắt ngắn gọn về những gì phương thức thực hiện.
- Sử dụng `<param>` cho các tham số của phương thức.
- Sử dụng `<returns>` cho giá trị trả về của phương thức.
- Sử dụng `<remarks>` cho thông tin bổ sung, bao gồm chi tiết triển khai, lưu ý sử dụng, hoặc bất kỳ ngữ cảnh liên quan nào khác.
- Sử dụng `<example>` cho ví dụ minh họa cách sử dụng thành viên.
- Sử dụng `<exception>` để mô tả các ngoại lệ mà phương thức có thể ném ra.
- Sử dụng `<see>` và `<seealso>` để tham chiếu đến các kiểu hoặc thành viên khác.
- Sử dụng `<inheritdoc/>` để kế thừa tài liệu từ lớp cơ sở hoặc interface.
  - Trừ khi có thay đổi hành vi lớn, khi đó bạn nên mô tả sự khác biệt.
- Sử dụng `<typeparam>` cho các tham số kiểu trong kiểu hoặc phương thức generic.
- Sử dụng `<typeparamref>` để tham chiếu tham số kiểu trong tài liệu.
- Sử dụng `<c>` cho đoạn mã ngắn inline.
- Sử dụng `<code>` cho khối mã.
- Sử dụng `<see langword>` cho các từ khóa đặc thù của ngôn ngữ như `null`, `true`, `false`, `int`, `bool`, v.v.
