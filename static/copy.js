function CopyToClipboard(id) {
    var r = document.createRange();
    r.selectNode(document.getElementById(id));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(r);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
}


/*
function copyEncrypted() {
    console.log('Copied!')
    var copyText = document.getElementById('encrypted')

    copyText.select();
    navigator.clipboard.writeText(copyText.value)



}

function copyKey() {
    var copyKey = document.getElementById('encryptedkey');
    
    copyKey.select();
    navigator.clipboard.writeText(copyKey.value)

}
*/