import argparse
import shutil
from ascii_video import video_to_ascii, LIGHT_REVERSE, width_ter
def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Convert video to ASCII.')

    # Add required argument for the video file
    parser.add_argument('video', help='The path to the video file.')

    # Optional parameters with defaults
    parser.add_argument('--ascii_list', default=LIGHT_REVERSE, help='List of characters for ASCII (default: LIGHT_REVERSE).')
    parser.add_argument('--new_width', type=int, default=width_ter, help='New width for ASCII output (default: terminal width).')
    parser.add_argument('--fps', type=int, default=60, help='Frames per second for ASCII output (default: 60).')
    parser.add_argument('--retain_aspect', action='store_true', help='Retain the original aspect ratio (default: False).')

    # Color-related options
    parser.add_argument('--grayscale', action='store_true', help='Convert video to ASCII using grayscale (default: color).')
    parser.add_argument('--true_color', action='store_true', help='Enable true-color ASCII output (default: False).')

    # Parse the arguments
    args = parser.parse_args()

    # Determine color mode: grayscale overrides everything
    color = not args.grayscale  # Default is color unless --grayscale is provided
    
    # Ensure true_color only works when color is enabled
    true_color = args.true_color if color else False

    # Call the video_to_ascii function with the parsed arguments
    video_to_ascii(
        video_path=args.video,
        ascii_list=args.ascii_list,
        new_width=args.new_width,
        fps=args.fps,
        retain_aspect=args.retain_aspect,
        color=color,
        true_color=true_color
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")