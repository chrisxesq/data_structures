# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps

    def sift_down(node_index):
        min_index = node_index
        if 2*node_index + 1 <size:
            l = 2*node_index + 1
            if data[l]<data[min_index]:
                min_index = l
        if 2*node_index + 2 <size:
            r = 2*node_index + 2
            if data[r]<data[min_index]:
                min_index = r 
        if node_index != min_index:
            swap_history.append((node_index, min_index))
            data[node_index], data[min_index] = data[min_index], data[node_index]
            return sift_down(min_index)
    
    swap_history = []
    size = len(data)
    for i in range(int(size/2),-1,-1):
        sift_down(i)
    return swap_history

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
