<template>
  <div id="PersonalCenter">
    <el-container class="home-container">
      <el-header>
        <div>
          <span>个人中心</span>
        </div>
        <el-button type="info" @click="logout">
          退出
        </el-button>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-menu
            background-color="#e4f5ef"
            text-color="#000000"
            active-text-color="#02a774"
            unique-opened
            @select="handleMenuSelect"
          >
            <!-- 一级菜单 -->
            <el-submenu index="0">
              <!-- 一级菜单模板 -->
  
              <template #title>
                <i class="el-icon-user"></i>
                <span>register</span>
              </template>
              <el-menu-item index="0-1">I want register</el-menu-item>
              <el-menu-item index="0-2">Registration history</el-menu-item>
            </el-submenu>
            <el-submenu index="1">
              <!-- 一级菜单模板 -->
              <template #title>
                <i class="el-icon-user"></i>
                <span>个人信息</span>
              </template>
              <el-menu-item index="1-1">个人信息管理</el-menu-item>
            </el-submenu>

            <el-submenu index="2">
              <template #title>
                <i class="el-icon-chat-dot-square"></i>
                <span>诊断心得</span>
              </template>
              <el-menu-item index="2-1">就诊反馈</el-menu-item>
            </el-submenu>

            <el-submenu index="3">
              <!-- 一级菜单模板 -->
              <template #title>
                <i class="el-icon-warning-outline"></i>
                <span>关于我们</span>
              </template>
              <el-menu-item index="3-1">版本信息</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          
          <div class="main-content">
            <el-form
              v-show="showFormReg"
              :model="form"
              :rules="rules"
              label-width="100px"
            >
              <!-- Registration Form -->
              <template v-if="selectedSubMenu === '0-1'">
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="Department" prop="department">
                      <el-select
                        v-model="form.department"
                        placeholder="Please select department"
                      >
                        <el-option
                          v-for="department in departments"
                          :key="department.value"
                          :label="department.label"
                          :value="department.value"
                        ></el-option>
                      </el-select>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="Timeslot" prop="timeslot">
                      <el-select
                        v-model="form.timeslot"
                        placeholder="Please select timeslot"
                      >
                        <el-option
                          v-for="timeslot in timeslots"
                          :key="timeslot.value"
                          :label="timeslot.label"
                          :value="timeslot.value"
                        ></el-option>
                      </el-select>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="Doctor" prop="doctor">
                      <el-select
                        v-model="form.doctor"
                        placeholder="Please select doctor"
                      >
                        <el-option
                          v-for="doctor in doctors"
                          :key="doctor.value"
                          :label="doctor.label"
                          :value="doctor.value"
                        ></el-option>
                      </el-select>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="Description" prop="description">
                      <el-input
                        type="textarea"
                        :rows="4"
                        placeholder="Please enter description"
                        v-model="form.description"
                      ></el-input>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="Additional Requirements" prop="requirements">
                      <el-input
                        type="textarea"
                        :rows="4"
                        placeholder="Please enter additional requirements"
                        v-model="form.requirements"
                      ></el-input>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item>
                      <el-button type="primary" @click="submitForm">Submit</el-button>
                    </el-form-item>
                  </el-col>
                </el-row>
              </template>
            </el-form>
            </div>
            <div class="main-content">
            <el-form
              v-show="showFormRegTable"
              :model="form"
              :rules="rules"
              label-width="100px"
            >

              <!-- Registration History -->
              <template v-if="selectedSubMenu === '0-2'">
                <el-table :data="registrationHistory" stripe>
                  <el-table-column prop="registrationId" label="Registration ID"></el-table-column>
                  <el-table-column prop="department" label="Department"></el-table-column>
                  <el-table-column prop="timeslot" label="Timeslot"></el-table-column>
                  <el-table-column prop="doctor" label="Doctor"></el-table-column>
                  <el-table-column prop="status" label="Status"></el-table-column>
                  <el-table-column label="Actions">
                    <template slot-scope="scope">
                      <el-button
                        v-if="scope.row.status === 'Pending'"
                        type="danger"
                        @click="cancelRegistration(scope.row.registrationId)"
                      >
                        Cancel
                      </el-button>
                      <el-button v-else disabled>Cancel</el-button>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </el-form>
          </div>
          <div class="main-content">
            <div id="feedback">
            <div class="private-container">
              <div class="message-box"
                v-show="showFeedback"
              >
                <div class="title">
                  <span>就诊心得反馈</span>
                </div>
                <!-- 信息更改 -->
                <el-form  label-width="100px" class="message-form">
                  <!-- 姓名 -->
                  <el-form-item label="反馈内容:" >
                    <el-input
                      type="textarea"
                      :rows="18"
                      placeholder="请输入内容"
                      v-model="textarea">
                    </el-input>
                  </el-form-item>
                </el-form>
                <div class="button">
                  <el-button v-show="showFeedback" type="success">提交</el-button>
                  <el-button type="info">清除</el-button>
                </div>
              </div>
            </div>
          </div>
          </div>
          <div class="main-content">
            <!--<h1>Welcome to Personal Center</h1>-->
            <el-form
              v-show="showForm"
              :model="form"
              :rules="rules"
              label-width="100px"
            >
            <el-row>
              <el-col :span="12">
                <el-form-item label="姓名" prop="name" required>
                  <el-input v-model="form.name" placeholder="必填"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="邮箱" prop="email" required>
                  <el-input v-model="form.email" placeholder="必填，用于接受挂号信息"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="12">
                <el-form-item label="电话" prop="phone" required>
                  <el-input v-model="form.phone" placeholder="必填，用于联络"></el-input>
                </el-form-item>
              </el-col>
              
              <el-col :span="12">
                <el-form-item label="身份证号" prop="IDnum" required>
                  <el-input v-model="form.id"  placeholder="必填，用于确认身份"></el-input>
                </el-form-item>

              </el-col>

            </el-row>
            
            <el-row>
              <el-col span="24">
                <el-form-item label="家庭住址" prop="address" >
                  <el-input v-model="form.address"  placeholder="选填，可用于邮寄"></el-input>
                </el-form-item>
              </el-col>
            </el-row>

            <el-row>
              <el-col span="24">
                <el-form-item label="过敏原信息" prop="allege">
                  <el-input v-model="form.name"  placeholder="可填写以便问诊医生参考"></el-input>
                </el-form-item>
              </el-col>
            </el-row>

            <el-form-item label="遗传病史" prop="history">
                  <el-input v-model="form.name" placeholder="可填写以便问诊医生参考"></el-input>
              </el-form-item>
              
              <el-form-item label="重大病史" prop="history">
                  <el-input v-model="form.name" placeholder="可填写以便问诊医生参考"></el-input>
              </el-form-item>
            
              <!-- Add more form items for other personal information -->
            </el-form>
            <el-button v-show="showForm" type="success" @click="submitForm">提交啊啊</el-button>
            <div v-if="submitSuccess" class="success-message">提交成功</div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'PersonalCenter',
  data() {
    return {
      showForm: false, // Flag to control form visibility
      showFormReg: false,
      showFeedback: false,
      showFormRegTable: false,
      form: {
        name: '',
        email: '',
        phone: '',
        address: '',
        department:'',
        timeslot:'',
        doctor:'',
        description:'',
        requirements:'',
        // Add more properties for other personal information
      },
      departments: [
      { value: '1', label: 'Department 1' },
      { value: '2', label: 'Department 2' },
      { value: '3', label: 'Department 3' },
      // Add more departments as needed
    ],
    timeslots: [
      { value: '1', label: 'Morning' },
      { value: '2', label: 'Afternoon' },
      { value: '3', label: 'Evening' },
      // Add more timeslots as needed
    ],
    doctors: [
      { value: '1', label: 'Doctor 1' },
      { value: '2', label: 'Doctor 2' },
      { value: '3', label: 'Doctor 3' },
      // Add more doctors as needed
    ],
      rules: {
        name: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { type: 'email', message: '邮箱格式不正确', trigger: ['blur', 'change'] },
        ],
        // Define rules for other form items
      },
      submitSuccess:false,
    };
  },
  methods: {
    logout() {
      // Handle logout logic here
    },

    submitForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          // Form is valid, perform submission logic here
          // Example: Submit the form data to the server
          console.log('form submitted')
          // Simulate an asynchronous operation with a timeout
          setTimeout(() => {
            // Reset the form and show success message
            this.form = {
              name: '',
              email: '',
              phone: '',
              address: '',
            };
            this.submitSuccess = true;
          }, 1000);
        }
        else{
          console.log('form incorrect!')
        }
      });
    },

    handleMenuSelect(index) {
      this.selectedSubMenu = index
      if (index === '0-1' ) {
        this.showFormReg = true;
        this.showFormRegTable = false;
        this.showForm = false;
        this.showFeedback = false;
      }
      if (index === '0-2' ) {
        this.showFormRegTable = true;
        this.showFormReg = false;
        this.showForm = false;
        this.showFeedback = false;
      }
      if (index === '1-1') {
        // Show the form when the "个人信息管理" menu item is selected
        this.showForm = true;
        this.showFeedback = false;
        this.showFormReg=false;
        this.showFormRegTable=false;
      }
      if (index === '2-1')
      {
        this.showFeedback = true;
        this.showForm=false;
      }
    },
  },
};
</script>

<style>

.success-message{
  margin-top: 10px;
  color: green;
}
.home-container {
  height: 100vh;
}

.el-header {
  background-color: #1f1e34;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  font-size: 20px;
}

.el-aside {
  background-color: #e4f5ef;
}

.el-main {
  background-color: #e4e4e4;
}
</style>
