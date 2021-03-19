+++
type = "question"
title = "TLS handshake without Server Certificate?"
description = '''I&#x27;ve been investigating an issue caused in combination with our proxy. During analysis it appears the TLS handshake protocol is either not followed or something else is happening. I would like to ask someone else to take a look and perhaps explain what might be happening. Filtering only on the SSL c...'''
date = "2017-07-05T00:50:00Z"
lastmod = "2017-07-05T23:43:00Z"
weight = 62514
keywords = [ "tls", "handshake", "cert", "certificate" ]
aliases = [ "/questions/62514" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TLS handshake without Server Certificate?](/questions/62514/tls-handshake-without-server-certificate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62514-score" class="post-score" title="current number of votes">0</div><span id="post-62514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been investigating an issue caused in combination with our proxy. During analysis it appears the TLS handshake protocol is either not followed or something else is happening. I would like to ask someone else to take a look and perhaps explain what might be happening.</p><p>Filtering only on the SSL communications, it appears the first two steps go OK. There is a Client Hello, Server Hello, then there are suddenly a couple of Encrypted Handshake Messages followed by a regular Server Key Exchange + Server Hello Done. What I am missing here is the Server Certificate, which I can only assume is sent in the Encrypted Handshake Messages. I made sure to clear my cache but this keeps occuring.</p><p>Is it possible to send the server Cert in an encrypted handshake? How does this work?</p><p>This is a capture made by browsing to www.timeanddate.com. From my corner of the globe, it resolves to 192.33.31.72. Another server like 151.101.60.69 does not show this behavior.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wask.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-cert" rel="tag" title="see questions tagged &#39;cert&#39;">cert</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '17, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p><span>JoepMeloen86</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></img></div></div><div id="comments-container-62514" class="comments-container"><span id="62515"></span><div id="comment-62515" class="comment"><div id="post-62515-score" class="comment-score"></div><div class="comment-text"><p>Full length frames (see the length of these frames) suggest to me that if you play with the various reassemble settings you may see something else. My assumption is that Wireshark can't make heads or tails from the individual frames, since these are part of a larger PDU. It therefore falls back to assuming that it's an Encrypted message.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-62515-info" class="comment-info"><span class="comment-age">(05 Jul '17, 02:29)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62516"></span><div id="comment-62516" class="comment"><div id="post-62516-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comments Jaap. It does appear the certificate is listed in the bytes (it's quite a long list).</p><p>Is this a shortcomming of Wireshark? Or (taking into account we have issues with this website) is the server not acting according to protocol?</p><p><a href="https://www.cloudshark.org/captures/a274aeee01ee">https://www.cloudshark.org/captures/a274aeee01ee</a></p></div><div id="comment-62516-info" class="comment-info"><span class="comment-age">(05 Jul '17, 04:34)</span> <span class="comment-user userinfo">JoepMeloen86</span></div></div></div><div id="comment-tools-62514" class="comment-tools"></div><div class="clear"></div><div id="comment-62514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62529"></span>

<div id="answer-container-62529" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62529-score" class="post-score" title="current number of votes">2</div><span id="post-62529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JoepMeloen86 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are affected by a shortcoming in the current SSL/TLS dissector (up to version 2.4) which is tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303</a></p><p>The problem is that your certificate message is quite large and spans multiple TLS records. This scenario is currently not supported in Wireshark, there is no reassembly of TLS handshake messages yet. I am working on this, hopefully it will be available in version 2.6.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jul '17, 08:41</strong> </span></p></div></div><div id="comments-container-62529" class="comments-container"><span id="62553"></span><div id="comment-62553" class="comment"><div id="post-62553-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. Looks like this is what i'm experiencing.</p></div><div id="comment-62553-info" class="comment-info"><span class="comment-age">(05 Jul '17, 23:43)</span> <span class="comment-user userinfo">JoepMeloen86</span></div></div></div><div id="comment-tools-62529" class="comment-tools"></div><div class="clear"></div><div id="comment-62529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

