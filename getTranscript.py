from youtube_transcript_api import YouTubeTranscriptApi

def getVideoTranscript(youtubeLink):
    videoId = None
    if "watch?v=" in youtubeLink:
        videoId = youtubeLink.split("watch?v=")[1]
    else:
        print("Cannot get the video id from the given link.")
        exit()

    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId,languages=['zh-TW', 'en'])
        fullText = ""
        for text in transcript:
            fullText += text['text'] + " "
        return fullText
    except Exception as e:
        return f'Youtube Link Extraction Error: {e}'

