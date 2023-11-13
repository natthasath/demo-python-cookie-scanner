from cookie.cookie import CookieScanner

# Example usage
if __name__ == "__main__":
    target_url = "https://idt.nida.ac.th/"
    scanner = CookieScanner(target_url)
    scanner.scan_cookies()