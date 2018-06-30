# Instructions

The 2_flask+pandas_example folder contains the files from the previous screencast. There's nothing to do here other than to see that you can use pandas and flask together.

If you run the web app, you'll find that it still works. To run the web app:
1. In the terminal, type `cd 2_flask+pandas_example`
2. Then `python worldbank.py`
3. The data variable will print out to the terminal
4. You can open the web app in the browser as well. You can do this using the `env | grep WORK` command in the terminal to see your WORKSPACE envirnomental variables. And from there the web address is `http://WORKSPACESPACEID-3001.WORKSPACEDOMAIN` replacing WORKSPACEID and WORKSPACEDOMAIN with your values.

The next step will be to use this wrangled data in a Plotly visualization. You can do this in the back-end of the web app with Plotly's Python library and Python dictionaries. And then finally, you'll need to send these dictionaries containing the visualizations to the front-end of the web app.

This is what you're going to do next.