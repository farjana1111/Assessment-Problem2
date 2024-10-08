# import requests
# import time

# # Define the URL of the application to check
# APP_URL = "http://your-application-url.com"

# # Function to check the application status
# def check_application():
#     try:
#         response = requests.get(APP_URL)
#         if response.status_code == 200:
#             print(f"Application is UP (Status Code: {response.status_code})")
#         else:
#             print(f"Application is DOWN (Status Code: {response.status_code})")
#     except requests.ConnectionError:
#         print("Application is DOWN (Connection Error)")

# # Check the application status every minute
# while True:
#     print("Checking application health...")
#     check_application()
#     time.sleep(60)  # Wait for 60 seconds before the next check



    
# import requests

# def check_application_health(url):
#     print("Checking application health...")
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print("Application is UP")
#         else:
#             print(f"Application is DOWN (HTTP Status Code: {response.status_code})")
#     except requests.ConnectionError as e:
#         print("Application is DOWN (Connection Error):", e)
#     except requests.Timeout as e:
#         print("Application is DOWN (Timeout Error):", e)
#     except Exception as e:
#         print("An error occurred:", e)

# # Example usage
# url = "http://your_application_url"  # Replace with your application URL
# check_application_health(url)






import requests

def check_application_health(url):
    print("Checking application health...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is UP")
        else:
            print(f"Application is DOWN (HTTP Status Code: {response.status_code})")
    except requests.ConnectionError as e:
        print("Application is DOWN (Connection Error):", e)
    except requests.Timeout as e:
        print("Application is DOWN (Timeout Error):", e)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
url = "http://localhost:8080"  # Replace with your actual application URL
check_application_health(url)