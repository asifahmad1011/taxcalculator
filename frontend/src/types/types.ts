export interface Result {
    items: Product[]
}

export interface Product {
    itemCode: number;
    itemName: string;
    Category: string;
    salesTaxExempted: boolean;
    isImported: boolean;
    price: number;
    quantity: number;
}


export interface ItemWithTax {
    itemName: string;
    price: number;
    quantity: number;
    taxOnProduct: number;
    totalPrice: number;
}

export interface Bill {
    items: ItemWithTax[];
    salesTaxTotal: number;
    grandTotal: number;

}