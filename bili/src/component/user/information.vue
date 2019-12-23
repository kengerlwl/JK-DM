<template>
  <div style="padding: 0 0 3rem 0;">
    <span style="font-size: 4rem; nargin: 3rem auto 3rem auto;">Information</span>
    <a-card hoverable style="max-width: 30rem; margin: 4rem auto 4rem auto;">
      <img alt="user" src="../../../static/img/user.jpg" slot="cover" />
      <a-card-meta title="UserName">
        <template slot="description">
          <p>Birth : 2019 / 12 / 1</p>
          <p>Years olds : 18</p>
          <p>hobby : watching anime video</p>
          <br />
        </template>
      </a-card-meta>
    </a-card>
  </div>
</template>
<script>
const listData = [];
for (let i = 0; i < 11; i++) {
  listData.push({
    title: `Anime ${i}`,
    avatar:
      "https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png",
    description:
      "Ant Design, a design language for background applications, is refined by Ant UED Team."
  });
  
}

export default {
  data() {
    return {
      listData,
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 5
      }
    };
  },
  methods: {
    callback(val) {
      console.log(val);
    },
    toPlay() {
      this.$emit("playList");
    }
  }
};
</script>