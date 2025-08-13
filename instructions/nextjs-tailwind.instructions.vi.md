---
description: "Tiêu chuẩn và hướng dẫn phát triển Next.js + Tailwind"
applyTo: "**/*.tsx, **/*.ts, **/*.jsx, **/*.js, **/*.css"
---

# Hướng dẫn Phát triển Next.js + Tailwind

Hướng dẫn để xây dựng các ứng dụng Next.js chất lượng cao với Tailwind CSS và TypeScript.

## Bối cảnh Dự án

- Next.js phiên bản mới nhất (App Router)
- TypeScript để đảm bảo an toàn kiểu dữ liệu
- Tailwind CSS để tạo kiểu

## Tiêu chuẩn Phát triển

### Kiến trúc

- Sử dụng App Router với server và client components
- Nhóm các route theo tính năng/miền
- Triển khai các ranh giới lỗi (error boundaries) phù hợp
- Sử dụng React Server Components làm mặc định
- Tận dụng tối ưu hóa tĩnh (static optimization) khi có thể

### TypeScript

- Bật chế độ nghiêm ngặt (strict mode)
- Định nghĩa kiểu dữ liệu rõ ràng
- Xử lý lỗi phù hợp với các bộ bảo vệ kiểu (type guards)
- Sử dụng Zod để xác thực kiểu dữ liệu lúc chạy (runtime)

### Tạo kiểu (Styling)

- Sử dụng Tailwind CSS với bảng màu nhất quán
- Các mẫu thiết kế đáp ứng (responsive design)
- Hỗ trợ chế độ tối (dark mode)
- Tuân thủ các phương pháp hay nhất về container queries
- Duy trì cấu trúc HTML có ngữ nghĩa

### Quản lý Trạng thái (State Management)

- Sử dụng React Server Components cho trạng thái phía máy chủ
- Sử dụng React hooks cho trạng thái phía máy khách
- Xử lý các trạng thái tải (loading) và lỗi (error) phù hợp
- Cập nhật lạc quan (optimistic updates) khi thích hợp

### Lấy dữ liệu (Data Fetching)

- Sử dụng Server Components để truy vấn cơ sở dữ liệu trực tiếp
- Sử dụng React Suspense cho các trạng thái tải
- Xử lý lỗi và logic thử lại (retry) phù hợp
- Các chiến lược vô hiệu hóa bộ đệm (cache invalidation)

### Bảo mật

- Xác thực và làm sạch đầu vào (input validation and sanitization)
- Kiểm tra xác thực phù hợp
- Bảo vệ chống tấn công CSRF
- Triển khai giới hạn tỷ lệ yêu cầu (rate limiting)
- Xử lý các route API an toàn

### Hiệu suất

- Tối ưu hóa hình ảnh với next/image
- Tối ưu hóa phông chữ với next/font
- Tải trước các route (route prefetching)
- Tách mã (code splitting) phù hợp
- Tối ưu hóa kích thước gói (bundle size)

## Quy trình Triển khai

1. Lập kế hoạch phân cấp component
2. Định nghĩa các kiểu (types) và giao diện (interfaces)
3. Triển khai logic phía máy chủ
4. Xây dựng các client component
5. Thêm xử lý lỗi phù hợp
6. Triển khai tạo kiểu đáp ứng (responsive styling)
7. Thêm các trạng thái tải (loading states)
8. Viết kiểm thử (tests)
