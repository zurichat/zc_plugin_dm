import { Vue } from "vue-property-decorator";
import { Category } from "@/models/Category";
export default class Categories extends Vue {
    categories: Category[];
    current: string;
    onSelect(category: Category): Category;
}
//# sourceMappingURL=Categories.vue?rollup-plugin-vue=script.d.ts.map