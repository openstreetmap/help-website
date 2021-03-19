+++
type = "question"
title = "Do you need a Four-way Handshake for each client?"
description = '''Thank you for your time. When decrypting 802.11 traffic I understand that we need all 4 portions of the handshake to decrypt the capture file. Assuming that my handshake is valid for that particular session of collection.  Do I need a handshake for each client or will one handshake be able to decryp...'''
date = "2013-04-25T06:24:00Z"
lastmod = "2013-04-25T07:59:00Z"
weight = 20796
keywords = [ "decryption", "eapol" ]
aliases = [ "/questions/20796" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Do you need a Four-way Handshake for each client?](/questions/20796/do-you-need-a-four-way-handshake-for-each-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20796-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thank you for your time.</p><p>When decrypting 802.11 traffic I understand that we need all 4 portions of the handshake to decrypt the capture file. Assuming that my handshake is valid for that particular session of collection.</p><p>Do I need a handshake for each client or will one handshake be able to decrypt multiple clients at the time of collection?</p></div><div id="question-tags" class="tags-container tags">decryption eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '13, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/a0a43b221a642dda68bc5cb3296fdebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pyRabbit&#39;s gravatar image" /><p>pyRabbit<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pyRabbit has no accepted answers">0%</span></p></div></div><div id="comments-container-20796" class="comments-container"></div><div id="comment-tools-20796" class="comment-tools"></div><div class="clear"></div><div id="comment-20796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20801"></span>

<div id="answer-container-20801" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20801-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For WPA(2) you need each unique handshake to decrpyt the unicast traffic from the associated client. This is due to nonce values being exchanged within the handshake and making each key somewhat unique.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '13, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-20801" class="comments-container"><span id="20804"></span><div id="comment-20804" class="comment"><div id="post-20804-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick answer. I also just verified this using my own network. You need all four parts of the EAPOL handshake (for each client) that you want to decrypt.</p></div><div id="comment-20804-info" class="comment-info"><span class="comment-age">(25 Apr '13, 10:07)</span> pyRabbit</div></div></div><div id="comment-tools-20801" class="comment-tools"></div><div class="clear"></div><div id="comment-20801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

