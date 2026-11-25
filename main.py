# how-many-tabs-do-you-have-open: one honest tab count, written to entry.txt.
import os
from pathlib import Path

def main():
    out_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = out_dir / 'entry.txt'
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write("314")

if __name__ == '__main__':
    main()
