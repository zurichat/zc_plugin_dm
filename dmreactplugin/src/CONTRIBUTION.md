# Guideline on how to contribute to the project

When contributing to the project, please follow these guidelines:

-   Check the issues we have on [GitHub](https://github.com/zurichat/zc_plugin_dm/issues).

-   Check the design you're creating on figma link here [Figma Design](https://www.figma.com/file/LQAKDdQteJwjrhtFTv7PlV/Zuri.Chat-DM?node-id=13%3A2)

#### Please note, the above guideline is a prequisite for this project.

## Contributing to the project

1.  Fork the repository on [GitHub](https://github.com/zurichat/zc_plugin_dm/fork)
2.  Clone the repository on your local machine `git clone https://github.com/zurichat/zc_plugin_dm.git`
3.  CD into the directory `$cd zc_plugin_dm` on your machine
4.  CD into the Directory `$cd dmreactplugin` and `$cd dmspa` on your machine
5.  Run `npm install or yarn` to install all the dependencies
6.  Run `yarn start` on both directories `dmreactplugin` and `dmspa` to start the server
7.  Launch your browser and go to `http://localhost:9000` or `http://localhost:9000/dm`

### Pull Requests Process

$ `git add .`

$ `git commit -m "your-message"`

##### the component you worked on

$ `git remote -v`

##### check your remote branches

$ `git remote add upstream git@github:zurichat/zc_plugin_dm.git`

##### Add upstream to repo directory to the upstream forked repository

$ `git fetch upstream`

##### Fetch from the upstream branch if there's an update

$ `git checkout -b <your_branch_name>`

##### Checkout your branch name here

$ `git push upstream`

##### Push the code to the upstream branch and make a pull-request to the **_dev branch_**

<hr>

**_THANK YOU FOR READING THIS DOCUMENTATION._**
