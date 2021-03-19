+++
type = "question"
title = "Viewing SSL packets"
description = '''If I just want to see encrypted SSL packets, do I need to capture the handshake (even if I am not decrypting the packets?) I am trying to find out this information to help a friend who started capturing after the handshake and is getting far fewer packets than expected. Thanks'''
date = "2012-05-04T14:01:00Z"
lastmod = "2012-05-05T02:27:00Z"
weight = 10689
keywords = [ "ssl" ]
aliases = [ "/questions/10689" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Viewing SSL packets](/questions/10689/viewing-ssl-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10689-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I just want to see encrypted SSL packets, do I need to capture the handshake (even if I am not decrypting the packets?) I am trying to find out this information to help a friend who started capturing after the handshake and is getting far fewer packets than expected.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '12, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/4cfda0fc12df1028d6acba3bac67bfc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcushing&#39;s gravatar image" /><p>dcushing<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcushing has no accepted answers">0%</span></p></div></div><div id="comments-container-10689" class="comments-container"></div><div id="comment-tools-10689" class="comment-tools"></div><div class="clear"></div><div id="comment-10689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10694"></span>

<div id="answer-container-10694" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10694-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For viewing SSL packets without decrypting them, you don't need the SSL handshake. However, you will only see "ApplicationData" frames. You will be able to see when the client and the server send data to each other and how much, but of course you won't see what information they are exchanging.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '12, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10694" class="comments-container"></div><div id="comment-tools-10694" class="comment-tools"></div><div class="clear"></div><div id="comment-10694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

