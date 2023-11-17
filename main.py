import logging

def setup_logging():
    """Set up the logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def read_and_parse_file(filename):
    """
    Generator to read and parse file line by line.
    :param filename: The name of the file to read.
    :yield: Parsed lines from the file.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except (FileNotFoundError, PermissionError) as e:
        logging.error(f"Error opening {filename}: {e}")
        return []

def combine_lyrics(lyrics_files):
    """
    Combines the lyrics from multiple files using generators.
    :param lyrics_files: A list of filenames containing lyrics.
    :return: A generator of combined lyrics.
    """
    file_generators = [read_and_parse_file(file) for file in lyrics_files]
    return zip(*file_generators)

def format_lyrics(lyrics_data):
    """
    Formats the combined lyrics for display.
    :param lyrics_data: Combined lyrics data.
    :return: A string containing the formatted lyrics.
    """
    return '\n\n'.join(['\n'.join(group) for group in lyrics_data])

def main():
    """
    Main function to process and display song lyrics.
    """
    print("Enter the names of lyric files separated by commas (e.g., file1.txt, file2.txt):")
    lyrics_files = [filename.strip() for filename in input().split(',')]
    lyrics_data = combine_lyrics(lyrics_files)
    formatted_lyrics = format_lyrics(lyrics_data)
    print(formatted_lyrics)
    save_to_file('result.txt', formatted_lyrics)

def save_to_file(filename, string):
    """
    Saves a string to a file.
    :param filename: The filename to save to.
    :param string: The string to save.
    """
    try:
        with open(filename, 'w') as file:
            file.write(string)
    except IOError as e:
        logging.error(f"Error saving to {filename}: {e}")

if __name__ == '__main__':
    setup_logging()
    main()