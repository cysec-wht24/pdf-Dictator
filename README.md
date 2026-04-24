# PDF Dictator

Reads a PDF aloud using Microsoft's Christopher Neural voice.

## Setup

### Windows
```cmd
python -m venv venv
venv\Scripts\activate
pip install pypdf edge-tts pygame keyboard
```

### Mac
```bash
python3 -m venv venv
source venv/bin/activate
pip install pypdf edge-tts pygame keyboard
```

## Usage

```cmd
python dictator.py
```

## Controls

| Key | Action |
|-----|--------|
| `Space` | Pause / Resume |

## Configuration

| Option | Location in code | Example |
|--------|-----------------|---------|
| Start page | `start_page = 19` | Change to any page number |
| Speed | `rate="0%"` | `-20%` slower, `+10%` faster |
| Voice | `VOICE = "en-US-ChristopherNeural"` | See edge-tts docs for others |

## Ignored Phrases

The following are stripped before speaking:
- NPTEL Online Certification Courses
- Indian Institute of Technology Kharagpur
- TYPE OF QUESTION: MCQ/MSQ
- week