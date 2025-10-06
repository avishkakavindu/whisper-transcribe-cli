import whisper
import argparse
import os
from pathlib import Path
import sys

# Supported file formats
SUPPORTED_FORMATS = [
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".mp3",
    ".wav",
    ".m4a",
    ".flac",
    ".webm",
]
VALID_MODELS = ["tiny", "base", "small", "medium", "large"]


def print_banner():
    """Welcome banner"""
    print("=" * 60)
    print("  VIDEO/AUDIO TRANSCRIPTION TOOL")
    print("  Powered by OpenAI Whisper")
    print(" please refer to usage instructions in readme")
    print("=" * 60)
    print()


def validate_file(file_path):
    """
    Validate that the file exists and is a supported format

    Args:
        file_path: Path to the file

    Returns:
        tuple: (is_valid, error_message)
    """
    if not os.path.exists(file_path):
        return False, f"File not found: '{file_path}'"

    file_ext = Path(file_path).suffix.lower()
    if file_ext not in SUPPORTED_FORMATS:
        return (
            False,
            f"Unsupported file format: '{file_ext}'\nSupported formats: {', '.join(SUPPORTED_FORMATS)}",
        )

    return True, None


def transcribe_video(video_path, model_size="base", output_path=None, language="en"):
    """
    Transcribe a video/audio file using OpenAI Whisper

    Args:
        video_path: Path to the video/audio file
        model_size: Whisper model size (tiny, base, small, medium, large)
        output_path: Custom output path (optional)
        language: Language code (default: "en" for English)
    """
    # Validate file
    is_valid, error_msg = validate_file(video_path)
    if not is_valid:
        print(f"\n❌ Error: {error_msg}")
        return None

    file_size = os.path.getsize(video_path) / (1024 * 1024)  # Size in MB
    print(f"📁 File: {video_path}")
    print(f"📊 Size: {file_size:.2f} MB")
    print()

    try:
        print(f"⏳ Loading Whisper model '{model_size}'...")
        print("   (This may take a moment on first run)")
        model = whisper.load_model(model_size)
        print("✓ Model loaded successfully!")
        print()

        print(f"🎙️  Transcribing audio...")
        print("   (This may take several minutes depending on file length)")
        print()

        # Transcribe with language specification
        transcribe_options = {"verbose": True, "language": language}

        result = model.transcribe(video_path, **transcribe_options)

        # Determine output path
        if output_path:
            transcript_path = output_path
        else:
            base_name = os.path.splitext(video_path)[0]
            transcript_path = f"{base_name}_transcript.txt"

        # Save transcript
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print()
        print("=" * 60)
        print(f"✅ SUCCESS! Transcript saved to:")
        print(f"   {transcript_path}")
        print("=" * 60)
        print()
        print("📝 Preview:")
        print("-" * 60)
        preview = result["text"][:500]
        print(preview + ("..." if len(result["text"]) > 500 else ""))
        print("-" * 60)

        return result

    except Exception as e:
        print(f"\n❌ Error during transcription: {str(e)}")
        print("   Please check that the file is not corrupted and try again.")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe video/audio files using OpenAI Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s video.mp4                    # Transcribe with default 'base' model
  %(prog)s video.mp4 -m large          # Use 'large' model for better accuracy
  %(prog)s audio.mp3 -o transcript.txt # Specify output file
  %(prog)s video.mkv -l es             # Specify Spanish language

Supported formats: {', '.join(SUPPORTED_FORMATS)}

Models (tiny → large = faster → more accurate):
  - tiny:   Fastest, lowest accuracy
  - base:   Good balance (default)
  - small:  Better accuracy
  - medium: High accuracy
  - large:  Best accuracy, slowest
        """,
    )

    parser.add_argument("file", help="Path to video/audio file to transcribe")

    parser.add_argument(
        "-m",
        "--model",
        choices=VALID_MODELS,
        default="base",
        help="Whisper model size (default: base)",
    )

    parser.add_argument(
        "-o", "--output", help="Output file path (default: <input>_transcript.txt)"
    )

    parser.add_argument(
        "-l",
        "--language",
        default="en",
        help="Language code (default: en). Examples: en, es, fr, de",
    )

    args = parser.parse_args()

    print_banner()
    transcribe_video(args.file, args.model, args.output, args.language)


if __name__ == "__main__":
    main()
