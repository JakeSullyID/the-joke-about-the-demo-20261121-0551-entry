import pathlib

def main():
    joke = "My AI agent refactored the monolith into a single pristine line of async poetry, and when it crashed, the stack trace whispered 'I have learned this from watching you'."
    output_dir = pathlib.Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_text(joke, encoding="utf-8")
    print(f"Joke: {joke}")
    print(f"Character count: {len(joke)}")

if __name__ == "__main__":
    main()
