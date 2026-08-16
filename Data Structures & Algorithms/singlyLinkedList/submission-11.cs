#nullable enable

public class Node {

    public int value { get; set; }
    public Node? nextNode { get; set; }

    public Node(int value, Node nextNode)
    {
        this.value = value;
        this.nextNode = nextNode;
    }
}


public class LinkedList {

    public Node? head { get; set; }

    public LinkedList() {
        this.head = null;
    }

    public int Get(int index) {
        var currentNode = this.head;
        var idx = 0;
        while(currentNode != null){
            if (idx == index){
                return currentNode.value;
            }
            currentNode = currentNode.nextNode;
            idx++;
        }

        return -1;
    }

    public void InsertHead(int val) {
        if (this.head == null){
            this.head = new Node(val, null);
        }
        else {
            Node secondNode = this.head;
            this.head = new Node(val, secondNode);
        }
    }

    public void InsertTail(int val) {
        if (this.head == null){
            this.head = new Node(val, null);
            return;
        }
        var currentNode = this.head;
        Node? lastNode = null;
        while(currentNode != null){
            lastNode = currentNode;
            currentNode = currentNode.nextNode;
        }
        lastNode.nextNode = new Node(val, null);
    }

    public bool Remove(int index) {
        if(this.head == null){
            return false;
        }
        if(index == 0){
            this.head = this.head.nextNode;
            return true;
        }
        var currentNode = this.head;
        var idx = 0;
        Node? lastNode = null;
        while(currentNode != null){
            if (idx == index){
                break;        
            }
            lastNode = currentNode;
            currentNode = currentNode.nextNode;
            idx++;
        }

        if (currentNode == null){
            return false;
        }
        if (lastNode != null) {
            lastNode.nextNode = currentNode.nextNode;
            return true;
        }

        lastNode.nextNode = currentNode.nextNode;

        return true;
    }

    public List<int> GetValues() {
        var currentNode = this.head;
        List<int> valueList = new List<int>();
        while(currentNode != null){
            valueList.Add(currentNode.value);
            currentNode = currentNode.nextNode;
        }
        return valueList;
    }
}