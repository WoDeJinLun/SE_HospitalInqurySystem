<template>
    <div class="invoice">
      <h1>药品票据</h1>
      <form>
        <div>
          <label for="name">患者姓名：</label>
          <input type="text" id="name" v-model="patientName">
        </div>
        <div>
          <label for="drug">药品名称：</label>
          <input type="text" id="drug" v-model="drugName">
        </div>
        <div>
          <label for="price">药品单价：</label>
          <input type="number" id="price" v-model="drugPrice">
        </div>
        <div>
          <label for="quantity">药品数量：</label>
          <input type="number" id="quantity" v-model="drugQuantity">
        </div>
        <div>
          <label for="total">总价格：</label>
          <input type="number" id="total" v-model="totalPrice" disabled>
        </div>
      </form>
      <div class="invoice-preview">
        <h3>医院收据</h3>
        <div class="invoice-details">
          <p>患者姓名：{{ patientName }}</p>
          <p>药品名称：{{ drugName }}</p>
          <p>药品单价：{{ drugPrice }} 元/个</p>
          <p>药品数量：{{ drugQuantity }}</p>
          <p>总价格：{{ totalPrice }} 元人民币</p>
        </div>
      </div>
      <button class="save-btn" @click="saveInvoice">保存票据</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        patientName: '',
        drugName: '',
        drugPrice: '',
        drugQuantity: '',
        totalPrice: ''
      };
    },
    methods: {
      // 计算总价格
      calculateTotalPrice() {
        if (this.drugPrice && this.drugQuantity) {
          this.totalPrice = (this.drugPrice * this.drugQuantity).toFixed(2);
        }
      },
      // 保存票据
      saveInvoice() {
        this.$message.success('保存成功')
        // TODO: 保存到数据库或本地存储等
        console.log({
          patientName: this.patientName,
          drugName: this.drugName,
          drugPrice: this.drugPrice,
          drugQuantity: this.drugQuantity,
          totalPrice: this.totalPrice
        });
      }
    },
    computed: {
      invoiceTitle() {
        return `${this.patientName} 的药品票据`;
      }
    },
    watch: {
      // 监听药品单价和数量的变化
      drugPrice: 'calculateTotalPrice',
      drugQuantity: 'calculateTotalPrice'
    }
  };
  </script>
  
  <style>
  h1 {
    font-size: 32px;
    margin-bottom: 20px;
    margin-top: 20px;
    text-align: center;
}

  h2 {
    font-size: 24px;
}
  .invoice {
    display: flex;
    flex-direction: column;
  }
  
  form div {
    display: flex;
    margin-bottom: 16px;
  }
  
  form label {
    flex: 0 0 120px;
    font-size: 16px;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 5px;
    margin-left: 10px;
  }
  
  form input[type="text"],
  form input[type="number"] {
    padding: 8px;
    border-radius: 3px;
    border: 1px solid #ccc;
    font-size: 16px;
    flex: 1;
    margin-right: 20px;
  }
  
  form input[type="number"]:disabled {
    background-color: #f5f5f5;
  }
  
  .invoice-preview {
    margin-top: 24px;
    padding: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .invoice-preview h3 {
    margin-bottom: 8px;
    text-align: center;
  }
  
  .invoice-preview p {
    margin-bottom: 4px;
  }
  
  .save-btn {
    width: 150px;
    height: 40px;
    background-color: #409eff;
    color: #fff;
    border-radius: 3px;
    margin-top: auto;
    margin-bottom: 16px;
    border: none;
    font-size: 18px;
    cursor: pointer;
  }
  
  .save-btn:hover {
    background-color: #66b1ff;
  }
  </style>