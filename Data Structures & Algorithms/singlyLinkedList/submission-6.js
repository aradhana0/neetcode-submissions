class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if(this.head === null) return -1;
        let curr = this.head;
        let i = 0;
        while(i < index) {
            i++;
            if(curr.next === null) return -1;
            curr = curr.next;
        }
        return curr.val;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const node = new Node(val);
        if(!this.head){
           this.head = node;
           this.tail = node;
        }
        else{
            node.next = this.head;
            this.head = node;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let node = new Node(val);
        if(!this.tail){
            this.tail = node;
            this.head = node;
        } 
        else {
            this.tail.next = node;
            this.tail = this.tail.next;
        }
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        if(this.head === null) return false;
        let curr = this.head;
        if(index === 0) {
            this.head = this.head.next;
            return true;
        } 
        while (i < index - 1 && curr) {
            i++;
            if(curr.next === null) return false;
            curr = curr.next;
        }

        if (curr.next === this.tail) {
            this.tail = curr;
        }
        console.log('curr--->', this.head);
        // Remove the node ahead of curr
        if (curr.next ) {
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let resArr = [];
        if(!this.head || this.head.next === null) return [];
        let curr = this.head;

        while(curr) {
            resArr.push(curr.val);
            curr = curr.next;
            
        }
        return resArr;
    }
}

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
