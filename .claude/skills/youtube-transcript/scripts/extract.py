#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Requires: pip install youtube-transcript-api

Usage:
  python extract.py <video-url-or-id> [output-file]
  python extract.py output.txt URL1 URL2 URL3

Flags:
  --no-timestamps    Omit timestamps from output
  --lang=CODE        Preferred language code (default: en)
  --list-langs       List available transcript languages for a video
"""

import sys
import re
import json
import urllib.request

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url_or_id: str) -> str | None:
    """Extract YouTube video ID from various URL formats or plain ID."""
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    m = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', url_or_id)
    if m:
        return m.group(1)
    m = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url_or_id)
    if m:
        return m.group(1)
    m = re.search(r'embed/([a-zA-Z0-9_-]{11})', url_or_id)
    if m:
        return m.group(1)
    return None


def get_video_metadata(video_id: str) -> tuple[str, str]:
    """Fetch video title and channel from YouTube oEmbed API."""
    try:
        url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get('title', 'Unknown'), data.get('author_name', 'Unknown')
    except Exception:
        return 'Unknown', 'Unknown'


def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS or MM:SS format."""
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours > 0:
        return f'{hours}:{minutes:02d}:{secs:02d}'
    return f'{minutes}:{secs:02d}'


def list_languages(video_id: str) -> None:
    """List available transcript languages for a video."""
    ytt = YouTubeTranscriptApi()
    transcript_list = ytt.list(video_id)
    print(f'Available transcripts for {video_id}:')
    for t in transcript_list:
        kind = 'auto-generated' if t.is_generated else 'manual'
        print(f'  {t.language_code:5s}  {t.language:30s}  ({kind})')


def fetch_transcript(video_id: str, languages: list[str] | None = None) -> dict:
    """Fetch transcript for a YouTube video."""
    ytt = YouTubeTranscriptApi()

    if languages is None:
        languages = ['en']

    try:
        transcript = ytt.fetch(video_id, languages=languages)
    except Exception:
        # Fall back to whatever is available
        transcript = ytt.fetch(video_id)

    snippets = list(transcript)
    title, channel = get_video_metadata(video_id)

    return {
        'video_id': video_id,
        'title': title,
        'channel': channel,
        'language': transcript.language,
        'language_code': transcript.language_code,
        'is_generated': transcript.is_generated,
        'segments': [
            {
                'start': s.start,
                'duration': s.duration,
                'text': s.text,
            }
            for s in snippets
        ],
    }


def format_transcript(data: dict, include_timestamps: bool = True) -> str:
    """Format transcript data as readable text."""
    kind = 'auto-generated' if data.get('is_generated') else 'manual'
    header = (
        f"Video: {data['title']}\n"
        f"Channel: {data['channel']}\n"
        f"URL: https://www.youtube.com/watch?v={data['video_id']}\n"
        f"Language: {data.get('language', 'Unknown')} ({kind})\n"
        f"Segments: {len(data['segments'])}\n"
        f"{'=' * 80}\n\n"
    )

    lines = []
    for seg in data['segments']:
        if include_timestamps:
            ts = format_timestamp(seg['start'])
            lines.append(f'{ts} {seg["text"]}')
        else:
            lines.append(seg['text'])

    return header + '\n'.join(lines)


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__.strip())
        sys.exit(1)

    # Parse flags
    include_timestamps = True
    lang = 'en'
    positional = []

    for arg in args:
        if arg == '--no-timestamps':
            include_timestamps = False
        elif arg.startswith('--lang='):
            lang = arg.split('=', 1)[1]
        elif arg == '--list-langs':
            # Next positional arg should be the video
            positional.append('--list-langs')
        else:
            positional.append(arg)

    # Handle --list-langs
    if '--list-langs' in positional:
        positional.remove('--list-langs')
        if positional:
            vid = extract_video_id(positional[0])
            if vid:
                list_languages(vid)
            else:
                print(f'Error: Could not extract video ID from "{positional[0]}"', file=sys.stderr)
        sys.exit(0)

    # Detect multi-video mode: first arg is .txt file, rest are URLs
    # Single video mode: first arg is URL/ID, optional second is output file
    output_file = None
    video_inputs = []

    if len(positional) >= 3 and positional[0].endswith('.txt'):
        output_file = positional[0]
        video_inputs = positional[1:]
    elif len(positional) == 2:
        video_inputs = [positional[0]]
        output_file = positional[1]
    else:
        video_inputs = [positional[0]]

    all_transcripts = []

    for inp in video_inputs:
        video_id = extract_video_id(inp)
        if not video_id:
            print(f'Error: Could not extract video ID from "{inp}"', file=sys.stderr)
            continue

        print(f'Fetching transcript for {video_id}...', file=sys.stderr)

        try:
            data = fetch_transcript(video_id, languages=[lang])
            print(
                f'  -> {data["title"]} ({len(data["segments"])} segments)',
                file=sys.stderr,
            )
            all_transcripts.append(format_transcript(data, include_timestamps))
        except Exception as e:
            print(f'  -> Error: {e}', file=sys.stderr)

    if not all_transcripts:
        print('No transcripts extracted.', file=sys.stderr)
        sys.exit(1)

    combined = '\n\n\n'.join(all_transcripts)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(combined)
        size_kb = len(combined.encode('utf-8')) / 1024
        print(f'\nSaved to: {output_file} ({size_kb:.1f} KB)', file=sys.stderr)
    else:
        print(combined)


if __name__ == '__main__':
    main()
