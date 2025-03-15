import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
# import seaborn as sns
# import matplotlib.pyplot as plt
from PIL import Image



# Streamli part

st.set_page_config(page_title='Airbnb Data Analysis', page_icon=':house:', layout='wide', initial_sidebar_state='expanded')
st.title('Airbnb Data Analysis')
st.write('')

# Load data
def load_data():
    df = pd.read_csv('C:\Sudhakar\Projects\Airbnb Analysis\Airbnb.csv')
    return df
df = load_data()

# Sidebar navigation
with st.sidebar:
    option = option_menu(
    menu_title='Navigation',  
    options=['Home', 'Data Analysis', 'About'], 
    icons=['house', 'bar-chart', 'info-circle'],   
    menu_icon='cast',  
    default_index=0 ) 
    
    
# Main content for option 'Home' 
if option == 'Home':
    
    st.image(Image.open(r"C:\Sudhakar\Projects\Airbnb Analysis\Dataset & Documents\img.JPG"), width= 400)


    st.header("About Airbnb") 
    st.write("") 
    st.write('''Airbnb is an online marketplace that connects people who want to rent out 
              their property with people who are looking for accommodations, 
              typically for short stays. Airbnb offers hosts a relatively easy way to 
              earn some income from their property.Guests often find that Airbnb rentals    
              are cheaper and homier than hotels.''') 
    st.write("") 
    st.write('''Airbnb Inc (Airbnb) operates an online platform for hospitality services. 
                  The company provides a mobile application (app) that enables users to list, 
                  discover, and book unique accommodations across the world. 
                  The app allows hosts to list their properties for lease, 
                  and enables guests to rent or lease on a short-term basis, 
                  which includes vacation rentals, apartment rentals, homestays, castles, 
                  tree houses and hotel rooms. The company has presence in China, India, Japan, 
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy, 
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others. 
                  Airbnb is headquartered in San Francisco, California, the US.''') 
     
    st.header("Background of Airbnb") 
    st.write("") 
    st.write('''Airbnb was born in 2007 when two Hosts welcomed three guests to their 
              San Francisco home, and has since grown to over 4 million Hosts who have 
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.''')




# Main content for option 'Data Analysis'
if option == 'Data Analysis':
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["PRICE ANALYSIS", "AVAILABILITY ANALYSIS", "LOCATION ANALYSIS", "GEOSPATIAL ANALYSIS", "TOP CHAERTS"])

    with tab1:
        st.header("Price Analysis")
        st.write("Price Analysis of Airbnb Listings")
        col1, col2 = st.columns(2)	
        
        with col1:
            country= st.selectbox("Select the Country",df["country"].unique())

            df_1= df[df["country"] == country]
            df_1.reset_index(drop= True, inplace= True)

            room_type= st.selectbox("Select the Room Type",df_1["room_type"].unique())
            
            df_2= df_1[df_1["room_type"] == room_type]
            df_2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df_2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)
            
            
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_type= st.selectbox("Select the Property_type",df_2["property_type"].unique())

            df_3= df_2[df_2["property_type"] == proper_type]
            df_3.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df_3.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)
        
        
        
        with col1:

            hostresponsetime= st.selectbox("Select the host response time",df_3["host_response_time"].unique())

            df_4= df_3[df_3["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df_4.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS FOR PRICE',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)

            st.plotly_chart(fig_do_bar)
           
            
        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df_4.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES BASED ON PRICE',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)
            
            
    with tab2:
        
        def data_load():
            availability_df = pd.read_csv("C:\Sudhakar\Projects\Airbnb Analysis\Airbnb.csv")
            return availability_df

        availability_df = data_load()

        st.title("**AVAILABILITY ANALYSIS**")
        col1, col2= st.columns(2)
        
        
        
        with col1:
            
            available_country = st.selectbox("Select the available country",availability_df["country"].unique())

            availability_df_1= df[df["country"] == available_country]
            availability_df_1.reset_index(drop= True, inplace= True)

            available_property_type= st.selectbox("Select the Property Type",availability_df_1["property_type"].unique())
            
            availability_df_2= availability_df_1[availability_df_1["property_type"] == available_property_type]
            availability_df_2.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(availability_df_2, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
            
            
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(availability_df_2, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)
        
        
        with col1:
            
            df_a_sunb_90= px.sunburst(availability_df_2, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(availability_df_2, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
        
        roomtype_a= st.selectbox("Select the available Room Type", availability_df_2["room_type"].unique())

        availability_df_3= availability_df_2[availability_df_2["room_type"] == roomtype_a]

        mul_bar_availability_df= pd.DataFrame(availability_df_3.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        mul_bar_availability_df.reset_index(inplace= True)

        fig_mul_bar_availability_df = px.bar(mul_bar_availability_df, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

        st.plotly_chart(fig_mul_bar_availability_df)
        
        
        
        
    with tab3:

        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("C:\Sudhakar\Projects\Airbnb Analysis\Airbnb.csv")
            return df

        location_df= datafr()

        country_location= st.selectbox("Select the country_location",location_df["country"].unique())

        location_df_1= location_df[location_df["country"] == country_location]
        location_df_1.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property_type_l",location_df_1["property_type"].unique())

        location_df_2= location_df_1[location_df_1["property_type"] == proper_ty_l]
        location_df_2.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(location_df_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + location_df_2['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= location_df_2[location_df_2["price"] <= differ_max_min*0.30 + location_df_2['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + location_df_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + location_df_2['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= location_df_2[location_df_2["price"] >= differ_max_min*0.30 + location_df_2['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + location_df_2['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + location_df_2['price'].min())+' '+str('to')+' '+str(location_df_2['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= location_df_2[location_df_2["price"] >= differ_max_min*0.60 + location_df_2['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= location_df_2['price'].max()-location_df_2['price'].min()

        val_sel= st.radio("Select the Price Range",[str(location_df_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + location_df_2['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + location_df_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + location_df_2['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + location_df_2['price'].min())+' '+str('to')+' '+str(location_df_2['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=['listing_url', 'name', 'summary', 'space', 'description',
                                                    'neighborhood_overview', 'notes', 'transit', 'access', 'interaction',
                                                    'house_rules', 'property_type', 'room_type', 'bed_type',
                                                    'cancellation_policy', 'last_scraped', 'calendar_last_scraped',
                                                    'amenities_x', 'images', 'host', 'address', 'availability', 'reviews',
                                                    'host_url', 'host_name', 'host_location', 'host_response_time',
                                                    'host_thumbnail_url', 'host_picture_url', 'host_neighbourhood',
                                                    'host_response_rate', 'host_is_superhost', 'host_has_profile_pic',
                                                    'host_identity_verified', 'host_verifications', 'street', 'suburb',
                                                    'government_area', 'market', 'country', 'country_code', 'location_type',
                                                    'is_location_exact', 'amenities_y']).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room Type for the location", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)
        
        
        
    with tab4:
        
        st.title("GEOSPATIAL AANALYSIS")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)   
        
        
        
    # Top Charts
    with tab5:

        country= st.selectbox("Select the Country type",df["country"].unique())

        top_chart_df= df[df["country"] == country]

        top_chart_property_type= st.selectbox("Select the Property type for view the chart",top_chart_df["property_type"].unique())

        top_chart_df_1= top_chart_df[top_chart_df["property_type"] == top_chart_property_type]
        top_chart_df_1.reset_index(drop= True, inplace= True)

        top_chart_df_1_sorted= top_chart_df_1.sort_values(by="price")
        top_chart_df_1_sorted.reset_index(drop= True, inplace= True)


        price_df= pd.DataFrame(top_chart_df_1_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        price_df.reset_index(inplace= True)
        price_df.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(price_df, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(price_df, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            price_df_1= pd.DataFrame(top_chart_df_1_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            price_df_1.reset_index(inplace= True)
            price_df_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(price_df_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(price_df_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room Type for chart view",top_chart_df_1_sorted["room_type"].unique())

        top_chart_df_2= top_chart_df_1_sorted[top_chart_df_1_sorted["room_type"] == room_type_t]

        top_chart_df_2_sorted_price= top_chart_df_2.sort_values(by= "price")

        top_chart_df_2_sorted_price.reset_index(drop= True, inplace = True)

        top_chart_df_2op_50_price= top_chart_df_2_sorted_price.head(100)

        fig_top_50_price_1= px.bar(top_chart_df_2op_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,top_chart_df_2op_50_price["price"].max()),
                                title= "MINIMUM NIGHTS, MAXIMUM NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(top_chart_df_2op_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED TYPE",
                                range_color=(0,top_chart_df_2op_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)
            
            
            
            


if option == 'About':
    
    st.header("ABOUT AIRBNB PROJECT") 
 
    st.subheader(":green[1. Data Collection:]") 
 
    st.write('''***Gather data from Airbnb's public API or other available sources. 
        Collect information on listings, hosts, reviews, pricing, and location data.***''') 
     
    st.subheader(":green[2. Data Cleaning and Preprocessing:]") 
 
    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality. 
        Convert data types, handle duplicates, and standardize formats.***''') 
     
    st.subheader(":green[3. Exploratory Data Analysis (EDA):]") 
 
    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data. 
        Explore relationships between variables and identify potential insights.***''') 
     
    st.subheader(":green[4. Visualization:]") 
 
    st.write('''***Create visualizations to represent key metrics and trends. 
        Use charts, graphs, and maps to convey information effectively. 
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''') 
     
    st.subheader(":green[5. Geospatial Analysis:]") 
 
    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings. 
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')
