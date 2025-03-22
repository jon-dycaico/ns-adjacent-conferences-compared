#Content Processing Tools

A Python-based toolkit for processing different types of content:
1. Conference videos and transcripts

## Repository Structure

```
contentmgmt/
├── conference_processing/    # Conference video processing workflow
│   ├── transcripts/         # Raw conference transcripts
│   └── summaries/          # Processed conference summaries
└── Pipfile                 # Python dependencies
```

## Setup

1. Install dependencies:
```bash
pipenv install
```

2. Activate virtual environment:
```bash
pipenv shell
```

## Conference Processing Workflow

1. Download conference videos and subtitles:
```bash
# Download single video with auto-generated subtitles
yt-dlp --write-auto-sub --sub-format vtt -o "conference_processing/transcripts/%(uploader)s/%(title)s.%(ext)s" VIDEO_URL

# Download entire playlist
yt-dlp --write-auto-sub --sub-format vtt -o "conference_processing/transcripts/%(uploader)s/%(title)s.%(ext)s" PLAYLIST_URL
```

2. Process transcripts and create summaries (manual process using downloaded content)

3. Organize summaries by conference in the `summaries` directory


## Dependencies

- Python 3.12
- yt-dlp: Video downloading
- webvtt-py: Subtitle processing
- PyMuPDF: PDF processing

## License

MIT License 
