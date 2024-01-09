import csv
import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    salaries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            salaries.append(float(row[0]))
    return salaries

def calculate_statistics(salaries):
    mean_salary = np.mean(salaries)
    std_dev = np.std(salaries)
    
    # Calculate X - value such that 10% of people have a salary below X
    x_percentile = np.percentile(salaries, 10)
    
    return round(mean_salary, 2), round(x_percentile, 2)

def plot_histogram_and_distribution(salaries, mean_salary, x_percentile):
    # Create a histogram
    plt.hist(salaries, bins=30, density=True, alpha=0.75, color='b', edgecolor='black')

    # Calculate and plot the probability density function
    x = np.linspace(min(salaries), max(salaries), 100)
    pdf = (1 / (np.std(salaries) * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_salary) / np.std(salaries))**2)
    plt.plot(x, pdf, color='red', linewidth=2, label='PDF')

    # Plot mean and X values on the graph
    plt.axvline(mean_salary, color='green', linestyle='dashed', linewidth=2, label=f'Mean Salary: {mean_salary}')
    plt.axvline(x_percentile, color='purple', linestyle='dashed', linewidth=2, label=f'X (10%): {x_percentile}')

    # Add labels and legend
    plt.xlabel('Annual Salary (Euros)')
    plt.ylabel('Probability Density')
    plt.title('Salary Distribution and Probability Density Function')
    plt.legend()

    # Show the plot
    plt.show()

def main():
    # Read data from the CSV file
    filename = "data5.csv"
    salaries = read_data(filename)

    # Calculate statistics
    mean_salary, x_percentile = calculate_statistics(salaries)

    # Plot histogram and distribution
    plot_histogram_and_distribution(salaries, mean_salary, x_percentile)

if __name__ == "__main__":
    main()
