---
description: "Hướng dẫn viết mã Node.js và JavaScript với kiểm thử Vitest"
applyTo: "**/*.js, **/*.mjs, **/*.cjs"
---

# Hướng dẫn Tạo mã

## Tiêu chuẩn viết mã

- Sử dụng JavaScript với các tính năng của ES2022 và các mô-đun ESM của Node.js (20+)
- Sử dụng các mô-đun tích hợp sẵn của Node.js và tránh các phụ thuộc bên ngoài nếu có thể
- Hỏi người dùng nếu bạn cần thêm bất kỳ phụ thuộc nào trước khi thêm chúng
- Luôn sử dụng async/await cho mã bất đồng bộ, và sử dụng hàm promisify từ 'node:util' để tránh callback
- Giữ mã đơn giản và dễ bảo trì
- Sử dụng tên biến và hàm có tính mô tả
- Không thêm nhận xét trừ khi thực sự cần thiết, mã nên tự giải thích
- Không bao giờ sử dụng `null`, luôn sử dụng `undefined` cho các giá trị tùy chọn
- Ưu tiên hàm hơn lớp

## Kiểm thử

- Sử dụng Vitest để kiểm thử
- Viết kiểm thử cho tất cả các tính năng mới và các bản sửa lỗi
- Đảm bảo các bài kiểm thử bao gồm các trường hợp biên và xử lý lỗi
- KHÔNG BAO GIỜ thay đổi mã gốc để dễ kiểm thử hơn, thay vào đó, hãy viết các bài kiểm thử bao quát mã gốc như nó vốn có

## Tài liệu

- Khi thêm tính năng mới hoặc thực hiện các thay đổi quan trọng, hãy cập nhật tệp README.md khi cần thiết

## Tương tác với người dùng

- Đặt câu hỏi nếu bạn không chắc chắn về chi tiết triển khai, lựa chọn thiết kế, hoặc cần làm rõ các yêu cầu
- Luôn trả lời bằng ngôn ngữ của câu hỏi, nhưng sử dụng tiếng Anh cho nội dung được tạo ra như mã, nhận xét hoặc tài
