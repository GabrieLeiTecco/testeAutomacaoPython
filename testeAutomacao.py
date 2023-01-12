{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "284af7ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyautogui\n",
    "import time\n",
    "\n",
    "pyautogui.PAUSE = 1.5\n",
    "\n",
    "pyautogui.press(\"win\")\n",
    "pyautogui.write(\"chrome\")\n",
    "pyautogui.press(\"enter\")\n",
    "#pyautogui.hotkey(\"ctrl\", \"shift\", \"p\")\n",
    "pyautogui.write(\"fotos cachorros fofos\")\n",
    "pyautogui.press(\"enter\")\n",
    "pyautogui.click(x=235, y=225)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
