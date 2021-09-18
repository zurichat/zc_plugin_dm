import { Vue } from "vue-property-decorator";
import { IEmoji } from "@/models/Emoji";
export default class EmojiItem extends Vue {
    emoji: IEmoji;
    size: number;
    withBorder: boolean;
    get styleSize(): {
        fontSize: string;
        lineHeight: string;
        height: string;
        width: string;
    };
}
//# sourceMappingURL=EmojiItem.vue?rollup-plugin-vue=script.d.ts.map