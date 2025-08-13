---
description: "Quy ước và hướng dẫn lập trình Python"
applyTo: "**/*.py"
---

# Quy ước Lập trình Python

## Hướng dẫn về Python

- Viết bình luận rõ ràng và ngắn gọn cho mỗi hàm.
- Đảm bảo các hàm có tên mô tả và bao gồm gợi ý kiểu (type hints).
- Cung cấp docstrings theo quy ước của PEP 257.
- Sử dụng module `typing` cho các chú thích kiểu (ví dụ: `List[str]`, `Dict[str, int]`).
- Chia các hàm phức tạp thành các hàm nhỏ hơn, dễ quản lý hơn.

## Hướng dẫn Chung

- Luôn ưu tiên tính dễ đọc và sự rõ ràng.
- Đối với mã liên quan đến thuật toán, hãy bao gồm giải thích về phương pháp tiếp cận được sử dụng.
- Viết mã với các thực hành tốt về khả năng bảo trì, bao gồm các bình luận về lý do tại sao một số quyết định thiết kế nhất định được đưa ra.
- Xử lý các trường hợp biên và viết xử lý ngoại lệ rõ ràng.
- Đối với các thư viện hoặc phụ thuộc bên ngoài, hãy đề cập đến cách sử dụng và mục đích của chúng trong các bình luận.
- Sử dụng quy ước đặt tên nhất quán và tuân theo các thực hành tốt nhất dành riêng cho ngôn ngữ.
- Viết mã ngắn gọn, hiệu quả, và đúng chuẩn ngôn ngữ (idiomatic) mà cũng dễ hiểu.

## Phong cách và Định dạng Mã

- Tuân theo hướng dẫn phong cách **PEP 8** cho Python.
- Duy trì thụt lề đúng cách (sử dụng 4 dấu cách cho mỗi cấp độ thụt lề).
- Đảm bảo các dòng không vượt quá 79 ký tự.
- Đặt docstrings của hàm và lớp ngay sau từ khóa `def` hoặc `class`.
- Sử dụng các dòng trống để tách các hàm, lớp và các khối mã khi thích hợp.

## Các trường hợp biên và Kiểm thử

- Luôn bao gồm các trường hợp kiểm thử cho các luồng quan trọng của ứng dụng.
- Tính đến các trường hợp biên phổ biến như đầu vào rỗng, kiểu dữ liệu không hợp lệ và tập dữ liệu lớn.
- Bao gồm các bình luận cho các trường hợp biên và hành vi mong đợi trong những trường hợp đó.
- Viết unit test cho các hàm và ghi lại chúng bằng docstrings giải thích các trường hợp kiểm thử.

## Ví dụ về Tài liệu Đúng cách

```python
def calculate_area(radius: float) -> float:
    """
    Tính diện tích của một hình tròn với bán kính cho trước.

    Tham số:
    radius (float): Bán kính của hình tròn.

    Trả về:
    float: Diện tích của hình tròn, được tính bằng π * radius^2.
    """
    import math
    return math.pi * radius ** 2
```
