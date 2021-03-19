+++
type = "question"
title = "Connect Direct Secure Plus decryption"
description = '''Is it possible to decrypt Connect Direct Secure Plus with Wireshark?'''
date = "2013-04-23T15:51:00Z"
lastmod = "2013-04-24T04:09:00Z"
weight = 20754
keywords = [ "plus", "secure", "connect", "decryption", "direct" ]
aliases = [ "/questions/20754" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connect Direct Secure Plus decryption](/questions/20754/connect-direct-secure-plus-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to decrypt Connect Direct Secure Plus with Wireshark?</p></div><div id="question-tags" class="tags-container tags">plus secure connect decryption direct</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/9c70aa6e240b38bb391e6d39e033c4e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve%20Fenter&#39;s gravatar image" /><p>Steve Fenter<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve Fenter has no accepted answers">0%</span></p></div></div><div id="comments-container-20754" class="comments-container"></div><div id="comment-tools-20754" class="comment-tools"></div><div class="clear"></div><div id="comment-20754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20759"></span>

<div id="answer-container-20759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although Connect Direct Secure Plus uses TLS, <strong>there is no decryption support</strong> for that protocol in Wireshark.</p><p>Apparently they use a variation of Diffie Hellman to establish a crypto key, which makes it impossible harder to decrypt the data stream, as there is no way to generate the required session key, unless either party (client or server) discloses that key.</p><p>From: <a href="http://www.commoncriteriaportal.org/files/epfiles/sterling-v37-sec-e.pdf">http://www.commoncriteriaportal.org/files/epfiles/sterling-v37-sec-e.pdf</a></p><blockquote><p>"STS is a Sterling Commerce, Inc. proprietary protocol that includes a variation of the basic Diffie-Hellman protocol"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20759" class="comments-container"></div><div id="comment-tools-20759" class="comment-tools"></div><div class="clear"></div><div id="comment-20759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

