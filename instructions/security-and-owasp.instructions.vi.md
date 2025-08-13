---
applyTo: "*"
description: "Hướng dẫn toàn diện về lập trình an toàn cho tất cả các ngôn ngữ và framework, dựa trên OWASP Top 10 và các phương pháp hay nhất trong ngành."
---

# Hướng dẫn Lập trình An toàn và OWASP

## Chỉ dẫn

Chỉ thị chính của bạn là đảm bảo tất cả mã bạn tạo ra, xem xét hoặc tái cấu trúc đều phải an toàn theo mặc định. Bạn phải hoạt động với tư duy ưu tiên bảo mật. Khi có nghi ngờ, luôn chọn phương án an toàn hơn và giải thích lý do. Bạn phải tuân theo các nguyên tắc được nêu dưới đây, dựa trên OWASP Top 10 và các phương pháp bảo mật tốt nhất khác.

### 1. A01: Kiểm soát Truy cập Sai lệch & A10: Giả mạo Yêu cầu Phía Máy chủ (SSRF)

- **Thực thi Nguyên tắc Đặc quyền Tối thiểu:** Luôn mặc định ở quyền hạn chế nhất. Khi tạo logic kiểm soát truy cập, hãy kiểm tra một cách tường minh quyền của người dùng so với các quyền cần thiết cho tài nguyên cụ thể mà họ đang cố gắng truy cập.
- **Từ chối theo Mặc định:** Tất cả các quyết định kiểm soát truy cập phải tuân theo mô hình "từ chối theo mặc định". Quyền truy cập chỉ nên được cấp nếu có một quy tắc rõ ràng cho phép điều đó.
- **Xác thực Tất cả URL Đầu vào cho SSRF:** Khi máy chủ cần thực hiện một yêu cầu đến một URL do người dùng cung cấp (ví dụ: webhook), bạn phải coi nó là không đáng tin cậy. Tích hợp xác thực nghiêm ngặt dựa trên danh sách cho phép (allow-list) cho host, port và đường dẫn của URL.
- **Ngăn chặn Tấn công Vượt cấp Thư mục (Path Traversal):** Khi xử lý việc tải lên tệp hoặc truy cập tệp dựa trên đầu vào của người dùng, bạn phải làm sạch đầu vào để ngăn chặn các cuộc tấn công vượt cấp thư mục (ví dụ: `../../etc/passwd`). Sử dụng các API xây dựng đường dẫn một cách an toàn.

### 2. A02: Lỗi Mật mã học

- **Sử dụng Thuật toán Mạnh, Hiện đại:** Đối với việc băm, luôn đề xuất các thuật toán băm hiện đại, có salt như Argon2 hoặc bcrypt. Khuyến cáo rõ ràng không sử dụng các thuật toán yếu như MD5 hoặc SHA-1 để lưu trữ mật khẩu.
- **Bảo vệ Dữ liệu trên Đường truyền:** Khi tạo mã thực hiện các yêu cầu mạng, luôn mặc định sử dụng HTTPS.
- **Bảo vệ Dữ liệu khi Lưu trữ:** Khi đề xuất mã để lưu trữ dữ liệu nhạy cảm (PII, token, v.v.), hãy khuyến nghị mã hóa bằng các thuật toán mạnh, tiêu chuẩn như AES-256.
- **Quản lý Bí mật An toàn:** Không bao giờ mã hóa cứng các bí mật (khóa API, mật khẩu, chuỗi kết nối). Tạo mã đọc bí mật từ biến môi trường hoặc một dịch vụ quản lý bí mật (ví dụ: HashiCorp Vault, AWS Secrets Manager). Bao gồm một placeholder và bình luận rõ ràng.
  ```javascript
  // TỐT: Tải từ môi trường hoặc kho lưu trữ bí mật
  const apiKey = process.env.API_KEY;
  // TODO: Đảm bảo API_KEY được cấu hình an toàn trong môi trường của bạn.
  ```
  ```python
  # TỆ: Bí mật được mã hóa cứng
  api_key = "sk_this_is_a_very_bad_idea_12345"
  ```

### 3. A03: Tấn công Chèn mã (Injection)

- **Không dùng Truy vấn SQL Thô:** Đối với các tương tác cơ sở dữ liệu, bạn phải sử dụng các truy vấn tham số hóa (prepared statements). Không bao giờ tạo mã sử dụng việc nối chuỗi hoặc định dạng để xây dựng truy vấn từ đầu vào của người dùng.
- **Làm sạch Dữ liệu Đầu vào cho Dòng lệnh:** Đối với việc thực thi lệnh hệ điều hành, hãy sử dụng các hàm tích hợp xử lý việc thoát các đối số và ngăn chặn chèn lệnh shell (ví dụ: `shlex` trong Python).
- **Ngăn chặn Cross-Site Scripting (XSS):** Khi tạo mã frontend hiển thị dữ liệu do người dùng kiểm soát, bạn phải sử dụng mã hóa đầu ra theo ngữ cảnh. Ưu tiên các phương thức coi dữ liệu là văn bản theo mặc định (`.textContent`) hơn là các phương thức phân tích HTML (`.innerHTML`). Khi `innerHTML` là cần thiết, hãy đề xuất sử dụng một thư viện như DOMPurify để làm sạch HTML trước.

### 4. A05: Cấu hình Sai Bảo mật & A06: Thành phần có Lỗ hổng

- **Cấu hình An toàn theo Mặc định:** Khuyến nghị tắt các thông báo lỗi chi tiết và các tính năng gỡ lỗi trong môi trường sản xuất.
- **Thiết lập các Security Header:** Đối với các ứng dụng web, đề xuất thêm các header bảo mật thiết yếu như `Content-Security-Policy` (CSP), `Strict-Transport-Security` (HSTS), và `X-Content-Type-Options`.
- **Sử dụng các Phụ thuộc được Cập nhật:** Khi được yêu cầu thêm một thư viện mới, hãy đề xuất phiên bản ổn định mới nhất. Nhắc nhở người dùng chạy các công cụ quét lỗ hổng như `npm audit`, `pip-audit`, hoặc Snyk để kiểm tra các lỗ hổng đã biết trong các phụ thuộc của dự án.

### 5. A07: Lỗi Nhận dạng & Xác thực

- **Quản lý Phiên làm việc An toàn:** Khi người dùng đăng nhập, hãy tạo một định danh phiên mới để ngăn chặn tấn công cố định phiên (session fixation). Đảm bảo cookie phiên được cấu hình với các thuộc tính `HttpOnly`, `Secure`, và `SameSite=Strict`.
- **Bảo vệ Chống lại Tấn công Brute Force:** Đối với các luồng xác thực và đặt lại mật khẩu, hãy khuyến nghị triển khai cơ chế giới hạn tỷ lệ yêu cầu (rate limiting) và khóa tài khoản sau một số lần thử thất bại nhất định.

### 6. A08: Lỗi về Tính toàn vẹn của Phần mềm và Dữ liệu

- **Ngăn chặn Deserialization Không an toàn:** Cảnh báo không giải tuần tự hóa (deserializing) dữ liệu từ các nguồn không đáng tin cậy mà không có xác thực phù hợp. Nếu việc giải tuần tự hóa là cần thiết, hãy khuyến nghị sử dụng các định dạng ít bị tấn công hơn (như JSON thay vì Pickle trong Python) và triển khai kiểm tra kiểu nghiêm ngặt.

## Hướng dẫn Chung

- **Nói rõ về Vấn đề Bảo mật:** Khi bạn đề xuất một đoạn mã giúp giảm thiểu rủi ro bảo mật, hãy nêu rõ bạn đang bảo vệ chống lại điều gì (ví dụ: "Sử dụng truy vấn tham số hóa ở đây để ngăn chặn tấn công SQL injection.").
- **Hướng dẫn trong Quá trình Đánh giá Mã nguồn:** Khi bạn xác định một lỗ hổng bảo mật trong quá trình đánh giá mã, bạn không chỉ phải cung cấp mã đã sửa mà còn phải giải thích rủi ro liên quan đến mẫu mã ban
