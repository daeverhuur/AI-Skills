---
name: youtube-transcript
description: "Extract transcripts from YouTube videos and save them as text files. Use when the user asks to: (1) Get a YouTube video transcript, (2) Extract or download subtitles/captions from a YouTube video, (3) Gather transcripts from multiple videos into one file, (4) Prepare video transcripts as input for creating skills or knowledge bases, (5) Convert YouTube video content to text. Triggers on: youtube transcript, video transcript, extract subtitles, get captions, youtube to text."
---

# YouTube Transcript Extractor

Extract full transcripts from YouTube videos programmatically using the `youtube-transcript-api` Python library.

## Prerequisites

The Python package `youtube-transcript-api` must be installed:

```bash
pip install youtube-transcript-api
```

## How to Use

The extraction script lives at `.claude/skills/youtube-transcript/scripts/extract.py`.

### Single Video

```bash
# Output to stdout
python .claude/skills/youtube-transcript/scripts/extract.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Save to file
python .claude/skills/youtube-transcript/scripts/extract.py "https://www.youtube.com/watch?v=VIDEO_ID" output.txt
```

### Multiple Videos into One File

When the user provides multiple YouTube URLs and wants them combined (common for skill creation):

```bash
python .claude/skills/youtube-transcript/scripts/extract.py combined.txt \
  "https://www.youtube.com/watch?v=ID1" \
  "https://www.youtube.com/watch?v=ID2" \
  "https://www.youtube.com/watch?v=ID3"
```

Each transcript is separated by blank lines and includes a header with title, channel, and URL.

### Options

| Flag | Description |
|------|-------------|
| `--no-timestamps` | Output plain text without timestamps |
| `--lang=CODE` | Preferred language (default: `en`). Falls back to any available language |
| `--list-langs` | List available transcript languages for a video |

### URL Formats

All of these work:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `VIDEO_ID` (plain 11-character ID)

## Workflow: Gathering Transcripts for Skill Creation

This is the primary use case. When the user wants to create a skill from YouTube videos:

1. **Collect URLs** — Ask the user for the YouTube video URLs they want to extract
2. **Extract transcripts** — Run the script in multi-video mode to combine all transcripts into one `.txt` file
3. **Review** — Confirm the output file was created and report video count, total size
4. **Use as input** — The combined transcript file is ready to be used as source material for creating a new skill

### Example

```bash
# User provides 3 video URLs about "React Server Components"
python .claude/skills/youtube-transcript/scripts/extract.py \
  react-server-components-transcripts.txt \
  "https://www.youtube.com/watch?v=abc123" \
  "https://www.youtube.com/watch?v=def456" \
  "https://www.youtube.com/watch?v=ghi789"
```

## Output Format

```
Video: Video Title Here
Channel: Channel Name
URL: https://www.youtube.com/watch?v=VIDEO_ID
Language: English (auto-generated)
Segments: 1234
================================================================================

0:00 first line of transcript
0:05 second line of transcript
...
```

## How It Works

The library uses YouTube's **Innertube API** (the same internal API YouTube's mobile app uses):

1. Fetches the video page HTML to extract the `INNERTUBE_API_KEY`
2. POSTs to `/youtubei/v1/player` pretending to be an Android client — this returns caption URLs without browser-only DRM tokens
3. GETs the caption URL which returns XML
4. Parses the XML into text snippets with timestamps

This bypasses restrictions that block direct `timedtext` API calls from servers. It also handles EU consent cookie requirements automatically.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `TranscriptsDisabled` | Video has no captions | Nothing to extract — the uploader disabled captions |
| `NoTranscriptFound` | No transcript in requested language | Try `--list-langs` to see available languages, or omit `--lang` |
| `IpBlocked` / `RequestBlocked` | YouTube rate limiting | Wait a few minutes and retry. For persistent blocks, the library supports proxy configuration |
| `VideoUnavailable` | Video is private or deleted | Verify the URL is correct and the video is public |
| `ModuleNotFoundError` | Package not installed | Run `pip install youtube-transcript-api` |
