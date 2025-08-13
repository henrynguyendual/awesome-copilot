---
description: "Hướng dẫn viết mã Dart và Flutter theo các khuyến nghị chính thức."
applyTo: "**/*.dart"
---

# Dart và Flutter

Các phương pháp hay nhất được đề xuất bởi các nhóm Dart và Flutter. Những hướng dẫn này được lấy từ [Effective Dart](https://dart.dev/effective-dart) và [Architecture Recommendations](https://docs.flutter.dev/app-architecture/recommendations).

## Effective Dart

Trong nhiều năm qua, chúng tôi đã viết rất nhiều mã Dart và học được nhiều điều về những gì hoạt động tốt và những gì không. Chúng tôi chia sẻ điều này với bạn để bạn cũng có thể viết mã nhất quán, mạnh mẽ và nhanh chóng. Có hai chủ đề bao quát:

1.  **Hãy nhất quán.** Khi nói đến những thứ như định dạng và cách viết hoa, các cuộc tranh luận về cái nào tốt hơn là chủ quan và không thể giải quyết được. Điều chúng tôi biết chắc chắn là việc _nhất quán_ là hữu ích một cách khách quan.

    Nếu hai đoạn mã trông khác nhau, đó là vì chúng _khác nhau_ theo một cách có ý nghĩa nào đó. Khi một đoạn mã nổi bật và thu hút sự chú ý của bạn, nó nên làm vậy vì một lý do hữu ích.

2.  **Hãy ngắn gọn.** Dart được thiết kế để quen thuộc, vì vậy nó kế thừa nhiều câu lệnh và biểu thức giống như C, Java, JavaScript và các ngôn ngữ khác. Nhưng chúng tôi tạo ra Dart vì có rất nhiều cơ hội để cải thiện những gì các ngôn ngữ đó cung cấp. Chúng tôi đã thêm một loạt các tính năng, từ nội suy chuỗi đến khởi tạo tham số chính thức, để giúp bạn thể hiện ý định của mình một cách đơn giản và dễ dàng hơn.

    Nếu có nhiều cách để nói một điều gì đó, bạn thường nên chọn cách ngắn gọn nhất. Điều này không có nghĩa là bạn nên `code golf` để nhồi nhét cả một chương trình vào một dòng duy nhất. Mục tiêu là mã _tiết kiệm_, không phải _dày đặc_.

### Các chủ đề

Chúng tôi chia các hướng dẫn thành một vài chủ đề riêng biệt để dễ tiếp thu:

- **Phong cách (Style)** – Điều này xác định các quy tắc để trình bày và tổ chức mã, hoặc ít nhất là những phần mà `dart format` không xử lý cho bạn. Chủ đề phong cách cũng chỉ định cách định dạng các định danh: `camelCase`, `using_underscores`, v.v.

- **Tài liệu (Documentation)** – Điều này cho bạn biết mọi thứ bạn cần biết về những gì nằm bên trong các bình luận. Cả bình luận tài liệu (doc comments) và các bình luận mã thông thường.

- **Sử dụng (Usage)** – Điều này dạy bạn cách tận dụng tốt nhất các tính năng của ngôn ngữ để triển khai hành vi. Nếu nó nằm trong một câu lệnh hoặc biểu thức, nó sẽ được đề cập ở đây.

- **Thiết kế (Design)** – Đây là chủ đề mềm nhất, nhưng có phạm vi rộng nhất. Nó bao gồm những gì chúng tôi đã học được về việc thiết kế các API nhất quán, có thể sử dụng được cho các thư viện. Nếu nó nằm trong một chữ ký kiểu hoặc khai báo, phần này sẽ đề cập đến nó.

### Cách đọc các chủ đề

Mỗi chủ đề được chia thành một vài phần. Các phần chứa một danh sách các hướng dẫn. Mỗi hướng dẫn bắt đầu bằng một trong những từ sau:

- **NÊN (DO)** các hướng dẫn mô tả các thực hành luôn phải được tuân theo. Hầu như sẽ không bao giờ có lý do hợp lệ để đi chệch hướng.

- **KHÔNG NÊN (DON'T)** các hướng dẫn là ngược lại: những điều hầu như không bao giờ là một ý tưởng tốt. Hy vọng rằng, chúng ta không có nhiều những điều này như các ngôn ngữ khác vì chúng ta có ít gánh nặng lịch sử hơn.

- **ƯU TIÊN (PREFER)** các hướng dẫn là các thực hành mà bạn _nên_ tuân theo. Tuy nhiên, có thể có những trường hợp mà việc làm khác đi lại có ý nghĩa. Chỉ cần đảm bảo bạn hiểu đầy đủ các hàm ý của việc bỏ qua hướng dẫn khi bạn làm vậy.

- **TRÁNH (AVOID)** các hướng dẫn là đối ngẫu của "ưu tiên": những thứ bạn không nên làm nhưng có thể có lý do chính đáng trong những trường hợp hiếm hoi.

- **CÂN NHẮC (CONSIDER)** các hướng dẫn là các thực hành mà bạn có thể muốn hoặc không muốn tuân theo, tùy thuộc vào hoàn cảnh, tiền lệ và sở thích của riêng bạn.

Một số hướng dẫn mô tả một **ngoại lệ** nơi quy tắc _không_ áp dụng. Khi được liệt kê, các ngoại lệ có thể không đầy đủ—bạn vẫn có thể cần phải sử dụng sự phán đoán của mình trong các trường hợp khác.

Điều này nghe có vẻ như cảnh sát sẽ đến gõ cửa nhà bạn nếu bạn không buộc dây giày đúng cách. Mọi thứ không tệ đến thế. Hầu hết các hướng dẫn ở đây đều là lẽ thường và tất cả chúng ta đều là những người hợp lý. Mục tiêu, như mọi khi, là mã đẹp, dễ đọc và dễ bảo trì.

### Các quy tắc

#### Phong cách

##### Định danh

- NÊN đặt tên các kiểu bằng `UpperCamelCase`.
- NÊN đặt tên các extension bằng `UpperCamelCase`.
- NÊN đặt tên các gói, thư mục và tệp nguồn bằng `lowercase_with_underscores`.
- NÊN đặt tên các tiền tố import bằng `lowercase_with_underscores`.
- NÊN đặt tên các định danh khác bằng `lowerCamelCase`.
- ƯU TIÊN sử dụng `lowerCamelCase` cho tên hằng số.
- NÊN viết hoa các từ viết tắt dài hơn hai chữ cái như các từ thông thường.
- ƯU TIÊN sử dụng ký tự đại diện (wildcards) cho các tham số callback không được sử dụng.
- KHÔNG NÊN sử dụng dấu gạch dưới ở đầu cho các định danh không phải là riêng tư (private).
- KHÔNG NÊN sử dụng các chữ cái tiền tố.
- KHÔNG NÊN đặt tên thư viện một cách tường minh.

##### Thứ tự

- NÊN đặt các import `dart:` trước các import khác.
- NÊN đặt các import `package:` trước các import tương đối.
- NÊN chỉ định các export trong một phần riêng biệt sau tất cả các import.
- NÊN sắp xếp các phần theo thứ tự bảng chữ cái.

##### Định dạng

- NÊN định dạng mã của bạn bằng `dart format`.
- CÂN NHẮC thay đổi mã của bạn để làm cho nó thân thiện hơn với trình định dạng.
- ƯU TIÊN các dòng có 80 ký tự hoặc ít hơn.
- NÊN sử dụng dấu ngoặc nhọn cho tất cả các câu lệnh điều khiển luồng.

#### Tài liệu

##### Bình luận

- NÊN định dạng các bình luận như các câu văn.
- KHÔNG NÊN sử dụng bình luận khối (block comments) cho tài liệu.

##### Bình luận tài liệu (Doc comments)

- NÊN sử dụng bình luận tài liệu `///` để ghi tài liệu cho các thành viên và kiểu.
- ƯU TIÊN viết bình luận tài liệu cho các API công khai.
- CÂN NHẮC viết một bình luận tài liệu ở cấp độ thư viện.
- CÂN NHẮC viết bình luận tài liệu cho các API riêng tư.
- NÊN bắt đầu bình luận tài liệu bằng một bản tóm tắt một câu.
- NÊN tách câu đầu tiên của một bình luận tài liệu thành một đoạn riêng.
- TRÁNH sự dư thừa với ngữ cảnh xung quanh.
- ƯU TIÊN bắt đầu bình luận của một hàm hoặc phương thức bằng động từ ngôi thứ ba nếu mục đích chính của nó là một tác dụng phụ (side effect).
- ƯU TIÊN bắt đầu bình luận của một biến hoặc thuộc tính không phải boolean bằng một cụm danh từ.
- ƯU TIÊN bắt đầu bình luận của một biến hoặc thuộc tính boolean bằng "Whether" theo sau là một cụm danh từ hoặc danh động từ.
- ƯU TIÊN một cụm danh từ hoặc cụm động từ không mệnh lệnh cho một hàm hoặc phương thức nếu việc trả về một giá trị là mục đích chính của nó.
- KHÔNG NÊN viết tài liệu cho cả getter và setter của một thuộc tính.
- ƯU TIÊN bắt đầu bình luận thư viện hoặc kiểu bằng các cụm danh từ.
- CÂN NHẮC bao gồm các mẫu mã trong bình luận tài liệu.
- NÊN sử dụng dấu ngoặc vuông trong bình luận tài liệu để tham chiếu đến các định danh trong phạm vi.
- NÊN sử dụng văn xuôi để giải thích các tham số, giá trị trả về và các ngoại lệ.
- NÊN đặt bình luận tài liệu trước các chú thích siêu dữ liệu (metadata annotations).

##### Markdown

- TRÁNH sử dụng markdown quá mức.
- TRÁNH sử dụng HTML để định dạng.
- ƯU TIÊN sử dụng hàng rào dấu backtick cho các khối mã.

##### Cách viết

- ƯU TIÊN sự ngắn gọn.
- TRÁNH các từ viết tắt trừ khi chúng rõ ràng.
- ƯU TIÊN sử dụng "this" thay vì "the" để chỉ một thể hiện của thành viên.

#### Sử dụng

##### Thư viện

- NÊN sử dụng chuỗi trong các chỉ thị `part of`.
- KHÔNG NÊN import các thư viện nằm trong thư mục `src` của một gói khác.
- KHÔNG NÊN cho phép một đường dẫn import đi vào hoặc ra khỏi `lib`.
- ƯU TIÊN các đường dẫn import tương đối.

##### Null

- KHÔNG NÊN khởi tạo biến một cách tường minh thành `null`.
- KHÔNG NÊN sử dụng giá trị mặc định tường minh là `null`.
- KHÔNG NÊN sử dụng `true` hoặc `false` trong các phép toán so sánh bằng.
- TRÁNH các biến `late` nếu bạn cần kiểm tra xem chúng đã được khởi tạo hay chưa.
- CÂN NHẮC thăng cấp kiểu (type promotion) hoặc các mẫu kiểm tra null để sử dụng các kiểu có thể null.

##### Chuỗi

- NÊN sử dụng các chuỗi liền kề để nối các chuỗi ký tự.
- ƯU TIÊN sử dụng nội suy để kết hợp chuỗi và giá trị.
- TRÁNH sử dụng dấu ngoặc nhọn trong nội suy khi không cần thiết.

##### Tập hợp (Collections)

- NÊN sử dụng các collection literal khi có thể.
- KHÔNG NÊN sử dụng `.length` để xem một tập hợp có rỗng hay không.
- TRÁNH sử dụng `Iterable.forEach()` với một hàm chữ (function literal).
- KHÔNG NÊN sử dụng `List.from()` trừ khi bạn có ý định thay đổi kiểu của kết quả.
- NÊN sử dụng `whereType()` để lọc một tập hợp theo kiểu.
- KHÔNG NÊN sử dụng `cast()` khi một thao tác gần đó sẽ thực hiện được.
- TRÁNH sử dụng `cast()`.

##### Hàm

- NÊN sử dụng khai báo hàm để liên kết một hàm với một tên.
- KHÔNG NÊN tạo một lambda khi một tear-off sẽ thực hiện được.

##### Biến

- NÊN tuân theo một quy tắc nhất quán cho `var` và `final` trên các biến cục bộ.
- TRÁNH lưu trữ những gì bạn có thể tính toán.

##### Thành viên

- KHÔNG NÊN bọc một trường trong một getter và setter một cách không cần thiết.
- ƯU TIÊN sử dụng một trường `final` để tạo một thuộc tính chỉ đọc.
- CÂN NHẮC sử dụng `=>` cho các thành viên đơn giản.
- KHÔNG NÊN sử dụng `this.` trừ khi để chuyển hướng đến một hàm tạo có tên hoặc để tránh che bóng (shadowing).
- NÊN khởi tạo các trường tại khai báo của chúng khi có thể.

##### Hàm tạo (Constructors)

- NÊN sử dụng các tham số khởi tạo (initializing formals) khi có thể.
- KHÔNG NÊN sử dụng `late` khi một danh sách khởi tạo hàm tạo (constructor initializer list) sẽ thực hiện được.
- NÊN sử dụng `;` thay vì `{}` cho các thân hàm tạo rỗng.
- KHÔNG NÊN sử dụng `new`.
- KHÔNG NÊN sử dụng `const` một cách dư thừa.

##### Xử lý lỗi

- TRÁNH các khối `catch` không có mệnh đề `on`.
- KHÔNG NÊN loại bỏ các lỗi từ các khối `catch` không có mệnh đề `on`.
- NÊN chỉ ném các đối tượng triển khai `Error` cho các lỗi lập trình.
- KHÔNG NÊN bắt `Error` hoặc các kiểu triển khai nó một cách tường minh.
- NÊN sử dụng `rethrow` để ném lại một ngoại lệ đã bắt.

##### Bất đồng bộ (Asynchrony)

- ƯU TIÊN async/await hơn là sử dụng các future thô.
- KHÔNG NÊN sử dụng `async` khi nó không có tác dụng hữu ích.
- CÂN NHẮC sử dụng các phương thức bậc cao hơn để biến đổi một stream.
- TRÁNH sử dụng Completer trực tiếp.
- NÊN kiểm tra `Future<T>` khi phân biệt một `FutureOr<T>` mà đối số kiểu của nó có thể là `Object`.

#### Thiết kế

##### Tên

- NÊN sử dụng các thuật ngữ một cách nhất quán.
- TRÁNH các từ viết tắt.
- ƯU TIÊN đặt danh từ mô tả nhất ở cuối cùng.
- CÂN NHẮC làm cho mã đọc giống như một câu văn.
- ƯU TIÊN một cụm danh từ cho một thuộc tính hoặc biến không phải boolean.
- ƯU TIÊN một cụm động từ không mệnh lệnh cho một thuộc tính hoặc biến boolean.
- CÂN NHẮC bỏ qua động từ cho một tham số boolean có tên.
- ƯU TIÊN tên "tích cực" cho một thuộc tính hoặc biến boolean.
- ƯU TIÊN một cụm động từ mệnh lệnh cho một hàm hoặc phương thức có mục đích chính là một tác dụng phụ.
- ƯU TIÊN một cụm danh từ hoặc cụm động từ không mệnh lệnh cho một hàm hoặc phương thức nếu việc trả về một giá trị là mục đích chính của nó.
- CÂN NHẮC một cụm động từ mệnh lệnh cho một hàm hoặc phương thức nếu bạn muốn thu hút sự chú ý đến công việc mà nó thực hiện.
- TRÁNH bắt đầu tên phương thức bằng `get`.
- ƯU TIÊN đặt tên một phương thức là `to...()` nếu nó sao chép trạng thái của đối tượng sang một đối tượng mới.
- ƯU TIÊN đặt tên một phương thức là `as...()` nếu nó trả về một biểu diễn khác được hỗ trợ bởi đối tượng ban đầu.
- TRÁNH mô tả các tham số trong tên của hàm hoặc phương thức.
- NÊN tuân theo các quy ước ghi nhớ hiện có khi đặt tên cho các tham số kiểu.

##### Thư viện

- ƯU TIÊN làm cho các khai báo trở nên riêng tư (private).
- CÂN NHẮC khai báo nhiều lớp trong cùng một thư viện.

##### Lớp và mixin

- TRÁNH định nghĩa một lớp trừu tượng một thành viên khi một hàm đơn giản sẽ thực hiện được.
- TRÁNH định nghĩa một lớp chỉ chứa các thành viên tĩnh.
- TRÁNH kế thừa một lớp không được thiết kế để được phân lớp.
- NÊN sử dụng các bổ từ lớp (class modifiers) để kiểm soát xem lớp của bạn có thể được kế thừa hay không.
- TRÁNH triển khai một lớp không được thiết kế để làm giao diện (interface).
- NÊN sử dụng các bổ từ lớp để kiểm soát xem lớp của bạn có thể là một giao diện hay không.
- ƯU TIÊN định nghĩa một `mixin` thuần túy hoặc một `class` thuần túy hơn là một `mixin class`.

##### Hàm tạo

- CÂN NHẮC làm cho hàm tạo của bạn là `const` nếu lớp hỗ trợ nó.

##### Thành viên

- ƯU TIÊN làm cho các trường và các biến cấp cao nhất là `final`.
- NÊN sử dụng các getter cho các hoạt động về mặt khái niệm là truy cập các thuộc tính.
- NÊN sử dụng các setter cho các hoạt động về mặt khái niệm là thay đổi các thuộc tính.
- KHÔNG NÊN định nghĩa một setter mà không có một getter tương ứng.
- TRÁNH sử dụng kiểm tra kiểu thời gian chạy để giả mạo việc nạp chồng (overloading).
- TRÁNH các trường `late final` công khai không có trình khởi tạo.
- TRÁNH trả về các kiểu `Future`, `Stream`, và collection có thể null.
- TRÁNH trả về `this` từ các phương thức chỉ để kích hoạt một giao diện fluent.

##### Kiểu

- NÊN chú thích kiểu cho các biến không có trình khởi tạo.
- NÊN chú thích kiểu cho các trường và các biến cấp cao nhất nếu kiểu không rõ ràng.
- KHÔNG NÊN chú thích kiểu một cách dư thừa cho các biến cục bộ đã được khởi tạo.
- NÊN chú thích các kiểu trả về trên các khai báo hàm.
- NÊN chú thích các kiểu tham số trên các khai báo hàm.
- KHÔNG NÊN chú thích các kiểu tham số được suy luận trên các biểu thức hàm.
- KHÔNG NÊN chú thích kiểu cho các tham số khởi tạo (initializing formals).
- NÊN viết các đối số kiểu trên các lệnh gọi generic không được suy luận.
- KHÔNG NÊN viết các đối số kiểu trên các lệnh gọi generic được suy luận.
- TRÁNH viết các kiểu generic không đầy đủ.
- NÊN chú thích bằng `dynamic` thay vì để cho việc suy luận thất bại.
- ƯU TIÊN các chữ ký trong các chú thích kiểu hàm.
- KHÔNG NÊN chỉ định một kiểu trả về cho một setter.
- KHÔNG NÊN sử dụng cú pháp typedef cũ.
- ƯU TIÊN các kiểu hàm nội tuyến hơn là typedefs.
- ƯU TIÊN sử dụng cú pháp kiểu hàm cho các tham số.
- TRÁNH sử dụng `dynamic` trừ khi bạn muốn vô hiệu hóa việc kiểm tra tĩnh.
- NÊN sử dụng `Future<void>` làm kiểu trả về của các thành viên bất đồng bộ không tạo ra giá trị.
- TRÁNH sử dụng `FutureOr<T>` làm kiểu trả về.

##### Tham số

- TRÁNH các tham số boolean vị trí.
- TRÁNH các tham số vị trí tùy chọn nếu người dùng có thể muốn bỏ qua các tham số trước đó.
- TRÁNH các tham số bắt buộc chấp nhận một giá trị đặc biệt "không có đối số".
- NÊN sử dụng các tham số bắt đầu bao gồm và kết thúc loại trừ để chấp nhận một phạm vi.

##### So sánh bằng

- NÊN ghi đè `hashCode` nếu bạn ghi đè `==`.
- NÊN làm cho toán tử `==` của bạn tuân theo các quy tắc toán học của sự bằng nhau.
- TRÁNH định nghĩa sự bằng nhau tùy chỉnh cho các lớp có thể thay đổi (mutable).
- KHÔNG NÊN làm cho tham số của `==` có thể null.

---

## Các khuyến nghị về kiến trúc Flutter

Trang này trình bày các phương pháp hay nhất về kiến trúc, tại sao chúng quan trọng, và
liệu chúng tôi có khuyến nghị chúng cho ứng dụng Flutter của bạn hay không.
Bạn nên xem những khuyến nghị này như là khuyến nghị,
chứ không phải là các quy tắc cứng nhắc, và bạn nên
điều chỉnh chúng cho phù hợp với các yêu cầu riêng của ứng dụng của bạn.

Các phương pháp hay nhất trên trang này có một mức độ ưu tiên,
phản ánh mức độ mà nhóm Flutter khuyến nghị nó.

- **Rất khuyến khích:** Bạn nên luôn triển khai khuyến nghị này nếu
  bạn đang bắt đầu xây dựng một ứng dụng mới. Bạn nên cân nhắc mạnh mẽ
  việc tái cấu trúc một ứng dụng hiện có để triển khai thực hành này trừ khi làm như vậy sẽ
  xung đột cơ bản với cách tiếp cận hiện tại của bạn.
- **Khuyến khích**: Thực hành này có khả năng sẽ cải thiện ứng dụng của bạn.
- **Tùy trường hợp**: Thực hành này có thể cải thiện ứng dụng của bạn trong một số trường hợp nhất định.

### Tách biệt các mối quan tâm (Separation of concerns)

Bạn nên tách ứng dụng của mình thành một lớp UI và một lớp dữ liệu. Trong các lớp đó, bạn nên tách logic thành các lớp theo trách nhiệm.

#### Sử dụng các lớp dữ liệu và UI được xác định rõ ràng.

**Rất khuyến khích**

Tách biệt các mối quan tâm là nguyên tắc kiến trúc quan trọng nhất.
Lớp dữ liệu cung cấp dữ liệu ứng dụng cho phần còn lại của ứng dụng, và chứa hầu hết logic nghiệp vụ trong ứng dụng của bạn.
Lớp UI hiển thị dữ liệu ứng dụng và lắng nghe các sự kiện người dùng từ người dùng. Lớp UI chứa các lớp riêng biệt cho logic UI và các widget.

#### Sử dụng mẫu repository trong lớp dữ liệu.

**Rất khuyến khích**

Mẫu repository là một mẫu thiết kế phần mềm giúp cô lập logic truy cập dữ liệu khỏi phần còn lại của ứng dụng.
Nó tạo ra một lớp trừu tượng giữa logic nghiệp vụ của ứng dụng và các cơ chế lưu trữ dữ liệu cơ bản (cơ sở dữ liệu, API, hệ thống tệp, v.v.).
Trong thực tế, điều này có nghĩa là tạo ra các lớp Repository và các lớp Service.

#### Sử dụng ViewModel và View trong lớp UI. (MVVM)

**Rất khuyến khích**

Tách biệt các mối quan tâm là nguyên tắc kiến trúc quan trọng nhất.
Sự tách biệt cụ thể này làm cho mã của bạn ít bị lỗi hơn nhiều vì các widget của bạn vẫn "ngu ngốc" (dumb).

#### Sử dụng `ChangeNotifier` và `Listenable` để xử lý các cập nhật widget.

**Tùy trường hợp**

> Có nhiều lựa chọn để xử lý quản lý trạng thái, và cuối cùng quyết định phụ thuộc vào sở thích cá nhân.

API `ChangeNotifier` là một phần của Flutter SDK, và là một cách tiện lợi để các widget của bạn quan sát các thay đổi trong ViewModel của bạn.

#### Không đặt logic trong các widget.

**Rất khuyến khích**

Logic nên được đóng gói trong các phương thức trên ViewModel. Logic duy nhất mà một view nên chứa là:

- Các câu lệnh if đơn giản để hiển thị và ẩn các widget dựa trên một cờ hoặc trường có thể null trong ViewModel
- Logic hoạt ảnh dựa vào widget để tính toán
- Logic bố cục dựa trên thông tin thiết bị, như kích thước màn hình hoặc hướng.
- Logic định tuyến đơn giản

#### Sử dụng một lớp domain.

**Tùy trường hợp**

> Sử dụng trong các ứng dụng có yêu cầu logic phức tạp.

Một lớp domain chỉ cần thiết nếu ứng dụng của bạn có các yêu cầu logic cực kỳ phức tạp làm lộn xộn các ViewModel của bạn,
hoặc nếu bạn thấy mình lặp lại logic trong các ViewModel.
Trong các ứng dụng rất lớn, các use-case là hữu ích, nhưng trong hầu hết các ứng dụng, chúng thêm vào sự phức tạp không cần thiết.

### Xử lý dữ liệu

Xử lý dữ liệu một cách cẩn thận làm cho mã của bạn dễ hiểu hơn, ít bị lỗi hơn, và
ngăn chặn dữ liệu bị định dạng sai hoặc không mong muốn được tạo ra.

#### Sử dụng luồng dữ liệu một chiều.

**Rất khuyến khích**

Các cập nhật dữ liệu chỉ nên chảy từ lớp dữ liệu đến lớp UI.
Các tương tác trong lớp UI được gửi đến lớp dữ liệu nơi chúng được xử lý.

#### Sử dụng `Command` để xử lý các sự kiện từ tương tác của người dùng.

**Khuyến khích**

Các Command ngăn chặn các lỗi kết xuất trong ứng dụng của bạn, và chuẩn hóa cách lớp UI gửi các sự kiện đến lớp dữ liệu.

#### Sử dụng các mô hình dữ liệu bất biến (immutable).

**Rất khuyến khích**

Dữ liệu bất biến là rất quan trọng trong việc đảm bảo rằng bất kỳ thay đổi cần thiết nào chỉ xảy ra ở đúng nơi, thường là lớp dữ liệu hoặc lớp domain.
Bởi vì các đối tượng bất biến không thể được sửa đổi sau khi tạo, bạn phải tạo một thể hiện mới để phản ánh các thay đổi.
Quá trình này ngăn chặn các cập nhật vô tình trong lớp UI và hỗ trợ một luồng dữ liệu một chiều, rõ ràng.

#### Sử dụng freezed hoặc built_value để tạo các mô hình dữ liệu bất biến.

**Khuyến khích**

Bạn có thể sử dụng các gói để giúp tạo ra các chức năng hữu ích trong các mô hình dữ liệu của mình, `freezed` hoặc `built_value`.
Chúng có thể tạo ra các phương thức mô hình phổ biến như tuần tự hóa/giải tuần tự hóa JSON, kiểm tra bằng nhau sâu và các phương thức sao chép.
Các gói tạo mã này có thể thêm thời gian xây dựng đáng kể vào các ứng dụng của bạn nếu bạn có nhiều mô hình.

#### Tạo các mô hình API và mô hình domain riêng biệt.

**Tùy trường hợp**

> Sử dụng trong các ứng dụng lớn.

Sử dụng các mô hình riêng biệt làm tăng sự dài dòng, nhưng ngăn chặn sự phức tạp trong các ViewModel và use-case.

### Cấu trúc ứng dụng

Mã được tổ chức tốt mang lại lợi ích cho cả sức khỏe của chính ứng dụng và nhóm làm việc trên mã.

#### Sử dụng dependency injection (tiêm phụ thuộc).

**Rất khuyến khích**

Dependency injection ngăn ứng dụng của bạn có các đối tượng có thể truy cập toàn cục, điều này làm cho mã của bạn ít bị lỗi hơn.
Chúng tôi khuyên bạn nên sử dụng gói `provider` để xử lý dependency injection.

#### Sử dụng `go_router` để điều hướng.

**Khuyến khích**

Go_router là cách được ưa thích để viết 90% các ứng dụng Flutter.
Có một số trường hợp sử dụng cụ thể mà go_router không giải quyết được,
trong trường hợp đó bạn có thể sử dụng `Flutter Navigator API` trực tiếp hoặc thử các gói khác được tìm thấy trên `pub.dev`.

#### Sử dụng các quy ước đặt tên được tiêu chuẩn hóa cho các lớp, tệp và thư mục.

**Khuyến khích**

Chúng tôi khuyên bạn nên đặt tên các lớp theo thành phần kiến trúc mà chúng đại diện.
Ví dụ, bạn có thể có các lớp sau:

- HomeViewModel
- HomeScreen
- UserRepository
- ClientApiService

Để rõ ràng, chúng tôi không khuyến nghị sử dụng các tên có thể bị nhầm lẫn với các đối tượng từ Flutter SDK.
Ví dụ, bạn nên đặt các widget được chia sẻ của mình trong một thư mục có tên `ui/core/`,
thay vì một thư mục có tên `/widgets`.

#### Sử dụng các lớp repository trừu tượng

**Rất khuyến khích**

Các lớp repository là nguồn chân lý cho tất cả dữ liệu trong ứng dụng của bạn,
và tạo điều kiện giao tiếp với các API bên ngoài.
Tạo các lớp repository trừu tượng cho phép bạn tạo các triển khai khác nhau,
có thể được sử dụng cho các môi trường ứng dụng khác nhau, chẳng hạn như "development" và "staging".

### Kiểm thử

Các thực hành kiểm thử tốt làm cho ứng dụng của bạn linh hoạt.
Nó cũng làm cho việc thêm logic mới và UI mới trở nên đơn giản và ít rủi ro.

#### Kiểm thử các thành phần kiến trúc một cách riêng biệt, và cùng nhau.

**Rất khuyến khích**

- Viết các unit test cho mỗi lớp service, repository và ViewModel. Các bài kiểm thử này nên kiểm tra logic của mỗi phương thức một cách riêng lẻ.
- Viết các widget test cho các view. Kiểm thử định tuyến và dependency injection là đặc biệt quan trọng.

#### Tạo các đối tượng giả (fakes) để kiểm thử (và viết mã tận dụng các đối tượng giả.)

**Rất khuyến khích**

Các đối tượng giả không quan tâm đến hoạt động bên trong của bất kỳ phương thức nào cho trước
mà chúng quan tâm đến đầu vào và đầu ra. Nếu bạn ghi nhớ điều này trong khi viết mã ứng dụng,
bạn buộc phải viết các hàm và lớp mô-đun, nhẹ với đầu vào và đầu ra được xác định rõ ràng.
