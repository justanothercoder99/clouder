import os
from functions import readFile, getWordCount, printToConsoleAndFile
import logging
import socket

os.chdir("/home/data")
output_file_path = "output/results.txt"

if_file = readFile("IF-1.txt")
always_remember = readFile("AlwaysRememberUsThisWay-1.txt")

if_file_counter = getWordCount(if_file)
always_remember_with_contractions_counter = getWordCount(always_remember)
always_remember_no_contractions_counter = getWordCount(always_remember, withContractions=False)

total_words = sum(if_file_counter.values()) + sum(always_remember_with_contractions_counter.values())
printToConsoleAndFile(output_file_path, f"Total number of words: {total_words}")

printToConsoleAndFile(output_file_path, "Top 3 Most Common words in IF-1.txt are:")
for word, count in if_file_counter.most_common(3):
    printToConsoleAndFile(output_file_path, f"{word}: {count}")


printToConsoleAndFile(output_file_path, "Top 3 Most Common words in AlwaysRememberUsThisWay-1.txt (without contractions) are:")
for word, count in always_remember_no_contractions_counter.most_common(3):
    printToConsoleAndFile(output_file_path, f"{word}: {count}")

host_ip = socket.gethostbyname(socket.gethostname())
printToConsoleAndFile(output_file_path, f"Host IP: {host_ip}")
