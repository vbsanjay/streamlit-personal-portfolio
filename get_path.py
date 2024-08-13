from pathlib import Path

# --- PATH SETTINGS ---

def get_paths():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    return {
        "css_file": current_dir / "styles" / "main.css",
        "resume_file": current_dir / "assets" / "CV.pdf",
        "profile_pic": current_dir / "assets" / "profile-pic.png"
    }