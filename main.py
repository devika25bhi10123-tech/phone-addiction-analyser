# ============================================================
#         📱 Phone Addiction Analyzer
#         A CLI tool to track and analyze your screen time
# ============================================================

import os

DATA_FILE = "data.txt"


# ------------------------------------------------------------
# 1. DATA STORAGE — Save a new screen time entry to file
# ------------------------------------------------------------
def save_entry(hours):
    """Append a new screen time entry to data.txt."""
    with open(DATA_FILE, "a") as f:
        f.write(f"{hours}\n")
    print("\n✅ Entry saved successfully!\n")


# ------------------------------------------------------------
# 2. USER INPUT — Ask for and validate screen time input
# ------------------------------------------------------------
def get_screen_time():
    """Prompt the user to enter daily screen time in hours."""
    print("\n" + "─" * 45)
    print("  📲  Enter Your Daily Screen Time")
    print("─" * 45)

    while True:
        try:
            hours = float(input("  How many hours did you spend on your phone today? "))
            if hours < 0:
                print("  ⚠️  Please enter a positive number.\n")
            elif hours > 24:
                print("  ⚠️  There are only 24 hours in a day! Try again.\n")
            else:
                return hours
        except ValueError:
            print("  ❌ Invalid input. Please enter a number (e.g. 3.5).\n")


# ------------------------------------------------------------
# 3. ADDICTION ANALYSIS — Classify usage and give feedback
# ------------------------------------------------------------
def analyze_usage(hours):
    """Classify screen time and display a message + suggestions."""
    print("\n" + "─" * 45)
    print(f"  📊  Analysis for {hours} hours of screen time")
    print("─" * 45)

    if hours < 3:
        category = "Healthy"
        emoji = "🟢"
        message = (
            "  🌟 Wow, look at you living your best life!\n"
            "  You're practically a productivity monk. Keep it up!"
        )
        suggestions = [
            "  ✅ Keep maintaining this healthy balance.",
            "  ✅ Try filling free time with a hobby, walk, or book.",
            "  ✅ You're setting a great example — tell a friend!",
        ]

    elif 3 <= hours <= 6:
        category = "Moderate"
        emoji = "🟡"
        message = (
            "  😐 Not bad, but your phone is starting to miss you\n"
            "  a little TOO much. Time to set some boundaries!"
        )
        suggestions = [
            "  💡 Try setting a daily screen time limit in your phone settings.",
            "  💡 Take a 10-minute break every hour — your eyes will thank you.",
            "  💡 Try leaving your phone in another room during meals.",
        ]

    else:
        category = "Addicted"
        emoji = "🔴"
        message = (
            "  😱 Uh oh! Your phone basically IS your hand at this point.\n"
            "  Time for a digital detox, friend!"
        )
        suggestions = [
            "  🚨 Set strict app limits — use built-in screen time tools.",
            "  🚨 Avoid using your phone 1 hour before bed (yes, really!).",
            "  🚨 Take a 5-minute break every 30 minutes of usage.",
            "  🚨 Try the '1 hour offline' challenge — you've got this!",
            "  🚨 Consider turning off non-essential notifications.",
        ]

    print(f"\n  {emoji}  Category: {category}\n")
    print(message)
    print("\n  📝 Suggestions:")
    for tip in suggestions:
        print(tip)

    print()
    save_entry(hours)


# ------------------------------------------------------------
# 4. REPORT — Read stored data and display statistics
# ------------------------------------------------------------
def view_report():
    """Read data.txt and display usage statistics."""
    print("\n" + "─" * 45)
    print("  📈  Your Usage Report")
    print("─" * 45)

    # Handle missing file
    if not os.path.exists(DATA_FILE):
        print("\n  ⚠️  No data found. Start by entering your screen time!\n")
        return

    try:
        with open(DATA_FILE, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        # Handle empty file
        if not lines:
            print("\n  ⚠️  Your data file is empty. Add some entries first!\n")
            return

        # Parse entries
        entries = [float(line) for line in lines]

        total_days   = len(entries)
        average_time = sum(entries) / total_days
        highest_time = max(entries)
        lowest_time  = min(entries)

        print(f"\n  📅  Days Tracked     : {total_days} day(s)")
        print(f"  ⏱️   Average Screen Time : {average_time:.2f} hours/day")
        print(f"  📈  Highest Screen Time : {highest_time:.2f} hours")
        print(f"  📉  Lowest Screen Time  : {lowest_time:.2f} hours")

        # Overall verdict based on average
        if average_time < 3:
            verdict = "🟢 Overall: Healthy lifestyle — keep it up!"
        elif average_time <= 6:
            verdict = "🟡 Overall: Moderate usage — room to improve."
        else:
            verdict = "🔴 Overall: High addiction risk — take action!"

        print(f"\n  {verdict}\n")

    except ValueError:
        print("\n  ❌ Data file contains invalid entries. Please check data.txt.\n")


# ------------------------------------------------------------
# 5. MENU — Main loop with options
# ------------------------------------------------------------
def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("   📱  PHONE ADDICTION ANALYZER  📱")
    print("=" * 45)
    print("   1️⃣   Enter daily screen time")
    print("   2️⃣   View usage report")
    print("   3️⃣   Exit program")
    print("─" * 45)


def main():
    """Main function — runs the app loop."""
    print("\n  Welcome to the 📱 Phone Addiction Analyzer!")
    print("  Track your screen time and take back your life.\n")

    while True:
        show_menu()

        try:
            choice = input("  👉 Enter your choice (1/2/3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  👋 Goodbye! Take care of yourself. 🌿\n")
            break

        if choice == "1":
            hours = get_screen_time()
            analyze_usage(hours)

        elif choice == "2":
            view_report()

        elif choice == "3":
            print("\n  👋 Thanks for using Phone Addiction Analyzer!")
            print("  🌿 Remember: real life happens off-screen. Goodbye!\n")
            break

        else:
            print("\n  ❌ Invalid choice. Please enter 1, 2, or 3.\n")


# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()