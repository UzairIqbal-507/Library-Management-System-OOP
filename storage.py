
import json
import os
import shutil
import glob

from datetime import datetime

from book import Book
from member import Member


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
MEMBERS_FILE = os.path.join(DATA_DIR, "members.json")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.json")


def setup_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

    for file_path in [BOOKS_FILE, MEMBERS_FILE, TRANSACTIONS_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)


def save_json(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(file_path):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print(f"Warning: Invalid data format in {os.path.basename(file_path)}")
        return []

    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {os.path.basename(file_path)}")
        return []


# BOOK STORAGE

def save_books(books):
    data = []

    for book in books:
        data.append({
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "availability": book.availability
        })

    save_json(BOOKS_FILE, data)


def load_books():
    data = load_json(BOOKS_FILE)
    books = []

    for item in data:
        try:
            book = Book(
                item["book_id"],
                item["title"],
                item["author"],
                item["category"]
            )

            book.availability = item.get("availability", True)
            books.append(book)

        except (KeyError, TypeError):
            continue

    return books


# MEMBER STORAGE

def save_members(members):
    data = []

    for member in members:
        data.append({
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "borrowed_books": member.borrowed_books
        })

    save_json(MEMBERS_FILE, data)


def load_members():
    data = load_json(MEMBERS_FILE)
    members = []

    for item in data:
        try:
            member = Member(
                item["member_id"],
                item["name"],
                item["email"]
            )

            member.borrowed_books = item.get("borrowed_books", [])
            members.append(member)

        except (KeyError, TypeError):
            continue

    return members


# TRANSACTION STORAGE

def save_transactions(transactions):
    save_json(TRANSACTIONS_FILE, transactions)


def load_transactions():
    return load_json(TRANSACTIONS_FILE)


# BACKUP METHODS

def backup_file(file_path):
    if not os.path.exists(file_path):
        return False

    os.makedirs(BACKUP_DIR, exist_ok=True)

    filename = os.path.basename(file_path).replace(".json", "")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")

    backup_path = os.path.join(
        BACKUP_DIR,
        f"{filename}_{timestamp}.json"
    )

    try:
        shutil.copy2(file_path, backup_path)
        return True

    except OSError as error:
        print(f"Backup error: {error}")
        return False


def get_latest_backup(file_path):
    filename = os.path.basename(file_path).replace(".json", "")

    pattern = os.path.join(
        BACKUP_DIR,
        f"{filename}_*.json"
    )

    backup_files = glob.glob(pattern)

    if not backup_files:
        return None

    return max(backup_files, key=os.path.getmtime)


def restore_all_files():
    files = [
        BOOKS_FILE,
        MEMBERS_FILE,
        TRANSACTIONS_FILE
    ]

    # First check that every backup exists.
    backups = {}

    for file_path in files:
        latest_backup = get_latest_backup(file_path)

        if latest_backup is None:
            print(
                f"Missing backup for: {os.path.basename(file_path)}"
            )
            return False

        backups[file_path] = latest_backup

    # Stage all backup copies before replacing current files.
    staged_files = {}

    try:
        for file_path, backup_path in backups.items():
            staged_path = file_path + ".restore_tmp"
            shutil.copy2(backup_path, staged_path)
            staged_files[file_path] = staged_path

        # Replace current files only after all staging copies succeed.
        for file_path, staged_path in staged_files.items():
            os.replace(staged_path, file_path)

        return True

    except OSError as error:
        print(f"Restore error: {error}")
        return False

    finally:
        # Remove any temporary files left behind.
        for staged_path in staged_files.values():
            if os.path.exists(staged_path):
                os.remove(staged_path)
