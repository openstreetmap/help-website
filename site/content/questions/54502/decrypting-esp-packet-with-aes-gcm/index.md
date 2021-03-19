+++
type = "question"
title = "Decrypting ESP packet with AES GCM"
description = '''I have a problem when trying to decrypt a presumably valid ESP packet using AES GCM. I have all the values needed but when trying to apply, whireshark does nothing.. It does not even try to attempt to decrypt. I have tried the same using CBC (with different values ofc) and successfully managed to de...'''
date = "2016-08-02T04:59:00Z"
lastmod = "2016-08-02T05:24:00Z"
weight = 54502
keywords = [ "decryption", "gcm", "decrypt", "aes-gcm", "esp" ]
aliases = [ "/questions/54502" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting ESP packet with AES GCM](/questions/54502/decrypting-esp-packet-with-aes-gcm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54502-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem when trying to decrypt a presumably valid ESP packet using AES GCM. I have all the values needed but when trying to apply, whireshark does nothing.. It does not even try to attempt to decrypt. I have tried the same using CBC (with different values ofc) and successfully managed to decrypt it. Is there a reason for this? Is AES GCM not fully implemented? Is there an extra option of some kind I need to set?</p></div><div id="question-tags" class="tags-container tags">decryption gcm decrypt aes-gcm esp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/a1442d44357122966b2283ac0547b5e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mathildh&#39;s gravatar image" /><p>mathildh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mathildh has no accepted answers">0%</span></p></div></div><div id="comments-container-54502" class="comments-container"></div><div id="comment-tools-54502" class="comment-tools"></div><div class="clear"></div><div id="comment-54502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54504"></span>

<div id="answer-container-54504" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54504-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>solved .. the encryption key must be 36 bytes, the first 32 is the key and the last 4 is the salt value</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '16, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/a1442d44357122966b2283ac0547b5e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mathildh&#39;s gravatar image" /><p>mathildh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mathildh has no accepted answers">0%</span></p></div></div><div id="comments-container-54504" class="comments-container"></div><div id="comment-tools-54504" class="comment-tools"></div><div class="clear"></div><div id="comment-54504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

