---
description: "Các mẫu thành phần và ứng dụng .NET WPF"
applyTo: "**/*.xaml, **/*.cs"
---

## Tóm tắt

Những hướng dẫn này chỉ dẫn GitHub Copilot hỗ trợ xây dựng các ứng dụng WPF chất lượng cao, dễ bảo trì và có hiệu suất tốt bằng cách sử dụng mẫu MVVM. Nó bao gồm các phương pháp hay nhất cho XAML, liên kết dữ liệu (data binding), khả năng phản hồi của giao diện người dùng (UI responsiveness) và hiệu suất .NET.

## Các loại dự án lý tưởng

- Ứng dụng máy tính để bàn (Desktop applications) sử dụng C# và WPF
- Các ứng dụng tuân theo mẫu thiết kế MVVM (Model-View-ViewModel)
- Các dự án sử dụng .NET 8.0 trở lên
- Các thành phần giao diện người dùng (UI components) được xây dựng bằng XAML
- Các giải pháp nhấn mạnh vào hiệu suất và khả năng phản hồi

## Mục tiêu

- Tạo mã soạn sẵn (boilerplate) cho `INotifyPropertyChanged` và `RelayCommand`
- Đề xuất sự tách biệt rõ ràng giữa logic của ViewModel và View
- Khuyến khích sử dụng `ObservableCollection<T>`, `ICommand`, và liên kết dữ liệu đúng cách
- Đề xuất các mẹo về hiệu suất (ví dụ: ảo hóa - virtualization, tải không đồng bộ - async loading)
- Tránh logic code-behind bị ràng buộc chặt chẽ
- Tạo ra các ViewModel có thể kiểm thử (testable)

## Ví dụ về các hành vi gợi ý

### ✅ Gợi ý tốt

- "Tạo một ViewModel cho màn hình đăng nhập với các thuộc tính cho tên người dùng và mật khẩu, và một LoginCommand"
- "Viết một đoạn mã XAML cho một ListView sử dụng ảo hóa giao diện người dùng (UI virtualization) và liên kết với một ObservableCollection"
- "Tái cấu trúc (refactor) trình xử lý sự kiện click trong code-behind này thành một RelayCommand trong ViewModel"
- "Thêm một biểu tượng tải (loading spinner) trong khi tìm nạp dữ liệu không đồng bộ trong WPF"

### ❌ Cần tránh

- Đề xuất logic nghiệp vụ (business logic) trong code-behind
- Sử dụng các trình xử lý sự kiện tĩnh (static event handlers) mà không có ngữ cảnh
- Tạo XAML bị ràng buộc chặt chẽ mà không có liên kết dữ liệu
- Đề xuất các phương pháp tiếp cận của WinForms hoặc UWP

## Các công nghệ ưu tiên

- C# với .NET 8.0+
- XAML với cấu trúc MVVM
- `CommunityToolkit.Mvvm` hoặc các triển khai `RelayCommand` tùy chỉnh
- Async/await cho giao diện người dùng không bị chặn (non-blocking UI)
- `ObservableCollection`, `ICommand`, `INotifyPropertyChanged`

## Các mẫu phổ biến cần tuân theo

- Liên kết dữ liệu theo hướng ViewModel-first
- Tiêm phụ thuộc (Dependency Injection) sử dụng .NET hoặc các bộ chứa của bên thứ ba (ví dụ: Autofac, SimpleInjector)
- Quy ước đặt tên trong XAML (PascalCase cho các điều khiển, camelCase cho các liên kết)
- Tránh các chuỗi ký tự "ma thuật" (magic strings) trong liên kết (sử dụng `nameof`)

## Các đoạn mã hướng dẫn mẫu mà Copilot có thể sử dụng

```csharp
public class MainViewModel : ObservableObject
{
    [ObservableProperty]
    private string userName;

    [ObservableProperty]
    private string password;

    [RelayCommand]
    private void Login()
    {
        // Thêm logic đăng nhập ở đây
    }
}
```

```xml
<StackPanel>
    <TextBox Text="{Binding UserName, UpdateSourceTrigger=PropertyChanged}" />
    <PasswordBox x:Name="PasswordBox" />
    <Button Content="Login" Command="{Binding LoginCommand}" />
```
