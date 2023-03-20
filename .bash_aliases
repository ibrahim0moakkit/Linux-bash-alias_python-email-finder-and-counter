alias new_emails='read -p "Enter filename: " filename && python3 ~/script.py "$filename" 1> ~/emails.txt && echo "Output saved to emails.txt" || echo "Error: failed to save output"'
