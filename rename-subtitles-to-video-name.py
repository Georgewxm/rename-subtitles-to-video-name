import os
import shutil
import argparse
import logging


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_and_move_largest_srt(base_dir, languages, dry_run=False, videos=None):
    """
    Renames and moves the largest .srt file in each subfolder of the 'Subs' directory to the base directory.

    Args:
        base_dir (str): The base directory path.
        languages (list): A list of languages to filter the .srt files.
        dry_run (bool, optional): If True, performs a dry run without actually moving the files. Defaults to False.
        videos (list, optional): A list of subfolder names to filter the operation. Defaults to None.

    Returns:
        None
    """
    subs_dir = os.path.join(base_dir, 'Subs')
    if not os.path.exists(subs_dir):
        logging.error("The 'Subs' folder does not exist in the provided directory.")
        return
    
    for folder in os.listdir(subs_dir):
        if videos and folder not in videos:
            continue
        
        current_folder = os.path.join(subs_dir, folder)
        if os.path.isdir(current_folder):
            srt_files = [f for f in os.listdir(current_folder) if f.endswith('.srt') and any(lang in f for lang in languages)]
            largest_file = None
            max_size = -1

            for file in srt_files:
                file_path = os.path.join(current_folder, file)
                size = os.path.getsize(file_path)
                if size > max_size:
                    max_size = size
                    largest_file = file

            if largest_file:
                new_file_name = folder + '.srt'
                source_file_path = os.path.join(current_folder, largest_file)
                new_file_path = os.path.join(base_dir, new_file_name)
                if not dry_run:
                    shutil.move(source_file_path, new_file_path)
                logging.info(f"{'Dry run: ' if dry_run else ''}Moved and renamed '{largest_file}' to '{new_file_path}'")

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('directory', type=str, help='The directory containing the "Subs" folder')
    parser.add_argument('--languages', nargs='*', default=['English'], help='Languages to extract, e.g., English Spanish')
    parser.add_argument('--dry-run', action='store_true', help='Run the script in dry run mode to see what would be done')
    parser.add_argument('--videos', nargs='*', help='Specific video IDs to process, e.g., video_1 video_2')
    args = parser.parse_args()

    setup_logging()
    rename_and_move_largest_srt(args.directory, args.languages, dry_run=args.dry_run, videos=args.videos)

if __name__ == "__main__":
    main()