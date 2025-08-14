---
mode: "agent"
tools: ["codebase"]
description: "Tạo các Dockerfile đa giai đoạn được tối ưu hóa cho bất kỳ ngôn ngữ hoặc framework nào"
---

Mục tiêu của bạn là giúp tôi tạo ra các Dockerfile đa giai đoạn hiệu quả, tuân thủ các phương pháp hay nhất, nhằm tạo ra các image container nhỏ hơn và an toàn hơn.

## Cấu trúc đa giai đoạn

- Sử dụng một giai đoạn `builder` để biên dịch, cài đặt dependency và các hoạt động khác tại thời điểm build.
- Sử dụng một giai đoạn `runtime` riêng biệt chỉ chứa những gì cần thiết để chạy ứng dụng.
- Chỉ sao chép các thành phần cần thiết từ giai đoạn `builder` sang giai đoạn `runtime`.
- Sử dụng tên giai đoạn có ý nghĩa với từ khóa `AS` (ví dụ: `FROM node:18 AS builder`).
- Sắp xếp các giai đoạn theo thứ tự logic: cài đặt dependency → build → kiểm thử → runtime.

## Base Image

- Bắt đầu với các base image chính thức, tối giản khi có thể.
- Chỉ định tag phiên bản chính xác để đảm bảo các bản build có thể tái tạo (ví dụ: `python:3.11-slim` thay vì chỉ `python`).
- Cân nhắc sử dụng các image `distroless` cho các giai đoạn runtime khi thích hợp.
- Sử dụng các image dựa trên Alpine để có dung lượng nhỏ hơn khi tương thích với ứng dụng của bạn.
- Đảm bảo image runtime có các dependency cần thiết ở mức tối thiểu.

## Tối ưu hóa Layer

- Sắp xếp các lệnh để tối đa hóa việc sử dụng cache của layer.
- Đặt các lệnh thay đổi thường xuyên (như thay đổi mã nguồn) sau các lệnh ít thay đổi hơn (như cài đặt dependency).
- Sử dụng `.dockerignore` để ngăn các tệp không cần thiết được đưa vào ngữ cảnh build.
- Kết hợp các lệnh `RUN` liên quan bằng `&&` để giảm số lượng layer.
- Cân nhắc sử dụng `COPY --chown` để thiết lập quyền trong một bước.

## Các phương pháp bảo mật

- Tránh chạy container với quyền `root` - sử dụng chỉ thị `USER` để chỉ định một người dùng không phải `root`.
- Xóa các công cụ build và các gói không cần thiết khỏi image cuối cùng.
- Quét image cuối cùng để tìm các lỗ hổng bảo mật.
- Thiết lập quyền truy cập tệp hạn chế.
- Sử dụng build đa giai đoạn để tránh đưa các bí mật build vào image cuối cùng.

## Cân nhắc về hiệu suất

- Sử dụng các đối số build (`build arguments`) cho cấu hình có thể thay đổi giữa các môi trường.
- Tận dụng cache của build một cách hiệu quả bằng cách sắp xếp các layer từ ít thay đổi nhất đến thay đổi thường xuyên nhất.
- Cân nhắc việc song song hóa trong các bước build khi có thể.
- Thiết lập các biến môi trường phù hợp như `NODE_ENV=production` để tối ưu hóa hành vi lúc runtime.
- Sử dụng các kiểm tra sức khỏe (`healthchecks`) phù hợp với loại ứng dụng bằng chỉ thị `HEALTHCHECK`.
