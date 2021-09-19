import { Vue } from "vue-property-decorator";
import { Emoji } from "@/models/Emoji";
export default class EmojiList extends Vue {
    data: any;
    emojisByRow: number;
    emojiWithBorder: boolean;
    emojiSize: number;
    filter: string;
    continuousList: boolean;
    category: string;
    hasSearch: boolean;
    searchByAlias(term: string, emoji: Emoji): boolean;
    calcScrollTop(): 88 | 44;
    get gridDynamic(): {
        gridTemplateColumns: string;
    };
    get dataFiltered(): any;
    get dataFilteredByCategory(): any;
    get categories(): any;
    get containerEmoji(): any;
    onSelect(emoji: Emoji): Emoji;
    onDataChanged(): void;
    onCategoryChanged(newValue: any): void;
}
//# sourceMappingURL=EmojiList.vue?rollup-plugin-vue=script.d.ts.map