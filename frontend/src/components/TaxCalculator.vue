<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-select
          v-model="selectedItemCode"
          :items="items.items"
          label="Select Product"
          :item-text="'itemName'"
          :item-value="'itemCode'"
        >
        </v-select>
      </v-col>
      <v-col cols="12">
        <v-btn depressed color="primary" @click="addItem()">
          Add To Cart
        </v-btn>
        <v-btn class="ml-4" depressed color="#EF5350" @click="clearCart()">
          Clear Cart
        </v-btn>
      </v-col>
      <v-col v-if="selectedItems.length > 0" cols="12">
        <v-data-table
          :headers="headers_selected_products"
          :items="selectedItems"
          :items-per-page="5"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
      <v-col v-if="selectedItems.length > 0" cols="12">
        <v-btn depressed color="primary" @click="calculateTax()">
          Generate Receipt
        </v-btn>
      </v-col>
      <v-col v-if="isShow" cols="12">
        <v-data-table
          :headers="headers_receipt"
          :items="receipt.items"
          :items-per-page="5"
          class="elevation-1"
        >
          <template slot="body.append">
            <tr class="black--text">
              <th class="title">Total Sales Tax</th>
              <th class="title">{{ receipt.salesTaxTotal }}</th>
            </tr>
            <tr class="black--text">
              <th class="title">Grand Total</th>
              <th class="title">{{ receipt.grandTotal }}</th>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import { Product, Result, Bill } from "../types/types";

export default Vue.extend({
  name: "TaxCalculator",

  data: () => ({
    baseURL: "http://localhost:8000/",
    items: {} as Result,
    selectedItems: [] as Product[],
    selectedItemCode: 0 as number,
    cart: [] as number[],
    isShow: false,
    receipt: {} as Bill,

    headers_selected_products: [
      {
        text: "Item Name",
        align: "start",
        sortable: true,
        value: "itemName",
      },
      { text: "Price", value: "price" },
      { text: "Quantity", value: "quantity" },
      // { text: "Imported", value: "isImported" },
      // { text: "Price Including Tax", value: "totalPrice" },
    ],
    headers_receipt: [
      {
        text: "Item Name",
        align: "start",
        sortable: true,
        value: "itemName",
      },
      { text: "Price Including Tax", value: "totalPrice" },
      { text: "Quantity", value: "quantity" },
      // { text: "SalesTax", value: "taxOnProduct" },
      // { text: "Price Without Tax", value: "price" },
    ],
  }),

  mounted() {
    // calling function at the time of component loading...
    this.getAllItems();
  },

  methods: {
    // Function to fetch all products
    async getAllItems(): Promise<Result> {
      var url = this.baseURL + "getAllProducts";
      await axios
        .get(url)
        .then((response) => {
          console.log("items", response.data);
          this.items = response.data;
          console.log("data..", this.items);
          // return this.$data.items;
        })
        .catch((error) => {
          alert(error);
        });
      return this.$data.items;
    },

    clearCart() {
      this.cart = [];
      this.receipt.items = [];
      this.receipt.salesTaxTotal = 0.0;
      this.receipt.grandTotal = 0.0;
      this.isShow = false;
      this.selectedItems = [];
    },

    // function for adding item to cart and data table
    // Item code is added into cart variable
    // A Complete object is being added into selectedItems array of objects
    addItem(): void {
      this.cart.push(this.selectedItemCode);
      console.log("items in cart", this.cart);
      var len = this.items.items.length;
      for (var i = 0; i < len; i++) {
        if (this.items.items[i].itemCode == this.selectedItemCode) {
          this.selectedItems.push(this.items.items[i]);
          console.log("testing...", this.selectedItems);
        }
      }
      console.log("selected items ..... ", this.selectedItems);
    },

    async calculateTax(): Promise<void> {
      var cartItems = { id: this.cart };
      console.log("items in cart,,", cartItems);
      var url = this.baseURL + "calculateTax";
      await axios
        .post(url, cartItems)
        .then((response) => {
          this.receipt.items = response.data.items;
          this.receipt.salesTaxTotal = response.data.salesTaxTotal;
          this.receipt.grandTotal = response.data.grandTotal;
          console.log("items", this.receipt);
          this.isShow = true;
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
});
</script>
