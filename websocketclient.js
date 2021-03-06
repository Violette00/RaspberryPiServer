var input = document.querySelector('input');
var preview = document.querySelector('.preview');

input.addEventListener('change', sendFile);
host = "ws://192.168.1.150:8765"

function sendFile(){
    console.log("The method is called");
    var curFiles = input.files;
    if (curFiles.length === 0){
        var para = document.createElement('p');
        para.textContent = 'No files currently selected for transfer';
        preview.appendChild(para);
    } else {
        var exampleSocket = new WebSocket(host);
        var file = curFiles[0];
        exampleSocket.onopen = function(event){
            var fileSize = file.size;
            var chunkSize = 64 * 1024;
            var offset = 0;
            var self = this;
            var chunkReaderBlock = null;
            var totalChunks = (Math.ceil(fileSize/chunkSize));
            console.log("Total Chunks = " + totalChunks);
            exampleSocket.send(file.name);
            exampleSocket.send(totalChunks);
            console.log(fileSize);
            exampleSocket.send(fileSize);
            var readEventHandler = function(evt){
                if (evt.target.error == null){
                    offset += chunkSize;
                    if (offset > fileSize){
                        offset = fileSize;
                    }
                    var para = document.createElement('p');
                    para.textContent = (offset/fileSize*100).toFixed(2) + '% complete';
                    preview.replaceChild(para, preview.childNodes[1]);
                    sendFileChunk(evt.target.result);
                } else {
                    console.log("Read error: " + evt.target.error);
                    return;
                }
                if (offset >= fileSize){
                    console.log("Done reading file");
                    exampleSocket.send("Complete");
                    return;
                }
                chunkReaderBlock(offset, chunkSize, file);
            }

            chunkReaderBlock = function(_offset, length, _file){
                var r = new FileReader();
                var blob = _file.slice(_offset, length + _offset);
                r.onload = readEventHandler;
                r.readAsArrayBuffer(blob);
            }

            var sendFileChunk = function(_file){
                exampleSocket.send(_file);
            }

            chunkReaderBlock(offset, chunkSize, file);
        }
    }
}

