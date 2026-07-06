import os
import sys
import yt_dlp
from typing import Optional

def download_tiktok_no_watermark(tiktok_url: str, output_filename: str = "tiktok_video") -> Optional[str]:
    """
    Downloads a TikTok video without a watermark using yt-dlp.
    
    :param tiktok_url: The full link to the TikTok video (handles desktop and mobile share URLs).
    :param output_filename: Name of the resulting video file (do not include extension).
    :return: Path to the downloaded file or None if extraction fails.
    """
    ydl_opts = {
        # 'bestvideo' generally extracts the raw, un-watermarked high-quality asset stream
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_filename}.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        # Rotate user-agents/headers to successfully blend into common web browsers
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Mode': 'navigate',
        }
    }

    try:
        print(f"[➔] Initializing core pipeline extraction for: {tiktok_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract info to get metadata and trigger asset fetch
            info_dict = ydl.extract_info(tiktok_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            print(f"[✔] Asset fetched successfully! File saved: {filename}")
            return filename
            
    except yt_dlp.utils.DownloadError as e:
        print(f"[✘] Download Error: Failed to extract clean stream.\nDetails: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[✘] Unexpected runtime error: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    print("=" * 65)
    print("     TikTok Watermark-Free Downloader Engine (Core Script)")
    print("=" * 65)
    
    target_url = input("Enter TikTok Video URL: ").strip()
    if not target_url:
        print("[!] URL cannot be blank. Exiting.")
        sys.exit(1)
        
    out_name = input("Enter output filename (Default: clean_tiktok): ").strip() or "clean_tiktok"
    
    download_tiktok_no_watermark(target_url, out_name)
