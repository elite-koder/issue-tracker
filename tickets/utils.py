import uuid


def get_unique_filename(original_filename):
    filename, ext = original_filename.rsplit(".", 1)
    suffix = f"_{uuid.uuid4()}.{ext}"
    extra_len = len(filename) + len(suffix) - 100
    if extra_len > 0:
        return f"{filename[:-extra_len]}{suffix}"
    return f"{filename}{suffix}"
