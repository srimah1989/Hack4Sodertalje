import pandas as pd
import matplotlib.pyplot as plt


labels = ['Positive', 'Negative']
colors = ['limegreen', 'tomato']
values = ['46', '53']

plt.pie(values, labels = labels, colors = colors, startangle=90, autopct = '%1.1f%%')
plt.title('Places or activities for elderly to meet in Södertälje 2021')
plt.tight_layout()
plt.savefig('places-for-elderly-to-meet.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

plt.show()