# scripts/playlistExtract.py

import tidalapi

def main():
    print("=== Playlist to Album Extractor (tidalapi) ===\n")

    # Login
    session = tidalapi.Session()
    session.login_oauth_simple()  # Opens browser for TIDAL login

    print(f"\nLogged in as: {session.user.username}\n")

    # Get playlist URL
    playlist_url = input("Enter playlist URL: ").strip()

    # Extract playlist ID
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Load playlist
    playlist = session.get_playlist(playlist_id)

    print(f"Playlist name: {playlist.name}")
    print(f"Found {playlist.num_tracks} tracks.\n")

    album_urls = set()

    # Extract album URLs
    for track in playlist.tracks():
        album = track.album
        if album:
            album_url = f"https://tidal.com/album/{album.id}"
            album_urls.add(album_url)

    # Write to file
    output_filename = input("Enter output filename (default: albums_from_playlist.txt): ").strip()
    if not output_filename:
        output_filename = "albums_from_playlist.txt"

    with open(output_filename, "w") as f:
        for url in sorted(album_urls):
            f.write(url + "\n")

    print(f"\nExtracted {len(album_urls)} unique album URLs.")
    print(f"Saved to: {output_filename}\n")

if __name__ == "__main__":
    main()
