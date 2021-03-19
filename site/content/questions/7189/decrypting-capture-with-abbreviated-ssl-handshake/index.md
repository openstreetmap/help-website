+++
type = "question"
title = "Decrypting capture with Abbreviated SSL handshake"
description = '''Hi, does anyone have any solution to decrypt captures with Abbreviated SSL handshake (RFC 2246).  What happens in a Abbreviated SSL handshake? From a previous SSL connection the client caches the session ID and resends it to the server to setup a new connection, so insted of the full SSL handshake w...'''
date = "2011-11-01T22:46:00Z"
lastmod = "2011-11-06T09:20:00Z"
weight = 7189
keywords = [ "ssl" ]
aliases = [ "/questions/7189" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting capture with Abbreviated SSL handshake](/questions/7189/decrypting-capture-with-abbreviated-ssl-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, does anyone have any solution to decrypt captures with Abbreviated SSL handshake (RFC 2246).</p><p><strong>What happens in a Abbreviated SSL handshake?</strong> From a previous SSL connection the client caches the session ID and resends it to the server to setup a new connection, so insted of the full SSL handshake where the keys are exchanged ,here only the session ID's are exchanged which makes it impossible to decrypt.</p><p>We require help on this as we are seeing more of this in our environment</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '11, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/3e5e9d76a54debaa630d909e37048da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepacket&#39;s gravatar image" /><p>deepacket<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepacket has no accepted answers">0%</span></p></div></div><div id="comments-container-7189" class="comments-container"></div><div id="comment-tools-7189" class="comment-tools"></div><div class="clear"></div><div id="comment-7189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7255"></span>

<div id="answer-container-7255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the session keys are cached, you either need to make sure you capture the full SSL handshake for the resumed SSL session or you need to make the client or server dump the keying material. Without either of those two, you are out of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '11, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7255" class="comments-container"></div><div id="comment-tools-7255" class="comment-tools"></div><div class="clear"></div><div id="comment-7255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

