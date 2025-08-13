---
description: "Hướng dẫn tạo test Playwright"
applyTo: "**"
---

## Hướng dẫn Viết Test

### Tiêu chuẩn Chất lượng Code

- **Locators**: Ưu tiên sử dụng các locator hướng tới người dùng, dựa trên vai trò (`getByRole`, `getByLabel`, `getByText`, v.v.) để đảm bảo tính ổn định và khả năng truy cập. Sử dụng `test.step()` để nhóm các tương tác và cải thiện khả năng đọc cũng như báo cáo của test.
- **Assertions**: Sử dụng các assertion web-first có khả năng tự động thử lại. Các assertion này bắt đầu bằng từ khóa `await` (ví dụ: `await expect(locator).toHaveText()`). Tránh dùng `expect(locator).toBeVisible()` trừ khi bạn đang kiểm tra cụ thể sự thay đổi về khả năng hiển thị.
- **Timeouts**: Dựa vào các cơ chế chờ tự động tích hợp sẵn của Playwright. Tránh việc đặt thời gian chờ cố định (hard-coded waits) hoặc tăng thời gian chờ mặc định.
- **Sự rõ ràng**: Sử dụng tiêu đề cho test và các bước (step) một cách mô tả, nêu rõ mục đích. Chỉ thêm comment để giải thích logic phức tạp hoặc các tương tác không rõ ràng.

### Cấu trúc Test

- **Imports**: Bắt đầu với `import { test, expect } from '@playwright/test';`.
- **Tổ chức**: Nhóm các test liên quan đến một tính năng vào trong một khối `test.describe()`.
- **Hooks**: Sử dụng `beforeEach` cho các hành động thiết lập chung cho tất cả các test trong một khối `describe` (ví dụ: điều hướng đến một trang).
- **Tiêu đề**: Tuân theo quy ước đặt tên rõ ràng, chẳng hạn như `Tính năng - Hành động hoặc kịch bản cụ thể`.

### Tổ chức Tệp

- **Vị trí**: Lưu trữ tất cả các tệp test trong thư mục `tests/`.
- **Đặt tên**: Sử dụng quy ước `<tinh-nang-hoac-trang>.spec.ts` (ví dụ: `login.spec.ts`, `search.spec.ts`).
- **Phạm vi**: Hướng tới việc có một tệp test cho mỗi tính năng chính hoặc trang của ứng dụng.

### Các Phương pháp Assertion Tốt nhất

- **Cấu trúc UI**: Sử dụng `toMatchAriaSnapshot` để xác minh cấu trúc cây trợ năng (accessibility tree) của một thành phần. Điều này cung cấp một snapshot toàn diện và dễ tiếp cận.
- **Số lượng phần tử**: Sử dụng `toHaveCount` để khẳng định số lượng phần tử được tìm thấy bởi một locator.
- **Nội dung văn bản**: Sử dụng `toHaveText` cho các kết quả khớp văn bản chính xác và `toContainText` cho các kết quả khớp một phần.
- **Điều hướng**: Sử dụng `toHaveURL` để xác minh URL của trang sau một hành động.

## Ví dụ về Cấu trúc Test

```typescript
import { test, expect } from "@playwright/test";

test.describe("Tính năng Tìm kiếm Phim", () => {
  test.beforeEach(async ({ page }) => {
    // Điều hướng đến ứng dụng trước mỗi bài test
    await page.goto("https://debs-obrien.github.io/playwright-movies-app");
  });

  test("Tìm kiếm một bộ phim theo tiêu đề", async ({ page }) => {
    await test.step("Kích hoạt và thực hiện tìm kiếm", async () => {
      await page.getByRole("search").click();
      const searchInput = page.getByRole("textbox", { name: "Search Input" });
      await searchInput.fill("Garfield");
      await searchInput.press("Enter");
    });

    await test.step("Xác minh kết quả tìm kiếm", async () => {
      // Xác minh cây trợ năng của kết quả tìm kiếm
      await expect(page.getByRole("main")).toMatchAriaSnapshot(`
        - main:
          - heading "Garfield" [level=1]
          - heading "search results" [level=2]
          - list "movies":
            - listitem "movie":
              - link "poster of The Garfield Movie The Garfield Movie rating":
                - /url: /playwright-movies-app/movie?id=tt5779228&page=1
                - img "poster of The Garfield Movie"
                - heading "The Garfield Movie" [level=2]
      `);
    });
  });
});
```

## Chiến lược Thực thi Test

1.  **Chạy lần đầu**: Thực thi các test với `npx playwright test --project=chromium`
2.  **Gỡ lỗi (Debug) các lỗi**: Phân tích các lỗi test và xác định nguyên nhân gốc rễ
3.  **Lặp lại**: Tinh chỉnh các locator, assertion, hoặc logic test khi cần thiết
4.  **Xác thực**: Đảm bảo các test vượt qua một cách nhất quán và bao phủ chức năng dự kiến
5.  **Báo cáo**: Cung cấp phản hồi về kết quả test và bất kỳ vấn đề nào được phát hiện

## Danh sách Kiểm tra Chất lượng

Trước khi hoàn thiện các test, hãy đảm bảo:

- [ ] Tất cả các locator đều có thể truy cập, cụ thể và tránh vi phạm chế độ nghiêm ngặt (strict mode)
- [ ] Các test được nhóm một cách logic và tuân theo một cấu trúc rõ ràng
- [ ] Các assertion có ý nghĩa và phản ánh mong đợi của người dùng
- [ ] Các test tuân theo quy ước đặt tên nhất quán
- [ ] Code được định dạng và chú thích đúng cách
