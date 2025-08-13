# Thực hành tốt nhất khi viết tài liệu Java (Javadoc)

-   Các thành viên `public` và `protected` nên được viết tài liệu bằng
    chú thích Javadoc.
-   Khuyến khích viết tài liệu cho cả thành viên `package-private` và
    `private`, đặc biệt nếu chúng phức tạp hoặc không tự giải thích.
-   Câu đầu tiên của chú thích Javadoc là phần mô tả tóm tắt. Nó nên là
    phần giới thiệu ngắn gọn về chức năng của phương thức và kết thúc
    bằng dấu chấm.
-   Sử dụng `@param` cho các tham số của phương thức. Phần mô tả bắt đầu
    bằng chữ thường và không kết thúc bằng dấu chấm.
-   Sử dụng `@return` cho giá trị trả về của phương thức.
-   Sử dụng `@throws` hoặc `@exception` để mô tả các ngoại lệ mà phương
    thức có thể ném ra.
-   Sử dụng `@see` để tham chiếu đến các kiểu hoặc thành viên khác.
-   Sử dụng `{@inheritDoc}` để kế thừa tài liệu từ lớp cơ sở hoặc
    interface.
    -   Trừ khi có thay đổi hành vi lớn, khi đó cần ghi rõ sự khác biệt.
-   Sử dụng `@param <T>` cho tham số kiểu trong các kiểu hoặc phương
    thức generic.
-   Sử dụng `{@code}` cho các đoạn mã inline.
-   Sử dụng `<pre>{@code ... }</pre>` cho các khối mã.
-   Sử dụng `@since` để chỉ ra thời điểm tính năng được giới thiệu (ví
    dụ: số phiên bản).
-   Sử dụng `@version` để chỉ định phiên bản của thành viên.
-   Sử dụng `@author` để ghi tên tác giả của mã.
-   Sử dụng `@deprecated` để đánh dấu một thành viên là đã lỗi thời và
    cung cấp lựa chọn thay thế.
