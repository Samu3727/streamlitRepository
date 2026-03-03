from pathlib import Path
import sys

try:
    from .templates.main_template import MainTemplate
except ImportError:
    repo_root = Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    from Frontend.src.components.templates.main_template import MainTemplate

def main():
    MainTemplate()

if __name__ == "__main__":
    main()