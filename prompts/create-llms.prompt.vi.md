---
mode: "agent"
description: "Tạo một tệp llms.txt từ đầu dựa trên cấu trúc kho chứa theo đặc tả llms.txt tại https://llmstxt.org/"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# Tạo tệp LLMs.txt từ cấu trúc kho chứa

Tạo một tệp `llms.txt` mới từ đầu trong thư mục gốc của kho chứa theo đặc tả chính thức của llms.txt tại https://llmstxt.org/. Tệp này cung cấp hướng dẫn cấp cao cho các mô hình ngôn ngữ lớn (LLM) về nơi tìm nội dung liên quan để hiểu mục đích và đặc tả của kho chứa.

## Chỉ thị chính

Tạo một tệp `llms.txt` toàn diện, đóng vai trò là điểm khởi đầu để các LLM hiểu và điều hướng kho chứa một cách hiệu quả. Tệp phải tuân thủ đặc tả llms.txt và được tối ưu hóa cho việc sử dụng của LLM trong khi vẫn dễ đọc đối với con người.

## Giai đoạn phân tích và lập kế hoạch

Trước khi tạo tệp `llms.txt`, bạn phải hoàn thành một phân tích kỹ lưỡng:

### Bước 1: Xem lại đặc tả llms.txt

- Xem lại đặc tả chính thức tại https://llmstxt.org/ để đảm bảo tuân thủ đầy đủ
- Hiểu cấu trúc định dạng và các hướng dẫn bắt buộc
- Lưu ý các yêu cầu cấu trúc markdown cụ thể

### Bước 2: Phân tích cấu trúc kho chứa

- Kiểm tra toàn bộ cấu trúc kho chứa bằng các công cụ thích hợp
- Xác định mục đích chính và phạm vi của kho chứa
- Lập danh mục tất cả các thư mục quan trọng và mục đích của chúng
- Liệt kê các tệp chính có giá trị cho việc hiểu của LLM

### Bước 3: Khám phá nội dung

- Xác định các tệp README và vị trí của chúng
- Tìm các tệp tài liệu (`.md` trong `/docs/`, `/spec/`, v.v.)
- Xác định vị trí các tệp đặc tả và mục đích của chúng
- Khám phá các tệp cấu hình và sự liên quan của chúng
- Tìm các tệp ví dụ và mẫu mã
- Xác định bất kỳ cấu trúc tài liệu hiện có nào

### Bước 4: Tạo kế hoạch triển khai

Dựa trên phân tích của bạn, hãy tạo một kế hoạch có cấu trúc bao gồm:

- Tóm tắt mục đích và phạm vi của kho chứa
- Danh sách các tệp thiết yếu được sắp xếp theo thứ tự ưu tiên để LLM hiểu
- Các tệp phụ cung cấp ngữ cảnh bổ sung
- Cấu trúc tổ chức cho tệp llms.txt

## Yêu cầu triển khai

### Tuân thủ định dạng

Tệp `llms.txt` phải tuân theo cấu trúc chính xác này theo đặc tả:

1.  **Tiêu đề H1**: Một dòng duy nhất với tên kho chứa/dự án (bắt buộc)
2.  **Tóm tắt dạng Blockquote**: Mô tả ngắn gọn ở định dạng blockquote (tùy chọn nhưng được khuyến nghị)
3.  **Chi tiết bổ sung**: Không hoặc nhiều phần markdown không có tiêu đề để cung cấp ngữ cảnh
4.  **Các mục danh sách tệp**: Không hoặc nhiều mục H2 chứa danh sách liên kết dạng markdown

### Yêu cầu về nội dung

#### Các yếu tố bắt buộc

- **Tên dự án**: Tiêu đề rõ ràng, mô tả dưới dạng H1
- **Tóm tắt**: Blockquote ngắn gọn giải thích mục đích của kho chứa
- **Các tệp chính**: Các tệp thiết yếu được tổ chức theo danh mục (các mục H2)

#### Định dạng liên kết tệp

Mỗi liên kết tệp phải tuân theo: `[tên-mô-tả](url-tương-đối): mô tả tùy chọn`

#### Tổ chức các mục

Tổ chức các tệp thành các mục H2 hợp lý như:

- **Documentation**: Các tệp tài liệu cốt lõi
- **Specifications**: Các đặc tả kỹ thuật và yêu cầu
- **Examples**: Mã mẫu và ví dụ sử dụng
- **Configuration**: Các tệp cài đặt và cấu hình
- **Optional**: Các tệp phụ (có ý nghĩa đặc biệt - có thể bỏ qua để có ngữ cảnh ngắn hơn)

### Nguyên tắc về nội dung

#### Ngôn ngữ và phong cách

- Sử dụng ngôn ngữ ngắn gọn, rõ ràng, không mơ hồ
- Tránh thuật ngữ chuyên ngành mà không giải thích
- Viết cho cả người đọc là con người và LLM
- Cụ thể và cung cấp thông tin trong các mô tả

#### Tiêu chí lựa chọn tệp

Bao gồm các tệp:

- Giải thích mục đích và phạm vi của kho chứa
- Cung cấp tài liệu kỹ thuật thiết yếu
- Hiển thị các ví dụ và mẫu sử dụng
- Xác định các giao diện và đặc tả
- Chứa hướng dẫn cấu hình và cài đặt

Loại trừ các tệp:

- Chỉ là chi tiết triển khai
- Chứa thông tin dư thừa
- Là các tạo phẩm xây dựng hoặc nội dung được tạo tự động
- Không liên quan đến việc hiểu dự án

## Các bước thực hiện

### Bước 1: Phân tích kho chứa

1.  Kiểm tra toàn bộ cấu trúc kho chứa
2.  Đọc tệp README.md chính để hiểu dự án
3.  Xác định tất cả các thư mục và tệp tài liệu
4.  Lập danh mục các tệp đặc tả và mục đích của chúng
5.  Tìm các tệp ví dụ và tệp cấu hình

### Bước 2: Lập kế hoạch nội dung

1.  Xác định tuyên bố mục đích chính
2.  Viết một bản tóm tắt ngắn gọn cho blockquote
3.  Nhóm các tệp đã xác định vào các danh mục hợp lý
4.  Ưu tiên các tệp theo tầm quan trọng để LLM hiểu
5.  Tạo mô tả cho mỗi liên kết tệp

### Bước 3: Tạo tệp

1.  Tạo tệp `llms.txt` trong thư mục gốc của kho chứa
2.  Tuân theo đặc tả định dạng chính xác
3.  Bao gồm tất cả các mục bắt buộc
4.  Sử dụng định dạng markdown phù hợp
5.  Đảm bảo tất cả các liên kết là đường dẫn tương đối hợp lệ

### Bước 4: Xác thực

1.  Xác minh sự tuân thủ với đặc tả tại https://llmstxt.org/
2.  Kiểm tra rằng tất cả các liên kết đều hợp lệ và có thể truy cập
3.  Đảm bảo tệp đóng vai trò là một công cụ điều hướng LLM hiệu quả
4.  Xác nhận tệp có thể đọc được bởi cả người và máy

## Đảm bảo chất lượng

### Xác thực định dạng

- ✅ Tiêu đề H1 với tên dự án
- ✅ Tóm tắt dạng Blockquote (nếu có)
- ✅ Các mục H2 cho danh sách tệp
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
- ✅ Triển khai các mục tùy chọn một cách thích hợp
- ✅ Tệp được đặt tại thư mục gốc của kho chứa (`/llms.txt`)

## Mẫu cấu trúc ví dụ

```txt
# [Tên kho chứa]

> [Mô tả ngắn gọn về mục đích và phạm vi của kho chứa]

[Các đoạn văn bản ngữ cảnh bổ sung tùy chọn không có tiêu đề]

## Documentation

- [README chính](README.md): Tài liệu chính của dự án và hướng dẫn bắt đầu
- [Hướng dẫn đóng góp](CONTRIBUTING.md): Nguyên tắc để đóng góp cho dự án
- [Quy tắc ứng xử](CODE_OF_CONDUCT.md): Nguyên tắc và kỳ vọng của cộng đồng

## Specifications

- [Đặc tả kỹ thuật](spec/technical-spec.md): Yêu cầu và ràng buộc kỹ thuật chi tiết
- [Đặc tả API](spec/api-spec.md): Định nghĩa giao diện và hợp đồng dữ liệu

## Examples

- [Ví dụ cơ bản](examples/basic-usage.md): Minh họa sử dụng đơn giản
- [Ví dụ nâng cao](examples/advanced-usage.md): Các mẫu triển khai phức tạp

## Configuration

- [Hướng dẫn cài đặt](docs/setup.md): Hướng dẫn cài đặt và cấu hình
- [Hướng dẫn triển khai](docs/deployment.md): Hướng dẫn triển khai lên môi trường sản phẩm

## Optional

- [Tài liệu kiến trúc](docs/architecture.md): Kiến trúc hệ thống chi tiết
- [Quyết định thiết kế](docs/decisions.md): Ghi chép lịch sử các quyết định thiết kế
```

## Tiêu chí thành công

Tệp `llms.txt` được tạo ra phải:

1.  Giúp LLM nhanh chóng hiểu được mục đích của kho chứa
2.  Cung cấp điều hướng rõ ràng đến các tài liệu thiết yếu
3.  Tuân thủ chính xác đặc tả chính thức của llms.txt
4.  Toàn diện nhưng ngắn gọn
5.  Phục vụ hiệu quả cho cả người đọc là con người và máy
6.  Bao gồm tất cả các tệp quan trọng để hiểu dự án
7.  Sử dụng ngôn ngữ rõ ràng, không mơ hồ trong toàn bộ tệp
8.  Tổ chức nội dung một cách hợp lý để dễ dàng tiếp thu
