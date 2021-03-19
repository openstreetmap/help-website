+++
type = "question"
title = "SRTP over H323"
description = '''Hi there. My Automation Testing Environment runs SRTP calls over H323.  In this case only payload part of RTP packet is encrypted. (Not whole RTP packet as in case of SIP/TLS). So if I&#x27;m Wiresharking the call, how do i actually know from its capture: a) If payload is actually encrypted. b) What encr...'''
date = "2012-01-25T15:03:00Z"
lastmod = "2012-01-26T01:21:00Z"
weight = 8612
keywords = [ "srtp", "h323" ]
aliases = [ "/questions/8612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SRTP over H323](/questions/8612/srtp-over-h323)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8612-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there.</p><p>My Automation Testing Environment runs SRTP calls over H323. In this case <strong>only payload</strong> part of RTP packet is encrypted. (Not whole RTP packet as in case of SIP/TLS).</p><p>So if I'm Wiresharking the call, how do i actually know from its capture:</p><p>a) If payload is actually encrypted.</p><p>b) What encryption algorithm is used.</p><p>I read that DTMF can give an exact answer for those questions. Could you please expand a bit about that?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">srtp h323</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '12, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/c4466d38ca3cff9247bbe6f54c46f0f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evgeny1976&#39;s gravatar image" /><p>evgeny1976<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evgeny1976 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '12, 15:05</p></div></div><div id="comments-container-8612" class="comments-container"></div><div id="comment-tools-8612" class="comment-tools"></div><div class="clear"></div><div id="comment-8612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8620"></span>

<div id="answer-container-8620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8620-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all you have to be aware of the difference between signaling and media.</p><ul><li>Signaling flows contain the control messages related to the call. Examples of such protocols are the H.323 family and SIP.</li><li>Media flows contain the media of a call. Speech, audio, video all are forms of media. These are usually transported using RTP.</li></ul><p>In your description you seem to indicate that in the H.323 context only the RTP payload is encrypted, while in the SIP?TLS context the whole RTP packet is encrypted. This is not true.</p><p>As said above H.323 and SIP are signaling protocols, which may or may not run over encrypted connections. When looking at encrypting media streams, Secure RTP (<a href="http://tools.ietf.org/html/rfc3711">SRTP</a>) is the standard solution. But these are independent!</p><p>If you want to look at the encrypted state of your media session, you'll have to check the RFC. From there you can see that it's just the payload that's encrypted, but not the header. So it should be possible to analyze the RTP stream itself, although the payload should not be presentable according to the declared codec.</p><p>If you want to know which encryption is used, you'll have to dig into either the static configuration or the signaling protocol messages. There the security features are set or negotiated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8620" class="comments-container"><span id="8648"></span><div id="comment-8648" class="comment"><div id="post-8648-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thank you for your help...</p><p>Analising the payload of RTP packet, how can I tell either it is encripted or not?</p></div><div id="comment-8648-info" class="comment-info"><span class="comment-age">(27 Jan '12, 03:37)</span> evgeny1976</div></div><span id="8651"></span><div id="comment-8651" class="comment"><div id="post-8651-score" class="comment-score"></div><div class="comment-text"><p>If you look <a href="http://tools.ietf.org/html/rfc3711#section-3.1">how the SRTP framework encrypts RTP packets</a> you'll see that you still have access to the payload type (PT) field. Using that you can try to interpret the payload data, play out the media though the applicable code. If it's unencrypted you will be able to, otherwise you won't.</p></div><div id="comment-8651-info" class="comment-info"><span class="comment-age">(27 Jan '12, 04:12)</span> Jaap ♦</div></div></div><div id="comment-tools-8620" class="comment-tools"></div><div class="clear"></div><div id="comment-8620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

