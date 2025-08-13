---
description: "Các mẫu TypeScript cho Azure Functions"
applyTo: "**/*.ts, **/*.js, **/*.json"
---

## Hướng dẫn Tạo mã

- Tạo mã TypeScript hiện đại cho Node.js
- Sử dụng `async/await` cho mã bất đồng bộ
- Bất cứ khi nào có thể, hãy sử dụng các mô-đun tích hợp sẵn của Node.js v20 thay vì các gói bên ngoài
- Luôn sử dụng các hàm bất đồng bộ của Node.js, như `node:fs/promises` thay vì `fs` để tránh chặn vòng lặp sự kiện
- Hỏi trước khi thêm bất kỳ phụ thuộc bổ sung nào vào dự án
- API được xây dựng bằng Azure Functions sử dụng gói `@azure/functions@4`.
- Mỗi điểm cuối (endpoint) nên có tệp hàm riêng và sử dụng quy ước đặt tên sau: `src/functions/<tên-tài-nguyên>-<động-từ-http>.ts`
- Khi thực hiện các thay đổi đối với API, hãy đảm bảo cập nhật lược đồ OpenAPI (nếu có) và tệp `README.md
