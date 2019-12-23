<template>
  <div>
    <span style="font-size: 5rem; margin-top: 2rem;">{{Title}}</span>
    <div>
      <div style="margin-top: 2rem;">
        <!-- <a-button type="primary" @click="resolve">test</a-button> -->

        <a-button type="primary" @click="showDrawer()">Select the episode</a-button>
        <a-drawer
          title="Play List"
          placement="right"
          :closable="false"
          @close="onClose"
          :visible="visible"
          width="270"
        >
          <a-list :grid="{ gutter: 1, column: 1 }" :dataSource="playList">
            <a-list-item
              slot="renderItem"
              slot-scope="item, index"
              
            >
              <a-card>
                <span slot="title">
                  <a-button :type="see[index]" @click="playMv( item[1],item[0],index)">
                    <a-icon type="play-circle" />
                    {{item[0]}}
                  </a-button>
                </span>
              </a-card>
            </a-list-item>
          </a-list>
        </a-drawer>
      </div>
    </div>
    <div style="padding: 1rem; margin: 3rem auto 1rem auto; max-width: 60rem;">
      <div style="padding: 1rem; margin: 0rem auto 1rem auto; max-width: 60rem; height: 50rem;">
        <iframe
          :key="menuKey"
          name="child"
          id="child"
          src="./../../static/index.html"
          width="100%"
          height="100%"
          frameborder="0"
          scrolling="no"
          style="position:related;top: 2.8px;left: 0px;"
        ></iframe>
      </div>
    </div>
    <!-- <div style="margin: 0 auto 10rem auto; font-size: 1rem;">
      <a :href="mvUrl">
        <a-button type="primary">
          <a-icon type="download" />Click me to download the video.
        </a-button>
      </a>
    </div> -->
  </div>
</template>
<script>
import $ from "jquery";
import axios from "axios";

export default {
  created: function() {
    var i ;
    for (i = 0; i < 100; i++) { 
      this.see.push("primary")
    }
    console.log(this.see)
    console.log("created");
    this.getData();
    for (let i = 0; i < 100; i++) {
      AfterClick.push("primary");
    }
  },
  data() {
    return {
      see:[],
      menuKey: 1,
      playList: {},
      visible: false,
      Title: "第01集",
      mvUrl: "",
    };
  },
  props: {
    playTitle: String,
    required: true
  },
  methods: {
    resolve() {
      console.log("resolve");
      this.menuKey = this.menuKey + 1;
    },

    showDrawer() {
      this.visible = true;
      this.$message.success("Success to open the play list.", 1);
    },
    onClose() {
      this.visible = false;
      this.$message.info("Close the play list.", 1);
    },
    playMv(url, title, event) {
      //  var el = event.currentTarget;
      //   console.log(el)
      //  el.setAttribute("type",""); 
      //  console.log(el.type)
      // $.cookie('playURL', null);
      this.see[event]= "";
      console.log(url);
      $.get("http://127.0.0.1:8000/save?url=" + url, function(data) {
        console.log(data);
      });
      this.mvUrl = url;
      console.log(this.mvUrl);
      this.Title = title;
      this.$message.info("Select " + this.Title + ".", 1);
      this.resolve();
      // $.cookie('playURL', this.mvUrl);
    },
    getData: function() {
      // this.dmurl = this.$route.query.url;

      console.log("getdata"),
        // (this.playList = );

        axios
          .get("http://127.0.0.1:8000/viewDm?keyW=" + this.playTitle)
          .then(response => {
            //如果在手机上访问需要更改域名
            console.log(response.data.data);
            this.playList = response.data.data;
            console.log(this.playList);
          });
      this.mvUrl = this.playList[0][1];
      console.log(this.playList);
    }
  },
  mounted() {}
};
</script>
<style>
.Comment {
  margin: 2rem auto 4rem auto;
  max-width: 40rem;
}
</style>