
# coding: utf-8

# In[1]:


pwd


# In[44]:


import json
class MosaicApp(object):
    #Initializing output per page and current page number requested
    def __init__(self, page_num):
        self.pagination_number = 10
        self.page_num = page_num
        
    ## For showing output based on the page number
    def api_pagination(self, output):
        current_page_output = []
        pagination_number = 10
        page_num_start = (self.page_num-1)*(self.pagination_number)
        page_num_end = (self.page_num)*(self.pagination_number)
        for page_no in range(page_num_start, page_num_end):
            current_page_output.append(output[page_no])
        return current_page_output
        
    # load the data in memory (As its just 5mB data used dictionary for now)
    # Can also use redis instead.
    def data_store(self):
        data_store = {}
        with open("AI_Dataset.json", "r") as read_file:
            data = read_file.read()
            data_store['data'] = json.loads(data)
        # return data_store
        current_page_output = self.api_pagination(data_store['data'])
        return current_page_output
    
    # Gives all the projectnames and description
    def all_projname_and_description(self, data_store):
        output = []
        # data = data_store['data']
        for record in data_store:
            inner_output = []
            if "Project School Name" in record:
                inner_output.append(record["Project School Name"])
            if "Project Description" in record:
                inner_output.append(record["Project Description"])
            if inner_output:
                output.append(inner_output)
        return output
        
    # Filter on required params
    def filter_on(self, data_store, params):
        filter_on_params = ["Project Phase Actual Start Date", 
                            "Project Phase Planned End Date", 
                            "Project Phase Actual End Date", 
                            "Project Budget Amount", 
                            "Final Estimate of Actual Costs Through End of Phase Amount", 
                            "Total Phase Actual Spending Amount"]
        if len(params)<1:
            return []
        else:
            filter_params = []
            for param in params:
                if param in filter_on_params:
                    filter_params.append(param)
        if len(filter_params)<1:
            return []
        else:
            output = []
            # data = data_store['data']
            for record in data_store:
                inner_output = []
                for param in filter_params:
                    if param in record:
                        inner_output.append(record.get(param))
                if inner_output:
                    output.append(inner_output)
            return output
            
            
        
m = MosaicApp(1)
data = m.data_store()
data1 = m.all_projname_and_description(data)
print(data1)
## Give the params you want the filtered output for
params = ["Project Phase Actual Start Date", 
          "Project Phase Planned End Date", 
          "Project Phase Actual End Date", 
          "Project Budget Amount", 
          "Final Estimate of Actual Costs Through End of Phase Amount", 
          "Total Phase Actual Spending Amount"]
data2 = m.filter_on(data, params)
print(data2)


# In[ ]:


# To Do for the UI
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()
    

