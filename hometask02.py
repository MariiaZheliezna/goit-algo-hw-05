def binary_search_modified(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    num_iterations = 0

    # не можемо надати верхню межу - пошуковий елемент більший за найбільший елемент масиву
    if upper_bound < x:
        return num_iterations, None
 
    while low <= high:
        num_iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return num_iterations, arr[mid]
 
    # якщо елемент не знайдений
    return num_iterations, upper_bound

def main():
    arr = [0.65, 0.799, 1.96, 2.74, 4.66, 6.78, 8.868, 11.73, 15.15, 19.788, 66.868]
    x = -2
    print(binary_search_modified(arr, x))
    
if __name__ == '__main__':
    main()