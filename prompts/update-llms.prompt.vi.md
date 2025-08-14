---
mode: "agent"
description: "Cập nhật tệp llms.txt trong thư mục gốc để phản ánh các thay đổi trong tài liệu hoặc thông số kỹ thuật theo đặc tả llms.txt tại https://llmstxt.org/"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Cập nhật tệp LLMs.txt

Cập nhật tệp `llms.txt` hiện có trong thư mục gốc của kho lưu trữ để phản ánh các thay đổi trong tài liệu, thông số kỹ thuật hoặc cấu trúc kho lưu trữ. Tệp này cung cấp hướng dẫn cấp cao cho các mô hình ngôn ngữ lớn (LLM) về nơi tìm nội dung liên quan để hiểu mục đích và thông số kỹ thuật của kho lưu trữ.

## Chỉ thị chính

Cập nhật tệp `llms.txt` hiện có để duy trì tính chính xác và tuân thủ đặc tả llms.txt đồng thời phản ánh cấu trúc và nội dung hiện tại của kho lưu trữ. Tệp phải được tối ưu hóa cho việc sử dụng của LLM mà vẫn dễ đọc đối với con người.

## Giai đoạn Phân tích và Lập kế hoạch

Trước khi cập nhật tệp `llms.txt`, bạn phải hoàn thành một phân tích kỹ lưỡng:

### Bước 1: Xem xét tệp hiện tại và đặc tả

- Đọc tệp `llms.txt` hiện có để hiểu cấu trúc hiện tại
- Xem lại đặc tả chính thức tại https://llmstxt.org/ để đảm bảo tuân thủ liên tục
- Xác định các khu vực có thể cần cập nhật dựa trên các thay đổi của kho lưu trữ

### Bước 2: Phân tích cấu trúc kho lưu trữ

- Kiểm tra cấu trúc kho lưu trữ hiện tại bằng các công cụ thích hợp
- So sánh cấu trúc hiện tại với những gì được ghi lại trong tệp `llms.txt` hiện có
- Xác định các thư mục, tệp hoặc tài liệu mới cần được đưa vào
- Ghi lại bất kỳ tệp nào đã bị xóa hoặc di chuyển cần được cập nhật

### Bước 3: Khám phá nội dung và phát hiện thay đổi

- Xác định các tệp README mới và vị trí của chúng
- Tìm các tệp tài liệu mới (tệp `.md` trong `/docs/`, `/spec/`, v.v.)
- Xác định vị trí các tệp đặc tả mới và mục đích của chúng
- Khám phá các tệp cấu hình mới và sự liên quan của chúng
- Tìm các tệp ví dụ và mẫu mã mới
- Xác định bất kỳ thay đổi nào đối với cấu trúc tài liệu hiện có

### Bước 4: Tạo kế hoạch cập nhật

Dựa trên phân tích của bạn, hãy tạo một kế hoạch có cấu trúc bao gồm:

- Các thay đổi cần thiết để duy trì tính chính xác
- Các tệp mới sẽ được thêm vào llms.txt
- Các tham chiếu lỗi thời cần được xóa hoặc cập nhật
- Các cải tiến về tổ chức để duy trì sự rõ ràng

## Yêu cầu triển khai

### Tuân thủ định dạng

Tệp `llms.txt` được cập nhật phải duy trì chính xác cấu trúc này theo đặc tả:

1.  **Tiêu đề H1**: Một dòng duy nhất với tên kho lưu trữ/dự án (bắt buộc)
2.  **Tóm tắt trích dẫn khối (Blockquote)**: Mô tả ngắn gọn ở định dạng trích dẫn khối (tùy chọn nhưng được khuyến nghị)
3.  **Chi tiết bổ sung**: Không hoặc nhiều phần markdown không có tiêu đề để cung cấp ngữ cảnh
4.  **Các phần danh sách tệp**: Không hoặc nhiều phần H2 chứa danh sách liên kết markdown

### Yêu cầu về nội dung

#### Các yếu tố bắt buộc

- **Tên dự án**: Tiêu đề rõ ràng, mô tả dưới dạng H1
- **Tóm tắt**: Trích dẫn khối ngắn gọn giải thích mục đích của kho lưu trữ
- **Các tệp chính**: Các tệp thiết yếu được sắp xếp theo danh mục (các phần H2)

#### Định dạng liên kết tệp

Mỗi liên kết tệp phải tuân theo: `[tên-mô-tả](url-tương-đối): mô tả tùy chọn`

#### Tổ chức các phần

Sắp xếp các tệp thành các phần H2 hợp lý như:

- **Tài liệu (Documentation)**: Các tệp tài liệu cốt lõi
- **Thông số kỹ thuật (Specifications)**: Các yêu cầu và thông số kỹ thuật
- **Ví dụ (Examples)**: Mã mẫu và ví dụ sử dụng
- **Cấu hình (Configuration)**: Các tệp thiết lập và cấu hình
- **Tùy chọn (Optional)**: Các tệp phụ (có ý nghĩa đặc biệt - có thể bỏ qua để có ngữ cảnh ngắn hơn)

### Nguyên tắc về nội dung

#### Ngôn ngữ và phong cách

- Sử dụng ngôn ngữ ngắn gọn, rõ ràng, không mơ hồ
- Tránh thuật ngữ chuyên ngành mà không có giải thích
- Viết cho cả người đọc là con người và LLM
- Cụ thể và nhiều thông tin trong các mô tả

#### Tiêu chí lựa chọn tệp

Bao gồm các tệp:

- Giải thích mục đích và phạm vi của kho lưu trữ
- Cung cấp tài liệu kỹ thuật thiết yếu
- Hiển thị các ví dụ và mẫu sử dụng
- Xác định các giao diện và thông số kỹ thuật
- Chứa các hướng dẫn cấu hình và thiết lập

Loại trừ các tệp:

- Chỉ là chi tiết triển khai
- Chứa thông tin dư thừa
- Là các tạo phẩm xây dựng hoặc nội dung được tạo ra
- Không liên quan đến việc hiểu dự án

## Các bước thực hiện

### Bước 1: Phân tích trạng thái hiện tại

1.  Đọc kỹ tệp `llms.txt` hiện có
2.  Kiểm tra toàn bộ cấu trúc kho lưu trữ hiện tại
3.  So sánh các tham chiếu tệp hiện có với nội dung kho lưu trữ thực tế
4.  Xác định các tham chiếu lỗi thời, thiếu hoặc không chính xác
5.  Ghi lại bất kỳ vấn đề cấu trúc nào với tệp hiện tại

### Bước 2: Lập kế hoạch nội dung

1.  Xác định xem câu lệnh mục đích chính có cần cập nhật không
2.  Xem xét và cập nhật tóm tắt trích dẫn khối nếu cần
3.  Lập kế hoạch bổ sung cho các tệp và thư mục mới
4.  Lập kế hoạch xóa bỏ nội dung lỗi thời hoặc đã di chuyển
5.  Sắp xếp lại các phần nếu cần để rõ ràng hơn

### Bước 3: Cập nhật tệp

1.  Cập nhật tệp `llms.txt` hiện có trong thư mục gốc của kho lưu trữ
2.  Duy trì tuân thủ đặc tả định dạng chính xác
3.  Thêm các tham chiếu tệp mới với mô tả phù hợp
4.  Xóa hoặc cập nhật các tham chiếu lỗi thời
5.  Đảm bảo tất cả các liên kết là đường dẫn tương đối hợp lệ

### Bước 4: Xác thực

1.  Xác minh việc tuân thủ liên tục với đặc tả của https://llmstxt.org/
2.  Kiểm tra xem tất cả các liên kết có hợp lệ và có thể truy cập được không
3.  Đảm bảo tệp vẫn đóng vai trò là một công cụ điều hướng LLM hiệu quả
4.  Xác nhận tệp vẫn có thể đọc được bởi cả con người và máy

## Đảm bảo chất lượng

### Xác thực định dạng

- ✅ Tiêu đề H1 với tên dự án
- ✅ Tóm tắt trích dẫn khối (nếu có)
- ✅ Các phần H2 cho danh sách tệp
- ✅ Định dạng liên kết markdown phù hợp
- ✅ Không có liên kết bị hỏng hoặc không hợp lệ
- ✅ Định dạng nhất quán trong toàn bộ tệp

### Xác thực nội dung

- ✅ Ngôn ngữ rõ ràng, không mơ hồ
- ✅ Bao quát toàn diện các tệp thiết yếu
- ✅ Tổ chức nội dung hợp lý
- ✅ Mô tả tệp phù hợp
- ✅ Đóng vai trò là công cụ điều hướng LLM hiệu quả

### Tuân thủ đặc tả

- ✅ Tuân thủ chính xác định dạng của https://llmstxt.org/
- ✅ Sử dụng cấu trúc markdown bắt buộc
- ✅ Triển khai các phần tùy chọn một cách thích hợp
- ✅ Tệp được đặt tại thư mục gốc của kho lưu trữ (`/llms.txt`)

## Chiến lược cập nhật

### Quy trình thêm

Khi thêm nội dung mới:

1.  Xác định phần thích hợp cho các tệp mới
2.  Tạo tên rõ ràng, mô tả cho các liên kết
3.  Viết mô tả ngắn gọn nhưng đầy đủ thông tin
4.  Duy trì thứ tự theo bảng chữ cái hoặc logic trong các phần
5.  Cân nhắc xem có cần các phần mới cho các loại nội dung mới không

### Quy trình xóa

Khi xóa nội dung lỗi thời:

1.  Xác minh các tệp thực sự đã bị xóa hoặc di chuyển
2.  Kiểm tra xem các tệp đã di chuyển có nên được cập nhật thay vì xóa không
3.  Xóa toàn bộ các phần nếu chúng trở nên trống rỗng
4.  Cập nhật các tham chiếu chéo nếu cần

### Quy trình sắp xếp lại

Khi tái cấu trúc nội dung:

1.  Duy trì luồng logic từ tổng quát đến cụ thể
2.  Giữ tài liệu thiết yếu trong các phần chính
3.  Chuyển nội dung phụ sang phần "Tùy chọn" nếu thích hợp
4.  Đảm bảo tổ chức mới cải thiện khả năng điều hướng của LLM

Cấu trúc ví dụ cho `llms.txt`:

```txt
# [Tên kho lưu trữ]

> [Mô tả ngắn gọn về mục đích và phạm vi của kho lưu trữ]

[Các đoạn văn bản ngữ cảnh bổ sung tùy chọn không có tiêu đề]

## Tài liệu

- [README chính](README.md): Tài liệu chính của dự án và hướng dẫn bắt đầu
- [Hướng dẫn đóng góp](CONTRIBUTING.md): Nguyên tắc để đóng góp cho dự án
- [Quy tắc ứng xử](CODE_OF_CONDUCT.md): Nguyên tắc và kỳ vọng của cộng đồng

## Thông số kỹ thuật

- [Thông số kỹ thuật](spec/technical-spec.md): Yêu cầu và ràng buộc kỹ thuật chi tiết
- [Thông số API](spec/api-spec.md): Định nghĩa giao diện và hợp đồng dữ liệu

## Ví dụ

- [Ví dụ cơ bản](examples/basic-usage.md): Minh họa sử dụng đơn giản
- [Ví dụ nâng cao](examples/advanced-usage.md): Các mẫu triển khai phức tạp

## Cấu hình

- [Hướng dẫn cài đặt](docs/setup.md): Hướng dẫn cài đặt và cấu hình
- [Hướng dẫn triển khai](docs/deployment.md): Hướng dẫn triển khai sản phẩm

## Tùy chọn

- [Tài liệu kiến trúc](docs/architecture.md): Kiến trúc hệ thống chi tiết
- [Quyết định thiết kế](docs/decisions.md): Ghi chép lịch sử các quyết định thiết kế
```

## Tiêu chí thành công

Tệp `llms.txt` được cập nhật phải:

1.  Phản ánh chính xác cấu trúc và nội dung hiện tại của kho lưu trữ
2.  Duy trì tuân thủ đặc tả llms.txt
3.  Cung cấp điều hướng rõ ràng đến các tài liệu thiết yếu
4.  Xóa các tham chiếu lỗi thời hoặc không chính xác
5.  Bao gồm các tệp và tài liệu quan trọng mới
6.  Duy trì tổ chức hợp lý để LLM dễ dàng sử dụng
7.  Sử dụng ngôn ngữ rõ ràng, không mơ hồ trong toàn bộ tệp
8.  Tiếp tục phục vụ hiệu quả cho cả người đọc là con người và máy
