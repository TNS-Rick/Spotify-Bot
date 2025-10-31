# Sostituto minimale di imghdr.what per riconoscere alcune immagini tramite magic bytes.
def what(file, h=None):
    """Return image type string ('jpeg','png','gif','bmp','webp') or None."""
    if h is None:
        try:
            with open(file, 'rb') as f:
                h = f.read(32)
        except Exception:
            return None
    if not h:
        return None
    if h.startswith(b'\xFF\xD8\xFF'):
        return 'jpeg'
    if h.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    if h.startswith(b'BM'):
        return 'bmp'
    if h.startswith(b'RIFF') and len(h) >= 12 and h[8:12] == b'WEBP':
        return 'webp'
    return None