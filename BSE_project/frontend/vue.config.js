const path = require("path");

module.exports = {
  publicPath: "/static",
  outputDir: path.resolve(__dirname, "../", "backend", "backend", "static"),
  indexPath: path.resolve(
    __dirname,
    "../",
    "backend",
    "backend",
    "templates",
    "index.html"
  ),
};
