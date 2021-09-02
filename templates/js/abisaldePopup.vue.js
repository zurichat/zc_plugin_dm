const Popup = {
    template: `
    <div class="popup-navbar">
        <div class="popup-content clearfix mx-auto popup-notification">
            <b-modal id="modal-1" title="BootsrapVue" class="d-flex flex-column">
                <p class="d-inline-flex p-3 justify-content-between">Turn off notifications for replies</p>
                <p class="d-inline-flex p-3 justify-content-between"><span>Mark unread</span> <span
                        class="left-popupbar">U</span></p>
                <p class="d-inline-flex p-3 justify-content-between active">Remind me about this</p>
                <p class="d-inline-flex p-3 justify-content-between">Copy link</p>
                <p class="d-inline-flex p-3 justify-content-between"><span>Pin to this
                        conversation</span><span class="left-popupbar">P</span>
                </p>
                <p class="d-inline-flex p-3 justify-content-between">Turn question into poll</p>
                <p class="d-inline-flex p-3 justify-content-between"><span>More message shortcuts</span><span><i
                            class="far fa-external-link"></i></span>
                </p>
            </b-modal>
        </div>
        <div class="popup-timer clearfix mx-auto mt-2 py-3">
            <b-modal id="modal-1" title="BootsrapVue" class="d-flex flex-column">
                <p class="d-inline-flex px-4 py-2 justify-content-between">In 20 minutes</p>
                <p class="d-inline-flex px-4 py-2 justify-content-between">In 1 hour</p>
                <p class="d-inline-flex px-4 py-2 justify-content-between">In 3 hours</p>
                <p class="d-inline-flex px-4 py-2 justify-content-between">Tomorrow</p>
                <p class="d-inline-flex px-4 py-2 justify-content-between">Next week
                </p>
                <p class="d-inline-flex px-4 py-2 justify-content-between"><span>Custom...</span><span>M</span>
                </p>
            </b-modal>
        </div>
    </div>
    `,
};
