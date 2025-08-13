---
description: "Quy ước viết mã và các phương pháp hay nhất cho ngôn ngữ lập trình Rust"
applyTo: "**/*.rs"
---

# Quy ước viết mã và các phương pháp hay nhất cho Rust

Tuân thủ các phương pháp Rust đặc trưng (idiomatic) và các tiêu chuẩn cộng đồng khi viết mã Rust.

Các hướng dẫn này dựa trên [The Rust Book](https://doc.rust-lang.org/book/), [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/), [quy ước đặt tên RFC 430](https://github.com/rust-lang/rfcs/blob/master/text/0430-finalizing-naming-conventions.md), và cộng đồng Rust rộng lớn tại [users.rust-lang.org](https://users.rust-lang.org).

## Hướng dẫn chung

- Luôn ưu tiên tính dễ đọc, an toàn và khả năng bảo trì.
- Sử dụng hệ thống kiểu dữ liệu mạnh (strong typing) và tận dụng hệ thống sở hữu (ownership) của Rust để đảm bảo an toàn bộ nhớ.
- Chia nhỏ các hàm phức tạp thành các hàm nhỏ hơn, dễ quản lý hơn.
- Đối với mã liên quan đến thuật toán, hãy bao gồm giải thích về phương pháp được sử dụng.
- Viết mã với các phương pháp bảo trì tốt, bao gồm các bình luận giải thích lý do đưa ra các quyết định thiết kế.
- Xử lý lỗi một cách linh hoạt bằng `Result<T, E>` và cung cấp thông báo lỗi có ý nghĩa.
- Đối với các phụ thuộc bên ngoài, hãy đề cập đến cách sử dụng và mục đích của chúng trong tài liệu.
- Sử dụng quy ước đặt tên nhất quán theo [RFC 430](https://github.com/rust-lang/rfcs/blob/master/text/0430-finalizing-naming-conventions.md).
- Viết mã Rust đặc trưng (idiomatic), an toàn và hiệu quả, tuân thủ các quy tắc của trình kiểm tra mượn (borrow checker).
- Đảm bảo mã biên dịch không có cảnh báo.

## Các mẫu nên tuân theo

- Sử dụng module (`mod`) và giao diện công khai (`pub`) để đóng gói logic.
- Xử lý lỗi đúng cách bằng `?`, `match`, hoặc `if let`.
- Sử dụng `serde` để tuần tự hóa (serialization) và `thiserror` hoặc `anyhow` cho các lỗi tùy chỉnh.
- Implement các trait để trừu tượng hóa các dịch vụ hoặc phụ thuộc bên ngoài.
- Cấu trúc mã bất đồng bộ bằng `async/await` và `tokio` hoặc `async-std`.
- Ưu tiên dùng enum thay cho các cờ (flags) và trạng thái để đảm bảo an toàn kiểu.
- Sử dụng mẫu builder để tạo các đối tượng phức tạp.
- Tách mã nhị phân và thư viện (`main.rs` và `lib.rs`) để dễ kiểm thử và tái sử dụng.
- Sử dụng `rayon` cho xử lý song song dữ liệu và các tác vụ tốn nhiều CPU.
- Sử dụng iterator thay vì vòng lặp dựa trên chỉ số vì chúng thường nhanh hơn và an toàn hơn.
- Sử dụng `&str` thay vì `String` cho tham số hàm khi bạn không cần quyền sở hữu.
- Ưu tiên mượn (borrowing) và các hoạt động không sao chép (zero-copy) để tránh cấp phát bộ nhớ không cần thiết.

### Sở hữu, Mượn và Vòng đời (Ownership, Borrowing, and Lifetimes)

- Ưu tiên mượn (`&T`) hơn là sao chép (`clone`) trừ khi việc chuyển quyền sở hữu là cần thiết.
- Sử dụng `&mut T` khi bạn cần sửa đổi dữ liệu được mượn.
- Chú thích vòng đời (lifetimes) một cách tường minh khi trình biên dịch không thể suy ra chúng.
- Sử dụng `Rc<T>` để đếm tham chiếu trong môi trường đơn luồng và `Arc<T>` để đếm tham chiếu an toàn trong môi trường đa luồng.
- Sử dụng `RefCell<T>` cho khả năng thay đổi nội tại (interior mutability) trong ngữ cảnh đơn luồng và `Mutex<T>` hoặc `RwLock<T>` cho ngữ cảnh đa luồng.

## Các mẫu cần tránh

- Không sử dụng `unwrap()` hoặc `expect()` trừ khi thực sự cần thiết—ưu tiên xử lý lỗi đúng cách.
- Tránh panic trong mã thư viện—thay vào đó hãy trả về `Result`.
- Không dựa vào trạng thái toàn cục có thể thay đổi—sử dụng dependency injection hoặc các container an toàn cho luồng.
- Tránh logic lồng nhau quá sâu—tái cấu trúc bằng các hàm hoặc combinator.
- Không bỏ qua các cảnh báo—coi chúng như lỗi trong quá trình CI.
- Tránh `unsafe` trừ khi bắt buộc và phải được ghi lại đầy đủ trong tài liệu.
- Không lạm dụng `clone()`, sử dụng mượn thay vì sao chép trừ khi cần chuyển quyền sở hữu.
- Tránh `collect()` quá sớm, giữ cho iterator ở trạng thái lười biếng (lazy) cho đến khi bạn thực sự cần collection.
- Tránh cấp phát bộ nhớ không cần thiết—ưu tiên mượn và các hoạt động không sao chép.

## Phong cách mã và định dạng

- Tuân thủ Hướng dẫn Phong cách Rust và sử dụng `rustfmt` để định dạng tự động.
- Giữ các dòng dưới 100 ký tự khi có thể.
- Đặt tài liệu cho hàm và struct ngay trước mục đó bằng cách sử dụng `///`.
- Sử dụng `cargo clippy` để phát hiện các lỗi phổ biến và thực thi các phương pháp hay nhất.

## Xử lý lỗi

- Sử dụng `Result<T, E>` cho các lỗi có thể phục hồi và `panic!` chỉ cho các lỗi không thể phục hồi.
- Ưu tiên toán tử `?` hơn `unwrap()` hoặc `expect()` để lan truyền lỗi.
- Tạo các kiểu lỗi tùy chỉnh bằng `thiserror` hoặc implement `std::error::Error`.
- Sử dụng `Option<T>` cho các giá trị có thể tồn tại hoặc không.
- Cung cấp thông báo lỗi và ngữ cảnh có ý nghĩa.
- Các kiểu lỗi phải có ý nghĩa và hoạt động tốt (implement các trait tiêu chuẩn).
- Xác thực các đối số của hàm và trả về lỗi thích hợp cho đầu vào không hợp lệ.

## Hướng dẫn thiết kế API

### Implement các Trait phổ biến

Nên implement các trait phổ biến khi thích hợp:

- `Copy`, `Clone`, `Eq`, `PartialEq`, `Ord`, `PartialOrd`, `Hash`, `Debug`, `Display`, `Default`
- Sử dụng các trait chuyển đổi tiêu chuẩn: `From`, `AsRef`, `AsMut`
- Các collection nên implement `FromIterator` và `Extend`
- Lưu ý: `Send` và `Sync` được trình biên dịch tự động implement khi an toàn; tránh implement thủ công trừ khi sử dụng mã `unsafe`

### An toàn kiểu và tính dự đoán được

- Sử dụng newtype để cung cấp sự phân biệt tĩnh
- Các đối số nên truyền tải ý nghĩa thông qua kiểu; ưu tiên các kiểu cụ thể hơn là tham số `bool` chung chung
- Sử dụng `Option<T>` một cách thích hợp cho các giá trị thực sự tùy chọn
- Các hàm có một "receiver" rõ ràng nên là các phương thức
- Chỉ các con trỏ thông minh (smart pointers) mới nên implement `Deref` và `DerefMut`

### Tương thích trong tương lai (Future Proofing)

- Sử dụng các trait được niêm phong (sealed traits) để bảo vệ khỏi các implement ở các crate phụ thuộc
- Các struct nên có các trường riêng tư (private)
- Các hàm nên xác thực các đối số của chúng
- Tất cả các kiểu công khai phải implement `Debug`

## Kiểm thử và Tài liệu

- Viết các unit test toàn diện bằng cách sử dụng các module `#[cfg(test)]` và chú thích `#[test]`.
- Sử dụng các module test bên cạnh mã mà chúng kiểm thử (`mod tests { ... }`).
- Viết các integration test trong thư mục `tests/` với tên tệp mô tả.
- Viết các bình luận rõ ràng và ngắn gọn cho mỗi hàm, struct, enum và logic phức tạp.
- Đảm bảo các hàm có tên mô tả và bao gồm tài liệu toàn diện.
- Ghi tài liệu cho tất cả các API công khai bằng rustdoc (bình luận `///`) theo [API Guidelines](https://rust-lang.github.io/api-guidelines/).
- Sử dụng `#[doc(hidden)]` để ẩn các chi tiết implement khỏi tài liệu công khai.
- Ghi tài liệu về các điều kiện lỗi, các kịch bản panic và các cân nhắc về an toàn.
- Các ví dụ nên sử dụng toán tử `?`, không phải `unwrap()` hoặc macro `try!` đã lỗi thời.

## Tổ chức dự án

- Sử dụng phiên bản ngữ nghĩa (semantic versioning) trong `Cargo.toml`.
- Bao gồm siêu dữ liệu toàn diện: `description`, `license`, `repository`, `keywords`, `categories`.
- Sử dụng các cờ tính năng (feature flags) cho chức năng tùy chọn.
- Tổ chức mã thành các module bằng cách sử dụng `mod.rs` hoặc các tệp được đặt tên.
- Giữ cho `main.rs` hoặc `lib.rs` ở mức tối thiểu - chuyển logic vào các module.

## Danh sách kiểm tra chất lượng

Trước khi xuất bản hoặc đánh giá mã Rust, hãy đảm bảo:

### Yêu cầu cốt lõi

- [ ] **Đặt tên**: Tuân thủ quy ước đặt tên RFC 430
- [ ] **Traits**: Implement `Debug`, `Clone`, `PartialEq` khi thích hợp
- [ ] **Xử lý lỗi**: Sử dụng `Result<T, E>` và cung cấp các kiểu lỗi có ý nghĩa
- [ ] **Tài liệu**: Tất cả các mục công khai đều có bình luận rustdoc kèm theo ví dụ
- [ ] **Kiểm thử**: Độ bao phủ test toàn diện bao gồm các trường hợp biên

### An toàn và Chất lượng

- [ ] **An toàn**: Không có mã `unsafe` không cần thiết, xử lý lỗi đúng cách
- [ ] **Hiệu suất**: Sử dụng iterator hiệu quả, cấp phát bộ nhớ tối thiểu
- [ ] **Thiết kế API**: Các hàm có thể dự đoán được, linh hoạt và an toàn về kiểu
- [ ] **Tương thích trong tương lai**: Các trường riêng tư trong struct, các trait được niêm phong khi thích hợp
- [ ] **Công cụ**: Mã vượt qua `cargo fmt`, `cargo clippy`, và
