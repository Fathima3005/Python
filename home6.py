blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

for x in blog_views:
    if x>1000:
        print("Trending")
    elif 500<= x <=1000 :
        print("average")     
    else:
        print("Low Traffic")

total_views=sum(blog_views) 
print("Total number of views:",total_views)    

trending_count=0
for x in blog_views:
  if x> 1000:
    trending_count = trending_count+1
print("Posts that were trending:",trending_count)