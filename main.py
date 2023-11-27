from cookie.cookie import CookieScanner

# Example usage
if __name__ == "__main__":
    target_url = "https://mba.nida.ac.th/th/home"
    scanner = CookieScanner(target_url)
    scanner.scan_cookies()