def stack_overflow(count:int):
    print(f"Trying to cause a stack overflow...{count}")
    stack_overflow(count + 1)

stack_overflow(0)