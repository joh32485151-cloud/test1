// var options = {
//     env: 'AutodeskProduction2',
//     api: 'streamingV2',  // for models uploaded to EMEA change this option to 'streamingV2_EU'
//     getAccessToken: function(onTokenReady) {
//         var token = 'YOUR_ACCESS_TOKEN';
//         var timeInSeconds = 3600; // Use value provided by Forge Authentication (OAuth) API
//         onTokenReady(token, timeInSeconds);
//     }
// };
var options = {
    'env': 'Local',
    'document': './CHTStaffDormitory/Resource/3D 視圖/3D - 全(維管系統) 9985200/3D - 全(維管系統).svf'
    //'document': './shaver/0.svf'
};
var viewer
Autodesk.Viewing.Initializer(options, () => {
    viewer = new Autodesk.Viewing.GuiViewer3D(document.getElementById('forgeViewer'));
    viewer.start(options.document, options, onDocumentLoadSuccess, onDocumentLoadFailure);
});


function onDocumentLoadSuccess() {
     
    //shaver
    // let result = [
    //     { dbId: 4, label: '<span style="color: red;">外殼</span>', css: 'temperatureBorder temperatureOk fas fa-thermometer-empty' },
    //     { dbId: 13, label: '<span style="color: red;">刀網</span>', css: 'temperatureBorder temperatureOk fas fa-thermometer-empty' }
    // ];

    //CHT_dorm
    let result = [
        { dbId: 246193, label: '<span style="color: red;">太陽能板</span>', css: 'temperatureBorder temperatureOk fas fa-thermometer-empty' },
        { dbId: 251104, label: '<span style="color: red;">智慧路燈</span>', css: 'temperatureBorder temperatureOk fas fa-thermometer-empty' }
    ];

    viewer.addEventListener(Autodesk.Viewing.GEOMETRY_LOADED_EVENT, (x) => {
        console.log("loaded");
        viewer.loadExtension('IconMarkupExtension', {
            icons: result,
        })
        viewer.getExtension('IconMarkupExtension').showIcons(true)
    });

    viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, function (e) {
        if (e.dbIdArray.length) {
            dbId = e.dbIdArray[0];
            console.log('DbIdxx: ' + dbId);
        }
    })
}

function onDocumentLoadFailure(viewerErrorCode) {
    console.log("Error !");
    console.error('onDocumentLoadFailure() - errorCode:' + viewerErrorCode);
}