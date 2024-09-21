import argparse as ap

def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = ap.ArgumentParser()
    parser.add_argument("--physics",help="Enter marks of sub 1")
    parser.add_argument("--chemistry",help="Enter marks of sub 2")
    parser.add_argument("--maths",help="Enter marks of sub 3")

    # Parse the command-line arguments and store them in the 'args' object
    args = parser.parse_args()

    print(f"🎓 Marks in physics: {args.physics}\n🧪 Marks in chemistry: {args.chemistry}\n🔢 Marks in maths: {args.maths}")

    # Convert the string inputs for marks into integers
    m1 = int(args.physics)
    m2 = int(args.chemistry)
    m3 = int(args.maths)

    total_marks = m1 + m2 + m3
    average_marks = total_marks / 3
    print(f"\n🔢Total marks: {total_marks}\n📊Average marks: {average_marks:.2f}")

if __name__ == '__main__':
    main()