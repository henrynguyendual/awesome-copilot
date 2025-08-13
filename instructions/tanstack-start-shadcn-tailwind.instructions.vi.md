---
description: "Hướng dẫn xây dựng ứng dụng TanStack Start"
applyTo: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx, **/*.css, **/*.scss, **/*.json"
---

# Hướng dẫn Phát triển TanStack Start với Shadcn/ui

Bạn là một nhà phát triển TypeScript chuyên nghiệp, chuyên về các ứng dụng TanStack Start với các mẫu React hiện đại.

## Ngăn xếp Công nghệ

- TypeScript (chế độ nghiêm ngặt)
- TanStack Start (định tuyến & SSR)
- Shadcn/ui (thành phần giao diện người dùng)
- Tailwind CSS (tạo kiểu)
- Zod (xác thực)
- TanStack Query (trạng thái phía client)

## Quy tắc Phong cách Code

- KHÔNG BAO GIỜ sử dụng kiểu `any` - luôn sử dụng các kiểu TypeScript phù hợp
- Ưu tiên sử dụng function component hơn class component
- Luôn xác thực dữ liệu bên ngoài bằng Zod schema
- Bao gồm các ranh giới lỗi (error boundary) và chờ (pending boundary) cho tất cả các route
- Tuân thủ các phương pháp tốt nhất về khả năng truy cập (accessibility) với các thuộc tính ARIA

## Mẫu Component

Sử dụng function component với các interface TypeScript phù hợp:

```typescript
interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
  variant?: "primary" | "secondary";
}

export default function Button({ children, onClick, variant = "primary" }: ButtonProps) {
  return (
    <button onClick={onClick} className={cn(buttonVariants({ variant }))}>
      {children}
    </button>
  );
}
```

## Tải dữ liệu (Data Fetching)

Sử dụng Route Loader cho:

- Dữ liệu ban đầu của trang cần thiết để render
- Các yêu cầu về SSR (Server-Side Rendering)
- Dữ liệu quan trọng cho SEO

Sử dụng React Query cho:

- Dữ liệu cập nhật thường xuyên
- Dữ liệu tùy chọn/phụ
- Các thay đổi dữ liệu phía client (mutations) với cập nhật lạc quan (optimistic updates)

```typescript
// Route Loader
export const Route = createFileRoute("/users")({
  loader: async () => {
    const users = await fetchUsers();
    return { users: userListSchema.parse(users) };
  },
  component: UserList,
});

// React Query
const { data: stats } = useQuery({
  queryKey: ["user-stats", userId],
  queryFn: () => fetchUserStats(userId),
  refetchInterval: 30000,
});
```

## Xác thực với Zod

Luôn xác thực dữ liệu bên ngoài. Định nghĩa các schema trong `src/lib/schemas.ts`:

```typescript
export const userSchema = z.object({
  id: z.string(),
  name: z.string().min(1).max(100),
  email: z.string().email().optional(),
  role: z.enum(["admin", "user"]).default("user"),
});

export type User = z.infer<typeof userSchema>;

// Phân tích cú pháp an toàn (Safe parsing)
const result = userSchema.safeParse(data);
if (!result.success) {
  console.error("Xác thực thất bại:", result.error.format());
  return null;
}
```

## Routes (Định tuyến)

Cấu trúc các route trong `src/routes/` với định tuyến dựa trên tệp. Luôn bao gồm các ranh giới lỗi và chờ:

```typescript
export const Route = createFileRoute("/users/$id")({
  loader: async ({ params }) => {
    const user = await fetchUser(params.id);
    return { user: userSchema.parse(user) };
  },
  component: UserDetail,
  errorBoundary: ({ error }) => <div className="text-red-600 p-4">Lỗi: {error.message}</div>,
  pendingBoundary: () => (
    <div className="flex items-center justify-center p-4">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary" />
    </div>
  ),
});
```

## Thành phần Giao diện (UI Components)

Luôn ưu tiên các component của Shadcn/ui hơn là các component tự tạo:

```typescript
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

<Card>
  <CardHeader>
    <CardTitle>Chi tiết người dùng</CardTitle>
  </CardHeader>
  <CardContent>
    <Button onClick={handleSave}>Lưu</Button>
  </CardContent>
</Card>;
```

Sử dụng Tailwind để tạo kiểu với thiết kế đáp ứng (responsive design):

```typescript
<div className="flex flex-col gap-4 p-6 md:flex-row md:gap-6">
  <Button className="w-full md:w-auto">Hành động</Button>
</div>
```

## Khả năng truy cập (Accessibility)

Ưu tiên sử dụng HTML ngữ nghĩa trước. Chỉ thêm ARIA khi không có thẻ ngữ nghĩa tương đương:

```typescript
// ✅ Tốt: HTML ngữ nghĩa với ARIA tối thiểu
<button onClick={toggleMenu}>
  <MenuIcon aria-hidden="true" />
  <span className="sr-only">Chuyển đổi Menu</span>
</button>

// ✅ Tốt: Chỉ dùng ARIA khi cần (cho các trạng thái động)
<button
  aria-expanded={isOpen}
  aria-controls="menu"
  onClick={toggleMenu}
>
  Menu
</button>

// ✅ Tốt: Các phần tử form ngữ nghĩa
<label htmlFor="email">Địa chỉ Email</label>
<input id="email" type="email" />
{errors.email && (
  <p role="alert">{errors.email}</p>
)}
```

## Tổ chức Tệp

```
src/
├── components/ui/    # Các component của Shadcn/ui
├── lib/schemas.ts    # Các schema của Zod
├── routes/           # Các route dựa trên tệp
└── routes/api/       # Các route phía server (.ts)
```

## Tiêu chuẩn Import

Sử dụng bí danh `@/` cho tất cả các import nội bộ:

```typescript
// ✅ Tốt
import { Button } from "@/components/ui/button";
import { userSchema } from "@/lib/schemas";

// ❌ Xấu
import { Button } from "../components/ui/button";
```

## Thêm Component

Cài đặt các component của Shadcn khi cần:

```bash
npx shadcn@latest add button card input dialog
```

## Các Mẫu Thường gặp

- Luôn xác thực dữ liệu bên ngoài với Zod
- Sử dụng route loader cho dữ liệu ban đầu, React Query cho các cập nhật
- Bao gồm ranh giới lỗi/chờ trên tất cả các route
- Ưu tiên các component của Shadcn hơn là UI tự tạo
- Sử dụng import `@/` một cách nhất quán
- Tuân thủ các phương pháp tốt nhất về khả năng truy cập
