---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "Đảm bảo rằng các kiểu Java được ghi tài liệu bằng các bình luận Javadoc và tuân thủ các phương pháp hay nhất để làm tài liệu."
---

# Các phương pháp hay nhất về tài liệu Java (Javadoc)

- Các thành viên `public` và `protected` nên được ghi tài liệu bằng các bình luận Javadoc.
- Khuyến khích ghi tài liệu cho cả các thành viên `package-private` và `private`, đặc biệt nếu chúng phức tạp hoặc không tự giải thích được.
- Câu đầu tiên của bình luận Javadoc là mô tả tóm tắt. Nó phải là một cái nhìn tổng quan ngắn gọn về những gì phương thức thực hiện và kết thúc bằng một dấu chấm.
- Sử dụng `@param` cho các tham số của phương thức. Phần mô tả bắt đầu bằng một chữ cái viết thường và không kết thúc bằng dấu chấm.
- Sử dụng `@return` cho các giá trị trả về của phương thức.
- Sử dụng `@throws` hoặc `@exception` để ghi tài liệu về các ngoại lệ được ném ra bởi các phương thức.
- Sử dụng `@see` để tham chiếu đến các kiểu hoặc thành viên khác.
- Sử dụng `{@inheritDoc}` để kế thừa tài liệu từ các lớp hoặc giao diện cơ sở.
  - Trừ khi có sự thay đổi lớn về hành vi, trong trường hợp đó bạn nên ghi lại sự khác biệt.
- Sử dụng `@param <T>` cho các tham số kiểu trong các kiểu hoặc phương thức generic.
- Sử dụng `{@code}` cho các đoạn mã nội tuyến.
- Sử dụng `<pre>{@code ... }</pre>` cho các khối mã.
- Sử dụng `@since` để chỉ ra thời điểm tính năng được giới thiệu (ví dụ: số phiên bản).
- Sử dụng `@version` để chỉ định phiên bản của thành viên.
- Sử dụng `@author` để chỉ định tác giả của mã.
- Sử dụng `@deprecated` để đánh dấu một thành viên là không còn được dùng nữa và cung cấp một giải pháp
