import logging

def setup_logging():
    """Set up the logging configuration."""
    # Configuring basic logging settings
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
                # Yielding each line stripped of leading/trailing whitespace
                yield line.strip()
    except (FileNotFoundError, PermissionError) as e:
        # Logging an error if the file cannot be opened
        logging.error(f"Error opening {filename}: {e}")
        # Returning an empty list in case of an error
        return []

def combine_lyrics(lyrics_files):
    """
    Combines the lyrics from multiple files using generators.
    :param lyrics_files: A list of filenames containing lyrics.
    :return: A generator of combined lyrics.
    """
    # Creating a list of generators for each file
    file_generators = [read_and_parse_file(file) for file in lyrics_files]
    # Returning a zipped generator that combines lines from all files
    return zip(*file_generators)

def format_lyrics(lyrics_data):
    """
    Formats the combined lyrics for display.
    :param lyrics_data: Combined lyrics data.
    :return: A string containing the formatted lyrics.
    """
    # Joining groups of lyrics, separated by two newlines
    return '\n\n'.join(['\n'.join(group) for group in lyrics_data])

def main():
    """
    Main function to process and display song lyrics.
    """
    # Prompting user for input
    print("Enter the names of lyric files separated by commas (e.g., file1.txt, file2.txt):")
    # Splitting the input into a list of filenames
    lyrics_files = [filename.strip() for filename in input().split(',')]
    # Combining lyrics from the specified files
    lyrics_data = combine_lyrics(lyrics_files)
    # Formatting the combined lyrics for display
    formatted_lyrics = format_lyrics(lyrics_data)
    # Printing the formatted lyrics
    print(formatted_lyrics)
    # Saving the formatted lyrics to a file
    save_to_file('result.txt', formatted_lyrics)

def save_to_file(filename, string):
    """
    Saves a string to a file.
    :param filename: The filename to save to.
    :param string: The string to save.
    """
    try:
        with open(filename, 'w') as file:
            # Writing the string to the file
            file.write(string)
    except IOError as e:
        # Logging an error if the file cannot be saved
        logging.error(f"Error saving to {filename}: {e}")

if __name__ == '__main__':
    # Setting up logging and running the main function
    setup_logging()
    main()