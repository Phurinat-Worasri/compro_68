def example_w_plus_mode():
    with open('exemp_e_w+.txt','w+') as file:
        file.write("This is the first line n the file.\n")
        file.write("This is the secone line n the file.\n")

        file.seek(0)

        content = file.read()
        print("Countent of the file:")
        print(countent)
example_w_plus_mode()