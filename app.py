import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import re

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- 1. EXTRACT VIDEO ID ---
def extract_video_id(url):
    regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None


# --- 2. TRANSCRIPT EXTRACTION (OLD API SAFE VERSION) ---
def extract_transcript_details(video_id):
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

    try:
        ytt_api = YouTubeTranscriptApi()

        transcript = ytt_api.fetch(video_id)

        text = " ".join([item.text for item in transcript])
        return text

    except (TranscriptsDisabled, NoTranscriptFound):
        st.error(" No captions available for this video.")
        return None

    except Exception as e:
        st.error(f" Transcript Error: {str(e)}")
        return None


# --- 3. GEMINI AI GENERATION ---
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-3-flash-preview")
    response = model.generate_content(prompt + transcript_text)
    return response.text


# --- 4. STREAMLIT UI ---
st.set_page_config(page_title="YouTube Summarizer")
st.title("YouTube Transcript to Detailed Notes Converter")

prompt_template = """
You are an AI note-making assistant.

Convert the following YouTube transcript into:
- Clear structured notes
- Bullet points
- Key insights
- Important examples (if any)

Keep it concise but informative (within 250 words).

Transcript:
"""

youtube_link = st.text_input("Enter YouTube Video Link:")

# Show thumbnail
if youtube_link:
    video_id = extract_video_id(youtube_link)

    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    else:
        st.warning("Please enter a valid YouTube URL.")

# Button click
if st.button("Get Detailed Notes"):
    video_id = extract_video_id(youtube_link)

    if video_id:
        with st.spinner("Fetching transcript and generating notes..."):
            transcript_data = extract_transcript_details(video_id)

            if transcript_data:
                summary = generate_gemini_content(transcript_data, prompt_template)
                st.markdown("## 📝 Detailed Notes:")
                st.write(summary)
            else:
                st.warning("Try another video with captions enabled.")

    else:
        st.error("Please provide a valid link first.")
