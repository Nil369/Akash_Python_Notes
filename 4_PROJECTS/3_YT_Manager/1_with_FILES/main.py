import json
import time

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            videos = json.load(file)
            print("\n✅ Data loaded successfully!")
            return videos
    except FileNotFoundError:
        print("\n⚠️ No data found! Starting with an empty list.")
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
    print("💾 Data saved successfully!")

def list_all_videos(videos):
    print("\n" + "*" * 70)
    if not videos:
        print("📂 No videos available. Please add some videos first.")
    else:
        print("🎥 List of YouTube Videos:")
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} (⏱️ Duration: {video['time']})")
    print("*" * 70 + "\n")

def add_video(videos):
    name = input("🔤 Enter video name: ")
    duration = input("⏱️ Enter video duration: ")
    videos.append({'name': name, 'time': duration})
    save_data_helper(videos)
    print(f"✅ Video '{name}' added successfully!")

def update_video(videos):
    list_all_videos(videos)
    if videos:
        try:
            index = int(input("✏️ Enter the video number to update: "))
            if 1 <= index <= len(videos):
                name = input("🔤 Enter the new video name: ")
                duration = input("⏱️ Enter the new video duration: ")
                videos[index - 1] = {'name': name, 'time': duration}
                save_data_helper(videos)
                print(f"✅ Video {index} updated successfully!")
            else:
                print("❌ Invalid video index selected!")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    else:
        print("⚠️ No videos available to update.")

def delete_video(videos):
    list_all_videos(videos)
    if videos:
        try:
            index = int(input("🗑️ Enter the video number to delete: "))
            if 1 <= index <= len(videos):
                removed_video = videos.pop(index - 1)
                save_data_helper(videos)
                print(f"🗑️ Video '{removed_video['name']}' deleted successfully!")
            else:
                print("❌ Invalid video index selected!")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    else:
        print("⚠️ No videos available to delete.")

def main():
    videos = load_data()
    while True:
        print("\n📺 YouTube Manager | Choose an option:")
        print("1. 📋 List all YouTube videos")
        print("2. ➕ Add a YouTube video")
        print("3. ✏️ Update a YouTube video")
        print("4. 🗑️ Delete a YouTube video")
        print("5. 🚪 Exit the app")
        
        choice = input("🔢 Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("👋 Exiting the app. Goodbye!")
                time.sleep(1)
                break
            case _:
                print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

