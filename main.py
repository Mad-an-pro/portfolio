from portf import builder

# create object from Data Class
data = builder.Data("Your Name")

# Edit Attributes of Object 
data.image = "Image Url"
data.about = "Enter details about you"

# To The the app
builder.RunApp(port=5000,dataobj=data)
