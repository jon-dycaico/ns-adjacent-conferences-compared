import os
import glob
import openai
from pathlib import Path

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_transcript(file_path):
    """Read and return the contents of a transcript file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_summary(text):
    """Generate a summary of the text using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates concise but informative summaries of conference talks. Focus on the key points, main arguments, and important takeaways. Use bullet points for clarity."},
                {"role": "user", "content": f"Please create a summary of this conference talk transcript. Focus on the main points and key takeaways:\n\n{text}"}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None

def process_transcripts():
    """Process all transcript files and generate summaries."""
    # Get all transcript files
    transcript_dir = Path("conference_processing/transcripts/devcon24")
    summary_dir = Path("conference_processing/summaries/devcon24")
    
    # Create summary directory if it doesn't exist
    summary_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each transcript
    for transcript_file in transcript_dir.glob("*.md"):
        print(f"Processing {transcript_file.name}...")
        
        # Read transcript
        text = read_transcript(transcript_file)
        
        # Generate summary
        summary = generate_summary(text)
        
        if summary:
            # Save summary
            summary_file = summary_dir / f"{transcript_file.stem}_summary.md"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"Summary saved to {summary_file}")
        else:
            print(f"Failed to generate summary for {transcript_file.name}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
    else:
        process_transcripts() 