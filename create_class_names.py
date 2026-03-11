import os

print("=== PlantCare-AI: Create class_names.txt ===\n")

# Ask user for the correct path
print("Please paste the full path to your 'train' folder.")
print("Example: C:\\PlantCare-AI\\dataset\\train")
print("(It should contain folders like Apple___Apple_scab, Blueberry___healthy, etc.)\n")

train_dir = input("Enter train folder path: ").strip().strip('"\'')  # removes quotes if copied from explorer

if not os.path.exists(train_dir):
    print(f"\n❌ Error: Path not found!\n   {train_dir}")
    print("Please check the path and try again.")
    exit()

# Get class names
class_names = sorted(os.listdir(train_dir))
print(f"\n✅ Found {len(class_names)} classes!")

# Create model/class_names.txt
os.makedirs("model", exist_ok=True)
with open("model/class_names.txt", "w", encoding="utf-8") as f:
    for name in class_names:
        f.write(name + "\n")

print(f"✅ Successfully created: model/class_names.txt")
print("You can now delete this create_class_names.py file if you want.")