#!/usr/bin/env python3
"""
Clean markdown files by removing '>' quote markers from the beginning of lines.
Creates a cleaned copy of the entire directory tree.

Usage:
    python clean_markdown_quotes.py <source_dir> <output_dir>
"""

import os
import sys
import shutil
from pathlib import Path


def clean_markdown_content(content: str) -> str:
    """
    Remove '>' quote markers from the beginning of lines in markdown content.
    
    Args:
        content: The original markdown content
        
    Returns:
        Cleaned content with quote markers removed
    """
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Remove leading '>' and optional space after it
        if line.startswith('>'):
            # Remove the '>' and any immediately following space
            cleaned_line = line[1:]
            if cleaned_line.startswith(' '):
                cleaned_line = cleaned_line[1:]
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def should_process_file(file_path: Path) -> bool:
    """
    Determine if a file should be processed.
    
    Args:
        file_path: Path to the file
        
    Returns:
        True if file should be cleaned, False otherwise
    """
    # Only process markdown files
    return file_path.suffix.lower() in ['.md', '.markdown']


def clean_directory_tree(source_dir: Path, output_dir: Path, verbose: bool = True):
    """
    Clean all markdown files in a directory tree, preserving structure.
    
    Args:
        source_dir: Source directory to read from
        output_dir: Output directory to write cleaned files to
        verbose: Print progress information
    """
    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' does not exist")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Track statistics
    stats = {
        'processed': 0,
        'copied': 0,
        'skipped': 0,
        'errors': 0
    }
    
    # Walk through source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate relative path
        rel_path = Path(root).relative_to(source_dir)
        current_output_dir = output_dir / rel_path
        
        # Create corresponding directory in output
        current_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Process each file
        for filename in files:
            source_file = Path(root) / filename
            output_file = current_output_dir / filename
            
            try:
                if should_process_file(source_file):
                    # Read, clean, and write markdown file
                    with open(source_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    cleaned_content = clean_markdown_content(content)
                    
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(cleaned_content)
                    
                    stats['processed'] += 1
                    if verbose:
                        print(f"Cleaned: {source_file.relative_to(source_dir)}")
                else:
                    # Copy non-markdown files as-is
                    shutil.copy2(source_file, output_file)
                    stats['copied'] += 1
                    if verbose:
                        print(f"Copied:  {source_file.relative_to(source_dir)}")
                        
            except Exception as e:
                stats['errors'] += 1
                print(f"Error processing {source_file}: {e}")
    
    # Print summary
    print("\n" + "="*60)
    print("CLEANING SUMMARY")
    print("="*60)
    print(f"Markdown files cleaned: {stats['processed']}")
    print(f"Other files copied:     {stats['copied']}")
    print(f"Errors encountered:     {stats['errors']}")
    print(f"Output directory:       {output_dir.absolute()}")
    print("="*60)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExample:")
        print("    python clean_markdown_quotes.py ./my_paper ./my_paper_cleaned")
        sys.exit(1)
    
    source_dir = Path(sys.argv[1])
    
    # Default output directory name
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = Path(f"{source_dir}_cleaned")
    
    print(f"Source directory: {source_dir.absolute()}")
    print(f"Output directory: {output_dir.absolute()}")
    print()
    
    # Confirm if output directory exists
    if output_dir.exists():
        response = input(f"Output directory '{output_dir}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
        shutil.rmtree(output_dir)
    
    clean_directory_tree(source_dir, output_dir)


if __name__ == "__main__":
    main()
