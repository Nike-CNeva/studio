from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from enum import Enum as PyEnum

# Enums (Duplicated from models.py for schema usage)
class ProductTypeEnum(str, PyEnum):
    PROFILE = "Профиля"
    KLAMER = "Клямера"
    BRACKET = "Кронштейны"
    EXTENSION_BRACKET = "Удлинители кронштейнов"
    CASSETTE = "Кассеты"
    FACING = "Фасонка"
    LINEAR_PANEL = "Линеарные панели"
    SHEET = "Листы"
    WALL_PANEL = "Стеновые панели(Продэкс)"
    OTHER = "Другое"

class UserTypeEnum(str, PyEnum):
    ADMIN = "Администратор"
    ENGINEER = "Инженер"
    OPERATOR = "Оператор"
    SUPERVISER = "Старший смены"
    
class ProfileTypeEnum(str, PyEnum):
    G40X40 = "Г-образный 40х40"
    G40X60 = "Г-образный 40х60"
    G50X50 = "Г-образный 50х50"
    P60 = "П-образный 60"
    P80 = "П-образный 80"
    P100 = "П-образный 100"
    Z20X20X40 = "З-образный 20х20х40"
    PGSH = "ПГШ"
    PVSH = "ПВШ"
    PNU = "ПНУ"
    OTHER = "Не стандрт"

class WorkshopEnum(str, PyEnum):
    PROFILE = "Прокат профилей"
    KLAMER = "Прокат клямеров"
    BRACKET = "Прокат кронштейнов"
    EXTENSION_BRACKET = "Гибка удлинителей кронштейнов"
    ENGINEER = "Инженер"
    BENDING = "Гибка"
    CUTTING = "Резка"
    COORDINATE_PUNCHING = "Координатка"
    PAINTING = "Покраска"

class ManagerEnum(str, PyEnum):
    NOVIKOV = "Новиков"
    SEMICHEV = "Семичев С."
    PTICHKINA = "Птичкина"
    VIKULINA = "Викулина"
    GAVRILOVEC = "Гавриловец"
    SEMICHEV_YOUNGER = "Семичев Д."

class KlamerTypeEnum(str, PyEnum):
    IN_LINE = "Рядный"
    STARTING = "Стартовый"
    ANGULAR = "Угловой"

class CassetteTypeEnum(str, PyEnum):
    KZT_STD = "Зактрытого типа(стандарт)"
    KOT_STD = "Открытого типа(стандарт)"
    KOTVO = "Открытого типа, отв. в вертикальных рустах"
    KZT = "Закрытого типа"
    KOT = "Открытого типа"
    OTHER = "Другое"

class MaterialFormEnum(str, PyEnum):
    SHEET = "Лист"
    COIL = "Рулон"
    STRIP = "Штрипс"

class MaterialTypeEnum(str, PyEnum):
    ALUMINIUM = "Алюминий"
    STEEL = "Сталь"
    STAINLESS_STEEL = "Нержавеющая сталь"
    ZINC = "Оцинковка"
    POLYMER = "Полимер"

class MaterialThicknessEnum(str, PyEnum):
    ZERO_FIVE = "0.5мм"
    ZERO_SEVEN = "0.7мм"
    ONE = "1.0мм"
    ONE_TWO = "1.2мм"
    ONE_FIVE = "1.5мм"
    TWO = "2.0мм"
    THREE = "3.0мм"

class UrgencyEnum(str, PyEnum):
    LOW = "Низкая"
    MEDIUM = "Нормальная"
    HIGH = "Высокая"

class StatusEnum(str, PyEnum):
    NEW = "Новая"
    IN_WORK = "В работе"
    COMPLETED = "Выполнена"
    CANCELED = "Отменена"
    ON_HOLD = "На удержании"

# Schemas
class UserBase(BaseModel):
    name: str
    firstname: Optional[str] = None
    email: Optional[str] = None
    telegram: Optional[str] = None
    username: str
    user_type: UserTypeEnum
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    name: Optional[str] = None
    firstname: Optional[str] = None
    email: Optional[str] = None
    telegram: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    user_type: Optional[UserTypeEnum] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class BidBase(BaseModel):
    task_number: Optional[str] = None
    customer_id: int
    manager: ManagerEnum

class BidCreate(BidBase):
    pass

class BidUpdate(BidBase):
    task_number: Optional[str] = None
    customer_id: Optional[int] = None
    manager: Optional[ManagerEnum] = None

class Bid(BidBase):
    id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    bid_id: int
    product_id: int
    material_id: int
    quantity: Optional[int] = None
    urgency: UrgencyEnum
    status: StatusEnum = StatusEnum.NEW
    waste: Optional[str] = None
    weight: Optional[str] = None
    completed_at: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    bid_id: Optional[int] = None
    product_id: Optional[int] = None
    material_id: Optional[int] = None
    quantity: Optional[int] = None
    urgency: Optional[UrgencyEnum] = None
    status: Optional[StatusEnum] = None
    waste: Optional[str] = None
    weight: Optional[str] = None
    completed_at: Optional[datetime] = None

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    name: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    type: ProductTypeEnum

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    type: Optional[ProductTypeEnum] = None

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class ProfileTypeBase(BaseModel):
    name: str

class ProfileTypeCreate(ProfileTypeBase):
    pass

class ProfileTypeUpdate(ProfileTypeBase):
    name: Optional[str] = None

class ProfileType(ProfileTypeBase):
    id: int

    class Config:
        from_attributes = True

class MaterialBase(BaseModel):
    form: str
    type: str
    thickness: str
    color_id: Optional[int]
    painting: bool

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    form: Optional[str]
    type: Optional[str]
    thickness: Optional[str]
    color_id: Optional[int]
    painting: Optional[bool]

class Material(MaterialBase):
    id: int

    class Config:
        from_attributes = True

class FilesBase(BaseModel):
    bid_id: int
    file_name: str
    file_path: str

class FilesCreate(FilesBase):
    pass

class FilesUpdate(FilesBase):
    bid_id: Optional[int]
    file_name: Optional[str]
    file_path: Optional[str]

class Files(FilesBase):
    id: int

    class Config:
        from_attributes = True
