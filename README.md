# Multi-Speaker Video Transcription with WhisperX

Automatically transcribe videos with speaker identification using OpenAI Whisper and Pyannote speaker diarization. This project provides a complete solution for converting multi-speaker videos into timestamped transcripts with speaker labels.

## Features

- 🎙️ **High-Accuracy Transcription**: Uses OpenAI Whisper large-v2 model
- 👥 **Speaker Diarization**: Identifies and labels different speakers automatically
- ⏱️ **Precise Timestamps**: Word-level alignment for accurate timing
- 🆓 **Completely Free**: Runs on Google Colab free tier with GPU
- 📝 **Easy Name Mapping**: Simple script to replace speaker IDs with actual names
- 🌐 **English Support**: Optimized for English language videos


## Attributes

**Input**: 1-hour video with 3 speakers  
**Output**: Timestamped transcript with speaker identification

```
Patrick-Marketing [135.0s-140.1s]:  A lot of people saying hello in the chat, sharing where they're from, reporting the weather.
Dr-Brandy-Robinson [369.2s-372.0s]: The core modules are the required course load.
Jared-VP_Consumer [669.0s-675.0s]:  Then as you move through those six projects, they all tie to one of our core courses.
```

### Background

I regularly screen record important meetings for reference, including my capstone project discussions. These recordings are valuable but present challenges:
- Video files are very large (500+ MB)
- Manual transcription is extremely time-consuming
- Identifying who said what is difficult from memory

### Solution Workflow

1. **Record Meeting**: Screen record the session
   - Original file size: ~500 MB
   
2. **Compress Video**: Use [HandBrake](https://handbrake.fr/) to reduce file size
   - Original: 500 MB
   - Compressed: 199 MB (60% reduction)
   - Quality: Maintains audio clarity for transcription
   
3. **Transcribe**: Upload to Google Colab and run this pipeline
   
4. **Get Results**: Accurate transcript with speaker identification in 10-15 minutes

### HandBrake Compression Settings

To optimize video files for transcription while maintaining audio quality:

| Setting | Value | Reason |
|---------|-------|--------|
| Video Codec | H.264 | Universal compatibility |
| Quality | RF 28-30 | Balances size and clarity |
| Audio Codec | AAC | Efficient speech encoding |
| Audio Bitrate | 128 kbps | Perfect for speech |
| Frame Rate | 15 fps | Speech doesn't need high fps |

**Result**: 60% file size reduction with no loss in transcription accuracy!

### Benefits

- ✅ Searchable meeting notes
- ✅ Accurate speaker attribution  
- ✅ Timestamped references for follow-up
- ✅ Smaller file sizes for easier storage and upload
- ✅ Review key points without watching entire video
- ✅ Perfect for capstone projects, important meetings, and lectures

## Prerequisites

- Google account (for Google Colab)
- HuggingFace account (free)
- Video file (MP4, AVI, MOV, etc.)
- [Optional] HandBrake for video compression

## Quick Start

### 1. Setup HuggingFace Access

1. Create account at [HuggingFace](https://huggingface.co/join)
2. Generate access token at [Settings → Tokens](https://huggingface.co/settings/tokens)
3. Accept model licenses:
   - [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
   - [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)

### 2. Run in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

1. Open the notebook: `AI_capstone_transcript.ipynb`
2. Enable GPU: **Runtime → Change runtime type → T4 GPU**
3. Replace `INSERT-YOUR-HF-TOKEN` with your HuggingFace token
4. Upload our video and run all cells

## Installation (Local)

```bash
# Create virtual environment
python3 -m venv whisper-env
source whisper-env/bin/activate  # Windows: whisper-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: Download from https://ffmpeg.org/download.html
```

## Project Structure

```
capstone_text/
├── AI_capstone_transcript.ipynb    # Main Colab notebook
├── real_speakers_names.py          # Script to replace speaker IDs
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── transcript_with_speakers.txt    # Output file for speaker diarization
├── final_transcript.txt            # Output file for final transcript
├── meeting_summary.md              # summary of the meeting by using Perplexity

```

## Technologies Used

- **[OpenAI Whisper](https://github.com/openai/whisper)**: State-of-the-art speech recognition
- **[WhisperX](https://github.com/m-bain/whisperX)**: Enhanced Whisper with word-level timestamps
- **[Pyannote.audio](https://github.com/pyannote/pyannote-audio)**: Speaker diarization
- **PyTorch**: Deep learning framework
- **FFmpeg**: Audio/video processing

## Limitations

- Currently optimized for English language
- Requires clear audio quality for best results
- Speaker diarization accuracy depends on distinct voices
- Free Colab tier has ~12-hour daily GPU limit



## Acknowledgments

- OpenAI Whisper team for the incredible speech recognition model
- Max Bain for WhisperX implementation
- Pyannote team for speaker diarization models
- Google Colab for free GPU access

---

⭐ If you found this helpful, please star the repository!
