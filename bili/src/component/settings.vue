<template>
  <div style="width: 30rem; margin: 3rem auto 3rem auto;">
    <p style="font-size: 3rem">Acount Manager</p>
    <a-card title :bordered="false" class="registerCard">
      <form action>
        <a-form :form="form" @submit="handleSubmit">
          <!-- username -->
          <a-form-item v-bind="formItemLayout">
            <span slot="label">
              Username&nbsp;
              <!-- <a-tooltip title="What do you want others to call you?">
                <a-icon type="question-circle-o" />
              </a-tooltip>-->
            </span>
            <a-input
              v-decorator="[
          'username',
          {
            rules: [{ required: true, message: 'Please input your username!', whitespace: true }],
          },
        ]"
            />
          </a-form-item>
          <!-- E-mail -->
          <a-form-item v-bind="formItemLayout" label="E-mail">
            <a-input
              v-decorator="[
          'email',
          {
            rules: [
              {
                type: 'email',
                message: 'The input is not valid E-mail!',
              },
              {
                required: true,
                message: 'Please input your E-mail!',
              },
            ],
          },
        ]"
            />
          </a-form-item>
          <!-- Password -->
          <a-form-item v-bind="formItemLayout" label="Password">
            <a-input
              v-decorator="[
          'password',
          {
            rules: [
              {
                required: true,
                message: 'Please input your password!',
              },
              {
                validator: validateToNextPassword,
              },
            ],
          },
        ]"
              type="password"
            />
          </a-form-item>
          <!-- comfirm password -->
          <a-form-item v-bind="formItemLayout" label="Confirm Password">
            <a-input
              v-decorator="[
          'confirm',
          {
            rules: [
              {
                required: true,
                message: 'Please confirm your password!',
              },
              {
                validator: compareToFirstPassword,
              },
            ],
          },
        ]"
              type="password"
              @blur="handleConfirmBlur"
            />
          </a-form-item>
          <!-- phone number -->
          <a-form-item v-bind="formItemLayout" label="Phone Number">
            <a-input
              v-decorator="[
          'phone',
          {
            rules: [{ required: true, message: 'Please input your phone number!' }],
          },
        ]"
              style="width: 100%"
            >
              <a-select
                slot="addonBefore"
                v-decorator="['prefix', { initialValue: '86' }]"
                style="width: 70px"
              >
                <a-select-option value="86">+86</a-select-option>
                <a-select-option value="87">+87</a-select-option>
              </a-select>
            </a-input>
          </a-form-item>
          <!-- captcha -->
          <a-form-item
            v-bind="formItemLayout"
            label="Captcha"
            extra="We must make sure that your are a human."
          >
            <a-row :gutter="8">
              <a-col :span="12">
                <a-input
                  v-decorator="[
              'captcha',
              { rules: [{ required: true, message: 'Please input the captcha you got!' }] },
            ]"
                />
              </a-col>
              <a-col :span="12">
                <a-button>Get captcha</a-button>
              </a-col>
            </a-row>
          </a-form-item>
          <!-- agree agreement -->
          <a-form-item v-bind="tailFormItemLayout">
            <a-checkbox v-decorator="['agreement', { valuePropName: 'checked' }]">
              have read the
              <a href>JK - agreement</a>
            </a-checkbox>
          </a-form-item>
          <!-- register button -->
          <a-form-item v-bind="tailFormItemLayout" style="float: right; margin-right: 1rem;">
            <a-button type="primary" html-type="submit" @click="showConfirm">Comfirm</a-button>
          </a-form-item>
        </a-form>
      </form>
    </a-card>
  </div>
</template>




<script>
export default {
  data() {
    return {
      confirmDirty: false,
      formItemLayout: {
        labelCol: {
          xs: { span: 24 },
          sm: { span: 8 }
        },
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 16 }
        }
      },
      tailFormItemLayout: {
        wrapperCol: {
          xs: {
            span: 24,
            offset: 0
          },
          sm: {
            span: 16,
            offset: 8
          }
        }
      }
    };
  },
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "register" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFieldsAndScroll((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
      });
    },
    handleConfirmBlur(e) {
      const value = e.target.value;
      this.confirmDirty = this.confirmDirty || !!value;
    },
    compareToFirstPassword(rule, value, callback) {
      const form = this.form;
      if (value && value !== form.getFieldValue("password")) {
        callback("Two passwords that you enter is inconsistent!");
      } else {
        callback();
      }
    },
    validateToNextPassword(rule, value, callback) {
      const form = this.form;
      if (value && this.confirmDirty) {
        form.validateFields(["confirm"], { force: true });
      }
      callback();
    },
    showConfirm() {
      this.$confirm({
        title: "Do you want to delete these items?",
        content:
          "When clicked the OK button, this dialog will be closed after 1 second",
        onOk() {
          return new Promise((resolve, reject) => {
            setTimeout(Math.random() > 0.5 ? resolve : reject, 1000);
          }).catch(() => console.log("Oops errors!"));
        },
        onCancel() {}
      });
    }
  }
};
</script>