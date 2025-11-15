from decorator import limit_calls

@limit_calls(3)
def hello():
    print("Привіт! Я функція :)")

for i in range(5):
    try:
        hello()
    except Exception as e:
        print(e)
