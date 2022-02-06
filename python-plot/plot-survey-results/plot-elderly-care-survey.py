import pandas as pd
import matplotlib.pyplot as plt


labels = ['Positive', 'Negative']
colors = ['limegreen', 'tomato']
values = ['60.1', '39.9']

plt.pie(values, labels = labels, colors = colors, startangle=90, autopct = '%1.1f%%')
plt.title('Elderly care in Södertälje 2021')
plt.tight_layout()
plt.savefig('elderly-care.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

plt.show()