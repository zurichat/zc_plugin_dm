<template>
  <div>
    <b-sidebar id="sidebar" right no-header z-index="0" bg-variant="white">
      <template #default="{ hide }">
        <div
          class="
            header
            d-flex
            justify-content-between
            align-items-center
            rounded-top
            py-2
            px-3
          "
          style="background: #00B87C"
        >
          <h4 id="sidebar-title" class="sidebar-header-title">Thread</h4>
          <p class="h3">
            <b-icon
              @click="hide"
              icon="x"
              style="color: #fff; cursor: pointer"
            ></b-icon>
          </p>
        </div>
        <div class="body pt-4 px-3">
          <div class="thread d-flex">
            <div class="thread-creator-image">
              <img :src="require('@/assets/woman.png')" alt="" />
            </div>
            <div class="thread-details">
              <b-list-group>
                <b-list-group-item
                  class="border-0 flex-column align-items-center py-0"
                >
                  <div class="d-flex align-items-center">
                    <span class="name">MamaGee</span>
                    <span class="time">6:05pm</span>
                  </div>
                </b-list-group-item>
                <b-list-group-item class="border-0">
                  <p>
                    Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                    Nobis mollitia, at temporibus quam repellendus quis.
                  </p>
                </b-list-group-item>
              </b-list-group>
            </div>
          </div>
          <div class="date-divider">
            <p>{{ replyCount }} replies</p>
            <hr />
          </div>
          <div class="thread-replies">
            <b-list-group>
              <div
                class="thread-reply d-flex mb-2"
                v-for="(replies, i) in thread_replies"
                :key="i"
              >
                <div class="thread-replier-image">
                  <div class="thread-creator-image">
                    <img
                      :src="require(`@/assets/${replies.userAvatar}`)"
                      alt=""
                    />
                  </div>
                </div>
                <b-list-group-item
                  href="#"
                  disabled
                  class="flex-column align-items-start border-0 py-0"
                >
                  <div class="d-flex align-items-center">
                    <span class="name">{{ replies.userName }}</span>
                    <span class="time">{{ replies.timeStamp }}</span>
                  </div>

                  <p>
                    {{ replies.reply }}
                  </p>
                </b-list-group-item>
              </div>
            </b-list-group>
          </div>
          <div class="text-field">
            <b-form-textarea
              id="textarea"
              placeholder="Reply...."
              rows="3"
              no-resize
            ></b-form-textarea>
            <div class="controls d-flex justify-content-between px-1">
              <div class="text-formating d-flex">
                <p><b-icon icon="lightning"></b-icon></p>
                <span class="vr" style="width: 1.5px; opacity: 0.6"></span>
                <p><b-icon icon="type-bold"></b-icon></p>
                <p><b-icon icon="type-italic"></b-icon></p>
                <p><b-icon icon="type-underline"></b-icon></p>
              </div>
              <div class="text-actions d-flex">
                <p><b-icon icon="emoji-smile"></b-icon></p>
                <p><b-icon icon="paperclip" rotate="45"></b-icon></p>
                <p class="text-muted">
                  <b-icon icon="cursor" rotate="45"></b-icon>
                </p>
                <span class="vr"></span>
                <p class="text-muted"><b-icon icon="chevron-down"></b-icon></p>
              </div>
            </div>
          </div>
              <b-form-checkbox
            id="checkbox"
            name="checkbox"
            size="sm"
            class="pt-3 px-0"
          >
            <label for="checkbox" class="pl-3 check-label">Also send as direct message</label>
          </b-form-checkbox>
        </div>
      </template>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  name: "ThreadReply",
  data() {
    return {
      thread_replies: [
        {
          userName: "MamaGee",
          timeStamp: "6:06pm",
          reply:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. quia id doloribus inventore blanditiis?",
          userAvatar: "woman.png",
        },
        {
          userName: "PapaGee",
          timeStamp: "6:07pm",
          reply:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. quia id doloribus inventore blanditiis?",
          userAvatar: "man.png",
        },
      ],
      name: "",
    };
  },
  methods: {},
  computed: {
    replyCount() {
      return this.thread_replies.length;
    },
    state() {
      return this.name.length >= 4;
    },
    invalidFeedback() {
      if (this.name.length > 0) {
        return "Enter at least 4 characters.";
      }
      return "Please enter something.";
    },
  },
};
</script>

<style scoped>
* {
  text-align: left !important;
}
.sidebar-header-title {
  color: #fff;
}
.date-divider {
  display: flex;
  align-items: center;
  width: 100%;
}
.date-divider p {
  flex: 0.5;
}
.date-divider p,
.thread-details span.time,
.thread-details p,
.thread-replies span.time,
.thread-replies p {
  font-size: 0.8rem;
  color: rgba(153, 153, 153, 1);
  font-weight: 400;
  text-align: left !important;
}
.thread-details p,
.thread-replies p {
  color: rgba(36, 36, 36, 1);
  line-height: 18px;
  letter-spacing: 1px;
}
.thread-details span.name,
.thread-replies span.name {
  font-weight: 600;
  color: rgba(36, 36, 36, 1);
  margin-right: 20px;
}
.date-divider hr {
  height: 1px;
  border: none;
  background: rgba(196, 196, 196, 1);
  width: auto;
  flex: 2;
}
.text-field {
  min-height: calc(1.5em + 0.75rem + 2px);
  width: 100%;
  position: relative;
}
.text-field textarea.form-control {
  padding-top: 15px;
}
.text-field textarea.form-control::placeholder {
  font-weight: 400;
  color: rgba(190, 190, 190, 1);
}
.text-field textarea.form-control:focus {
  border-color: rgb(15, 17, 20);
  box-shadow: 0 0 0 0.25rem rgba(15, 17, 20, 25%);
}
.controls {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 30px;
}
.text-formating p:not(:last-child),
.text-actions p:not(:last-child) {
  margin-right: 15px !important;
  cursor: pointer;
}
.vr {
  margin: 0 5px 0 -5px;
  height: 25px;
}
label.check-label{
    padding-left: 10px;
}
</style>