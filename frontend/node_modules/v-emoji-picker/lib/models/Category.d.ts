export interface ICategory {
    name: string;
    icon: string;
}
export declare class Category implements ICategory {
    name: string;
    icon: string;
    constructor(name: string, icon: string);
    get label(): {
        search: string;
        categories: {
            Activity: string;
            Flags: string;
            Foods: string;
            Frequently: string;
            Objects: string;
            Nature: string;
            Peoples: string;
            Symbols: string;
            Places: string;
        };
    };
}
//# sourceMappingURL=Category.d.ts.map