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
      patientName: "",
      drugName: "",
      drugPrice: "",
      drugQuantity: "",
      totalPrice: "",
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
      this.$message.success("保存成功");
      // TODO: 保存到数据库或本地存储等
      console.log({
        patientName: this.patientName,
        drugName: this.drugName,
        drugPrice: this.drugPrice,
        drugQuantity: this.drugQuantity,
        totalPrice: this.totalPrice,
      });
    },
  },
  computed: {
    invoiceTitle() {
      return `${this.patientName} 的药品票据`;
    },
  },
  watch: {
    // 监听药品单价和数量的变化
    drugPrice: "calculateTotalPrice",
    drugQuantity: "calculateTotalPrice",
  },
};
</script>

<style>


.invoice {
  display: flex;
  flex-direction: column;
  background-color: #d0f0c0;
  padding: 16px;
  border-radius: 5px;
  max-width: 500px;
  margin: 0;
  margin-left: 0;
}


h1 {
  font-size: 32px;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
  color: #448f1d;
}

h3 {
  font-size: 24px;
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
  color: #448f1d;
}

form input[type="text"],
form input[type="number"] {
  padding: 8px;
  border-radius: 3px;
  border: 1px solid #448f1d;
  font-size: 16px;
  flex: 1;
  margin-right: 20px;
}

form input[type="number"]:disabled {
  background-color: #f0f0f0;
}

.invoice-preview {
  margin-top: 24px;
  padding: 16px;
  border: 1px solid #448f1d;
  border-radius: 5px;
  background-color: #eaf7e0;
}

.invoice-preview h3 {
  margin-bottom: 8px;
  text-align: center;
  color: #448f1d;
}

.invoice-preview p {
  margin-bottom: 4px;
  color: #448f1d;
}

.save-btn {
  width: 150px;
  height: 40px;
  background-color: #448f1d;
  color: #fff;
  border-radius: 3px;
  margin-top: auto;
  margin-bottom: 16px;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

.save-btn:hover {
  background-color: #32741c;
}

.medical-record {
  display: flex;
  flex-direction: column;
  background-color: #d0f0c0;
  padding: 16px;
  border-radius: 5px;
  max-width: 500px;
  margin: 0 auto;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
  color: #448f1d;
}

.form-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
}

.form-group label {
  flex: 0 0 120px;
  font-size: 16px;
  color: #448f1d;
}

.form-group input,
.form-group select,
.form-group textarea {
  flex: 1;
  height: 30px;
  border-radius: 3px;
  border: 1px solid #448f1d;
  padding: 5px;
  font-size: 16px;
  margin-left: 30px;
}

.form-group textarea {
  height: 100px;
  resize: none;
}

.send-btn {
  width: 200px;
  height: 40px;
  background-color: #448f1d;
  color: #fff;
  border-radius: 3px;
  margin-top: 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

</style>
