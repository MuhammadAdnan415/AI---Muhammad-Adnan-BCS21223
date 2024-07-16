{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Implement Stack using Python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stack Created\n",
      "5 Pushed into Stack\n",
      "15 Pushed into Stack\n",
      "25 Pushed into Stack\n",
      "35 Pushed into Stack\n",
      "45 Pushed into Stack\n",
      "45 Popped from Stack\n",
      "35 is the Top Element\n",
      "[35, 25, 15, 5]\n"
     ]
    }
   ],
   "source": [
    "class Stack:\n",
    "    def __init__(self):\n",
    "        self.stack = []\n",
    "        print(\"Stack Created\")\n",
    "\n",
    "    def push(self, data):\n",
    "        self.stack.append(data)\n",
    "        print(data, \"Pushed into Stack\")\n",
    "\n",
    "    def pop(self):\n",
    "        if len(self.stack) == 0:\n",
    "            return \"Stack is Empty\"\n",
    "        else:\n",
    "            print(self.stack[-1], \"Popped from Stack\")\n",
    "            return self.stack.pop()\n",
    "\n",
    "    def peek(self):\n",
    "        if len(self.stack) == 0:\n",
    "            return \"Stack is Empty\"\n",
    "        else:\n",
    "            print(self.stack[-1], \"is the Top Element\")\n",
    "            return self.stack[-1]\n",
    "\n",
    "    def display(self):\n",
    "        if len(self.stack) == 0:\n",
    "            return \"Stack is Empty\"\n",
    "        else:\n",
    "            return self.stack[::-1]\n",
    "\n",
    "\n",
    "stack = Stack()\n",
    "stack.push(5)\n",
    "stack.push(15)\n",
    "stack.push(25)\n",
    "stack.push(35)\n",
    "stack.push(45)\n",
    "stack.pop()\n",
    "stack.peek()\n",
    "print(stack.display())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Implement Queue using Python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Queue Created\n",
      "5 Enqueued into Queue\n",
      "15 Enqueued into Queue\n",
      "25 Enqueued into Queue\n",
      "35 Enqueued into Queue\n",
      "45 Enqueued into Queue\n",
      "5 Dequeued from Queue\n",
      "15 is the Front Element\n",
      "55 Enqueued into Queue\n",
      "15 Dequeued from Queue\n",
      "[25, 35, 45, 55]\n"
     ]
    }
   ],
   "source": [
    "class Queue:\n",
    "    def __init__(self):\n",
    "        self.queue = []\n",
    "        print(\"Queue Created\")\n",
    "\n",
    "    def enqueue(self, data):\n",
    "        self.queue.append(data)\n",
    "        print(data, \"Enqueued into Queue\")\n",
    "\n",
    "    def dequeue(self):\n",
    "        if len(self.queue) == 0:\n",
    "            return \"Queue is Empty\"\n",
    "        else:\n",
    "            print(self.queue[0], \"Dequeued from Queue\")\n",
    "            return self.queue.pop(0)\n",
    "\n",
    "    def peek(self):\n",
    "        if len(self.queue) == 0:\n",
    "            return \"Queue is Empty\"\n",
    "        else:\n",
    "            print(self.queue[0], \"is the Front Element\")\n",
    "            return self.queue[0]\n",
    "\n",
    "    def display(self):\n",
    "        if len(self.queue) == 0:\n",
    "            return \"Queue is Empty\"\n",
    "        else:\n",
    "            return self.queue\n",
    "\n",
    "\n",
    "queue = Queue()\n",
    "queue.enqueue(5)\n",
    "queue.enqueue(15)\n",
    "queue.enqueue(25)\n",
    "queue.enqueue(35)\n",
    "queue.enqueue(45)\n",
    "queue.dequeue()\n",
    "queue.peek()\n",
    "queue.enqueue(55)\n",
    "queue.dequeue()\n",
    "print(queue.display())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# In computer science, a binary search or half-interval search algorithm finds the position of a target value within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and executes in logarithmic time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element is present at index 4\n"
     ]
    }
   ],
   "source": [
    "def binary_search(arr, x):\n",
    "    low = 0\n",
    "    high = len(arr) - 1\n",
    "\n",
    "    while low <= high:\n",
    "        mid = (high + low) // 2\n",
    "\n",
    "        if arr[mid] < x:\n",
    "            low = mid + 1\n",
    "\n",
    "        elif arr[mid] > x:\n",
    "            high = mid - 1\n",
    "\n",
    "        else:\n",
    "            return mid\n",
    "\n",
    "    return -1\n",
    "\n",
    "\n",
    "arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]\n",
    "\n",
    "\n",
    "result = binary_search(arr, 10)\n",
    "\n",
    "if result != -1:\n",
    "    print(\"Element is present at index\", result)\n",
    "else:\n",
    "    print(\"Element is not present in array\")"
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
