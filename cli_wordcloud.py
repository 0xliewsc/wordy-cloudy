import argparse
import os
import sys
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description='Generate a word cloud from text input',
        epilog='If no input file is provided, text will be read from stdin'
    )
    parser.add_argument('input_file', 
                       help='Optional path to the text file. If omitted, text will be read from stdin')
    parser.add_argument('--output', '-o', help='Output image filename (png)')
    parser.add_argument('--width', type=int, default=800, help='Width of the output image')
    parser.add_argument('--height', type=int, default=400, help='Height of the output image')
    parser.add_argument('--background_color', default='white', help='Background color of the word cloud')
    args = parser.parse_args()

    # Read and process input text efficiently for large files
    wordcloud = WordCloud(
        width=args.width,
        height=args.height,
        background_color=args.background_color,
        stopwords=STOPWORDS.update(['and', 'the', 'of']),
        max_words=2000
    )

    if args.input_file:
        if not os.path.exists(args.input_file):
            raise FileNotFoundError(f"Input file {args.input_file} does not exist")
        
        with open(args.input_file, 'r') as f:
            # Read entire content into memory
            text = f.read().lower()
    else:
        if sys.stdin.isatty():
            print("No input provided. Please provide text either via a file or stdin.")
            parser.print_usage()
            return
            
        # Read from stdin
        text = sys.stdin.read().strip()
        
        # Check for empty input
        if not text:
            print("Error: No text provided. Please enter some text.")
            return
    
    # Process the text
    # Create wordcloud object and generate
    wordcloud = WordCloud(
        width=args.width,
        height=args.height,
        background_color=args.background_color,
        stopwords=STOPWORDS.update(['and', 'the', 'of']),
        max_words=2000
    ).generate(text)

    if args.output:
        # Save the image to file
        wordcloud.to_file(args.output)
        print(f"Word cloud saved as {args.output}")
    else:
        # Show the image in a window
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show(block=True)
        plt.close()

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
