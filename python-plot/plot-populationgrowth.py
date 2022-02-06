import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/demographics-data/data2use_in_plot.csv')#, names=headers)

fig,ax = plt.subplots()

ax.plot(df.year,df.population,'-<',color='red')
ax.set_xlabel("Year")
ax.set_ylabel("Total Population", color = 'red')

ax2 = ax.twinx()
ax2.plot(df.year, df.seniors, '-o' , color = 'green')
ax2.set_ylabel("Population >65 years", color = 'green')
ax2.set_xticklabels(df.year)
fig.tight_layout()
fig.savefig('demographics-plot.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
plt.show()