# Error Handling Lab

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("\n📄 File content:")
            print(f.read())
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: Permission denied.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def main():
    filename = input("Enter the filename: ")
    read_file(filename)

if __name__ == "__main__":
    main()
