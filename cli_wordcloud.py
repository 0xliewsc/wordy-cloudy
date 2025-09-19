import argparse
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Generate a word cloud from text input')
    parser.add_argument('input_file', help='Path to the text file')
    parser.add_argument('--output', '-o', help='Output image filename (png)')
    parser.add_argument('--width', type=int, default=800, help='Width of the output image')
    parser.add_argument('--height', type=int, default=400, help='Height of the output image')
    parser.add_argument('--background_color', default='white', help='Background color of the word cloud')
    args = parser.parse_args()

    # Read input text
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"Input file {args.input_file} does not exist")

    with open(args.input_file, 'r') as f:
        text = f.read()
    
    # Process the text
    processed_text = text.lower()

    # Create wordcloud object
    wordcloud = WordCloud(
        width=args.width,
        height=args.height,
        background_color=args.background_color,
        stopwords=STOPWORDS.update(['and', 'the', 'of']),
        max_words=2000
    ).generate(processed_text)

    if args.output:
        # Save the image to file
        wordcloud.to_file(args.output)
        print(f"Word cloud saved as {args.output}")
    else:
        # Show the image in a window
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
