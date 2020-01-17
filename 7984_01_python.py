# import pandas, numpy
# Create the required data frames by reading in the files
df=pd.read_excel('SaleData.xlsx')
df_3=pd.read_csv('diamonds.csv')
df_2=pd.read_csv("imdb.csv",escapechar='\\')

# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    
	ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):'
	return(df.groupby([df.OrderDate.dt.year,df.Region])["Sale_amt"].sum())
   

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
	df['days_diff']=df['OrderDate'].sub(pd.to_datetime(date))
	return df

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df2):
	df2=pd.DataFrame()
	df2["SalesMan"]=df.groupby(["Manager"])["SalesMan"].unique()
	return df2
    
# Q5 For all regions find number of salesman and number of units
def slsmn_units(df2):
 	df2=pd.DataFrame()
	df2["Salesman_count"]=df.groupby(["Region"])["SalesMan"].nunique()
	df2["total_sales"]=df.groupby(["Region"])["Sale_amt"].sum()
	return(df2)	  

# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    q10=(df.groupby(["Manager"])["Sale_amt"].sum()/df["Sale_amt"].sum())*100
    return q10

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df_2):
	return(df_2.loc[4]["imdbRating"])

# Q8 return titles of movies with shortest and longest run time
def movies(df_2):
	return(df_2.iloc[[df_2["duration"].idxmax(),df_2["duration"].idxmin()]])

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df_2):
	return(df_2.sort_values(['year','imdbRating'],ascending=[True,False]))

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df_2):
	return(df_2[(df_2["duration"]>30 )&(df_2["duration"]<180)])

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df_3):
	return(len(df_3[df_3.duplicated()]))

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df_3):
	return(df_3.dropna(subset=["carat","cut"]))

# Q13 subset only numeric columns
def sub_numeric(df_3):
	df3=df_3.select_dtypes(include=np.number)
	return(df3)
# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	df_3['z']=df_3['z'].apply(pd.to_numeric,errors='coerce')
	df_3['volume']=df_3.apply(lambda df: df['x']*df['y']*df['z'] if df['depth']>60 else 8,axis=1)
	return(df_3)

# Q15 impute missing price values with mean
def impute(df):
	return(df_3.fillna(df_3.mean()))
