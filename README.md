# How to use this example
To get started with this example, follow the steps below to set up and run the tool in your preferred environment. We provide at least three ways to run this tool:

## 1. Run the app locally

Create a virtual environment:
```bash
python -m venv .venv
```

On macOS or Linux, activate the virtual environment:
```bash
source .venv/bin/activate
```

Run the app:
```bash
streamlit run uploader.py
```

You should be able to see the app on `localhost:8051` (if port 8051 is available). If the port is in use, the command output will indicate the port being used. Open the specified port in your browser to access the app.

## 2. Run the app on Galaxy

Visit [the Galaxy Cancer server](https://cancer.usegalaxy.org/root?tool_id=interactive_test_uploader) to experience the tool.

Alternatively, set up the tool on your local Galaxy instance. The Galaxy tool XML file is provided under the `tools` folder in this repository.

## 3. Deploy the tool using any cloud computing platform like Streamlit Cloud

You can deploy this tool on cloud platforms such as Streamlit Cloud for broader accessibility. Follow the deployment instructions provided by the respective platform to set up and run the app seamlessly.