# case-study-tada

How to:
1. Build image with the following command:
   docker build -t tadacasestudy .
2. If container casestudy_alfin is exists, remove it:
   docker rm casestudy_alfin
3. Create a container and run it as casestudy_alfin:
   docker run -d --name casestudy_alfin tadacasestudy
3. Export the converted json file from the container to local directory
   docker cp casestudy_alfin:/tada/casestudy/files/member_registration.json <<local path>>
