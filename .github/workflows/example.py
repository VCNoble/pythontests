import os


def main ():
  print("Hello from Turners!")
  token = os.environ.get("GOOGLE_APIKEY")
  if not token:
    raise RuntimeError("GOOGLE_APIKEY env var is not set!")
  print("Passed! we found Turners env var")
  
if __name__=='__main__':
  main()
