def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()

inner_function() # NameError потому что не существует вне области видимости test_function)