import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import re
import requests

def load_words(filename):
    """Load words from a CSV file."""
    words = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                words.extend(row)  # Assuming words are separated by commas
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
    return words

def search_words(pattern, words):
    """Search for words matching the given pattern."""
    regex_pattern = pattern.replace('_', '.')  # Convert underscores to regex dots
    return [word for word in words if re.fullmatch(regex_pattern, word)]

def browse_file():
    """Allow the user to select a CSV file."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        global word_list
        word_list = load_words(file_path)
        status_label.config(text=f"Loaded {len(word_list)} words")

def find_matches():
    """Find and display matching words."""
    if not word_list:
        messagebox.showwarning("Warning", "Load a word list first!")
        return
    pattern = pattern_entry.get()
    if not pattern or len(pattern) != word_length.get():
        messagebox.showwarning("Warning", "Enter a valid pattern!")
        return
    matches = search_words(pattern, word_list)
    result_list.delete(0, tk.END)
    for match in matches:
        result_list.insert(tk.END, match)

def set_word_length():
    """Update the pattern entry length."""
    pattern_entry.delete(0, tk.END)
    pattern_entry.insert(0, '_' * word_length.get())

def fetch_from_api():
    """Fetch words from WordsAPI and append to the word list."""
    user_id = 13102
    token = "Qgu5ybC4sjwf2GLD"
    # url = (f"https://www.stands4.com/services/v2/ana.php?uid={user_id}&tokenid={token}&term=sweet&format=json")
    # url = "https://www.stands4.com/services/v2/ana.php?uid=13102&tokenid=Qgu5ybC4sjwf2GLD&term=sweet&format=json"
    headers = {
        "Accept": "application/json"
    }
    # api-endpoint
    URL = "https://www.stands4.com/services/v2/ana.php"

    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'uid':13102,
              'tokenid':'Qgu5ybC4sjwf2GLD'}

    try:
        # response = requests.get("https://www.stands4.com/services/v2/ana.php?uid=13102&tokenid=Qgu5ybC4sjwf2GLD&term=sweet&format=json")
        # response = requests.get(url, headers=headers, params={"letters": 6, "limit": 50})
        # sending get request and saving the response as response object
        response = requests.get(url = URL, params = PARAMS)
        if response.status_code == 200:

        # extracting data in json format
            data = response.json()


                # extracting latitude, longitude and formatted address
                # of the first matching location
            # latitude = data['results'][0]['geometry']['location']['lat']
            # longitude = data['results'][0]['geometry']['location']['lng']
            # formatted_address = data['results'][0]['formatted_address']

        # printing the output
            # print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"%(latitude, longitude,formatted_address))
            print(data)
               
                # new_words = [entry["word"] for entry in data.get("results", []) if "word" in entry]
                # if not new_words:
                #     messagebox.showwarning("Warning", "No words found from API")
                #     return
                # global word_list
                # word_list.extend(new_words)
                # messagebox.showinfo("Success", f"Added {len(new_words)} words from API")
            messagebox.showinfo("Success", f"Added x words from API")
# def fetch_from_api():
#     """Fetch words from WordsAPI and append to the word list."""
#     api_key = "b2ae199e59mshee595fde5f388c8p1533bfjsn2065483af9bf"  # Replace with your actual API key
#     url = "https://wordsapiv1.p.rapidapi.com/words/"
#     headers = {
#         "X-RapidAPI-Key": api_key,
#         "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
#         "Accept": "application/json"
#     }
#     try:
#         response = requests.get(url, headers=headers, params={"letters": 6, "limit": 50})
#         if response.status_code == 200:
#             data = response.json()
#             new_words = [entry["word"] for entry in data.get("results", []) if "word" in entry]
#             if not new_words:
#                 messagebox.showwarning("Warning", "No words found from API")
#                 return
#             global word_list
#             word_list.extend(new_words)
#             messagebox.showinfo("Success", f"Added {len(new_words)} words from API")
        else:
            messagebox.showerror("Error", f"Failed to fetch words from API: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"API request failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("Crossword Solver")
root.geometry("400x400")

tk.Label(root, text="Select Word List:").pack()
tk.Button(root, text="Browse", command=browse_file).pack()

status_label = tk.Label(root, text="No file loaded", fg="red")
status_label.pack()

tk.Label(root, text="Word Length:").pack()
word_length = tk.IntVar(value=6)
tk.Spinbox(root, from_=3, to=12, textvariable=word_length, command=set_word_length).pack()

tk.Label(root, text="Enter Pattern (_ for unknowns):").pack()
pattern_entry = tk.Entry(root)
pattern_entry.pack()
pattern_entry.insert(0, "______")

tk.Button(root, text="Find Matches", command=find_matches).pack()
tk.Button(root, text="Fetch Words from API", command=fetch_from_api).pack()

result_list = tk.Listbox(root)
result_list.pack(fill=tk.BOTH, expand=True)

word_list = []
root.mainloop()
