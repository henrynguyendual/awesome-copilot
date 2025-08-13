---
description: "Hướng dẫn xây dựng các ứng dụng Java cơ bản"
applyTo: "**/*.java"
---

# Phát triển Java

## Hướng dẫn Chung

- Đầu tiên, hỏi người dùng xem họ có muốn tích hợp các công cụ phân tích tĩnh (SonarQube, PMD, Checkstyle) vào thiết lập dự án của họ không. Nếu có, hãy cung cấp hướng dẫn về việc lựa chọn và cấu hình công cụ.
- Nếu người dùng từ chối các công cụ phân tích tĩnh hoặc muốn tiếp tục mà không có chúng, hãy tiếp tục triển khai các Nguyên tắc tốt nhất, các mẫu lỗi và hướng dẫn phòng chống code smell được nêu dưới đây.
- Chủ động giải quyết các code smell trong quá trình phát triển thay vì tích lũy nợ kỹ thuật.
- Tập trung vào khả năng đọc, khả năng bảo trì và hiệu suất khi tái cấu trúc các vấn đề đã xác định.
- Sử dụng các cảnh báo và đề xuất do IDE / Trình soạn thảo mã báo cáo để phát hiện sớm các mẫu phổ biến trong quá trình phát triển.

## Các nguyên tắc tốt nhất

- **Records**: Đối với các lớp chủ yếu dùng để lưu trữ dữ liệu (ví dụ: DTO, cấu trúc dữ liệu bất biến), **nên sử dụng Java Records thay vì các lớp truyền thống**.
- **Pattern Matching**: Sử dụng pattern matching cho biểu thức `instanceof` và `switch` để đơn giản hóa logic điều kiện và ép kiểu.
- **Suy luận kiểu (Type Inference)**: Sử dụng `var` để khai báo biến cục bộ nhằm cải thiện khả năng đọc, nhưng chỉ khi kiểu dữ liệu đã rõ ràng từ phía bên phải của biểu thức.
- **Tính bất biến (Immutability)**: Ưu tiên các đối tượng bất biến. Đặt các lớp và trường là `final` khi có thể. Sử dụng các collection từ `List.of()`/`Map.of()` cho dữ liệu cố định. Sử dụng `Stream.toList()` để tạo danh sách bất biến.
- **Streams và Lambdas**: Sử dụng Streams API và biểu thức lambda để xử lý collection. Sử dụng tham chiếu phương thức (ví dụ: `stream.map(Foo::toBar)`).
- **Xử lý Null**: Tránh trả về hoặc chấp nhận `null`. Sử dụng `Optional<T>` cho các giá trị có thể không tồn tại và các phương thức tiện ích của `Objects` như `equals()` và `requireNonNull()`.

### Quy ước đặt tên

- Tuân theo hướng dẫn về phong cách Java của Google:
  - `UpperCamelCase` cho tên lớp và interface.
  - `lowerCamelCase` cho tên phương thức và biến.
  - `UPPER_SNAKE_CASE` cho hằng số.
  - `lowercase` cho tên package.
- Sử dụng danh từ cho lớp (`UserService`) và động từ cho phương thức (`getUserById`).
- Tránh viết tắt và ký pháp Hungarian.

### Các mẫu lỗi (Bug Patterns)

| ID Quy tắc | Mô tả                                                        | Ví dụ / Ghi chú                                                                              |
| ---------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| `S2095`    | Các tài nguyên nên được đóng                                 | Sử dụng try-with-resources khi làm việc với streams, files, sockets, v.v.                    |
| `S1698`    | Các đối tượng nên được so sánh bằng `.equals()` thay vì `==` | Đặc biệt quan trọng đối với Strings và các kiểu nguyên thủy được bao bọc (boxed primitives). |
| `S1905`    | Các ép kiểu dư thừa nên được loại bỏ                         | Dọn dẹp các ép kiểu không cần thiết hoặc không an toàn.                                      |
| `S3518`    | Các điều kiện không nên luôn đánh giá là true hoặc false     | Chú ý đến các vòng lặp vô hạn hoặc các điều kiện if không bao giờ thay đổi.                  |
| `S108`     | Mã không thể truy cập nên được loại bỏ                       | Mã sau `return`, `throw`, v.v., phải được dọn dẹp.                                           |

## Code Smells

| ID Quy tắc | Mô tả                                                       | Ví dụ / Ghi chú                                                               |
| ---------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `S107`     | Các phương thức không nên có quá nhiều tham số              | Tái cấu trúc thành các lớp trợ giúp hoặc sử dụng mẫu builder.                 |
| `S121`     | Các khối mã trùng lặp nên được loại bỏ                      | Hợp nhất logic vào các phương thức dùng chung.                                |
| `S138`     | Các phương thức không nên quá dài                           | Chia nhỏ logic phức tạp thành các đơn vị nhỏ hơn, có thể kiểm thử.            |
| `S3776`    | Độ phức tạp nhận thức nên được giảm                         | Đơn giản hóa logic lồng nhau, trích xuất phương thức, tránh các cây `if` sâu. |
| `S1192`    | Các chuỗi ký tự (string literal) không nên bị trùng lặp     | Thay thế bằng hằng số hoặc enum.                                              |
| `S1854`    | Các phép gán không sử dụng nên được loại bỏ                 | Tránh các biến chết—loại bỏ hoặc tái cấu trúc.                                |
| `S109`     | Các số "ma thuật" (magic number) nên được thay bằng hằng số | Cải thiện khả năng đọc và bảo trì.                                            |
| `S1188`    | Các khối catch không nên để trống                           | Luôn ghi log hoặc xử lý ngoại lệ một cách có ý nghĩa.                         |

## Xây dựng và Xác minh

- Sau khi thêm hoặc sửa đổi mã, hãy xác minh dự án tiếp tục xây dựng thành công.
- Nếu dự án sử dụng Maven, hãy chạy `mvn clean install`.
- Nếu dự án sử dụng Gradle, hãy chạy `./gradlew build` (hoặc `gradlew.bat build` trên Windows).
- Đảm bảo tất cả các bài kiểm thử đều vượt qua như một phần của quá
