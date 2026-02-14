
import json

def load_data():
    try:
        with open("youtube_videos.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def list_all_videos(videos):
    print("\n" + "*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']} | Duration: {video['duration']} | Channel: {video['channel']}")
    print("*" * 70)

def add_video(videos):
    title = input("Enter video title: ")
    duration = input("Enter video duration: ")
    channel = input("Enter video channel: ")
    videos.append({"title": title, "duration": duration, "channel": channel})
    save_data(videos)

def save_data(videos):
    with open("youtube_videos.txt", "w") as file:
        json.dump(videos, file, indent=4)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        title = input("Enter new video title: ")
        duration = input("Enter new video duration: ")
        channel = input("Enter new video channel: ")
        videos[index] = {"title": title, "duration": duration, "channel": channel}
        save_data(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data(videos)
    else:
        print("Invalid index")
    pass


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Please select an option:")
        print("1. Add a Youtube video")
        print("2. List all Youtube videos")
        print("3. Update a Youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the application")
        input_option = input("Enter your choice ")

        match input_option:
            case "1":
                add_video(videos)
            case "2":
                list_all_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid option, please try again")


if __name__ == "__main__":
    main()
