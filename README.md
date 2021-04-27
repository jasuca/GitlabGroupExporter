# (BETA) GitlabGroupExporter 
Export group with all projects and subgroups

# Requirements  

* python >=3.6
* admin rights over gitlab (owner role to export groups and projects, admin rights to create groups, projects...)
* API token on both Gitlab (asigned to your gitlab user)

# Install  
1. Install requirements

```sh
pip3 install -r requirements.txt
```

# Usage  

## Configuration file (config.yml)

Set your configuration with config.yml (on root path)

```
vim config.yml
```

```yaml
origin:
  gitlab_url: https://oldgitlab.com
  token: XXXX
  group_id: 2
  skip_projects:
    - RRR
    - WWWW
destination:
  gitlab_url: http://newgitlab.com
  token: XXXX
  group_name: ZZZZZ
```

### Variables description
 * **origin:gitlab_url**: Gitlab url from you want to export the group
 * **origin:token**: Gitlab token with API access from old gitlab instance
 * **destination:gitlab_url**: Gitlab url where you want to import that new group
 * **destination:token**: Gitlab token with API access from new gitlab instance
 * **origin:group_id**: Group Id from the group that you want to export (on old gitlab instance)
 * **destination:group_name**: New group name that you will create (import) over that new gitlab instance

## Example command  

```
mkdir /tmp/gitlab 
python3 main.py -p /tmp/gitlab/ -l INFO
```
**Note:** Directory must be created and need to be empty. When you set the directory on the command, need to end with slash '/'

# Examples  

# Group to be exported  

![Old group](/img/old_gitlab.png)

# New group imported from old gitlab instance  

![New group](/img/new_gitlab.png)

# Command
![Command example](/img/command-example.png)

# Config  

![Config example](/img/config-example.png)

# Result
![Result](/img/result-example.png)


Then, delete the directory if you no longer need it.

```sh
rmdir /tmp/gitlab
```

# About code

* This code written in python possibly has many unanticipated improvements. It is not a program designed at a productive level contemplating all the possible errors that may exist.

* It is only a functional program designed to automate.

* This code is build on top of GitLab API. Learn more on their [Docs](https://python-gitlab.readthedocs.io/)

* As for the python code itself, possible improvements are welcome. I am not a 100% experienced python programmer, but I am having fun. Enjoy :)