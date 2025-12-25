# tools.py
import datetime
import math
import random
import time
import re

# ---------------- Calculator ----------------
def calculator(expression):
    try:
        # Remove extra characters, keep only numbers/operators
        expr = "".join(re.findall(r"[0-9\+\-\*\/\(\)\.]+", expression))
        result = str(eval(expr))
        return f"ACTION: FINISH ANSWER: {result}"
    except:
        return f"ACTION: FINISH ANSWER: Invalid expression"

# ---------------- Calendar (India) ----------------
SPECIAL_DAYS = {
    "01-01": "New Year's Day",
    "14-01": "Makar Sankranti / Pongal",
    "14-02": "Valentine's Day",
    "17-03": "Holi (approximate)",
    "14-04": "Baisakhi / Tamil New Year / Vishu",
    "26-01": "Republic Day",
    "01-05": "Labour Day",
    "15-08": "Independence Day",
    "02-10": "Gandhi Jayanti",
    "21-06": "International Yoga Day",
    "05-09": "Teacher's Day",
    "30-01": "Martyrs' Day",
    "04-11": "Diwali (approximate)",
    "25-12": "Christmas",
    "31-10": "Halloween"
}

def calendar_tool(command):
    try:
        command = command.lower()
        # Special day query
        if "special" in command:
            match = re.search(r'(\d{1,2})[-/](\d{1,2})', command)
            if match:
                day, month = match.groups()
                key = f"{int(day):02d}-{int(month):02d}"
                output = SPECIAL_DAYS.get(key, "No special event found for this day")
                return f"ACTION: FINISH ANSWER: {output}"
            return "ACTION: FINISH ANSWER: Invalid special day format"

        # Day of week query
        match = re.search(r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', command)
        if match:
            day, month, year = match.groups()
            dt = datetime.date(int(year), int(month), int(day))
            weekday = dt.strftime("%A")
            return f"ACTION: FINISH ANSWER: {weekday}"

        return "ACTION: FINISH ANSWER: Invalid calendar command"
    except Exception as e:
        return f"ACTION: FINISH ANSWER: Error: {str(e)}"

# ---------------- Unit Conversion ----------------
def unit_conversion(command):
    try:
        parts = command.lower().split()
        if len(parts) != 4 or parts[0] != "convert":
            return "ACTION: FINISH ANSWER: Format: convert <value> <from_unit> <to_unit>"

        value = float(parts[1])
        from_unit = parts[2]
        to_unit = parts[3]

        if from_unit == "km" and to_unit == "miles":
            output = f"{value} km = {value * 0.621371:.2f} miles"
        elif from_unit == "miles" and to_unit == "km":
            output = f"{value} miles = {value / 0.621371:.2f} km"
        elif from_unit == "kg" and to_unit == "lb":
            output = f"{value} kg = {value * 2.20462:.2f} lb"
        elif from_unit == "lb" and to_unit == "kg":
            output = f"{value} lb = {value / 2.20462:.2f} kg"
        elif from_unit == "c" and to_unit == "f":
            output = f"{value}C = {value * 9/5 + 32:.2f}F"
        elif from_unit == "f" and to_unit == "c":
            output = f"{value}F = {(value - 32) * 5/9:.2f}C"
        else:
            output = "Conversion not supported"

        return f"ACTION: FINISH ANSWER: {output}"
    except:
        return "ACTION: FINISH ANSWER: Error in conversion command"

# ---------------- Multiplication Table ----------------
def multiplication_table(n):
    try:
        n = int(n)
        lines = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
        output = "\n".join(lines)
        return f"ACTION: FINISH ANSWER:\n{output}"
    except:
        return "ACTION: FINISH ANSWER: Invalid input for multiplication table"

# ---------------- Fibonacci Sequence ----------------
def fibonacci(n):
    try:
        n = int(n)
        if n <= 0:
            return "ACTION: FINISH ANSWER: Enter a positive integer"
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return f"ACTION: FINISH ANSWER: {seq[:n]}"
    except:
        return "ACTION: FINISH ANSWER: Invalid input for Fibonacci"

# ---------------- Factorial ----------------
def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "ACTION: FINISH ANSWER: Factorial not defined for negative numbers"
        return f"ACTION: FINISH ANSWER: {math.factorial(n)}"
    except:
        return "ACTION: FINISH ANSWER: Invalid input for factorial"


# ---------------- Prime / GCD / LCM ----------------
def is_prime(n):
    try:
        n = int(n)
        if n <= 1:
            output = f"{n} is not prime"
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    output = f"{n} is not prime"
                    break
            else:
                output = f"{n} is prime"
        return f"ACTION: FINISH ANSWER: {output}"
    except:
        return "ACTION: FINISH ANSWER: Invalid input for prime check"

def gcd(command):
    try:
        # Extract all integers from the command
        numbers = list(map(int, re.findall(r"-?\d+", command)))

        if len(numbers) < 2:
            return "ACTION: FINISH ANSWER: Please provide two integers for GCD"

        a, b = numbers[0], numbers[1]
        return f"ACTION: FINISH ANSWER: {math.gcd(a, b)}"

    except Exception as e:
        return f"ACTION: FINISH ANSWER: Error calculating GCD: {e}"

def lcm(command):
    try:
        # Extract all integers from the command
        numbers = list(map(int, re.findall(r"-?\d+", command)))

        if len(numbers) < 2:
            return "ACTION: FINISH ANSWER: Please provide two integers for LCM"

        a, b = numbers[0], numbers[1]
        lcm_value = abs(a * b) // math.gcd(a, b)
        return f"ACTION: FINISH ANSWER: {lcm_value}"

    except Exception as e:
        return f"ACTION: FINISH ANSWER: Error calculating LCM: {e}"


# ---------------- Current Time ----------------
def current_time(command=None):
    try:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return f"ACTION: FINISH ANSWER: {now}"
    except:
        return "ACTION: FINISH ANSWER: Error fetching current time"

# ---------------- Text Analysis ----------------
def text_analysis(text, mode="wordcount"):
    if mode == "wordcount":
        output = f"Word count: {len(text.split())}"
    elif mode == "charcount":
        output = f"Character count: {len(text)}"
    else:
        output = "Mode not supported (wordcount / charcount)"
    return f"ACTION: FINISH ANSWER: {output}"

# ---------------- Tools Dictionary ----------------
TOOLS = {
    "CALCULATOR": calculator,
    "CALENDAR": calendar_tool,
    "UNIT_CONVERSION": unit_conversion,
    "MULTIPLICATION_TABLE": multiplication_table,
    "FIBONACCI": fibonacci,
    "FACTORIAL": factorial,
    "IS_PRIME": is_prime,
    "GCD": gcd,
    "LCM": lcm,
    "CURRENT_TIME": current_time,
    "TEXT_ANALYSIS": text_analysis
}
