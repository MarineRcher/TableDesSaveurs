const express = require('express');
const app = express();
const port = 3000;
app.get('/', (req, res) => {
    res.send('The sedulous hyena ate the antelope!');
});
app.listen(port, function (err) {
    if (err)
        console.log("Error in server setup");
    console.log("Server listening on Port", port);
});
//# sourceMappingURL=app.js.map