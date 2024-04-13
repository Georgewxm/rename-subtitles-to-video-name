# rename-subtitles-to-video-name.py

This script is designed to rename and move the largest `.srt` (subtitle) file from each subfolder of a 'Subs' directory to a base directory. The script allows you to specify the languages of the subtitle files you want to extract and move. You can also perform a dry run to see what would be done without actually moving the files.

## Usage

The script can be run from the command line with the following syntax:

```sh
python move_largest_srt.py <directory> [--languages] [--dry-run] [--videos]
```

### Arguments

- `directory`: The base directory containing the 'Subs' folder. This is a required argument.
- `--languages`: A list of languages to filter the `.srt` files. Defaults to `['English']` if not specified.
- `--dry-run`: If included, performs a dry run without actually moving the files.
- `--videos`: A list of specific video IDs (subfolder names) to process. If not specified, the script will process all subfolders.

## Examples

To move the largest English `.srt` file from each subfolder in the 'Subs' directory to the base directory, you can run:

```sh
python move_largest_srt.py /path/to/base/directory
```

To move the largest English or Spanish `.srt` file from each subfolder in the 'Subs' directory to the base directory, you can run:

```sh
python move_largest_srt.py /path/to/base/directory --languages English Spanish
```

To perform a dry run without actually moving the files, you can run:

```sh
python move_largest_srt.py /path/to/base/directory --dry-run
```

To move the largest English `.srt` file from specific subfolders (e.g., 'video_1' and 'video_2') in the 'Subs' directory to the base directory, you can run:

```sh
python move_largest_srt.py /path/to/base/directory --videos video_1 video_2
```

## Logging

The script uses Python's built-in logging module to log its operations. The log messages are printed to the console. The log level is set to INFO, so the script will log both INFO and ERROR messages. INFO messages are used to log the operations of the script, such as moving and renaming files. ERROR messages are used to log any errors that occur during the execution of the script, such as if the 'Subs' folder does not exist in the provided directory.