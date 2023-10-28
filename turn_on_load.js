const ewelink = require('ewelink-api');

(async () => {

  const connection = new ewelink({
    email: 'email@email.com',
    password: 'pass',
    region: 'EU',
    APP_ID: 'xxx',
    APP_SECRET: 'xxx',
  });
  const id = "xxx" // pastir
  
  /* get specific devide info */
  const device = await connection.getDevice(id);
  const status = await connection.getDevicePowerState(id);
  //console.log(status);
  if (device.online && status.status == "ok"){
    /* toggle device */
    const status = await connection.setDevicePowerState(id, 'off');
    console.log(status);
  }

})();
