---
description: "Tiêu chuẩn tạo tài liệu và nội dung"
applyTo: "**/*.md"
---

## Quy tắc Nội dung Markdown

Các quy tắc nội dung markdown sau đây được thực thi trong các trình xác thực:

1.  **Tiêu đề**: Sử dụng các cấp độ tiêu đề phù hợp (H2, H3, v.v.) để cấu trúc nội dung của bạn. Không sử dụng tiêu đề H1, vì tiêu đề này sẽ được tạo dựa trên tiêu đề chính.
2.  **Danh sách**: Sử dụng dấu đầu dòng hoặc danh sách được đánh số cho danh sách. Đảm bảo thụt lề và khoảng cách phù hợp.
3.  **Khối mã**: Sử dụng các khối mã có rào cản cho các đoạn mã. Chỉ định ngôn ngữ để tô sáng cú pháp.
4.  **Liên kết**: Sử dụng cú pháp markdown phù hợp cho các liên kết. Đảm bảo rằng các liên kết hợp lệ và có thể truy cập được.
5.  **Hình ảnh**: Sử dụng cú pháp markdown phù hợp cho hình ảnh. Bao gồm văn bản thay thế (alt text) để hỗ trợ khả năng truy cập.
6.  **Bảng**: Sử dụng bảng markdown cho dữ liệu dạng bảng. Đảm bảo định dạng và căn chỉnh phù hợp.
7.  **Độ dài dòng**: Giới hạn độ dài dòng ở 400 ký tự để dễ đọc.
8.  **Khoảng trắng**: Sử dụng khoảng trắng thích hợp để phân tách các phần và cải thiện khả năng đọc.
9.  **Front Matter**: Bao gồm YAML front matter ở đầu tệp với các trường siêu dữ liệu bắt buộc.

## Định dạng và Cấu trúc

Thực hiện theo các hướng dẫn sau để định dạng và cấu trúc nội dung markdown của bạn:

- **Tiêu đề**: Sử dụng `##` cho H2 và `###` cho H3. Đảm bảo rằng các tiêu đề được sử dụng theo cách phân cấp. Đề xuất cấu trúc lại nếu nội dung bao gồm H4, và đề xuất mạnh mẽ hơn cho H5.
- **Danh sách**: Sử dụng `-` cho các dấu đầu dòng và `1.` cho các danh sách được đánh số. Thụt lề các danh sách lồng nhau bằng hai dấu cách.
- **Khối mã**: Sử dụng ba dấu backtick (`) để tạo các khối mã có rào cản. Chỉ định ngôn ngữ sau các dấu backtick mở để tô sáng cú pháp (ví dụ: `csharp`).
- **Liên kết**: Sử dụng `[văn bản liên kết](URL)` cho các liên kết. Đảm bảo rằng văn bản liên kết mang tính mô tả và URL hợp lệ.
- **Hình ảnh**: Sử dụng `![văn bản thay thế](URL hình ảnh)` cho hình ảnh. Bao gồm một mô tả ngắn gọn về hình ảnh trong văn bản thay thế.
- **Bảng**: Sử dụng `|` để tạo bảng. Đảm bảo rằng các cột được căn chỉnh đúng cách và có bao gồm các tiêu đề.
- **Độ dài dòng**: Ngắt dòng ở 80 ký tự để cải thiện khả năng đọc. Sử dụng ngắt dòng mềm cho các đoạn văn dài.
- **Khoảng trắng**: Sử dụng các dòng trống để phân tách các phần và cải thiện khả năng đọc. Tránh sử dụng khoảng trắng quá nhiều.

## Yêu cầu Xác thực

Đảm bảo tuân thủ các yêu cầu xác thực sau:

- **Front Matter**: Bao gồm các trường sau trong YAML front matter:

  - `post_title`: Tiêu đề của bài đăng.
  - `author1`: Tác giả chính của bài đăng.
  - `post_slug`: Slug URL cho bài đăng.
  - `microsoft_alias`: Bí danh Microsoft của tác giả.
  - `featured_image`: URL của hình ảnh nổi bật.
  - `categories`: Các danh mục cho bài đăng. Các danh mục này phải từ danh sách trong /categories.txt.
  - `tags`: Các thẻ cho bài đăng.
  - `ai_note`: Cho biết liệu AI có được sử dụng trong việc tạo bài đăng hay không.
  - `summary`: Một bản tóm tắt ngắn gọn của bài đăng. Đề xuất một bản tóm tắt dựa trên nội dung khi có thể.
  - `post_date`: Ngày xuất bản của bài đăng.

- **Quy tắc Nội dung**: Đảm bảo rằng nội dung tuân theo các quy tắc nội dung markdown được chỉ định ở trên.
- **Định dạng**: Đảm bảo rằng nội dung được định dạng và cấu trúc đúng theo các hướng dẫn.
- **Xác thực**: Chạy các công cụ xác thực để kiểm tra sự tuân thủ các quy tắc và hướng dẫn.
