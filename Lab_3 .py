
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 1: Find numbers divisible by 7 and multiple of 5, between 1500 and 2700"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1505\n",
      "1540\n",
      "1575\n",
      "1610\n",
      "1645\n",
      "1680\n",
      "1715\n",
      "1750\n",
      "1785\n",
      "1820\n",
      "1855\n",
      "1890\n",
      "1925\n",
      "1960\n",
      "1995\n",
      "2030\n",
      "2065\n",
      "2100\n",
      "2135\n",
      "2170\n",
      "2205\n",
      "2240\n",
      "2275\n",
      "2310\n",
      "2345\n",
      "2380\n",
      "2415\n",
      "2450\n",
      "2485\n",
      "2520\n",
      "2555\n",
      "2590\n",
      "2625\n",
      "2660\n",
      "2695\n"
     ]
    }
   ],
   "source": [
    "for number in range(1500, 2701):\n",
    "    if (number % 7 == 0) and (number % 5 == 0):\n",
    "        print(number)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 2: Convert temperatures between Celsius and Fahrenheit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50°C is 122.0°F\n",
      "45°F is 7.222222222222222°C\n"
     ]
    }
   ],
   "source": [
    "def celsius_to_fahrenheit(celsius):\n",
    "    return (celsius * 9/5) + 32\n",
    "\n",
    "def fahrenheit_to_celsius(fahrenheit):\n",
    "    return (fahrenheit - 32) * 5/9\n",
    "\n",
    "celsius = 50\n",
    "fahrenheit = 45\n",
    "\n",
    "print(f\"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F\")\n",
    "print(f\"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 3: Guess a number between 1 to 9\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Try again!\n",
      "Try again!\n",
      "Try again!\n",
      "Well guessed!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "number_to_guess = random.randint(1, 9)\n",
    "\n",
    "while True:\n",
    "    guess = int(input(\"Guess a number between 1 and 9: \"))\n",
    "    if guess == number_to_guess:\n",
    "        print(\"Well guessed!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Try again!\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 4: Construct a pattern using nested for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
# @@ -162,10 +162,16 @@
    }
   ],
   "source": [
    "for i in range(1, 6):\n",
    "    print('*' * i)\n",
    "for i in range(4, 0, -1):\n",
    "    print('*' * i)\n"
    "\n",
    "for i in range(1, 6):  \n",
    "    for j in range(i):  \n",
    "        print('*', end='')  \n",
    "    print()  \n",
    "\n",
    "for i in range(4, 0, -1):  \n",
    "    for j in range(i):  \n",
    "        print('*', end='')  \n",
    "    print()  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 5: Reverse a word provided by the user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed word: dammah\n"
     ]
    }
   ],
   "source": [
    "word = input(\"Enter a word: \")\n",
    "reversed_word = word[::-1]\n",
    "print(\"Reversed word:\", reversed_word)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 6: Count the number of even and odd numbers from a series of numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of even numbers: 4\n",
      "Number of odd numbers: 5\n"
     ]
    }
   ],
   "source": [
    "numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)\n",
    "even_count = 0\n",
    "odd_count = 0\n",
    "\n",
    "for number in numbers:\n",
    "    if number % 2 == 0:\n",
    "        even_count += 1\n",
    "    else:\n",
    "        odd_count += 1\n",
    "\n",
    "print(\"Number of even numbers:\", even_count)\n",
    "print(\"Number of odd numbers:\", odd_count)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 7: Print each item and its corresponding type from a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1452 <class 'int'>\n",
      "11.23 <class 'float'>\n",
      "(1+2j) <class 'complex'>\n",
      "True <class 'bool'>\n",
      "w3resource <class 'str'>\n",
      "(0, -1) <class 'tuple'>\n",
      "[5, 12] <class 'list'>\n",
      "{'class': 'V', 'section': 'A'} <class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]\n",
    "\n",
    "for item in datalist:\n",
    "    print(item, type(item))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 8: Print numbers from 0 to 6 except 3 and 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for number in range(7):\n",
    "    if number == 3 or number == 6:\n",
    "        continue\n",
    "    print(number)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 9: Get the Fibonacci series between 0 to 50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "a, b = 0, 1\n",
    "\n",
    "while a <= 50:\n",
    "    print(a, end=' ')\n",
    "    a, b = b, a + b\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 10: Print \"FizzBuzz\" for multiples of 3 and 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 51):\n",
    "    if i % 3 == 0 and i % 5 == 0:\n",
    "        print(\"FizzBuzz\")\n",
    "    elif i % 3 == 0:\n",
    "        print(\"Fizz\")\n",
    "    elif i % 5 == 0:\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(i)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 11: Generate a two-dimensional array based on given rows and columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]\n"
     ]
    }
   ],
   "source": [
    "rows = 3\n",
    "cols = 4\n",
    "array = []\n",
    "\n",
    "for i in range(rows):\n",
    "    row = []\n",
    "    for j in range(cols):\n",
    "        row.append(i * j)\n",
    "    array.append(row)\n",
    "\n",
    "print(array)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 12: Accept a sequence of lines and print them in lower case\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi\n",
      "myself hammad\n",
      "i am doing python\n"
     ]
    }
   ],
   "source": [
    "lines = []\n",
    "\n",
    "while True:\n",
    "    line = input(\"Enter a line (blank line to terminate): \")\n",
    "    if not line:\n",
    "        break\n",
    "    lines.append(line.lower())\n",
    "\n",
    "for line in lines:\n",
    "    print(line)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 13: Print binary numbers divisible by 5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1010,101\n"
     ]
    }
   ],
   "source": [
    "binary_numbers = input(\"Enter 4-digit binary numbers separated by commas: \").split(',')\n",
    "divisible_by_5 = []\n",
    "for binary in binary_numbers:\n",
    "    decimal = int(binary, 2)  \n",
    "    if decimal % 5 == 0:      \n",
    "        divisible_by_5.append(binary)\n",
    "\n",
    "print(\",\".join(divisible_by_5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 14: Count the number of digits and letters in a string\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Letters: 6\n",
      "Digits: 2\n"
     ]
    }
   ],
   "source": [
    "s = \"Python 3.2\"\n",
    "letters = 0\n",
    "digits = 0\n",
    "\n",
    "for char in s:\n",
    "    if char.isdigit():\n",
    "        digits += 1\n",
    "    elif char.isalpha():\n",
    "        letters += 1\n",
    "\n",
    "print(\"Letters:\", letters)\n",
    "print(\"Digits:\", digits)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 15: Check the validity of a password\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Password is valid\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def check_password(password):\n",
    "    if (len(password) >= 6 and len(password) <= 16 and\n",
    "        re.search(r'[a-z]', password) and\n",
    "        re.search(r'[A-Z]', password) and\n",
    "        re.search(r'[0-9]', password) and\n",
    "        re.search(r'[$#@]', password)):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "password = input(\"Enter a password: \")\n",
    "if check_password(password):\n",
    "    print(\"Password is valid\")\n",
    "else:\n",
    "    print(\"Password is invalid\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}