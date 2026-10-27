class DynamicArray {
    int[] array;
    int size = 0;
    int capacity;

    public DynamicArray(int capacity) {
        this.array = new int[capacity];
        this.capacity = capacity;
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (this.size + 1 > this.capacity){
            this.resize();
        }

        this.array[this.size] = n;
        this.size++;
    }

    public int popback() {
        int last = this.array[this.size - 1];
        this.size--;
        return last;
    }

    private void resize() {
        int newCapacity = this.capacity * 2;
        int[] temp = new int[newCapacity];
        for(int i = 0; i < this.size; i++){
            temp[i] = this.array[i];
        }

        this.array = temp;
        this.capacity = newCapacity;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
