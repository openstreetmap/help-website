+++
type = "question"
title = "Unable to decode SPDY traffic"
description = '''I am having trouble decoding SPDY traffic. Looking at the ssl_debug output the packets are getting decrypted correctly but for some reason they are not being decoded properly in the GUI. They are not even being shown decrypted, just listed as &quot;Encrypted Application Data&quot;. I have managed to get this ...'''
date = "2015-01-11T13:41:00Z"
lastmod = "2015-02-10T07:50:00Z"
weight = 39058
keywords = [ "spdy", "ssl", "http" ]
aliases = [ "/questions/39058" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decode SPDY traffic](/questions/39058/unable-to-decode-spdy-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39058-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having trouble decoding SPDY traffic. Looking at the ssl_debug output the packets are getting decrypted correctly but for some reason they are not being decoded properly in the GUI. They are not even being shown decrypted, just listed as "Encrypted Application Data".</p><p>I have managed to get this all working for HTTP over SSL and both the HTTP1 and HTTP2 (SPDY) web servers are using the same cipher suite and certificate.</p><p><strong>Useful info</strong></p><p>Linux Ubuntu 14.10 (utopic) x86_64</p><p>Wireshark 1.12.1 (from Ubuntu packages)</p><p><a href="https://drive.google.com/folderview?id=0B79L6jllB7SPaXNqRk45ZXp5S1U&amp;usp=sharing">pcaps and ssl_debug logs</a></p><p><a href="https://raw.githubusercontent.com/robyoung/http2play/master/provisioning/files/ssl/server.key">server key</a></p></div><div id="question-tags" class="tags-container tags">spdy ssl http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '15, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/09cbeba69993bb82b3fc7b70926dfc4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robyoung&#39;s gravatar image" /><p>robyoung<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robyoung has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '15, 09:43</p></div></div><div id="comments-container-39058" class="comments-container"><span id="39148"></span><div id="comment-39148" class="comment"><div id="post-39148-score" class="comment-score"></div><div class="comment-text"><p>can you please add the server key, so we can do our own experiments with the capture files?</p></div><div id="comment-39148-info" class="comment-info"><span class="comment-age">(15 Jan '15, 01:04)</span> Kurt Knochner ♦</div></div><span id="39280"></span><div id="comment-39280" class="comment"><div id="post-39280-score" class="comment-score"></div><div class="comment-text"><p>@kurt-knochner sorry about that, I've added link to it.</p></div><div id="comment-39280-info" class="comment-info"><span class="comment-age">(19 Jan '15, 09:43)</span> robyoung</div></div></div><div id="comment-tools-39058" class="comment-tools"></div><div class="clear"></div><div id="comment-39058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39772"></span>

<div id="answer-container-39772" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39772-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that your capture runs on top of port 443 for which the HTTP dissector has registered. If you expand the SSL record tree, you see "Application Data: http".</p><p>Luckily, you can override this protocol via the SSL keys UAT (<code>~/.wireshark/ssl_keys</code>). This line works for me (tested with v1.99.1rc0-232-g5e4e17c and v1.99.3rc0-78-g895b013):</p><pre><code>&quot;any&quot;,&quot;443&quot;,&quot;spdy&quot;,&quot;server.key&quot;,&quot;&quot;</code></pre><p>You must use port <code>443</code>, specifying the wildcard <code>*</code> somehow gives precedence to the HTTP dissector.</p><p>Side-note: in your specific capture, the ALPN and NPN TLS extensions are advertised by the client, but the server responds only with NPN. The NPN extension merely gives a hint for the selected protocol, it is up to the client to respond with an appropriate protocol response. ALPN on the other hand requires exactly one value and this hint is implemented in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=3222cd1df6b0c8a43d959a7913fc3bf4b53e9422">this patch</a> (v1.99.3rc0-69-g3222cd1). As ALPN is the successor of NPN, it was not deemed necessary to implement NPN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-39772" class="comments-container"></div><div id="comment-tools-39772" class="comment-tools"></div><div class="clear"></div><div id="comment-39772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

