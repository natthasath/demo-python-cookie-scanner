import requests
from http.cookies import SimpleCookie

class CookieScanner:
    def __init__(self, url):
        self.url = url

    def scan_cookies(self):
        try:
            # Send a GET request to the specified URL
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print(f"Scanning cookies for {self.url}:\n")

                # Parse the cookies from the response headers
                cookies = SimpleCookie()
                cookies.load(response.headers.get('Set-Cookie', ''))

                # Display each cookie and its value
                for cookie in cookies.values():
                    print(f"Cookie: {cookie.key}, Value: {cookie.value}")

                print("\nCookie scanning completed.")
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"An error occurred: {e}")