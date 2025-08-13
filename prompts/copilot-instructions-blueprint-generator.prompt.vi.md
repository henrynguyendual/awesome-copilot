# Trình Tạo Bản Thiết Kế Hướng Dẫn Cho Copilot

## Biến Cấu Hình
${PROJECT_TYPE="Tự động phát hiện|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Nhiều|Khác"} <!-- Công nghệ chính -->
${ARCHITECTURE_STYLE="Phân lớp|Microservices|Nguyên khối|Domain-Driven|Event-Driven|Serverless|Kết hợp"} <!-- Kiến trúc -->
${CODE_QUALITY_FOCUS="Khả năng bảo trì|Hiệu năng|Bảo mật|Khả năng truy cập|Khả năng kiểm thử|Tất cả"} <!-- Chất lượng code -->
${DOCUMENTATION_LEVEL="Tối thiểu|Tiêu chuẩn|Toàn diện"} <!-- Tài liệu -->
${TESTING_REQUIREMENTS="Unit|Integration|E2E|TDD|BDD|Tất cả"} <!-- Kiểm thử -->
${VERSIONING="Semantic|CalVer|Tùy chỉnh"} <!-- Phiên bản -->

## Prompt Sinh Ra

"Tạo file copilot-instructions.md toàn diện để hướng dẫn GitHub Copilot sinh code phù hợp với tiêu chuẩn, kiến trúc và phiên bản công nghệ của dự án. Hướng dẫn phải dựa hoàn toàn vào các mẫu code có sẵn, không được giả định.

### 1. Cấu Trúc Hướng Dẫn Chính

```markdown
# Hướng Dẫn GitHub Copilot

## Nguyên Tắc Ưu Tiên

Khi sinh code cho repository này:

1. **Tương Thích Phiên Bản**: Luôn phát hiện và tuân theo chính xác phiên bản ngôn ngữ, framework, và thư viện đang dùng
2. **File Ngữ Cảnh**: Ưu tiên các tiêu chuẩn trong thư mục .github/copilot
3. **Mẫu Codebase**: Nếu file ngữ cảnh không có hướng dẫn cụ thể, quét codebase để tìm mẫu đã thiết lập
4. **Nhất Quán Kiến Trúc**: Tuân thủ kiến trúc ${ARCHITECTURE_STYLE}
5. **Chất Lượng Code**: Ưu tiên ${CODE_QUALITY_FOCUS == "Tất cả" ? "khả năng bảo trì, hiệu năng, bảo mật, truy cập, và kiểm thử" : CODE_QUALITY_FOCUS}
```

(Phần tiếp theo giữ nguyên cấu trúc, dịch toàn bộ các mục: Phát hiện phiên bản, Hướng dẫn quét codebase, Tiêu chuẩn chất lượng code, Yêu cầu tài liệu, Cách tiếp cận kiểm thử, Hướng dẫn công nghệ cụ thể, Quy tắc quản lý phiên bản, Thực hành tốt nhất, Hướng dẫn riêng cho dự án, Phân tích codebase, Ghi chú triển khai, và Đầu ra mong đợi.)