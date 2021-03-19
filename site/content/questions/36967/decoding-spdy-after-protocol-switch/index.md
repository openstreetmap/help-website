+++
type = "question"
title = "Decoding spdy after protocol switch"
description = '''I have an unusual SPDY-based protocol that I&#x27;m trying to decode. The session begins by the client making an HTTP GET request to the server. The client then makes itself a SPDY server and the server becomes a SPDY client. This allows the server to request data from the client using normal HTTP reques...'''
date = "2014-10-10T12:32:00Z"
lastmod = "2014-10-21T07:09:00Z"
weight = 36967
keywords = [ "spdy", "ssl", "dissector" ]
aliases = [ "/questions/36967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding spdy after protocol switch](/questions/36967/decoding-spdy-after-protocol-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36967-score" class="post-score" title="current number of votes">0</div><span id="post-36967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an unusual SPDY-based protocol that I'm trying to decode. The session begins by the client making an HTTP GET request to the server. The client then makes itself a SPDY server and the server becomes a SPDY client. This allows the server to request data from the client using normal HTTP requests.</p><p>I'd like to decode the SPDY packets in wireshark. Except for the initial handshake, the rest of the communication is standard SPDY. But when I configure SSL to decode the port as spdy, the packets still appear as SSL. The SSL Record indicates:</p><pre><code>TLSv1 Record Layer: Application Data Protocol: spdy</code></pre><p>And I can see the decrypted SSL data. But it doesn't decode the SPDY packet.</p><p>If I reconfigure to decode the SSL port as HTTP, then it decodes the initial HTTPS handshake, but the rest of the packets are still listed as SSL.</p><p>I'm familiar with dissectors, and am investigating in the source now, but can wireshark handle switching protocols in the middle of a TLS session?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spdy" rel="tag" title="see questions tagged &#39;spdy&#39;">spdy</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '14, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/ed9a0d8cd44b62539b141f6c10405db1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20Napier&#39;s gravatar image" /><p><span>Rob Napier</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob Napier has one accepted answer">100%</span></p></div></div><div id="comments-container-36967" class="comments-container"></div><div id="comment-tools-36967" class="comment-tools"></div><div class="clear"></div><div id="comment-36967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37238"></span>

<div id="answer-container-37238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37238-score" class="post-score" title="current number of votes">0</div><span id="post-37238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like Wireshark was not able to decode the SSL/TLS session, maybe because your client/server are using DH/DHE (Diffie Hellmann) ciphers. See also here: <a href="https://ask.wireshark.org/questions/37223/wireshark-decryption-limitation">https://ask.wireshark.org/questions/37223/wireshark-decryption-limitation</a></p><p>Can you please check this in the SSL debug file?</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; SSL debug file</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37238" class="comments-container"></div><div id="comment-tools-37238" class="comment-tools"></div><div class="clear"></div><div id="comment-37238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

