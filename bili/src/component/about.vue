<template>
  <div>
    <p class="aboutTitle">JK - Alfred</p>
    <div>
      <p style="font-size: 1.5rem">We are CSU CS's students.</p>
      <a-avatar :size="64" icon="user" />
      <a-avatar :size="64">LWL</a-avatar>
      <a-avatar :size="64">REM</a-avatar>
      <a-avatar :size="64">LGX</a-avatar>
      <a-avatar :size="64">LUM</a-avatar>
      <div class="member">
        <a-table :columns="columns" :dataSource="data" bordered>
          <template slot="name" slot-scope="text">
            <a href="javascript:;">{{text}}</a>
          </template>
          <template slot="nickname" slot-scope="text">
            <a href="javascript:;">{{text}}</a>
          </template>
          <template slot="email" slot-scope="text">
            <a href="javascript:;">{{text}}</a>
          </template>
          <template slot="area" slot-scope="text">
            <a href="javascript:;">{{text}}</a>
          </template>
          <template slot="title" class="blueText"></template>
          <template slot="footer"></template>
        </a-table>
      </div>
    </div>
    <p style="font-size: 1.5rem">Our Development Environment</p>
    <div style="text-align: start; padding: 4rem; font-size: 1.3rem">
      <ul>
        <li>Arch Linux 5.3.11</li>
        <li>Vue 2.9.6</li>
        <li>npm 6.12.1</li>
        <li>Python 3.8.0</li>
        <li>Scrapy</li>
        <li>Ant Design 1.4.8</li>
      </ul>
    </div>
  </div>
</template>
<script>
const columns = [
  {
    title: "Name",
    dataIndex: "name",
    scopedSlots: { customRender: "name" }
  },
  {
    title: "Nickname",
    dataIndex: "nickname",
    scopedSlots: { customRender: "nickname" }
  },
  {
    title: "Email",
    className: "email",
    dataIndex: "email",
    scopedSlots: { customRender: "email" }
  },
  {
    title: "Area of ​​Project",
    dataIndex: "area",
    scopedSlots: { customRender: "area" }
  }
];

const data = [
  {
    key: "1",
    name: "LWL",
    nickname: "LWL",
    email: "2892211452@qq.com",
    area: "Python, Django, Scrapy"
  },
  {
    key: "2",
    name: "Huang Po Hsun",
    nickname: "REM",
    email: "fh831.cp9gw@gmail.com",
    area: "Vue, CSS, Js, Ant design"
  },
  {
    key: "3",
    name: "LGX",
    nickname: "灼热之翼",
    email: "1349621303@qq.com",
    area: "Vue, Ant design, document"
  },
  {
    key: "4",
    name: "Lumusen",
    nickname: "Lumusen",
    email: "Lumusen8209180535@gmail.com",
    area: "Vue, Ant design, document"
  }
];
export default {
  data() {
    return {
      data,
      columns
    };
  }
};
</script>
<style>
.aboutTitle {
  text-align: center;
  /* color: brown; */
  font-size: 3rem;
  margin-top: 2rem;
}

.blueText {
  color: blue;
}

.member {
  padding: 4rem;
}
</style>
