+++
type = "question"
title = "SSL Dissector not displaying &quot;Client Hello&quot;"
description = '''I analyzed a file today regarding an SSL session (or at least attempt thereof). The fourth packet in line should be a Client Hello packet with all the necessary SSL data underneath. But it wasn&#x27;t. It only showed a PSH,ACK type of packet. When comparing this to a similar file (in which the SSL sessio...'''
date = "2016-02-15T08:23:00Z"
lastmod = "2016-02-17T08:36:00Z"
weight = 50212
keywords = [ "ssl", "dissector" ]
aliases = [ "/questions/50212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Dissector not displaying "Client Hello"](/questions/50212/ssl-dissector-not-displaying-client-hello)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I analyzed a file today regarding an SSL session (or at least attempt thereof). The fourth packet in line should be a Client Hello packet with all the necessary SSL data underneath. But it wasn't. It only showed a PSH,ACK type of packet.</p><p>When comparing this to a similar file (in which the SSL sessions successfully initiated) I did see the Client Hello packet. Although the size of the two packets was exactly the same, one showed as a Client Hello packet, the other as a regular TCP packet. Even when specifically specifying the packet as being part of the SSL protocol (right click &gt; decode as), it refused to show me more info in the details pane.</p><p>I only got the issue resolved by isolating this one packet in a separate file and then opening it again. Only then was it shown as an SSL packet and could I see the details.</p><p>I added a screenshot to avoid heavy scrubbing. Can anyone give me an explanation as to why Wireshark shows this behavior? It must have something to do with the fact the SSL handshake failed.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ssl.png" alt="screen" /></p></div><div id="question-tags" class="tags-container tags">ssl dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '16, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p>JoepMeloen86<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></img></div></div><div id="comments-container-50212" class="comments-container"><span id="50215"></span><div id="comment-50215" class="comment"><div id="post-50215-score" class="comment-score"></div><div class="comment-text"><p>Assuming that SSL works in general, anonymizing the capture by just substituting the IP addresses should be secure enough if you wouldn't publish any key material, and would allow much better analysis.</p><p>Without access to the capture, I would suggest that you export to a new file all frames <em>starting from frame 149</em> in the current one (the first SYN packet), and to another new file, all frames <em>up to frame 152</em>. Opening both these new files should answer the question whether Wireshark has problems to properly decode the packet due to something it can see <em>before</em> that packet (like other TCP packets using the same pair of sockets), or because the SSL handshake has failed <em>after</em> that packet.</p><p>It may turn out that it is worth opening a bug on Wireshark bugzilla. Posting the capture file there would be necessary but you can mark it as a "private attachment" accessible only to the core developers.</p></div><div id="comment-50215-info" class="comment-info"><span class="comment-age">(15 Feb '16, 10:45)</span> sindy</div></div><span id="50233"></span><div id="comment-50233" class="comment"><div id="post-50233-score" class="comment-score"></div><div class="comment-text"><p>The problem is the same with packet 149 and up. The problem is gone when exporting packet 152 and lower.</p><p>So it seems that as soon as the SSL handshake is unsuccessful, it doesn't classify it as SSL and is unable to.</p><p>Do you still suggest to post it on wireshark bugzilla ?</p></div><div id="comment-50233-info" class="comment-info"><span class="comment-age">(16 Feb '16, 02:44)</span> JoepMeloen86</div></div><span id="50234"></span><div id="comment-50234" class="comment"><div id="post-50234-score" class="comment-score"></div><div class="comment-text"><p>Yes, as it is the most reliable way to inform the respective developer about the bug.</p></div><div id="comment-50234-info" class="comment-info"><span class="comment-age">(16 Feb '16, 02:56)</span> sindy</div></div></div><div id="comment-tools-50212" class="comment-tools"></div><div class="clear"></div><div id="comment-50212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50274"></span>

<div id="answer-container-50274" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50274-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Registered: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12132">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12132</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p>JoepMeloen86<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></div></div><div id="comments-container-50274" class="comments-container"><span id="50275"></span><div id="comment-50275" class="comment"><div id="post-50275-score" class="comment-score"></div><div class="comment-text"><p>Looks OK to me using a build from master, so probably fixed. Try a newer build from <a href="https://www.wireshark.org/download/automated/win64/">automated downloads</a>.</p></div><div id="comment-50275-info" class="comment-info"><span class="comment-age">(17 Feb '16, 09:02)</span> grahamb ♦</div></div><span id="50294"></span><div id="comment-50294" class="comment"><div id="post-50294-score" class="comment-score"></div><div class="comment-text"><p>According to bug report it might be caused by the followed up HTTP packet from a proxy server. A suggested downgrade back to 1.12 resolves the issue but doesn't display the HTTP packet anymore (which it was displaying in 2.0.1)</p><p>Anyway, for completeness I tested with the latest build from master as you suggested but the issue persists.</p><p>I will wait for the bug report conclusion</p></div><div id="comment-50294-info" class="comment-info"><span class="comment-age">(17 Feb '16, 23:29)</span> JoepMeloen86</div></div></div><div id="comment-tools-50274" class="comment-tools"></div><div class="clear"></div><div id="comment-50274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

