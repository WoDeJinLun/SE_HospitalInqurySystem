<template>
  <div id="PersonalCenter">
    <el-container class="home-container">
      <el-header>
        <div>
          <span>个人中心</span>
        </div>
        <el-button type="info" @click="goTo('/')">
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
                <i class="el-icon-phone"></i>
                <span>挂号</span>
              </template>
              <el-menu-item index="0-1">我要挂号</el-menu-item>
              <el-menu-item index="0-2">挂号历史</el-menu-item>
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
                  <div class="block">
                    <el-form-item label="挂号科室" prop="挂号科室">
                    <el-cascader
                      v-model="value"
                      :options="departments"
                      @change="ResetTimeDoctor()">
                    </el-cascader>
                    </el-form-item>
                  </div>     
                </el-col>  
                </el-row>      
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="挂号时段" prop="挂号时段">
                      <el-select
                        v-model="form.timeslot"
                        placeholder="请选择"
                        @change="ResetDoctor()"
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
                    <el-form-item label="医生" prop="医生">
                      <el-select
                        v-model="form.doctor"
                        placeholder="请选择"
                      >
                        <el-option
                          v-for="doctor in random_doctors"
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
                    <el-form-item label="病情描述" prop="description">
                      <el-input
                        type="textarea"
                        :rows="4"
                        placeholder="请输入病情描述"
                        v-model="form.description"
                      ></el-input>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item label="特殊要求" prop="requirements">
                      <el-input
                        type="textarea"
                        :rows="4"
                        placeholder="（选填）请输入问诊的特殊要求"
                        v-model="form.requirements"
                      ></el-input>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="24">
                    <el-form-item>
                      <el-button type="primary" @click="submitFor">提交</el-button>
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
                        @click="cancelRegistration(scope.row)"
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
                  <el-input v-model="form.allege"  placeholder="可填写以便问诊医生参考"></el-input>
                </el-form-item>
              </el-col>
            </el-row>

            <el-form-item label="遗传病史" prop="historya">
                  <el-input v-model="form.historya" placeholder="可填写以便问诊医生参考"></el-input>
              </el-form-item>
              
              <el-form-item label="重大病史" prop="historyb">
                  <el-input v-model="form.historyb" placeholder="可填写以便问诊医生参考"></el-input>
              </el-form-item>
            
              <!-- Add more form items for other personal information -->
            </el-form>
            <el-button v-show="showForm" type="success" >提交</el-button>
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
      registrationHistory:[],
      RegistID:0,
      showForm: false, // Flag to control form visibility
      showFormReg: false,
      showFeedback: false,
      showFormRegTable: false,
      selectedSubMenu: '',
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
      departments: [{
            value: 'duoxueke',
            label: '多学科联合诊治',
            children: [{
              value: 'duoxuekejiefanglu',
              label: '多学科联合诊治-解放路',
            }]
          }, {
            value: 'quanke',
            label: '全科医学科',
            children: [{
              value: 'quankejiefanglu',
              label: '全科医学科门诊-解放路',
            }]
          },
          {
            value: 'neike',
            label: '内科',
            children: [{
              value: 'neifenmi',
              label: '内分泌科',
            }, {
              value: 'xinxueguan',
              label: '心血管科',
              
            }, {
              value: 'shenjing',
              label: '神经内科',
            }, {
              value: 'xueye',
              label: '血液内科',
              
            }, {
              value: 'huxi',
              label: '呼吸内科',
              
            }, {
              value: 'xiaohua',
              label: '消化内科',
            }, {
              value: 'yichuan',
              label: '医学遗传科',
            }, {
              value: 'fengshi',
              label: '风湿免疫科',
            }, {
              value: 'guomin',
              label: '过敏科（变态反应科）',
            }, {
              value: 'shenzang',
              label: '肾脏内科',
            }, {
              value: 'jingshen',
              label: '精神科',
            }, {
              value: 'ganran',
              label: '感染性疾病科',
            }]
          }, {
            value: 'waike',
            label: '外科',
            children: [{
              value: 'ruxian',
              label: '乳腺外科'
            }, {
              value: 'zhengxing',
              label: '整形科'
            }, {
              value: 'gandanyi',
              label: '肝胆胰外科'
            }, {
              value: 'xueguan',
              label: '血管外科'
            }, {
              value: 'dachang',
              label: '大肠外科'
            }, {
              value: 'puwai',
              label: '普外科'
            }, {
              value: 'jiazhuangxian',
              label: '甲状腺外科'
            }, {
              value: 'weichang',
              label: '胃肠外科'
            }, {
              value: 'gu',
              label: '骨科'
            }, {
              value: 'miniao',
              label: '泌尿外科'
            }, {
              value: 'shenjingwai',
              label: '神经外科'
            }, {
              value: 'xiongwai',
              label: '胸外科'
            }]
          }, {
            value: 'fuchanke',
            label: '妇产科'
          }, {
            value: 'erke',
            label: '儿科'
          }],
    timeslots: [
      { value: '1', label: '8:00-8:30' },
      { value: '2', label: '8:30-9:00' },
      { value: '3', label: '9:00-9:30' },
      { value: '4', label: '9:30-10:00' },
      { value: '5', label: '10:00-10:30' },
      { value: '6', label: '10:30-11:00' },
      { value: '7', label: '11:00-11:30' },
      { value: '8', label: '14:00-14:30' },
      { value: '9', label: '14:30-15:00' },
      { value: '10', label: '15:00-15:30' },
      { value: '11', label: '15:30-16:00' },
      { value: '12', label: '16:00-16:30' },
      { value: '13', label: '16:30-17:00' },  
      // Add more timeslots as needed
    ],
    random_doctors:[

    ],
    doctors: [
      { value: 1, label: '医生 1' },
      { value: 2, label: '医生 2' },
      { value: 3, label: '医生 3' },
      { value: 4, label: '医生 4' },
      { value: 5, label: '医生 5' },
      { value: 6, label: '医生 6' },
      { value: 7, label: '医生 7' },
      { value: 8, label: '医生 8' },
      { value: 9, label: '医生 9' },
      { value: 10, label: '医生 10' },
      { value: 11, label: '医生 11' },
      { value: 12, label: '医生 12' },
      { value: 13, label: '医生 13' },
      { value: 14, label: '医生 14' },
      { value: 15, label: '医生 15' },
      { value: 16, label: '医生 16' },
      { value: 17, label: '医生 17' },
      { value: 18, label: '医生 18' },
      { value: 19, label: '医生 19' },
      { value: 20, label: '医生 20' },
      { value: 21, label: '医生 21' },
      { value: 22, label: '医生 22' },
      { value: 23, label: '医生 23' },
      { value: 24, label: '医生 24' },
      { value: 25, label: '医生 25' },
      { value: 26, label: '医生 26' },
      { value: 27, label: '医生 27' },
      { value: 28, label: '医生 28' },
      { value: 29, label: '医生 29' },
      { value: 30, label: '医生 30' },
      { value: 31, label: '医生 31' },
      { value: 32, label: '医生 32' },
      { value: 33, label: '医生 33' },
      { value: 34, label: '医生 34' },
      { value: 35, label: '医生 35' },
      { value: 36, label: '医生 36' },
      { value: 37, label: '医生 37' },
      { value: 38, label: '医生 38' },
      { value: 39, label: '医生 39' },
      { value: 40, label: '医生 40' },
      { value: 41, label: '医生 41' },
      { value: 42, label: '医生 42' },
      { value: 43, label: '医生 43' },
      { value: 44, label: '医生 44' },
      { value: 45, label: '医生 45' },
      { value: 46, label: '医生 46' },
      { value: 47, label: '医生 47' },
      { value: 48, label: '医生 48' },
      { value: 49, label: '医生 49' },
      { value: 50, label: '医生 50' },
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
    goTo (path) {
      this.$router.push(path)
    },
    getDepartmentLabel(value) {
      const department = this.departments.find((dept) => dept.value === value);
      return department ? department.label : '';
    },
    getTimeslotLabel(value) {
      const timeslot = this.timeslots.find((slot) => slot.value === value);
      return timeslot ? timeslot.label : '';
    },
    getDoctorLabel(value) {
      const doctor = this.random_doctors.find((doc) => doc.value === value);
      return doctor ? doctor.label : '';
    },
    submitFor() {
      const departmentLabel = this.getDepartmentLabel(this.value[0]);
      const timeslotLabel = this.getTimeslotLabel(this.form.timeslot);
      const doctorLabel = this.getDoctorLabel(this.form.doctor);

      const registration = {
        registrationId: 2, // Generate a unique registration ID
        department: departmentLabel,
        timeslot: timeslotLabel,
        doctor: doctorLabel,
        status: 'Pending',
      };

      this.$message.success('保存成功');
      this.registrationHistory.push(registration);
    },
    genRegID()
    {
        this.RegistID += 1;
        return this.RegistID;
    },
    ResetTimeDoctor(){
      this.form.timeslot=null;
      this.form.doctor=null;
      this.random_doctors=[]
    },
    ResetDoctor(){
      this.form.doctor=null;
      this.random_doctors = this.getRandomDoctors(5).sort();
    },
    getRandomDoctors(count) {
    const shuffled = this.doctors.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count).sort();
    },
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
    cancelRegistration(row) {
      const index = this.registrationHistory.indexOf(row);
      if (index > -1) {
        this.registrationHistory.splice(index, 1);
        this.$message.success('Registration canceled');
      }
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
