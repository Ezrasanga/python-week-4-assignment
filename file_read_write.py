# File Read & Write Challenge

def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()
        
        modified_content = modify_content(content)
        
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)
        
        print("✅ File processed successfully. Modified content written to output.txt")

    except FileNotFoundError:
        print("❌ Error: input.txt not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
