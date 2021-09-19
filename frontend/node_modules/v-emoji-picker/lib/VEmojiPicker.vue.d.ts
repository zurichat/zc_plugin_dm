import { Vue } from "vue-property-decorator";
import { IEmoji } from "./models/Emoji";
import { ICategory } from "./models/Category";
import { MapEmojis } from "./models/MapEmojis";
export default class VEmojiPicker extends Vue {
    customEmojis: IEmoji[];
    customCategories: ICategory[];
    limitFrequently: number;
    emojisByRow: number;
    continuousList: boolean;
    emojiSize: number;
    emojiWithBorder: boolean;
    showSearch: boolean;
    showCategories: boolean;
    dark: boolean;
    initialCategory: string;
    exceptCategories: ICategory[];
    exceptEmojis: IEmoji[];
    i18n: Object;
    mapEmojis: MapEmojis;
    currentCategory: string;
    filterEmoji: string;
    created(): void;
    beforeDestroy(): void;
    onSearch(term: string): Promise<void>;
    changeCategory(category: ICategory): Promise<void>;
    updateFrequently(emoji: IEmoji): Promise<void>;
    mapperEmojisCategory(emojis: IEmoji[]): Promise<void>;
    restoreFrequentlyEmojis(): Promise<void>;
    saveFrequentlyEmojis(emojis: IEmoji[]): Promise<void>;
    get categoriesFiltered(): ICategory[];
    onSelectEmoji(emoji: IEmoji): Promise<IEmoji>;
    onChangeCategory(category: ICategory): Promise<ICategory>;
    onChangeCustomEmojis(newEmojis: IEmoji[]): void;
}
//# sourceMappingURL=VEmojiPicker.vue?rollup-plugin-vue=script.d.ts.map