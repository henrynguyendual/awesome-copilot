---
description: "Hướng dẫn tạo test Playwright Python bằng AI dựa trên tài liệu chính thức."
applyTo: "**"
---

# Hướng dẫn Tạo Test Playwright Python

## Nguyên tắc Viết Test

### Tiêu chuẩn Chất lượng Code

- **Locators (Bộ định vị)**: Ưu tiên sử dụng các bộ định vị hướng tới người dùng, dựa trên vai trò (get_by_role, get_by_label, get_by_text) để tăng tính ổn định và khả năng truy cập.
- **Assertions (Xác nhận)**: Sử dụng các xác nhận web-first có khả năng tự động thử lại thông qua API `expect` (ví dụ: `expect(page).to_have_title(...)`). Tránh dùng `expect(locator).to_be_visible()` trừ khi bạn đang kiểm tra cụ thể sự thay đổi về khả năng hiển thị của một phần tử, vì các xác nhận cụ thể hơn thường đáng tin cậy hơn.
- **Timeouts (Thời gian chờ)**: Dựa vào các cơ chế chờ tự động tích hợp sẵn của Playwright. Tránh việc đặt thời gian chờ cố định (hard-coded waits) hoặc tăng thời gian chờ mặc định.
- **Clarity (Rõ ràng)**: Sử dụng tiêu đề test mang tính mô tả (ví dụ: `def test_navigation_link_works():`) để nêu rõ mục đích. Chỉ thêm bình luận để giải thích logic phức tạp, không phải để mô tả các hành động đơn giản như "nhấp vào một nút".

### Cấu trúc Test

- **Imports**: Mỗi tệp test nên bắt đầu bằng `from playwright.sync_api import Page, expect`.
- **Fixtures**: Sử dụng fixture `page: Page` làm đối số trong các hàm test của bạn để tương tác với trang trình duyệt.
- **Setup (Thiết lập)**: Đặt các bước điều hướng như `page.goto()` ở đầu mỗi hàm test. Đối với các hành động thiết lập được chia sẻ giữa nhiều test, hãy sử dụng các fixture tiêu chuẩn của Pytest.

### Tổ chức Tệp

- **Location (Vị trí)**: Lưu trữ các tệp test trong một thư mục `tests/` chuyên dụng hoặc tuân theo cấu trúc dự án hiện có.
- **Naming (Đặt tên)**: Các tệp test phải tuân theo quy ước đặt tên `test_<feature-or-page>.py` để Pytest có thể phát hiện.
- **Scope (Phạm vi)**: Hướng tới việc có một tệp test cho mỗi tính năng hoặc trang chính của ứng dụng.

## Các Phương pháp Xác nhận Tốt nhất

- **Element Counts (Đếm phần tử)**: Sử dụng `expect(locator).to_have_count()` để xác nhận số lượng phần tử được tìm thấy bởi một bộ định vị.
- **Text Content (Nội dung văn bản)**: Sử dụng `expect(locator).to_have_text()` để khớp văn bản chính xác và `expect(locator).to_contain_text()` để khớp một phần.
- **Navigation (Điều hướng)**: Sử dụng `expect(page).to_have_url()` để xác minh URL của trang.
- **Assertion Style (Kiểu xác nhận)**: Ưu tiên `expect` hơn `assert` để có các bài test UI đáng tin cậy hơn.

## Ví dụ

```python
import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # Đi đến url bắt đầu trước mỗi bài test.
    page.goto("https://playwright.dev/")

def test_main_navigation(page: Page):
    expect(page).to_have_url("https://playwright.dev/")

def test_has_title(page: Page):
    # Mong đợi tiêu đề "chứa" một chuỗi con.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.get_by_role("link", name="Get started").click()

    # Mong đợi trang có một tiêu đề với tên là Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

## Chiến lược Thực thi Test

1. **Execution (Thực thi)**: Các bài test được chạy từ terminal bằng lệnh `pytest`.
2. **Debug Failures (Gỡ lỗi khi thất bại)**: Phân tích các lần test thất bại và xác định
