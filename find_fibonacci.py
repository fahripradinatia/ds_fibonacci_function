def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    fibonacci_numbers = [0,1]

    for i in range(2,20):
      fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

    if x in fibonacci_numbers:
      return True
    else:
      return False

if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
