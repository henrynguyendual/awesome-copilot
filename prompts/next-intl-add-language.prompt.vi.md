---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "findTestFiles", "search", "writeTest"]
description: "Thêm ngôn ngữ mới vào ứng dụng Next.js + next-intl"
---

Đây là hướng dẫn để thêm một ngôn ngữ mới vào dự án Next.js sử dụng next-intl cho việc quốc tế hóa (internationalization),

- Đối với i18n, ứng dụng sử dụng next-intl.
- Tất cả các bản dịch đều nằm trong thư mục `./messages`.
- Thành phần giao diện người dùng (UI component) là `src/components/language-toggle.tsx`.
- Cấu hình định tuyến (routing) và middleware được xử lý trong:
  - `src/i18n/routing.ts`
  - `src/middleware.ts`

Khi thêm một ngôn ngữ mới:

- Dịch tất cả nội dung của `en.json` sang ngôn ngữ mới. Mục tiêu là có tất cả các mục JSON bằng ngôn ngữ mới để có một bản dịch hoàn chỉnh.
- Thêm đường dẫn trong `routing.ts` và `middleware.ts`.
- Thêm ngôn ngữ vào `language-toggle.tsx
