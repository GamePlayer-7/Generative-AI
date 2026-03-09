def create_user(**details):
    print(f"User Details:")
    for key,value in details.items():
        print(f"{key}: {value}")

create_user(name="Sagar", age=32, city="Mumbai", job="Senior Engineer")
create_user(name="Rahul", age=28, city="Mumbai", job="Engineer")