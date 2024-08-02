
function MapAddList(tiles){
    tiles.forEach(MapAddTile);
}
function MapAddTile(tile){
    ctx = $("#map-main")[0].getContext("2d");
    var img = new Image();
    img.onload = function() {
      ctx.drawImage(img, (tile.x+5)*224, (tile.y+5)*224, 224, 224);
    };
    img.src = `./images/${tile.skin}.png`;
}