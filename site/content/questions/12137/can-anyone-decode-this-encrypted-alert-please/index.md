+++
type = "question"
title = "Can anyone decode this Encrypted Alert please?"
description = '''The hex data shown below is a TLSv1 packet taken from a Wireshark trace. It shows an Encrypted Alert message according to Wireshark. The only problem is I cannot work out just what the alert really is - according to my research on the web the alert code level and description bytes contain the values...'''
date = "2012-06-24T11:17:00Z"
lastmod = "2012-06-24T15:37:00Z"
weight = 12137
keywords = [ "encryption", "codes", "alert" ]
aliases = [ "/questions/12137" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can anyone decode this Encrypted Alert please?](/questions/12137/can-anyone-decode-this-encrypted-alert-please)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The hex data shown below is a TLSv1 packet taken from a Wireshark trace. It shows an Encrypted Alert message according to Wireshark. The only problem is I cannot work out just what the alert really is - according to my research on the web the alert code level and description bytes contain the values 53 and AD - however these do not correspond to any values I can find. I believe the level code can be 1 or 2 and the description can be one of about 30 codes but decimal 173 is not one of these. Could anyone be good enough to enlighten me as to where I am going wrong in my analysis of the message and, ideally, tell me what the alert code really is? Many thanks.<br />
</p><p><code>0000  00 1e 4f ae ac 2d 00 15 e9 28 85 8b 08 00 45 00   ..O..-...(....E. 0010  00 4d 44 64 40 00 33 06 c0 00 c3 e1 bc c1 c0 a8   [email protected] 0020  01 fb 01 bb c4 65 b7 c7 fc 59 cf 6b 1d 28 50 18   .....e...Y.k.(P. 0030  00 36 b3 28 00 00 15 03 01 00 20 53 ad 3c 5d c6   .6.(...... S.&lt;]. 0040  96 44 3c cd 88 6f fa 0d 36 a5 99 84 0e c2 2c e5   .D&lt;..o..6.....,. 0050  b3 d2 e3 48 00 78 50 0c 20 d2 a7                  ...H.xP. ..</code></p></div><div id="question-tags" class="tags-container tags">encryption codes alert</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '12, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/fb0522d199e7d00e24223257614c16a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bernard46&#39;s gravatar image" /><p>Bernard46<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bernard46 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '12, 11:19</p></div></div><div id="comments-container-12137" class="comments-container"></div><div id="comment-tools-12137" class="comment-tools"></div><div class="clear"></div><div id="comment-12137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12138"></span>

<div id="answer-container-12138" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12138-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I may have found the answer to my own question! Searching round the web a bit more I came across a post elsewhere which suggested that the actual codes are encrypted, hence the "Encrypted" Alert! I would be grateful if anyone can confirm this - it would explain why I seem to be seeing a lot of different alert codes with no consistency and none of them appear in the TLS specifications!<br />
</p><p>It may be that I have to try and find the developers and ask them if they would mind debugging this area in order to find out what is going on!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '12, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/fb0522d199e7d00e24223257614c16a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bernard46&#39;s gravatar image" /><p>Bernard46<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bernard46 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12138" class="comments-container"></div><div id="comment-tools-12138" class="comment-tools"></div><div class="clear"></div><div id="comment-12138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

