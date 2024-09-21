import sqlite3
import time

# Database setup
def create_table():
    conn = sqlite3.connect('youtube.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect('youtube.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, duration FROM videos')
    videos = cursor.fetchall()
    conn.close()
    if videos:
        print("\n✅ Data loaded successfully!")
        return [{'id': video[0], 'name': video[1], 'time': video[2]} for video in videos]
    else:
        print("\n⚠️ No data found! Starting with an empty list.")
        return []

def save_data_helper(name, duration):
    conn = sqlite3.connect('youtube.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO videos (name, duration) VALUES (?, ?)', (name, duration))
    conn.commit()
    conn.close()
    print("💾 Video saved successfully!")

def list_all_videos(videos):
    print("\n" + "*" * 70)
    if not videos:
        print("📂 No videos available. Please add some videos first.")
    else:
        print("🎥 List of YouTube Videos:")
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} (⏱️ Duration: {video['time']})")
    print("*" * 70 + "\n")

def add_video():
    name = input("🔤 Enter video name: ")
    duration = input("⏱️ Enter video duration: ")
    save_data_helper(name, duration)
    print(f"✅ Video '{name}' added successfully!")

def update_video(videos):
    list_all_videos(videos)
    if videos:
        try:
            index = int(input("✏️ Enter the video number to update: "))
            if 1 <= index <= len(videos):
                video_id = videos[index - 1]['id']
                name = input("🔤 Enter the new video name: ")
                duration = input("⏱️ Enter the new video duration: ")
                conn = sqlite3.connect('youtube.db')
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE videos
                    SET name = ?, duration = ?
                    WHERE id = ?
                ''', (name, duration, video_id))
                conn.commit()
                conn.close()
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
                video_id = videos[index - 1]['id']
                conn = sqlite3.connect('youtube.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
                conn.commit()
                conn.close()
                print(f"🗑️ Video '{videos[index - 1]['name']}' deleted successfully!")
            else:
                print("❌ Invalid video index selected!")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    else:
        print("⚠️ No videos available to delete.")

def main():
    create_table()  # Create the table if it doesn't exist
    videos = load_data()
    while True:
        print("\n==================== 📺YouTube Manager | Choose an option =====================")
        print("1. 📋 List all YouTube videos")
        print("2. ➕ Add a YouTube video")
        print("3. ✏️ Update a YouTube video")
        print("4. 🗑️ Delete a YouTube video")
        print("5. 🚪 Exit the app")
        print("="*80)
        choice = input("🔢 Enter your choice: ")
        
        match choice:
            case '1':
                videos = load_data()  
                list_all_videos(videos)
            case '2':
                add_video()
            case '3':
                videos = load_data() 
                update_video(videos)
            case '4':
                videos = load_data()  
                delete_video(videos)
            case '5':
                print("👋 Exiting the app. Goodbye!")
                time.sleep(1)
                break
            case _:
                print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
