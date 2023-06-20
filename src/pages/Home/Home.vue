
<template>
  <section class="home" style="background-color: #f3f3f3;">
    <!--首页头部-->
    <HeaderTop title="首页">
      <span class="header_login" slot="right">
        <span class="header_login_text" @click="goTo('/login')">登录 | 注册</span>
      </span>
    </HeaderTop>
    <!--首页导航-->
    <nav class="home_nav" style="background-color: #d8f3ee;" @click="goTo('/chat')">
      <div class="nav_list">
        <a href="javascript:" class="link_to_question">
          <div class="nav_container">
            <i class="iconfont icon-wenzhen" style="color: #28B8A1;"></i>
          </div>
          <span>问诊</span>
        </a>
        <a href="javascript:" class="link_to_question" @click="goTo('/register')">
          <div class="nav_container">
            <i class="iconfont icon-jiancha" style="color: #28B8A1;"></i>
          </div>
          <span>挂号</span>
        </a>
        <a href="javascript:" class="link_to_question" @click="goTo('/bill')">
          <div class="nav_container">
            <i class="iconfont icon-yishengzhenduan" style="color: #28B8A1;"></i>
          </div>
          <span>收据</span>
        </a>
        <a href="javascript:" class="link_to_question" @click="goTo('/CaseRecord')">
          <div class="nav_container">
            <i class="iconfont icon-hulizhenduan" style="color: #28B8A1;"></i>
          </div>
          <span>病历</span>
        </a>
      </div>
      <div class="nav_btn">
        <mt-button type="primary" size="normal" class="mt_btn" style="background-color: #28B8A1;" @click="goTo('/chat')">查疾病</mt-button>
        <mt-button type="primary" size="normal" class="mt_btn" style="background-color: #28B8A1;" @click="goTo('\leftuptest')">就诊反馈</mt-button>
      </div>
    </nav>
    <!--首页内容-->
    <section class="home_content" style="background-color: #f3f3f3;">
      <div class="title" style="background-color: #fff;">
        <span class="left" style="font-size: 18px;">护理小常识</span>
        <span class="right" style="font-size: 12px;">更多</span>
      </div>
      <NursingKnowledgeList/>
    </section>
  </section>
</template>

<script>
import HeaderTop from '../../components/HeaderTop/HeaderTop'
import NursingKnowledgeList from '../../components/NursingKnowledgeList/NursingKnowledgeList'
export default {
  components: {
    HeaderTop,
    NursingKnowledgeList
  },
  methods:{
    goTo (path) {
      this.$router.push(path)
    }
  }
}
</script>

<style lang="stylus" ref="stylesheet/stylus">
.home //问诊
  width 100%
  .home_nav
    margin-top 45px
    height 260px
    .nav_list
      display flex
      justify-content center
      align-items flex-start
      flex-wrap wrap
      .link_to_question
        width: 25%
        margin-top: 15px
        text-align: center
        font-size: 13px
        margin-left:

 -5px
        .nav_container
          display block
          width 92%
          text-align center
          padding-bottom 10px
          font-size 0
          .iconfont
            font-size 36px
            color #28B8A1
          span
            font-size 20px !important
    .nav_btn
      margin-top 36px
      .mt_btn
        width 80%
        background #28B8A1
        display block
        margin 30px auto
  .home_content
    background #f3f3f3
    height 500px
    .title
      padding 10px 20px
      background #fff
      .left
        font-size 18px
      .right
        float right
        font-size 12px
</style>
