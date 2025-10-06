# Video & Audio Transcription Tool

A user-friendly Python tool to transcribe video and audio files using OpenAI's Whisper model.

## Features

- 🎙️ Transcribes video and audio files to text using Whisper AI
- 📊 File validation and progress indicators
- 🌍 Multi-language support with auto-detection
- 🎯 Multiple accuracy levels (5 model sizes)
- 📁 Custom output path support
- ✨ Clean, intuitive command-line interface with helpful error messages
- 📝 Automatic transcript preview after completion

## Prerequisites

- Python 3.7 or higher
- FFmpeg (required by Whisper for audio processing)

## Installation

1. **Install FFmpeg**
   - **Windows**:
     - Install Chocolatey first: [chocolatey.org/install](https://chocolatey.org/install)
     - Then run: `choco install ffmpeg`
     - Or download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install directly:
   ```bash
   pip install openai-whisper
   ```

   Note: This will also install PyTorch and other required dependencies.

## Quick Start

**Simplest usage:**
```bash
python transcribe.py your-video.mp4
```

This will:
1. Load the base model (good balance of speed and accuracy)
2. Transcribe in English (default language)
3. Save to `your-video_transcript.txt` in the same directory
4. Show a preview of the transcript when complete

## Usage Guide

### Command Structure

```bash
python transcribe.py <file> [OPTIONS]
```

**Required:**
- `<file>` - Path to your video or audio file

**Optional flags:**
- `-m, --model` - Choose model size (tiny/base/small/medium/large)
- `-o, --output` - Specify custom output file path
- `-l, --language` - Set language code (default: en)
- `--help` - Show help message with all options

### Get Help

View all available options and examples:
```bash
python transcribe.py --help
```

### Step-by-Step Examples

#### 1. Basic Transcription (Recommended for Most Users)

```bash
python transcribe.py "meeting-recording.mp4"
```

**What happens:**
- ⏳ Downloads/loads the `base` model (once, ~140MB)
- 🎙️ Transcribes audio in English
- 💾 Saves to `meeting-recording_transcript.txt`
- 📝 Shows preview of first 500 characters

**Expected time:** ~1-2 minutes per hour of audio (CPU), faster with GPU

#### 2. High Accuracy Transcription

For important content where accuracy matters (interviews, lectures, legal recordings):

```bash
python transcribe.py "interview.mp4" -m large
```

**What changes:**
- Uses `large` model (~2.9GB, downloaded once)
- Much more accurate but slower
- Best for professional use

**Expected time:** ~5-10 minutes per hour of audio (CPU)

#### 3. Quick Draft Transcription

For long videos where you need a quick rough transcript:

```bash
python transcribe.py "3-hour-lecture.mp4" -m tiny
```

**What changes:**
- Uses `tiny` model (~39MB)
- Fastest processing
- Lower accuracy, may have more errors

**Expected time:** ~30 seconds per hour of audio (CPU)

#### 4. Non-English Content

For Spanish, French, German, or other languages:

```bash
python transcribe.py "spanish-podcast.mp3" -l es
python transcribe.py "french-video.mp4" -l fr
python transcribe.py "german-interview.mkv" -l de
```

**Common language codes:**
- `en` - English (default)
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `zh` - Chinese
- `ar` - Arabic

[See full list of supported languages](https://github.com/openai/whisper#available-models-and-languages)

#### 5. Custom Output Location

Save transcript to a specific location:

```bash
python transcribe.py "video.mp4" -o "C:/Documents/transcripts/my-transcript.txt"
```

Or organize by date:

```bash
python transcribe.py "meeting.mp4" -o "transcripts/2025-10-06-meeting.txt"
```

#### 6. Combined Options

For maximum accuracy Spanish podcast with custom output:

```bash
python transcribe.py "podcast-ep1.mp3" -m large -l es -o "transcripts/episode-1.txt"
```

### Model Comparison

| Model | Size | Speed | Accuracy | Best For |
|-------|------|-------|----------|----------|
| `tiny` | 39 MB | ⚡⚡⚡⚡⚡ | ⭐⭐ | Quick drafts, testing |
| `base` | 140 MB | ⚡⚡⚡⚡ | ⭐⭐⭐ | **Default - balanced** |
| `small` | 460 MB | ⚡⚡⚡ | ⭐⭐⭐⭐ | Better accuracy |
| `medium` | 1.5 GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | Professional work |
| `large` | 2.9 GB | ⚡ | ⭐⭐⭐⭐⭐⭐ | Maximum accuracy |

**Note:** First run downloads the model. Subsequent runs are faster.

### What You'll See While Running

```
============================================================
  VIDEO/AUDIO TRANSCRIPTION TOOL
  Powered by OpenAI Whisper
============================================================

📁 File: your-video.mp4
📊 Size: 245.67 MB

⏳ Loading Whisper model 'base'...
   (This may take a moment on first run)
✓ Model loaded successfully!

🎙️  Transcribing audio...
   (This may take several minutes depending on file length)

[Whisper progress output appears here]

============================================================
✅ SUCCESS! Transcript saved to:
   your-video_transcript.txt
============================================================

📝 Preview:
------------------------------------------------------------
[First 500 characters of your transcript...]
------------------------------------------------------------
```

## Output

By default, transcripts are saved with `_transcript.txt` suffix:
- Input: `video.mkv` → Output: `video_transcript.txt`
- Input: `audio.mp3` → Output: `audio_transcript.txt`

You can customize the output path using the `-o` flag.

## Supported Formats

**Video formats:**
- `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`

**Audio formats:**
- `.mp3`, `.wav`, `.m4a`, `.flac`

## Troubleshooting

### FFmpeg not found
If you get an error about FFmpeg not being found, ensure it's installed and in your system PATH.

### Out of memory
If you run out of memory with larger models, try using a smaller model size (e.g., `tiny` or `base`).

### CUDA errors
Whisper will automatically use GPU if available. If you encounter CUDA errors, it will fall back to CPU processing.

## License

This project uses OpenAI's Whisper model. See [Whisper repository](https://github.com/openai/whisper) for license details.
