
function MapAddList(tiles){
    tiles.forEach(MapAddTile);
}
function MapAddTile(tile){
    if (tile.x == 6 && tile.y == 12
        || tile.x == 7 && tile.y == 12
        || tile.x == 8 && tile.y == 12
        || tile.x == 9 && tile.y == 12
        || tile.x == 10 && tile.y == 12
        || tile.x == 11 && tile.y == 12
    ){
        console.log(tile);
    }
    if ($(`#map${tile.x}${tile.y}`).length == 0){
        $("#map-main").append(
            `<div class="map-tile image-${tile.skin}" `+
            `id="map${tile.x}-${tile.y}" `+
            `style="`+
                `left:${(tile.x+5)*40}px;`+
                `top:${(tile.y+5)*40}px;`+
            `">${tile.x},${tile.y}</div>`);
    }
    // if (!(tile.x in MAP)){
    //     MAP[tile.x] = {}
    // }
    // if (!(tile.y in MAP[tile.x])){
    //     MAP[tile.x][tile.y] = {
    //         name: tile["name"],
    //         skin: tile["skin"],
    //         content: tile["content"]
    //     };
    // }
}