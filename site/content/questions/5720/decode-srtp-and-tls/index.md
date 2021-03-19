+++
type = "question"
title = "Decode SRTP and TLS"
description = '''Hi there, I am trying to troubleshoot a voice quality issue on a tls and srtp VOIP call. Normally on a TCP and RTP call, I can use the player to play back these packets so I can listen to the voice quality between handset and call server or gateway with call server. However wireshark can&#x27;t seems to ...'''
date = "2011-08-17T00:03:00Z"
lastmod = "2011-08-17T01:30:00Z"
weight = 5720
keywords = [ "srtp" ]
aliases = [ "/questions/5720" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode SRTP and TLS](/questions/5720/decode-srtp-and-tls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5720-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am trying to troubleshoot a voice quality issue on a tls and srtp VOIP call. Normally on a TCP and RTP call, I can use the player to play back these packets so I can listen to the voice quality between handset and call server or gateway with call server. However wireshark can't seems to decode and play a VOIP call setup using tls and srtp even if the correct RSA key.pem file specified under the SSL protocol.</p><p>Am I missing something or it is a limitation on the wireshark?</p><p>David Lau</p></div><div id="question-tags" class="tags-container tags">srtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '11, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/5e02c496e3c5e3865ad0e6a29f796825?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Lau&#39;s gravatar image" /><p>David Lau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Lau has no accepted answers">0%</span></p></div></div><div id="comments-container-5720" class="comments-container"></div><div id="comment-tools-5720" class="comment-tools"></div><div class="clear"></div><div id="comment-5720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5721"></span>

<div id="answer-container-5721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5721-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a Wireshark limitation at the moment. The SIP dissector (I assume here SIP/TLS !) isn't yet able to create a crypto context for the RTP dissector to use. The RTP dissector isn't yet able to integrate with libsrtp to decrypt the media.</p><p>It would be a nice Summer of Code project...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '11, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5721" class="comments-container"><span id="5722"></span><div id="comment-5722" class="comment"><div id="post-5722-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>thanks for the response and can't wait for this feature to be available.</p><p>cheers.</p></div><div id="comment-5722-info" class="comment-info"><span class="comment-age">(17 Aug '11, 01:53)</span> David Lau</div></div></div><div id="comment-tools-5721" class="comment-tools"></div><div class="clear"></div><div id="comment-5721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

