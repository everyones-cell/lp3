# Huffman Encoding using Greedy Strategy
import heapq

text = input("Enter text: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

heap = [[f, ch] for ch, f in freq.items()]
heapq.heapify(heap)

if len(heap) == 1:
    codes = {heap[0][1]: "0"}
else:
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, [a[0] + b[0], a, b])

    codes = {}
    def make_codes(node, code=""):
        if len(node) == 2 and isinstance(node[1], str):
            codes[node[1]] = code
        else:
            make_codes(node[1], code + "0")
            make_codes(node[2], code + "1")
    make_codes(heap[0])

print("Huffman codes:")
for ch, code in codes.items():
    print(repr(ch), ":", code)
print("Encoded:", "".join(codes[ch] for ch in text))
