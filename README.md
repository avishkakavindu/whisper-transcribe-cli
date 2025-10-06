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

## Usage

### Get Help

View all available options:
```bash
python transcribe.py --help
```

### Basic Usage

Transcribe a file with default settings (base model, auto-detect language):
```bash
python transcribe.py video.mp4
```

### Choose a Different Model

Use `-m` or `--model` to specify model size:
```bash
python transcribe.py video.mp4 -m large
```

Available models (from fastest to most accurate):
- `tiny` - Fastest, lowest accuracy
- `base` - Good balance (default)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy, slowest

### Specify Output File

Use `-o` or `--output` to set a custom output path:
```bash
python transcribe.py audio.mp3 -o my_transcript.txt
```

### Specify Language

Use `-l` or `--language` to set the language (auto-detect if not specified):
```bash
python transcribe.py video.mkv -l es  # Spanish
python transcribe.py video.mkv -l fr  # French
python transcribe.py video.mkv -l de  # German
```

### Complete Examples

```bash
# Basic transcription with default settings
python transcribe.py "my-recording.mp4"

# High accuracy transcription
python transcribe.py "interview.mkv" -m large

# Spanish audio with custom output
python transcribe.py "podcast.mp3" -m medium -l es -o "podcast_transcript.txt"

# Quick transcription of long video
python transcribe.py "long-video.mp4" -m tiny
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
