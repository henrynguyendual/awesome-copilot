---
description: "Các phương pháp hay nhất để viết test JavaScript/TypeScript bằng Jest, bao gồm các chiến lược mocking, cấu trúc test và các mẫu phổ biến."
---

### Cấu trúc Test

- Đặt tên file test với hậu tố `.test.ts` hoặc `.test.js`
- Đặt file test bên cạnh code mà nó kiểm thử hoặc trong một thư mục `__tests__` riêng
- Sử dụng tên test mang tính mô tả, giải thích hành vi mong đợi
- Sử dụng các khối `describe` lồng nhau để tổ chức các test liên quan
- Tuân theo mẫu: `describe('Component/Function/Class', () => { it('nên làm gì đó', () => {}) })`

### Mocking hiệu quả

- Mock các phụ thuộc bên ngoài (API, cơ sở dữ liệu, v.v.) để cô lập các bài test của bạn
- Sử dụng `jest.mock()` cho các mock ở cấp độ module
- Sử dụng `jest.spyOn()` cho các mock hàm cụ thể
- Sử dụng `mockImplementation()` hoặc `mockReturnValue()` để định nghĩa hành vi của mock
- Reset các mock giữa các bài test bằng `jest.resetAllMocks()` trong `afterEach`

### Kiểm thử mã bất đồng bộ (Async Code)

- Luôn trả về promise hoặc sử dụng cú pháp async/await trong các bài test
- Sử dụng các matcher `resolves`/`rejects` cho promise
- Đặt thời gian chờ (timeout) thích hợp cho các bài test chạy chậm bằng `jest.setTimeout()`

### Kiểm thử Snapshot

- Sử dụng kiểm thử snapshot cho các thành phần UI hoặc các đối tượng phức tạp ít khi thay đổi
- Giữ cho snapshot nhỏ và tập trung
- Xem xét các thay đổi của snapshot một cách cẩn thận trước khi commit

### Kiểm thử Component React

- Sử dụng React Testing Library thay vì Enzyme để kiểm thử component
- Kiểm thử hành vi người dùng và khả năng truy cập của component
- Truy vấn các phần tử theo vai trò truy cập (accessibility roles), nhãn (labels), hoặc nội dung văn bản (text content)
- Sử dụng `userEvent` thay vì `fireEvent` để có các tương tác người dùng thực tế hơn

## Các Matcher phổ biến của Jest

- Cơ bản: `expect(value).toBe(expected)`, `expect(value).toEqual(expected)`
- Kiểm tra tính đúng/sai (Truthiness): `expect(value).toBeTruthy()`, `expect(value).toBeFalsy()`
- Số: `expect(value).toBeGreaterThan(3)`, `expect(value).toBeLessThanOrEqual(3)`
- Chuỗi: `expect(value).toMatch(/pattern/)`, `expect(value).toContain('substring')`
- Mảng: `expect(array).toContain(item)`, `expect(array).toHaveLength(3)`
- Đối tượng: `expect(object).toHaveProperty('key', value)`
- Ngoại lệ: `expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
- Hàm mock: `expect(mockFn).toHaveBeenCalled()`, `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`
