import shutil
import os

source_dir = r"C:\Users\mapet\.gemini\antigravity-ide\brain\386798d7-5a4a-41aa-8950-e73ffb47d349"
dest_dir = r"C:\Development\personal_portfolio\images"

files = [
    "nrz_pipeline_1783669944629.png",
    "local_link_1783669956924.png",
    "obd_edge_1783669968272.png",
    "zdf_finance.png" # Placeholder for the one we are generating now, might have timestamp so we will use listdir to find it.
]

for file in os.listdir(source_dir):
    if file.startswith("nrz_pipeline") or file.startswith("local_link") or file.startswith("obd_edge") or file.startswith("zdf_finance"):
        if file.endswith(".png"):
            src = os.path.join(source_dir, file)
            # Make a clean name
            if file.startswith("nrz_pipeline"): name = "nrz-pipeline.png"
            elif file.startswith("local_link"): name = "local-link.png"
            elif file.startswith("obd_edge"): name = "obd-edge.png"
            elif file.startswith("zdf_finance"): name = "zdf-finance.png"
            
            dst = os.path.join(dest_dir, name)
            shutil.copy2(src, dst)
            print(f"Copied {src} to {dst}")

# Also copy ZET5 video
video_src = r"C:\Users\mapet\Music\Videos\emergency mode trigger.mp4"
video_dst = os.path.join(dest_dir, "zet5-video.mp4")
if os.path.exists(video_src):
    shutil.copy2(video_src, video_dst)
    print(f"Copied {video_src} to {video_dst}")
