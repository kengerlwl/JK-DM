<template>
  <div id="appLogin">
    <div class="title">
      <span>JK - Alfred</span>
    </div>
    <a-card title="Login" :bordered="false" class="loginCard">
      <form action>
        <a-form
          id="components-form-demo-normal-login"
          :form="form"
          class="login-form"
          @submit="handleSubmit"
        >
          <!-- username -->
          <a-form-item>
            <a-input
              v-decorator="[
          'userName',
          { rules: [{ required: true, message: 'Please input your username!' }] },
        ]"
              placeholder="Username"
            >
              <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
            </a-input>
          </a-form-item>

          <!-- passsword -->
          <a-form-item>
            <a-input
              v-decorator="[
          'password',
          { rules: [{ required: true, message: 'Please input your Password!' }] },
        ]"
              type="password"
              placeholder="Password"
            >
              <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
            </a-input>
          </a-form-item>

          <!-- remember me checkbox -->
          <a-form-item>
            <a-checkbox
              v-decorator="[
          'remember',
          {
            valuePropName: 'checked',
            initialValue: true,
          },
        ]"
            >Remember me</a-checkbox>
            <a class="login-form-forgot" href>Forgot password</a>
            <a-button type="primary" html-type="submit" class="login-form-button">
              <router-link to="/main">Sign in</router-link>
            </a-button>Or
            <router-link to="/register">register now!</router-link>
          </a-form-item>
        </a-form>
      </form>
    </a-card>
  </div>
</template>
<style>
#appLogin {
  background: url("../../static/img/1.jpg") no-repeat fixed center center/cover;
  padding: 5rem;
  height: 100%;
}

.loginCard {
  width: 30rem;
  margin: auto;
  opacity: 80%;
}

.title {
  font-size: 5rem;
  color: aliceblue;
  text-align: center;
  opacity: 80%;
}

#components-form-demo-normal-login .login-form {
  max-width: 300px;
}
#components-form-demo-normal-login .login-form-forgot {
  float: right;
}
#components-form-demo-normal-login .login-form-button {
  width: 100%;
}
</style>
<script>

export default {
  name:'login',
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
      });
    }
  }
};
</script>
