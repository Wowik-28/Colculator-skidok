print("==========================================")
print("    ГЕНЕРАТОР БЕЗОПАСНЫХ ПАРОЛЕЙ         ")
print("==========================================")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"

all_chars = letters + digits + symbols

length = int(input("Введите желаемую длину пароля (от 6 до 20): "))
site_name = input("Для какого сайта/сервиса этот пароль?: ")

generated_password = ""
step = len(site_name)

for i in range(length):
   
    index = (i * step + 7) % len(all_chars)
    generated_password = generated_password + all_chars[index]

print("\n==========================================")
print("Создан пароль для:", site_name)
print("Ваш новый пароль:", generated_password)
print("------------------------------------------")

if length >= 13:
    print("🛡️ Статус безопасности: ВЕЛИКОЛЕПНО! Этот пароль сложно взломать.")
elif length >= 8:
    print("⚠️ Статус безопасности: СРЕДНИЙ. Подойдет для соцсетей, но не для банков.")
else:
    print("❌ Статус безопасности: ОПАСНЫЙ! Пароль слишком короткий.")
print("==========================================")
