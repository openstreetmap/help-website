+++
type = "question"
title = "Decoding TLS Traffic"
description = '''Hey guys, I just wanted to know whether it&#x27;s possible to decode TLS_PSK_AES_128_CBC_SHA, having the pre-shared keys.'''
date = "2010-10-25T17:39:00Z"
lastmod = "2010-10-26T10:38:00Z"
weight = 637
keywords = [ "tls_aes" ]
aliases = [ "/questions/637" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding TLS Traffic](/questions/637/decoding-tls-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I just wanted to know whether it's possible to decode TLS_PSK_AES_128_CBC_SHA, having the pre-shared keys.</p></div><div id="question-tags" class="tags-container tags">tls_aes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/f1ce81c0f25db0cd4e04754fffbd8295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TylerDurden1983&#39;s gravatar image" /><p>TylerDurden1983<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TylerDurden1983 has no accepted answers">0%</span></p></div></div><div id="comments-container-637" class="comments-container"><span id="664"></span><div id="comment-664" class="comment"><div id="post-664-score" class="comment-score"></div><div class="comment-text"><p>Did you check http://wiki.wireshark.org/SSL? Good resource page for TLS decryption.</p></div><div id="comment-664-info" class="comment-info"><span class="comment-age">(26 Oct '10, 09:18)</span> lchappell ♦</div></div></div><div id="comment-tools-637" class="comment-tools"></div><div class="clear"></div><div id="comment-637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="675"></span>

<div id="answer-container-675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-675-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Given the right keys, the instructions in http://wiki.wireshark.org/SSL should point you in the right direction. Be sure that you have all keys in the proper format; I ran into problems with a system that wouldn't directly export keys to a PEM file, and I had to manually take it through a few steps with openssl (the use of which is discussed on the wiki page) to massage the keys into a PEM file before I could proceed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-675" class="comments-container"><span id="686"></span><div id="comment-686" class="comment"><div id="post-686-score" class="comment-score"></div><div class="comment-text"><p>From what I have read in the Wiki link, it seems Wireshark can only decode RSA encrypted traffic, unless i am missing somethin</p></div><div id="comment-686-info" class="comment-info"><span class="comment-age">(26 Oct '10, 14:09)</span> TylerDurden1983</div></div></div><div id="comment-tools-675" class="comment-tools"></div><div class="clear"></div><div id="comment-675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

