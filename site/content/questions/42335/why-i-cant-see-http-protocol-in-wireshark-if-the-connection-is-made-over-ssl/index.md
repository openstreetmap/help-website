+++
type = "question"
title = "Why I cant see HTTP protocol in wireshark if the connection is made over ssl"
description = '''Hi Guys , If I set the packet capture for any ssl site , all I can see first TCP connection is made and then SSL protocol packets . I understand the concern that may be HTTP protocol data is being encapsulated into SSL but while doing troubleshooting how can I make sure user is trying which site/URL...'''
date = "2015-05-12T08:25:00Z"
lastmod = "2015-05-12T10:44:00Z"
weight = 42335
keywords = [ "wireshark" ]
aliases = [ "/questions/42335" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why I cant see HTTP protocol in wireshark if the connection is made over ssl](/questions/42335/why-i-cant-see-http-protocol-in-wireshark-if-the-connection-is-made-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42335-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys ,</p><p>If I set the packet capture for any ssl site , all I can see first TCP connection is made and then SSL protocol packets . I understand the concern that may be HTTP protocol data is being encapsulated into SSL but while doing troubleshooting how can I make sure user is trying which site/URL ? is there any way out to see http protocol packets ?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '15, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/962349492f305ec7bae240fb8c9996ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tech%20round&#39;s gravatar image" /><p>tech round<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tech round has no accepted answers">0%</span></p></div></div><div id="comments-container-42335" class="comments-container"></div><div id="comment-tools-42335" class="comment-tools"></div><div class="clear"></div><div id="comment-42335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42336"></span>

<div id="answer-container-42336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42336-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt the traffic you need the RSA key file. That means you need to private key information. Unless you have access to the server, you will not be able to access this file (i.e., you will not be able to decrypt).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '15, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42336" class="comments-container"></div><div id="comment-tools-42336" class="comment-tools"></div><div class="clear"></div><div id="comment-42336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42339"></span>

<div id="answer-container-42339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42339-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without decrypting the traffic you could do a reverse dns lookup of the destination ip, check the server name in the client hello and inspect the certificate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '15, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-42339" class="comments-container"></div><div id="comment-tools-42339" class="comment-tools"></div><div class="clear"></div><div id="comment-42339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

