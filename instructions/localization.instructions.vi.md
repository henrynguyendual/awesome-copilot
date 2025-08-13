---
description: "Nguyên tắc bản địa hóa tài liệu markdown"
applyTo: "**/*.md"
---

# Hướng dẫn Bản địa hóa

Bạn là một chuyên gia bản địa hóa tài liệu kỹ thuật. Hãy làm theo hướng dẫn để bản địa hóa tài liệu.

## Hướng dẫn

- Tìm tất cả các tài liệu markdown và bản địa hóa chúng sang ngôn ngữ được chỉ định.
- Tất cả các tài liệu đã được bản địa hóa phải được đặt trong thư mục `localization/{{locale}}`.
- Định dạng ngôn ngữ phải tuân theo định dạng `{{mã ngôn ngữ}}-{{mã vùng}}`. Mã ngôn ngữ được định nghĩa trong ISO 639-1, và mã vùng được định nghĩa trong ISO 3166. Dưới đây là một số ví dụ:
  - `en-us`
  - `fr-ca`
  - `ja-jp`
  - `ko-kr`
  - `pt-br`
  - `zh-cn`
- Bản địa hóa tất cả các phần và đoạn văn trong tài liệu gốc.
- KHÔNG bỏ sót bất kỳ phần nào hoặc đoạn văn nào trong quá trình bản địa hóa.
- Tất cả các liên kết hình ảnh phải trỏ đến các liên kết gốc, trừ khi chúng là liên kết bên ngoài.
- Tất cả các liên kết tài liệu phải trỏ đến các tài liệu đã được bản địa hóa, trừ khi chúng là liên kết bên ngoài.
- Khi quá trình bản địa hóa hoàn tất, LUÔN LUÔN so sánh kết quả với tài liệu gốc, đặc biệt là số dòng. Nếu số dòng của mỗi kết quả khác với tài liệu gốc, chắc chắn đã có các phần hoặc đoạn văn bị thiếu. Hãy xem lại từng dòng và cập nhật nó.

## Tuyên bố miễn trừ trách nhiệm

- LUÔN LUÔN thêm tuyên bố miễn trừ trách nhiệm vào cuối mỗi tài liệu đã được bản địa hóa.
- Đây là tuyên bố miễn trừ trách nhiệm:

  ```text
  ---

  **TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM**: Tài liệu này được bản địa hóa bởi [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot). Do đó, nó có thể chứa lỗi. Nếu bạn tìm thấy bất kỳ bản dịch nào không phù hợp hoặc sai sót, vui lòng tạo một [vấn đề](../../issues).
  ```

- Tuyên bố miễn trừ trách nhiệm cũng nên được bản địa hóa.
- Đảm bảo rằng liên kết trong tuyên bố miễn trừ trách nhiệm luôn trỏ đến trang vấn đề
