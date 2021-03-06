def partition3(a, l, r):
    x = a[r]
    j = r
    for i in range(l+1, r+1):
        if a[i] <= x:
            j -=1
            a[i], a[j] = a[j], a[i]
    a[r], a[j] = a[j], a[r]
    return j


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    n = partition3(a,l,r)
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
