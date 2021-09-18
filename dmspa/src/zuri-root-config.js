import { registerApplication, start } from 'single-spa';

registerApplication({
    name: '@zuri/dmplugins',
    app: () => System.import('@zuri/dmplugins'),
    activeWhen: ['/dm'],
});

// registerApplication({
//   name: "@zuri/navbar",
//   app: () => System.import("@zuri/navbar"),
//   activeWhen: ["/"]
// });

start({
    urlRerouteOnly: true,
});
