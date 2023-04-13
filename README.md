# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Windows)

To activate the Virtual machine,put in the project directory then use: 

    .\venv\Scripts\activate

To deactivate the Virtual machine run: 

    deactivate

1. This will activate the virtual environment.  Yous should see `(venv)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container(on your local machine with port 5000)

    >docker run -p 5000:5000 YOUR_NAME
