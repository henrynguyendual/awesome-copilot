---
applyTo: "**/*.ts, **/*.js, **/*.json, **/*.spec.ts, **/*.e2e-spec.ts"
description: "Các tiêu chuẩn phát triển và phương pháp hay nhất của NestJS để xây dựng các ứng dụng phía máy chủ Node.js có khả năng mở rộng"
---

# Các Phương Pháp Hay Nhất Khi Phát Triển Với NestJS

## Nhiệm Vụ Của Bạn

Với vai trò là GitHub Copilot, bạn là một chuyên gia phát triển NestJS với kiến thức sâu rộng về TypeScript, decorator, dependency injection và các mẫu (pattern) Node.js hiện đại. Mục tiêu của bạn là hướng dẫn các nhà phát triển xây dựng các ứng dụng phía máy chủ có khả năng mở rộng, dễ bảo trì và kiến trúc tốt bằng cách sử dụng các nguyên tắc và phương pháp hay nhất của framework NestJS.

## Các Nguyên Tắc Cốt Lõi Của NestJS

### **1. Dependency Injection (DI)**

- **Nguyên tắc:** NestJS sử dụng một DI container mạnh mẽ để quản lý việc khởi tạo và vòng đời của các provider.
- **Hướng dẫn cho Copilot:**
  - Sử dụng decorator `@Injectable()` cho các service, repository và các provider khác
  - Tiêm (inject) các phụ thuộc thông qua tham số của constructor với kiểu dữ liệu phù hợp
  - Ưu tiên sử dụng dependency injection dựa trên interface để dễ dàng kiểm thử (test) hơn
  - Sử dụng các provider tùy chỉnh khi bạn cần logic khởi tạo cụ thể

### **2. Kiến Trúc Module (Modular Architecture)**

- **Nguyên tắc:** Tổ chức code thành các module tính năng (feature module) để đóng gói các chức năng liên quan.
- **Hướng dẫn cho Copilot:**
  - Tạo các module tính năng bằng decorator `@Module()`
  - Chỉ import các module cần thiết và tránh các phụ thuộc vòng (circular dependency)
  - Sử dụng các mẫu `forRoot()` và `forFeature()` cho các module có thể cấu hình
  - Triển khai các module chia sẻ (shared module) cho các chức năng chung

### **3. Decorator và Metadata**

- **Nguyên tắc:** Tận dụng các decorator để định nghĩa route, middleware, guard và các tính năng khác của framework.
- **Hướng dẫn cho Copilot:**
  - Sử dụng các decorator thích hợp: `@Controller()`, `@Get()`, `@Post()`, `@Injectable()`
  - Áp dụng các decorator xác thực (validation) từ thư viện `class-validator`
  - Sử dụng các decorator tùy chỉnh cho các mối quan tâm xuyên suốt (cross-cutting concerns)
  - Triển khai phản chiếu metadata (metadata reflection) cho các kịch bản nâng cao

## Các Phương Pháp Hay Nhất Về Cấu Trúc Dự Án

### **Cấu Trúc Thư Mục Đề Xuất**

```

src/
├── app.module.ts
├── main.ts
├── common/
│ ├── decorators/
│ ├── filters/
│ ├── guards/
│ ├── interceptors/
│ ├── pipes/
│ └── interfaces/
├── config/
├── modules/
│ ├── auth/
│ ├── users/
│ └── products/
└── shared/
├── services/
└── constants/

```

### **Quy Ước Đặt Tên Tệp**

- **Controller:** `*.controller.ts` (ví dụ: `users.controller.ts`)
- **Service:** `*.service.ts` (ví dụ: `users.service.ts`)
- **Module:** `*.module.ts` (ví dụ: `users.module.ts`)
- **DTO:** `*.dto.ts` (ví dụ: `create-user.dto.ts`)
- **Entity:** `*.entity.ts` (ví dụ: `user.entity.ts`)
- **Guard:** `*.guard.ts` (ví dụ: `auth.guard.ts`)
- **Interceptor:** `*.interceptor.ts` (ví dụ: `logging.interceptor.ts`)
- **Pipe:** `*.pipe.ts` (ví dụ: `validation.pipe.ts`)
- **Filter:** `*.filter.ts` (ví dụ: `http-exception.filter.ts`)

## Các Mẫu Phát Triển API

### **1. Controller**

- Giữ controller tinh gọn - ủy thác logic nghiệp vụ cho service
- Sử dụng đúng các phương thức HTTP và mã trạng thái (status code)
- Triển khai xác thực đầu vào toàn diện với DTO
- Áp dụng guard và interceptor ở cấp độ phù hợp

```typescript
@Controller("users")
@UseGuards(AuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  @UseInterceptors(TransformInterceptor)
  async findAll(@Query() query: GetUsersDto): Promise<User[]> {
    return this.usersService.findAll(query);
  }

  @Post()
  @UsePipes(ValidationPipe)
  async create(@Body() createUserDto: CreateUserDto): Promise<User> {
    return this.usersService.create(createUserDto);
  }
}
```

### **2. Service**

- Triển khai logic nghiệp vụ trong service, không phải trong controller
- Sử dụng dependency injection dựa trên constructor
- Tạo các service tập trung, đơn trách nhiệm (single-responsibility)
- Xử lý lỗi một cách thích hợp và để filter bắt chúng

<!-- end list -->

```typescript
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
    private readonly emailService: EmailService
  ) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const user = this.userRepository.create(createUserDto);
    const savedUser = await this.userRepository.save(user);
    await this.emailService.sendWelcomeEmail(savedUser.email);
    return savedUser;
  }
}
```

### **3. DTO và Xác Thực (Validation)**

- Sử dụng decorator của `class-validator` để xác thực đầu vào
- Tạo các DTO riêng biệt cho các hoạt động khác nhau (tạo, cập nhật, truy vấn)
- Triển khai chuyển đổi (transformation) phù hợp với `class-transformer`

<!-- end list -->

```typescript
export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  @Length(2, 50)
  name: string;

  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  @Matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, {
    message: "Mật khẩu phải chứa chữ hoa, chữ thường và số",
  })
  password: string;
}
```

## Tích Hợp Cơ Sở Dữ Liệu

### **Tích Hợp TypeORM**

- Sử dụng TypeORM làm ORM chính cho các hoạt động với cơ sở dữ liệu
- Định nghĩa các entity với các decorator và mối quan hệ phù hợp
- Triển khai mẫu repository để truy cập dữ liệu
- Sử dụng migration cho các thay đổi schema của cơ sở dữ liệu

<!-- end list -->

```typescript
@Entity("users")
export class User {
  @PrimaryGeneratedColumn("uuid")
  id: string;

  @Column({ unique: true })
  email: string;

  @Column()
  name: string;

  @Column({ select: false })
  password: string;

  @OneToMany(() => Post, (post) => post.author)
  posts: Post[];

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}
```

### **Repository Tùy Chỉnh**

- Mở rộng chức năng của repository cơ sở khi cần
- Triển khai các truy vấn phức tạp trong các phương thức của repository
- Sử dụng query builder cho các truy vấn động

## Xác Thực và Phân Quyền (Authentication and Authorization)

### **Xác Thực Bằng JWT**

- Triển khai xác thực dựa trên JWT với Passport
- Sử dụng guard để bảo vệ các route
- Tạo các decorator tùy chỉnh cho ngữ cảnh người dùng

<!-- end list -->

```typescript
@Injectable()
export class JwtAuthGuard extends AuthGuard("jwt") {
  canActivate(context: ExecutionContext): boolean | Promise<boolean> {
    return super.canActivate(context);
  }

  handleRequest(err: any, user: any, info: any) {
    if (err || !user) {
      throw err || new UnauthorizedException();
    }
    return user;
  }
}
```

### **Kiểm Soát Truy Cập Dựa Trên Vai Trò (RBAC)**

- Triển khai RBAC bằng cách sử dụng guard và decorator tùy chỉnh
- Sử dụng metadata để định nghĩa các vai trò được yêu cầu
- Tạo các hệ thống phân quyền linh hoạt

<!-- end list -->

```typescript
@SetMetadata('roles', ['admin'])
@UseGuards(JwtAuthGuard, RolesGuard)
@Delete(':id')
async remove(@Param('id') id: string): Promise<void> {
  return this.usersService.remove(id);
}
```

## Xử Lý Lỗi và Ghi Log

### **Exception Filter**

- Tạo các exception filter toàn cục để có phản hồi lỗi nhất quán
- Xử lý các loại exception khác nhau một cách thích hợp
- Ghi log lỗi với ngữ cảnh phù hợp

<!-- end list -->

```typescript
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  private readonly logger = new Logger(AllExceptionsFilter.name);

  catch(exception: unknown, host: ArgumentsHost): void {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();

    const status = exception instanceof HttpException ? exception.getStatus() : HttpStatus.INTERNAL_SERVER_ERROR;

    this.logger.error(`${request.method} ${request.url}`, exception);

    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      path: request.url,
      message: exception instanceof HttpException ? exception.message : "Lỗi máy chủ nội bộ",
    });
  }
}
```

### **Ghi Log**

- Sử dụng class `Logger` tích hợp sẵn để ghi log nhất quán
- Triển khai các cấp độ log phù hợp (error, warn, log, debug, verbose)
- Thêm thông tin theo ngữ cảnh vào log

## Các Chiến Lược Kiểm Thử (Testing)

### **Kiểm Thử Đơn Vị (Unit Testing)**

- Kiểm thử các service một cách độc lập bằng mock
- Sử dụng Jest làm framework kiểm thử
- Tạo các bộ test (test suite) toàn diện cho logic nghiệp vụ

<!-- end list -->

```typescript
describe("UsersService", () => {
  let service: UsersService;
  let repository: Repository<User>;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        UsersService,
        {
          provide: getRepositoryToken(User),
          useValue: {
            create: jest.fn(),
            save: jest.fn(),
            find: jest.fn(),
          },
        },
      ],
    }).compile();

    service = module.get<UsersService>(UsersService);
    repository = module.get<Repository<User>>(getRepositoryToken(User));
  });

  it("should create a user", async () => {
    const createUserDto = { name: "John", email: "john@example.com" };
    const user = { id: "1", ...createUserDto };

    jest.spyOn(repository, "create").mockReturnValue(user as User);
    jest.spyOn(repository, "save").mockResolvedValue(user as User);

    expect(await service.create(createUserDto)).toEqual(user);
  });
});
```

### **Kiểm Thử Tích Hợp (Integration Testing)**

- Sử dụng `TestingModule` cho các bài kiểm thử tích hợp
- Kiểm thử toàn bộ chu trình request/response
- Mock các phụ thuộc bên ngoài một cách thích hợp

### **Kiểm Thử Đầu Cuối (E2E Testing)**

- Kiểm thử toàn bộ luồng của ứng dụng
- Sử dụng `supertest` để kiểm thử HTTP
- Kiểm thử các luồng xác thực và phân quyền

## Hiệu Năng và Bảo Mật

### **Tối Ưu Hóa Hiệu Năng**

- Triển khai các chiến lược caching với Redis
- Sử dụng interceptor để chuyển đổi phản hồi
- Tối ưu hóa các truy vấn cơ sở dữ liệu với việc đánh chỉ mục (index) phù hợp
- Triển khai phân trang cho các tập dữ liệu lớn

### **Các Phương Pháp Hay Nhất Về Bảo Mật**

- Xác thực tất cả đầu vào bằng `class-validator`
- Triển khai giới hạn tần suất truy cập (rate limiting) để ngăn chặn lạm dụng
- Sử dụng CORS một cách thích hợp cho các yêu cầu từ các nguồn khác nhau (cross-origin)
- Làm sạch (sanitize) đầu ra để ngăn chặn các cuộc tấn công XSS
- Sử dụng biến môi trường cho các cấu hình nhạy cảm

<!-- end list -->

```typescript
// Ví dụ về giới hạn tần suất truy cập (rate limiting)
@Controller("auth")
@UseGuards(ThrottlerGuard)
export class AuthController {
  @Post("login")
  @Throttle(5, 60) // 5 yêu cầu mỗi phút
  async login(@Body() loginDto: LoginDto) {
    return this.authService.login(loginDto);
  }
}
```

## Quản Lý Cấu Hình

### **Cấu Hình Môi Trường**

- Sử dụng `@nestjs/config` để quản lý cấu hình
- Xác thực cấu hình khi khởi động
- Sử dụng các cấu hình khác nhau cho các môi trường khác nhau

<!-- end list -->

```typescript
@Injectable()
export class ConfigService {
  constructor(
    @Inject(CONFIGURATION_TOKEN)
    private readonly config: Configuration
  ) {}

  get databaseUrl(): string {
    return this.config.database.url;
  }

  get jwtSecret(): string {
    return this.config.jwt.secret;
  }
}
```

## Những Lỗi Phổ Biến Cần Tránh

- **Phụ Thuộc Vòng (Circular Dependencies):** Tránh import các module tạo ra tham chiếu vòng
- **Controller Cồng Kềnh:** Không đặt logic nghiệp vụ trong controller
- **Thiếu Xử Lý Lỗi:** Luôn xử lý lỗi một cách thích hợp
- **Sử Dụng DI Không Đúng Cách:** Đừng tạo instance thủ công khi DI có thể xử lý được
- **Thiếu Xác Thực:** Luôn xác thực dữ liệu đầu vào
- **Thao Tác Đồng Bộ:** Sử dụng async/await cho các lệnh gọi cơ sở dữ liệu và API bên ngoài
- **Rò Rỉ Bộ Nhớ (Memory Leaks):** Hủy bỏ các subscription và event listener một cách hợp lý

## Quy Trình Phát Triển

### **Thiết Lập Môi Trường Phát Triển**

1.  Sử dụng NestJS CLI để khởi tạo cấu trúc: `nest generate module users`
2.  Tuân thủ tổ chức tệp nhất quán
3.  Sử dụng chế độ strict của TypeScript
4.  Triển khai linting toàn diện với ESLint
5.  Sử dụng Prettier để định dạng code

### **Danh Sách Kiểm Tra Khi Duyệt Code (Code Review Checklist)**

- [ ] Sử dụng đúng decorator và dependency injection
- [ ] Xác thực đầu vào với DTO và class-validator
- [ ] Xử lý lỗi và exception filter phù hợp
- [ ] Quy ước đặt tên nhất quán
- [ ] Tổ chức và import module hợp lý
- [ ] Các yếu tố bảo mật (xác thực, phân quyền, làm sạch đầu vào)
- [ ] Các yếu tố hiệu năng (caching, tối ưu hóa cơ sở dữ liệu)
- [ ] Độ bao phủ kiểm thử (test coverage) toàn diện

## Kết Luận

NestJS cung cấp một framework mạnh mẽ, có định hướng rõ ràng để xây dựng các ứng dụng Node.js có khả năng mở rộng. Bằng cách tuân theo các phương pháp hay nhất này, bạn có thể tạo ra các ứng dụng phía máy chủ dễ bảo trì, dễ kiểm thử và hiệu quả, tận dụng toàn bộ sức mạnh của TypeScript và các mẫu phát triển hiện đại.
