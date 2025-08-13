Đây là hướng dẫn thêm một ngôn ngữ mới vào dự án Next.js sử dụng next-intl cho việc quốc tế hóa (i18n).

- Đối với i18n, ứng dụng sử dụng next-intl.
- Tất cả bản dịch nằm trong thư mục `./messages`.
- Thành phần UI là `src/components/language-toggle.tsx`.
- Cấu hình định tuyến (routing) và middleware được xử lý tại:
  - `src/i18n/routing.ts`
  - `src/middleware.ts`

Khi thêm một ngôn ngữ mới:

- Dịch toàn bộ nội dung của `en.json` sang ngôn ngữ mới. Mục tiêu là có tất cả các mục JSON được dịch đầy đủ để hoàn thiện bản dịch.
- Thêm đường dẫn vào `routing.ts` và `middleware.ts`.
- Thêm ngôn ngữ vào `language-toggle.tsx`.