def cel_to_fahr():
  fahr = float(input("input fahr-degree: "))
  print("result:", (5 / 9) * (fahr - 32))


def add_all_digits(): 
  digit_str = input("number: ")
  number = int(digit_str)
  if not (0 < number < 1000):
    exit(1)
  sum = 0
  for _ in range(len(digit_str)):
    sum += number % 10
    number //= 10
  print(sum)


def interest_for_the_next_month():
  balance = float(input("Blanace: "))
  annual_interest_rate = float(input("Annual Interest Rate : "))
  print("interest", balance * (annual_interest_rate / 1200))


if __name__ == "__main__":
  # cel_to_fahr()
  # add_all_digits()
  # interest_for_the_next_month()
  pass