# Thực hành tốt nhất khi viết test JavaScript/TypeScript với Jest

## Cấu trúc bài test

-   Đặt tên file test với hậu tố `.test.ts` hoặc `.test.js`.

-   Đặt file test cạnh file code hoặc trong thư mục `__tests__` riêng.

-   Sử dụng tên test mô tả rõ hành vi mong đợi.

-   Sử dụng các khối `describe` lồng nhau để nhóm các test liên quan.

-   Theo mẫu:

    ``` javascript
    describe('Component/Function/Class', () => {
      it('should do something', () => {})
    })
    ```

## Mocking hiệu quả

-   Mock các dependency bên ngoài (API, DB, ...) để tách biệt test.
-   Dùng `jest.mock()` để mock ở cấp module.
-   Dùng `jest.spyOn()` để mock một hàm cụ thể.
-   Dùng `mockImplementation()` hoặc `mockReturnValue()` để định nghĩa
    hành vi mock.
-   Reset mock giữa các test với `jest.resetAllMocks()` trong
    `afterEach`.

## Kiểm thử async code

-   Luôn return promise hoặc dùng async/await trong test.
-   Sử dụng matcher `resolves`/`rejects` cho promise.
-   Thiết lập timeout phù hợp cho test chậm với `jest.setTimeout()`.

## Snapshot Testing

-   Sử dụng snapshot cho UI component hoặc object phức tạp thay đổi ít.
-   Giữ snapshot nhỏ và tập trung.
-   Kiểm tra kỹ snapshot trước khi commit.

## Kiểm thử React Component

-   Ưu tiên React Testing Library thay vì Enzyme.
-   Kiểm thử hành vi người dùng và khả năng truy cập (accessibility).
-   Query element bằng role, label hoặc text content.
-   Dùng `userEvent` thay vì `fireEvent` để mô phỏng tương tác thực tế
    hơn.

## Matcher phổ biến trong Jest

-   **Cơ bản:** `expect(value).toBe(expected)`,
    `expect(value).toEqual(expected)`
-   **Truthy/Falsy:** `expect(value).toBeTruthy()`,
    `expect(value).toBeFalsy()`
-   **Số:** `expect(value).toBeGreaterThan(3)`,
    `expect(value).toBeLessThanOrEqual(3)`
-   **Chuỗi:** `expect(value).toMatch(/pattern/)`,
    `expect(value).toContain('substring')`
-   **Mảng:** `expect(array).toContain(item)`,
    `expect(array).toHaveLength(3)`
-   **Object:** `expect(object).toHaveProperty('key', value)`
-   **Ngoại lệ:** `expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
-   **Hàm mock:** `expect(mockFn).toHaveBeenCalled()`,
    `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`
