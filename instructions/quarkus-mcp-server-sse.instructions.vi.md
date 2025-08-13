---
applyTo: "*"
description: "Các tiêu chuẩn và hướng dẫn phát triển cho Máy chủ MCP Quarkus với giao thức truyền tải HTTP SSE"
---

# Máy chủ MCP Quarkus

Xây dựng các máy chủ MCP với Java 21, Quarkus, và giao thức truyền tải HTTP SSE.

## Công nghệ (Stack)

- Java 21 với Quarkus Framework
- Phần mở rộng Máy chủ MCP: `mcp-server-sse`
- CDI để chèn phụ thuộc (dependency injection)
- Điểm cuối MCP (Endpoint): `http://localhost:8080/mcp/sse`

## Khởi động nhanh

```bash
quarkus create app --no-code -x rest-client-jackson,qute,mcp-server-sse your-domain-mcp-server
```

## Cấu trúc

- Sử dụng quy ước đặt tên chuẩn của Java (PascalCase cho lớp, camelCase cho phương thức)
- Tổ chức trong các package: `model`, `repository`, `service`, `mcp`
- Sử dụng kiểu Record cho các mô hình dữ liệu bất biến (immutable)
- Việc quản lý trạng thái cho dữ liệu bất biến phải được thực hiện bởi tầng repository
- Thêm Javadoc cho các phương thức public

## Công cụ MCP (MCP Tools)

- Phải là các phương thức public trong các CDI bean `@ApplicationScoped`
- Sử dụng `@Tool(name="ten_cong_cu", description="mo_ta_ro_rang")`
- Không bao giờ trả về `null` - thay vào đó hãy trả về thông báo lỗi
- Luôn xác thực tham số và xử lý lỗi một cách mượt mà

## Kiến trúc

- Phân tách các mối quan tâm: Công cụ MCP → Tầng Service → Tầng Repository
- Sử dụng `@Inject` để chèn phụ thuộc
- Đảm bảo các hoạt động dữ liệu an toàn cho luồng (thread-safe)
- Sử dụng `Optional<T>` để tránh ngoại lệ con trỏ null (null pointer exceptions)

## Các vấn đề thường gặp

- Không đặt logic nghiệp vụ trong các công cụ MCP (sử dụng tầng service)
- Không ném ngoại lệ (exceptions) từ các công cụ (trả về chuỗi lỗi)
- Đừng quên xác thực các tham số đầu vào
- Kiểm thử với các trường hợp biên
