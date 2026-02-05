with open("transcript_with_speakers.txt", "r") as file:
    transcript = file.read()

# Replace speaker names
context = (
    transcript.replace("SPEAKER_01", "Patrick-Marketing")
    .replace("SPEAKER_00", "Jared-VP_Consumer")
    .replace("SPEAKER_02", "Dr-Brandy-Robinson")
)

with open("final_transcript.txt", "w") as file:
    file.write(context)
