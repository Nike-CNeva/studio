# **App Name**: Производственный Планировщик

## Core Features:

- Управление Пользователями и Ролями: Система управления пользователями с ролями: администратор, инженер, оператор, старший смены. Разграничение прав доступа в зависимости от роли.
- Управление Производственными Задачами: Создание и управление задачами для цехов: прокат профиля, клямеров, кронштейнов, гибка, резка, координатно-пробивной.  Возможность добавления документов (фото, PDF, NC файлы, Excel).
- Интерфейс для Цехов: Интуитивно понятный интерфейс для отображения задач в каждом цехе.  Фильтрация и сортировка задач по различным параметрам (заказчик, тип изделия, срочность, статус).
- Система Уведомлений: Уведомления о новых задачах, изменениях статуса и комментариях. Интеграция с Telegram для оперативных уведомлений.
- Автоматическое Извлечение Данных из PDF: Автоматическое заполнение полей (количество листов, отходность, количество изделий) на основе анализа загруженных PDF-файлов с чертежами. Use an AI tool to extract the information from the PDFs.

## Style Guidelines:

- Primary color: #3498db (Blue) for a professional and reliable feel.
- Secondary color: #ecf0f1 (Light Grey) for backgrounds and neutral elements.
- Accent: #f39c12 (Orange) for highlighting important actions and status indicators.
- Responsive design for accessibility across different devices (desktops, tablets, phones).
- Clear and consistent icons to represent different production processes and task statuses.
- Subtle transitions and animations to provide feedback on user interactions.

## Original User Request:
я работаю на производстве фасадных металлических изделий
(профиля, кронштейны, фасонка, металлокасеты, линеарные панели и прочее)
я являюсь начальником производства и мне нужно организовывать план работы.
есть такие цеха как:
раскрой листов на заготовки для будущей гибки по написанным программам для станков,
в данном цеху есть два координатно-пробивных станка(FinnPowerA5F и FinnPowerC5).
есть инженер который пишет программы для данных станков.
есть прокат профилей(настраеваемая линия под разные типы и длины профиля),
где из штрипса прокатывают профиль в зависимости от задач под клиента или на склад(штрипс поставляется поставщиками).
так же есть станок проката кронштейнов из штрипса(кронштейны могут иметь разные размеры ШхДхВ),
кронштейны производятся как на склад так и под клиента.
еще есть станок проката клямеров из штрипса
(клямера имеют 2 типа металла, 2 толщины металла, и 3 типа "рядный", "концевой", "угловой"(делаеться путем разрубания "рядного" пополам)).
есть станок по раскрою рулонов металла на листы(рулони получаем от поставщиков),
листы используются как готовая продукция, либо для цеха раскроя на заготовки, либо под дальнейший раскрой на гильотине,
в зависимости от задачи.
есть гильотина для раскроя заготовленных ранее листов на заготовки под гибку или иногда на более мелкие листы для заказчика.
так же есть несколько станков которые гнут заготовки в изделия:
есть листогибочный пресс с наборами пуансонов и матриц,
еще есть панелегиб "salvagnini" который в полуавтоматическом режиме изготавливает кассеты путем гибки.
еще есть 2 гибочных станка "SCHRÖDER" они так же как и панелегиб используются для гибки кассет, но могут использоватся и для других целей.
еще есть гибочный станок "Schechtl" на нем в основном гнется фасонка и синеарные панели.
еще есть правильная машина, для правки заготовок кассет после раскоя, перед гибкой, но это делается только при необходимости.
я бы хотел написать программу для составления и передачи плана(очередности) работы для каждого цеха или определенного станка, сотрудника.
что бы эта программа была как сервер в котором я как администратор создаю и распределяю списки заданий
а остальные сотрудники в зависимости от места работы могут подключится через интернет(с телефона или планшета) или локальную сеть(компьютеры в некоторых цехах),
для этого можно использовать отдельно написанную программу клиент или для простоты браузер, 
и в зависимости от того кто подключается, ему выводится список задач для исполнения,
где он может изменить статус задачи или написать комментарий при каких либо проблеммах.
нужна возможность добавления документов(фотографии заявок клиентов, pdf, nc(файлы для станков), exel таблицы с данными о задаче).
также нужно что бы у каждой задачи был номер, который вводится при создании задачи(берется из 1с предприятие) и  наименование заказчика,
так же поле с комментарием что бы можно было описать задачу или проблемы(ввод не обязателен).
нужны разные права доступа, что бы я как администратор мог создавать и управлять задачами, пользователями и другими функциями.
а остальные пользователи в зависимости от участка и должности,только смотреть или помечать готовность.
так же нужна функция уведомлений для того что бы каждый мог узнать о новой задачи или о готовности задач.
пример сценария:
я создаю план задач для инженера, линни раскроя металла на листы, на прокатные станки.
инженер выполняет план по очереди, подгружает файлы и ставит готовность, так же делает оператор линии раскроя металла на листы.
после того как инженер выполнил свою задачу из плана я могу перераспределить задачу в очередь задач цеха раскроя металла на листы.
после того как оператор линии раскроя на листывыполнил свою задачу из очереди и установил статус готов,
я перевожу данную задачу дальше в цех раскроя на заготовки или в цех гибки в зависимости от самой задачи,
так же статус готов может означать полное исполнение задачи если в ней требовалось нарезать просто листы.
цех раскроя на заготовки при частичном либо полном исполнении передает задачу в гибку.
я бы хотел использовать fastApi, pydantic без использования виртуального окружения. нужен полный бэкенд и так же полный фронтэнд со стилизацией и бутстрапом(или другим фреймворком)
нужно минимизировать количество файлов в проекте, но что бы структура была правильной.
создать правильную структуру будующей базы данных. создать структуру бэкенда и фронтенда. создать план реализации данного проекта.
добавить функции которые необходимы но небыли упомянуты. программирование и ответы должны быть для русскоязычного пользователя.
как я вижу отображение задач для разных цехов:

цех проката:
прокат профиля:
№ заявки: 542(может быть пустым)
Заказчик: Формула строительства (может быть склад, без номера заявки)
Вид профиля: Г60х40х3000 (есть много вариаций)
Количество профиля: 8000 штук (при этом в день делается не более 1500шт. так что хотелось бы это как то помечать в задаче)
Комментарий: (может быть пустым)
Дата размещения: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
заказчик, тип профиля, общее количество/осталось изготовить, срочность, статус 

прокат клямеров:
№ заявки: (обычно даже под склад создают заявку в 1с, но может быть пустым)
Заказчик: Склад
Тип клямера: Рядный 1.2 нерж 
Количество клямеров: 16000 штук (в день делается около 3000шт. так что тоже нужна пометка сколько готово на данный момент)
Комментарий: (может быть пустым)
Дата размещения: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
заказчик, тип клямера, общее количество/осталось изготовить, срочность, статус 

прокат кронштейнов:
№ заявки: 257(может быть пустым, если работаем под склад)
Заказчик: Формула строительства (может быть склад)
Тип кронштейна: 70х150х70х2 (возможны разные варианты(в одной заявке может быть несколько типов))
Количество кронштейнов: как в случае с профилями и клямерами нужно видеть прогрес
Комментарий: (может быть пустым)
Дата размещения: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
заказчик, тип кронштейна, общее количество/осталось изготовить, срочность, статус 


инженер:(как отдельный цех)
№ заявки:
Заказчик: Формула строительства
Ф.И.О. мененджера:
Тип: Кассеты закрытого типа стандартной формы (в одной заявке может быть несколько типов)
Металл: оцинкованный 1.2 (в одной заявке может быть несколько типов металла)
Общее количество изделий: из заявки
Файлы заказа: фото, exel, pdf, dxf, dwg...
Комментарий: (может быть пустым)
Дата размещения: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
(заполняется инженером или автоматически:)
Количество листов: (хотелось бы заполнять автоматически на основании pdf файлов загруженных инженером)
Отходность: (хотелось бы заполнять автоматически на основании pdf файлов загруженных инженером)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
№заявки, заказчик, тип, металл, количество, срочность, статус 


цех раскроя металла на листы(+гильотина):
№ заявки:
Заказчик: Формула строительства
Куда: (заказчик, координатка, гильотина)
Тип металла(+толщина): (в одной заявке может быть несколько типов металла)
Количество изделий: (если известно)
Размер и количество листов: (если есть данные(для гильотины оператор сам считает листы))
Комментарий: (может быть пустым)
Файлы: файлы из заявки + файлы инженера
Дата создания: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Вес: (записываеться оператором вес срезанного металла(может быть несколько пунктов))
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
№заявки, заказчик, куда, тип металла(+толщина), срочность, статус 


Цех гибки:(общий для всех станков)
№ заявки:
Заказчик:
Тип изделий: (фасонка, кассеты, линеарные панели, профиль, кронштейны. в одной заявке может быть несколько типов)
Тип металла(+толщина): (в одной заявке может быть несколько типов металла)
Количество изделий: 
Комментарий: (может быть пустым)
Файлы: файлы из заявки
Дата создания: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
№заявки, заказчик, тип изделий, тип металла(+толщина), количество изделий, срочность, статус


Координатно-пробивной цех: 
Станок: (A5F, C5 но не обязательно)
№заявки:
Заказчик:
Тип металла(+толщина): 
Количество листов: (хотелось бы заполнять автоматически на основании pdf файлов загруженных инженером)
Файлы: (.nc для станка(загружаются инженером) pdf (загружается инженером, по ним расчитывается количество и размер листов,
а так же количество и размер изделий)количество файлов может быть от 1 до нескольких сотен
(хотелось бы реализовать либо просмотр pdf с возможностью редактирования,
либо просто создавать страницы с необходимыми данными(укажу позднее)что бы оператор мог отображать ход исполнения заказа)
можно открывать изначально отображать только названия файлов и сделать кнопку "подробнее" что бы уже открывались файлы pdf для просмотра и указания процесса изготовления)
Количество изделий: (хотелось бы заполнять автоматически на основании pdf файлов загруженных инженером)
Комментарий: (может быть пустым)
Дата создания: на момент создания
Срочность: (срочно, оычно, не срочно)
Статус: (новая, в работе, ожидание, готово)
Дата завершения: (заполняется по факту завершения)
при этом когда мы смотрим список задач для данного станка хотелось бы видеть информацию:
№заявки, заказчик, тип металла(+толщина), количество листов, срочность, статус

мне нужно создать файл models.py для fastapi и Pydantic-схемы используя следующие данные.
если что то непонятно, уточни!
User:
id:(автоматически с проверкой пустых значений),
name:(обязательно),
firstname:(обязательно),
post:,
telegram:,
username:(обязательно),
password_hash:(обязательно),
role:(admin - Администратор, engineer - Инженер, operator - Оператор, supervisor - Старший смены),
workshop:(один юзер может иметь несколько, админ имеет все)(profile - Прокат профиля, klamer - Прокат клямера, bracket - Прокат кронштейнов, extension_bracket - Производство удлинительей кронштейна, engineer - Инженер, bending - Гибка, cutting - Резка листов, coordinate_punching - Координатно-пробивной цех),
is_active:

Bid:(вид полной задачи)
id:(автоматически с проверкой пустых значений),
task_number:,
customer:(обязательно),
manager_name:,
Task:
product_type:(может быть несколько)(profile(strip type: zink. strip thickness: 0.5, 1.0, 1.2. strip width: 78, 96, 124, 146, 167.), klamer(strip type: zink, stainless. strip thickness: 1.0, 1.2. strip width: 36, 66.), bracket(type: zink. strip thickness: 1.2, 2.0. strip width: 50, 70, 88, 93.), facing, cassette(kzt, kot, kotvo, kzt not standart, kot not standart, other), linear_panel, sheet, extension_bracket, wall panel),
material:(для каждого типа изделия)(sheet type: polymer - полимер, zink - цинк, stainless - нержавеющая сталь, blackness - черная сталь. sheet thickness: 0.5, 0.7, 1.0, 1.2, 1.5, 2.0, 3.0. strip type: zink, stainless. strip thickness: 0.5, 1.0, 1.2, 2.0. strip width: 36, 50, 66, 70, 78, 88, 93, 96, 124, 146, 167.),
quantity:(для каждого типа изделия)(обязательно),
urgency:(для каждого типа изделия)(urgent - срочно, normal - обычная, not_urgant - не срочно),
status:(для каждого типа изделия)(new - новая, in_progress - в работе, waiting - ожидание, done - готово),
workshop:(для каждого типа изделия)(profile, klamer, bracket, extension_bracket, engineer, bending, cutting, coordinate_punching),
responsible:(для каждого типа изделия, может быть несколько)(User(admin(profile, klamer, bracket, extension_bracket, engineer, bending, cutting, coordinate_punching), engineer(engineer), operator(profile), (klamer), (bracket), (extension_bracket), (bending), (cutting), (coordinate_punching), supervisor(extension_bracket, bending, cutting, coordinate_punching),
sheets_size_count:имеет значение только для(engineer, cutting, coordinate_punching),
waste:нужен только engineer,
weight:нужен только cutting,
files:(фотографии, изображения, pdf, nc, exel, dwg, dxf.),
comment:,
created_at:,
completed_at:

отображение задач в списке для:
admin: task_number, customer, product_type, material, quantity, sheets_size_count, urgency, status, workshop, created_at
profile: task_number, customer, product_type, quantity, urgency, status, created_at
klamer: task_number, customer, product_type, quantity, urgency, status, created_at
bracket: task_number, customer, product_type, quantity, urgency, status, created_at
extension_bracket: task_number, customer, product_type, quantity, urgency, status, created_at
engineer: task_number, customer, product_type, material, quantity, urgency, status, created_at
bending: task_number, customer, product_type, quantity, urgency, status, created_at
cutting: task_number, customer, product_type, material, sheets_size_count, urgency, status, created_at
coordinate_punching: task_number, customer, product_type, material, sheets_size_count, urgency, status, created_at

если в задаче несколько пунктов выводим:(пример для админа)
задача: task_number, customer
product_type(1): material, quantity, sheets_size_count, urgency, status, workshop, created_at
product_type(2): material, quantity, sheets_size_count, urgency, status, workshop, created_at
product_type(3): material, quantity, sheets_size_count, urgency, status, workshop, created_at
в зависимости от количества пунктов. по аналогии для других workshop

все пункты задачи не повашие в "отображение задач в списке для:" и "если в задаче несколько пунктов выводим:"
добавляем когда открываем просмотр задачи.

также нужны таблицы для: файлов(отображается только внутри задачи), комментариев(отображается только внутри задачи), уведомлений(привязка к User).
так же необходимо установить все необходимые ENUMS (Перечисления) и зависимости в таблицах

хочу, чтобы структура формы диктовалась бэкендом (FastAPI + Jinja2), нужно передавать данные о полях динамически и рендерить их на стороне фронтенда на основе JSON-ответа от сервера.
первое поле "номер заявки" вводится число.
следующее поле добавляется горизонтально "заказчик" выбираем из списка из бд , если нужного заказчика нет - пишем в поле нового
следующее поле добавляется горизонтально "мененджер" выбираем из списка из ENUM
ниже добавляем кнопку которая будет добавлять следующий список полей.
ниже поле "изделие" - выбираем изделие из списка загруженного из бд,
ниже в зависимости от выбора, должны отображаться поля если нужны:
для профиля - тип профиля(список ENUM), длина профиля;
для клямера - тип клямера(список ENUM);
для кронштейнов - ширина, длина, толщина;
для удлинителей кронштейнов - длина, ширина, пятка(чекбокс);
для кассет - тип кассет(список ENUM);
для линеарных панелей - рабочая(число), руст(число), длина, торцы(чекбокс);
для фасонки, листов, стеновых панелей и прочего - добавлять ничего не нужно.
ниже поле выбыбора формы материала из списка ENUM в зависимости от выбора изделия:
штрипсы для: профиль, клямер, кронштейн.
ролик для: удлинитель кронштейнов, кассет, линеарных панелей, фасонки, листов, прочего.
листы для: прифиль, кронштейнов, удлинителей кронштейнов, кассет, фасонки, линеарных панелей, листов, стеновых панелей, прочего.
далее горизонтально поле выбора типа материала из списка ENUM на основании выбора формы материала:
для штрипсы: Нержавеющая сталь, Оцинковка.
для рулонов: Оцинковка, Полимер.
для листов: Алюминий, Сталь, Нержавеющая сталь, Оцинковка, Полимер.
далее горизонтально на основании выбора типа материала нужно выбрать толщину материала:
для алюминия: 1.0, 2.0
для стали: 1.0, 1.5, 2.0
для нержавейки: 1.0, 1.2, 2.0
для цинка: 0.5, 0.7, 1.0, 1.2, 1.5, 2.0, 3.0
для полимера: 0.5, 0.7, 1.0, 1.2
далее горизонтально если выбран полимер для него нужно текстовое поле куда будем вводить цвет.
далее горизонтально нужен чекбокс который будет указыват кразятся изделия или нет.
ниже нужно поле для количества изделий.
ниже поле выбора срочности из списка ENUM.
ниже поле выбора статуса из списка ENUM.
ниже кнопка добавить лист которая рядом в строку добавляет поля для листов.
ширина, длина, количество.
ниже нужна кнопка для загрузки файлов.
ниже поле для комментариев.


профиля:
    тип профиля:
        поле ввода типа профиля(если выбран "не стандарт")
    длина профиля:
    количество профиля:
    материал:
        штрипс:
            оцинковка:
                0,5
                1,0
                1,2
клямера:
    тип клямера:
    количество:
    материал:
        штрипс:
            нержавейка:
                1,0
                1,2
            оцинковка:
                1,0
                1,2
кронштейны:
    ширина:
    длина:
    количество:
    материал:
        штрипс:
            оцинковка:
                2,0
удлинители кронштейнов:
    ширина:
    длина:
    угловой?:
    количество:
    материал:
        рулон:
            цинк:
                1,0
                1,2
        листы:
            нержавейка:
                1,0
                1,2
кассеты:
    тип кассет:
        поле описания(если выбрано "другое")
    количество:
    материал:
        рулон:
            цинк:
                0,7
                1,0
                1,2
            полимер:
                0,7
        листы:
            алюминий:
                1,0
                2,0
            оцинковка:
                1,5
                2,0
                3,0
            нержавейка:
                1,0
                1,2    
    цвет:
    красим?:(если не выбран "полимер")
линеарные панели:
    рабочая:
    руст:
    длина:
    закрытые торцы?:
    количество:
    материал:
        рулон:
            оцинковка:
                0,7
            полимер:
                0,7
    цвет:
    красим?:(если не выбран "полимер")
фасонка:
    количество:
    материал:
        рулон:
            полимер:
                0,5
                0,7
            цинк:
                0,5
                0,7
                1,0
                1,2
        листы:
            цинк:
                1,5
                2,0
                3,0
            нержавейка:
                1,0
                1,2
            чернина:
                1,5
                2,0
            алюминий:
                1,0
                2,0
    цвет:
    красим?:(если не выбран "полимер")
листы:
    количество:
    материал:
        рулон:
            полимер:
                0,5
                0,7
            цинк:
                0,5
                0,7
                1,0
                1,2
        листы:
            цинк:
                1,5
                2,0
                3,0
            нержавейка:
                1,0
                1,2
            чернина:
                1,5
                2,0
            алюминий:
                1,0
                2,0
    цвет:
    красим?:(если не выбран "полимер")
стеновые панели:
    количество:
    материал:
        листы:
            чернина:
                1,5
                2,0
            цинк:
                1,2
                1,5
                2,0
другое:
    количество:
    материал:
        штрипс:
            цинк:
                0,5
                1,0
                1,2
                2,0
            нержавейка:
                1,0
                1,2
        рулон:
            цинк:
                0,5
                0,7
                1,0
                1,2
            полимер:
                0,5
                0,7
        листы:
            алюминий:
                1,0
                2,0
            нержавейка:
                1,0
                1,2
            цинк:
                1,5
                2,0
                3,0
            чернина:
                1,5
                2,0
    цвет:
    красим?:(если не выбран "полимер")   ^ from sqlalchemy import JSON, Table, Column, Integer, String, Boolean, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func
from enum import Enum as PyEnum

# Enums
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

# Промежуточные таблицы (Many-to-Many)
user_workshop_association = Table(
    "user_workshop_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("workshop_id", Integer, ForeignKey("workshop.id"), primary_key=True)
)

task_responsible_association = Table(
    "task_responsible_association",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("task.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)

comment_user_association = Table(
    "comment_user_association",
    Base.metadata,
    Column("comment_id", Integer, ForeignKey("comment.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)

# Users Table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    telegram = Column(String(50), nullable=True, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    user_type = Column(Enum(UserTypeEnum), nullable=False)
    is_active = Column(Boolean, default=True)
    # Связь Many-to-Many с Task (Ответственные)
    tasks = relationship("Task", secondary=task_responsible_association, back_populates="responsible_users")
    workshops = relationship("Workshop", secondary=user_workshop_association, back_populates="users")
    comments = relationship("Comment", secondary=comment_user_association, back_populates="users")

# Bid Table
class Bid(Base):
    __tablename__ = "bid"
    id = Column(Integer, primary_key=True, index=True)
    task_number = Column(String(50), nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    manager = Column(Enum(ManagerEnum), nullable=False)
    files = relationship("Files", back_populates="bid", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="bid", cascade="all, delete-orphan")
    customer = relationship("Customer", back_populates="bid")


# Task Table
class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    bid_id = Column(Integer, ForeignKey("bid.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), nullable=False)
    material_id = Column(Integer, ForeignKey("material.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=True)
    urgency = Column(Enum(UrgencyEnum), nullable=False)
    status = Column(Enum(StatusEnum), default="NEW")
    waste = Column(String(50), nullable=True)
    weight = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # One-to-Many связи
    sheets = relationship("Sheets", back_populates="task", cascade="all, delete-orphan")
    
    bid = relationship("Bid", back_populates="tasks")
    product = relationship("Product", back_populates="tasks", cascade="all, delete-orphan", single_parent=True)
    material = relationship("Material", back_populates="tasks", cascade="all, delete-orphan", single_parent=True)
    # One-to-Many связь с Comment
    comments = relationship("Comment", back_populates="task", cascade="all, delete-orphan")
    workshops = relationship("TaskWorkshop", back_populates="task", cascade="all, delete-orphan")
    # Many-to-Many связи
   
    responsible_users = relationship("User", secondary=task_responsible_association, back_populates="tasks")

# Workshop Table
class Workshop(Base):
    __tablename__ = "workshop"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(WorkshopEnum), nullable=False)
    # Связь Many-to-Many с Task
    task_workshops = relationship("TaskWorkshop", back_populates="workshop", cascade="all, delete-orphan")
    users = relationship("User", secondary=user_workshop_association, back_populates="workshops")
    
# TaskWorkshop Table
class TaskWorkshop(Base):
    __tablename__ = "task_workshops"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id", ondelete="CASCADE"))
    workshop_id = Column(Integer, ForeignKey("workshop.id", ondelete="CASCADE"))
    status = Column(Enum(StatusEnum), default="ON_HOLD")  # Статус выполнения в цехе

    task = relationship("Task", back_populates="workshops")
    workshop = relationship("Workshop", back_populates="task_workshops")
    
# Customer Table
class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    bid = relationship("Bid", back_populates="customer")

# Product Table
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(ProductTypeEnum), nullable=False)
    tasks = relationship("Task", back_populates="product", uselist=False)
    profile = relationship("Profile", back_populates="product", cascade="all, delete-orphan")
    klamer = relationship("Klamer", back_populates="product", cascade="all, delete-orphan")
    bracket = relationship("Bracket", back_populates="product", cascade="all, delete-orphan")
    extension_bracket = relationship("ExtensionBracket", back_populates="product", cascade="all, delete-orphan")
    cassette = relationship("Cassette", back_populates="product", cascade="all, delete-orphan")
    linear_panel = relationship("LinearPanel", back_populates="product", cascade="all, delete-orphan")

# Profile Table
class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    profile_type_id = Column(Integer, ForeignKey("profile_type.id"), nullable=False)
    length = Column(Integer, nullable=False)
    product = relationship("Product", back_populates="profile")
    profile_type = relationship("ProfileType")

class ProfileType(Base):
    __tablename__ = "profile_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

# Klamer Table
class Klamer(Base):
    __tablename__ = "klamer"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    type = Column(Enum(KlamerTypeEnum), nullable=False)
    product = relationship("Product", back_populates="klamer")

# Bracket Table
class Bracket(Base):
    __tablename__ = "bracket"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    width = Column(Integer, nullable=False)
    length = Column(String(50), nullable=False)
    thickness = Column(Integer, nullable=False)
    product = relationship("Product", back_populates="bracket")

# Extension Bracket Table
class ExtensionBracket(Base):
    __tablename__ = "extension_bracket"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    width = Column(Integer, nullable=False)
    length = Column(String(50), nullable=False)
    heel = Column(Boolean, default=True)
    product = relationship("Product", back_populates="extension_bracket")

# Cassette Table
class Cassette(Base):
    __tablename__ = "cassette"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    cassette_type = Column(Enum(CassetteTypeEnum), nullable=False)
    description = Column(String(255), nullable=True)
    product = relationship("Product", back_populates="cassette")

# Linear Panel Table
class LinearPanel(Base):
    __tablename__ = "linear_panel"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    field = Column(Integer, nullable=False)
    rust = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    butt_end = Column(Boolean, nullable=False, default=False)
    product = relationship("Product", back_populates="linear_panel")

# Materials Tables
class Material(Base):
    __tablename__ = "material"
    id = Column(Integer, primary_key=True, index=True)
    form = Column(Enum(MaterialFormEnum), nullable=False)
    type = Column(Enum(MaterialTypeEnum), nullable=False)
    thickness = Column(Enum(MaterialThicknessEnum), nullable=False)
    color_id = Column(Integer, ForeignKey("material_color.id"), nullable=True)
    painting = Column(Boolean, default=False)
    tasks = relationship("Task", back_populates="material")
    color = relationship("MaterialColor", back_populates="materials")

# MaterialColor Table
class MaterialColor(Base):
    __tablename__ = "material_color"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    materials = relationship("Material", back_populates="color", passive_deletes=True)


# Additional Tables
class Sheets(Base):
    __tablename__ = "sheets"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)  # Привязываем к Task
    width_sheet = Column(Integer, ForeignKey("sheet_width.id"), nullable=False)
    length_sheet = Column(Integer, ForeignKey("sheet_length.id"), nullable=False )
    quantity = Column(Integer, nullable=False)
    # Обратная связь One-to-Many
    task = relationship("Task", back_populates="sheets")
    width = relationship("SheetWidth", back_populates="sheets")
    length = relationship("SheetLength", back_populates="sheets")

class SheetWidth(Base):
    __tablename__ = "sheet_width"
    id = Column(Integer, primary_key=True, index=True)
    width = Column(String(50), nullable=False, unique=True)
    sheets = relationship("Sheets", back_populates="width")

class SheetLength(Base):
    __tablename__ = "sheet_length"
    id = Column(Integer, primary_key=True, index=True)
    length = Column(String(50), nullable=False, unique=True)
    sheets = relationship("Sheets", back_populates="length")

class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    bid_id = Column(Integer, ForeignKey("bid.id"), nullable=False)  # Привязываем к Task
    file_name = Column(String(255), nullable=False)
    file_path = Column(String, nullable=False)

    # Обратная связь One-to-Many
    bid = relationship("Bid", back_populates="files")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    comment = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_read = Column(Boolean, default=False)


    # One-to-Many связь с Task
    task = relationship("Task", back_populates="comments")

    # Many-to-Many связь с User
    users = relationship("User", secondary=comment_user_association, back_populates="comments")
  