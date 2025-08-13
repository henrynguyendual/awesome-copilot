---
applyTo: "**"
---

# Các Thực Hành Tốt Nhất cho Next.js dành cho LLM (2025)

_Cập nhật lần cuối: Tháng 7 năm 2025_

Tài liệu này tóm tắt các thực hành tốt nhất, mới nhất và có thẩm quyền để xây dựng, cấu trúc và bảo trì các ứng dụng Next.js. Nó được dành cho các LLM và nhà phát triển sử dụng để đảm bảo chất lượng mã, khả năng bảo trì và khả năng mở rộng.

---

## 1. Cấu Trúc & Tổ Chức Dự Án

- **Sử dụng thư mục `app/`** (App Router) cho tất cả các dự án mới. Ưu tiên sử dụng nó thay cho thư mục `pages/` cũ.
- **Các thư mục cấp cao nhất:**
  - `app/` — Định tuyến, layout, trang và route handler
  - `public/` — Tài sản tĩnh (hình ảnh, phông chữ, v.v.)
  - `lib/` — Các tiện ích dùng chung, API client và logic
  - `components/` — Các component UI có thể tái sử dụng
  - `contexts/` — Các React context provider
  - `styles/` — Các stylesheet toàn cục và module
  - `hooks/` — Các React hook tùy chỉnh
  - `types/` — Các định nghĩa kiểu TypeScript
- **Colocation (Sắp xếp cùng vị trí):** Đặt các tệp (component, style, test) gần nơi chúng được sử dụng, nhưng tránh các cấu trúc lồng nhau quá sâu.
- **Route Groups (Nhóm Route):** Sử dụng dấu ngoặc đơn (ví dụ: `(admin)`) để nhóm các route mà không ảnh hưởng đến đường dẫn URL.
- **Private Folders (Thư mục riêng tư):** Thêm tiền tố `_` (ví dụ: `_internal`) để không tham gia vào việc định tuyến và để chỉ ra các chi tiết triển khai nội bộ.

- **Feature Folders (Thư mục theo tính năng):** Đối với các ứng dụng lớn, nhóm theo tính năng (ví dụ: `app/dashboard/`, `app/auth/`).
- **Sử dụng `src/`** (tùy chọn): Đặt tất cả mã nguồn vào trong `src/` để tách biệt khỏi các tệp cấu hình.

## 2.1. Tích Hợp Server và Client Component (App Router)

**Không bao giờ sử dụng `next/dynamic` với `{ ssr: false }` bên trong một Server Component.** Điều này không được hỗ trợ và sẽ gây ra lỗi khi build hoặc lúc chạy.

**Cách tiếp cận đúng:**

- Nếu bạn cần sử dụng một Client Component (ví dụ: một component sử dụng hook, API của trình duyệt, hoặc các thư viện chỉ dành cho client) bên trong một Server Component, bạn phải:
  1. Di chuyển tất cả logic/UI chỉ dành cho client vào một Client Component riêng biệt (với `'use client'` ở trên cùng).
  2. Import và sử dụng Client Component đó trực tiếp trong Server Component (không cần `next/dynamic`).
  3. Nếu bạn cần kết hợp nhiều yếu tố chỉ dành cho client (ví dụ: một thanh điều hướng với menu thả xuống của hồ sơ), hãy tạo một Client Component duy nhất chứa tất cả chúng.

**Ví dụ:**

```tsx
// Server Component
import DashboardNavbar from "@/components/DashboardNavbar";

export default async function DashboardPage() {
  // ...logic phía server...
  return (
    <>
      <DashboardNavbar /> {/* Đây là một Client Component */}
      {/* ...phần còn lại của trang được render ở server... */}
    </>
  );
}
```

**Tại sao:**

- Server Component không thể sử dụng các tính năng chỉ dành cho client hoặc import động với SSR bị vô hiệu hóa.
- Client Component có thể được render bên trong Server Component, nhưng không thể làm ngược lại.

**Tóm tắt:**
Luôn di chuyển UI chỉ dành cho client vào một Client Component và import nó trực tiếp trong Server Component của bạn. Không bao giờ sử dụng `next/dynamic` với `{ ssr: false }` trong một Server Component.

---

## 2. Các Thực Hành Tốt Nhất về Component

- **Các loại Component:**
  - **Server Components** (mặc định): Dùng để tìm nạp dữ liệu, xử lý logic nặng và UI không có tương tác.
  - **Client Components:** Thêm `'use client'` ở đầu tệp. Sử dụng cho tính tương tác, trạng thái, hoặc các API của trình duyệt.
- **Khi nào nên tạo một Component:**
  - Nếu một mẫu UI được tái sử dụng nhiều hơn một lần.
  - Nếu một phần của trang phức tạp hoặc khép kín.
  - Nếu nó cải thiện khả năng đọc hoặc khả năng kiểm thử.
- **Quy ước đặt tên:**
  - Sử dụng `PascalCase` cho tệp và export của component (ví dụ: `UserCard.tsx`).
  - Sử dụng `camelCase` cho các hook (ví dụ: `useUser.ts`).
  - Sử dụng `snake_case` hoặc `kebab-case` cho các tài sản tĩnh (ví dụ: `logo_dark.svg`).
  - Đặt tên các context provider là `XyzProvider` (ví dụ: `ThemeProvider`).
- **Đặt tên tệp:**
  - Tên tệp phải khớp với tên component.
  - Đối với các tệp chỉ có một export, hãy sử dụng export default cho component.
  - Đối với nhiều component liên quan, sử dụng tệp `index.ts` (barrel file).
- **Vị trí Component:**
  - Đặt các component dùng chung trong `components/`.
  - Đặt các component dành riêng cho route vào bên trong thư mục route tương ứng.
- **Props:**
  - Sử dụng interface của TypeScript cho props.
  - Ưu tiên các kiểu prop rõ ràng và giá trị mặc định.
- **Kiểm thử (Testing):**
  - Đặt các tệp test cùng vị trí với component (ví dụ: `UserCard.test.tsx`).

## 3. Quy Ước Đặt Tên (Chung)

- **Thư mục:** `kebab-case` (ví dụ: `user-profile/`)
- **Tệp:** `PascalCase` cho component, `camelCase` cho tiện ích/hook, `kebab-case` cho tài sản tĩnh
- **Biến/Hàm:** `camelCase`
- **Types/Interfaces:** `PascalCase`
- **Hằng số:** `UPPER_SNAKE_CASE`

## 4. API Routes (Route Handlers)

- **Ưu tiên API Routes hơn Edge Functions** trừ khi bạn cần độ trễ cực thấp hoặc phân phối theo địa lý.
- **Vị trí:** Đặt các API route trong `app/api/` (ví dụ: `app/api/users/route.ts`).
- **Phương thức HTTP:** Export các hàm async được đặt tên theo các động từ HTTP (`GET`, `POST`, v.v.).
- **Request/Response:** Sử dụng API `Request` và `Response` của Web. Sử dụng `NextRequest`/`NextResponse` cho các tính năng nâng cao.
- **Dynamic Segments:** Sử dụng `[param]` cho các API route động (ví dụ: `app/api/users/[id]/route.ts`).
- **Xác thực (Validation):** Luôn xác thực và làm sạch dữ liệu đầu vào. Sử dụng các thư viện như `zod` hoặc `yup`.
- **Xử lý lỗi:** Trả về các mã trạng thái HTTP và thông báo lỗi phù hợp.
- **Xác thực người dùng (Authentication):** Bảo vệ các route nhạy cảm bằng middleware hoặc kiểm tra session phía server.

## 5. Các Thực Hành Tốt Nhất Chung

- **TypeScript:** Sử dụng TypeScript cho tất cả mã nguồn. Bật chế độ `strict` trong `tsconfig.json`.
- **ESLint & Prettier:** Thực thi phong cách mã và linting. Sử dụng cấu hình ESLint chính thức của Next.js.
- **Biến môi trường:** Lưu trữ các bí mật trong `.env.local`. Không bao giờ commit các bí mật vào kiểm soát phiên bản.
- **Kiểm thử (Testing):** Sử dụng Jest, React Testing Library, hoặc Playwright. Viết test cho tất cả logic và component quan trọng.
- **Khả năng tiếp cận (Accessibility):** Sử dụng HTML ngữ nghĩa và các thuộc tính ARIA. Kiểm thử bằng trình đọc màn hình.
- **Hiệu suất (Performance):**
  - Sử dụng tối ưu hóa Image và Font tích hợp sẵn.
  - Sử dụng Suspense và các trạng thái tải cho dữ liệu bất đồng bộ.
  - Tránh các gói client lớn; giữ hầu hết logic trong Server Components.
- **Bảo mật (Security):**
  - Làm sạch tất cả dữ liệu đầu vào của người dùng.
  - Sử dụng HTTPS trong môi trường production.
  - Thiết lập các header HTTP an toàn.
- **Tài liệu (Documentation):**
  - Viết README và bình luận mã rõ ràng.
  - Ghi tài liệu cho các API và component công khai.

# Tránh Các Tệp Ví Dụ Không Cần Thiết

Không tạo các tệp ví dụ/demo (như ModalExample.tsx) trong codebase chính trừ khi người dùng yêu cầu cụ thể một ví dụ trực tiếp, một story của Storybook, hoặc một component tài liệu rõ ràng. Giữ cho kho mã sạch sẽ và tập trung vào sản phẩm theo mặc định.

# Luôn sử dụng tài liệu và hướng dẫn mới nhất

- Đối với mọi yêu cầu liên quan đến nextjs, hãy bắt đầu bằng cách tìm kiếm tài liệu, hướng dẫn và ví dụ mới nhất về nextjs.
- Sử dụng các công cụ sau để tìm nạp và tìm kiếm tài liệu nếu có:
  - `resolve_library_id` để giải quyết tên gói/thư viện trong tài liệu.
  - `get_library_docs` để có
