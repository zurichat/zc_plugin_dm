<template>
  <div class="hello">

    <div >
      <div class="attachfilepop border rounded" >
         <p class="mt-4 px-4 small">Your recent files</p> 
        <div class="d-flex px-3 py-2 files">
          <b-icon icon="folder-fill" scale="2" class="py-3"></b-icon>
          <div class="d-block px-4">
            <p class="my-0">HNG Task 1.jpg</p>
            <p class="my-0 small">7 Sept</p>
          </div>
        </div>
        <div class="d-flex px-3 py-2 files">
          <b-icon icon="folder-fill" scale="2" class="py-3"></b-icon>
          <div class="d-block px-4">
            <p class="my-0">HNG Task 2.jpg</p>
            <p class="my-0 small">7 Sept</p>
          </div>
        </div>
        <div class="d-flex px-3 py-2 files">
          <b-icon icon="folder-fill" scale="2" class="py-3"></b-icon>
          <div class="d-block px-4">
            <p class="my-0">HNG Task 3.jpg</p>
            <p class="my-0 small">7 Sept</p>
          </div>
        </div>
        <p class="mb-0 px-4 mb-3 mt-2 small">View all your files</p>
        <div class="addfile  border-top ">
          <p class="mb-0 mt-3 px-4 small">Add a file from ....</p>
          <div class="py-2 files px-4">
            <span
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                viewBox="0 0 18 18"
                fill="none"
              >
                <g clip-path="url(#clip0)">
                  <path
                    d="M12.0003 12.375H17.9999L12.0003 1.125H5.99951L12.0003 12.375Z"
                    fill="#616061"
                  />
                  <path
                    d="M5.57111 12.375L3.00049 16.875H15.1876L18.0001 12.375H5.57111Z"
                    fill="#616061"
                  />
                  <path
                    d="M5.99963 1.125L0 11.6246L3.00038 16.875L8.8965 6.5565L5.99963 1.125Z"
                    fill="#616061"
                  />
                </g>
                <defs>
                  <clipPath id="clip0">
                    <rect width="18" height="18" fill="white" />
                  </clipPath>
                </defs>
              </svg>
            </span>

            <label class="custom-file-upload">
              <input type="file" />
              Upload from your Google drive
            </label>
          </div>

          <div class="py-2 mb-4 files px-4">
            <span><b-icon icon="laptop"></b-icon> </span
            ><label class="custom-file-upload">
              <input type="file" />
              Upload from your computer
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return { 
     toggle: true,
      selectedFile: null,
    
    };
  },
  components: {},
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    // toggle(){
    //     this.display=!this.display
    // }
  },
};
</script>


</template>

<script>
export default {};
</script>

<style scoped>
input[type="file"] {
  display: none;
}

.custom-file-upload {
  display: inline-block;
  padding: 6px 12px;
  cursor: pointer;
}

.attachfilepop {
  width: 340px;
}

.files:hover{
    color:white;
background: rgba(18, 100, 163, 1);
cursor: pointer;
}

.attachfilepop{
    transition: 0.5s ease-out;
    position:absolute;
    z-index: 3;
    background: white;
    bottom:70px;
    right:100px;
}
</style>
