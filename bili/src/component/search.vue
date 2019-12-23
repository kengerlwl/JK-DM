<template>
  <div>

    <!-- back to top -->
    <div>
      <a-back-top />
      <strong style="color: rgba(64, 64, 64, 0.6)"></strong>
    </div>
    <span style="font-size: 4rem; nargin: 3rem auto 3rem auto;">Search result</span>
    <div style="max-width: 70rem; margin: 1rem auto 1rem auto;">
      <a-list itemLayout="vertical" size="large" :pagination="pagination" :dataSource="animeList">
        <!-- <div slot="footer">
            <b>ant design vue</b> footer part
        </div>-->
        <a-card
          slot="renderItem"
          slot-scope="item, index"
          key="item.title"
          hoverable
          @click="toPlay(item[0], item[1])"
        >
          <a-list-item-meta :description="item[0]">
            <span slot="title" style="font-size: 3rem;">{{item[1]}}</span>
            <img slot="avatar" width="130" alt="logo" :src="item[2]" />
          </a-list-item-meta>
        </a-card>
      </a-list>
    </div>
  </div>
</template>
<script>

export default {
  data() {
    return {
      pagination: {
        onChange: page => {
          console.log(page);
        },
        pageSize: 10
      },
    };
  },
  methods: {
    click:function(){animeList
        console.log(animeList)
    },
    callback(val) {
      console.log(val);
    },
    toPlay(playTitle, playName) {
      this.$notification.open({
        message: playName,
        description: playTitle,
        onClick: () => {
          console.log("Notification Clicked!");
        },
        duration: 2
      });
      this.$emit("playList", playTitle);
    }
    // toPlay() {
    //   this.$emit("playList");
    // }
  },
  props: ['animeList']
};
</script>