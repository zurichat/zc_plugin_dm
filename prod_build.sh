#Build script to be run before commiting and pushing to remote
#
#static files route set to remote host
#change this to your remote host address + /static
#example: https://dm.zuri.chat/static
export BASE_URL="http://localhost/static"

#change to frontend directory and build app with npm
cd frontend
npm install
npm run build

#change to root directory
cd ..

#stage, commit and push your code to remote
#do not forget to pull from upstream before pushing