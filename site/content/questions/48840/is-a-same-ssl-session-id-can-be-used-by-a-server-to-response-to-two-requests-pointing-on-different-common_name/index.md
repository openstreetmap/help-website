+++
type = "question"
title = "Is a same SSL Session ID can be used by a server to response to two requests pointing on different common_name"
description = '''It is a little bit tricky, but I&#x27;d like to know if a SSL server serving two different common name can reuse the same SSL Session ID when these request actually point on different common name ? It is not somehting I try to do but something I&#x27;ve got on my network and I&#x27;d like to figure out. To clarify...'''
date = "2016-01-04T08:26:00Z"
lastmod = "2016-01-04T13:28:00Z"
weight = 48840
keywords = [ "ssl", "session", "id" ]
aliases = [ "/questions/48840" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is a same SSL Session ID can be used by a server to response to two requests pointing on different common\_name](/questions/48840/is-a-same-ssl-session-id-can-be-used-by-a-server-to-response-to-two-requests-pointing-on-different-common_name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48840-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It is a little bit tricky, but I'd like to know if a SSL server serving two different common name can reuse the same SSL Session ID when these request actually point on different common name ?</p><p>It is not somehting I try to do but something I've got on my network and I'd like to figure out.</p><p>To clarify, let's assume a client makes two requests:</p><ul><li><p>First request to <a href="https://host_01.com">https://host_01.com</a>, and he gets for instance SessionID = 0x1234</p></li><li><p>Second request to <a href="https://host_02.com">https://host_02.com</a>, and he gets SessionID = 0X1234 (same session ID)</p></li></ul><p>host_01.com and host_02.com have different IP addresses that could actually point on the same server.</p></div><div id="question-tags" class="tags-container tags">ssl session id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '16, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/f339eec46a150b979c3331614c93bb9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shared%20Trash&#39;s gravatar image" /><p>Shared Trash<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shared Trash has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '16, 09:03</p></div></div><div id="comments-container-48840" class="comments-container"></div><div id="comment-tools-48840" class="comment-tools"></div><div class="clear"></div><div id="comment-48840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48841"></span>

<div id="answer-container-48841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48841-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="https://www.ietf.org/rfc/rfc4346.txt">RFC 4346</a>:</p><blockquote><p>session identifier An arbitrary byte sequence chosen by the server to identify an active or resumable session state.</p></blockquote><p>Thus it seems to me to be possible to get the same session ID for 2 different sessions, the server would have to differentiate the session ID's for each session as they will refer to a different session state.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '16, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48841" class="comments-container"><span id="48843"></span><div id="comment-48843" class="comment"><div id="post-48843-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb for your quick answser. But mod_ssl and other popular/common ssl modules don't usually do that, it may mean that owner of this server had written some specific code to do so ?</p></div><div id="comment-48843-info" class="comment-info"><span class="comment-age">(04 Jan '16, 09:06)</span> Shared Trash</div></div></div><div id="comment-tools-48841" class="comment-tools"></div><div class="clear"></div><div id="comment-48841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48853"></span>

<div id="answer-container-48853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48853-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do note that the Session ID is established by the server. It would be a bit silly for a server to send the same session identifier twice as that would associate different secrets to the same session ID. (The Client Random is also incorporated in the master secret calculation, hence the server cannot force the use of exactly the same master secret.)</p><p>From <a href="https://tools.ietf.org/html/rfc5246">RFC 5246 (TLS 1.2)</a>:</p><blockquote><p>session identifier<br />
An arbitrary byte sequence chosen by the server to identify an active or resumable session state.</p></blockquote><p>and:</p><blockquote><p>The client sends a ClientHello using the Session ID of the session to be resumed. <strong>The server then checks its session cache for a match.</strong> If a match is found, and the server is willing to re-establish the connection under the specified session state, it will send a ServerHello with the same Session ID value.<br />
</p></blockquote><p>Even if an attacker manages to capture the Session ID, he cannot send it to the server and impersonate the victim client as he does not posess master secret related to that session ID (see <a href="https://tools.ietf.org/html/rfc5246#appendix-F.1.4">section F.1.4. Resuming Sessions</a> for details).</p><p>On a related topic, in 2014, Delignat-Lavaud and Bhargavan presented the <a href="https://bh.ht.vc/vhost_confusion.pdf">Virtual Host confusion</a> attack which makes it possible to redirect traffic to a different vhost. Another attack related to session resumption (from the same authors and Pironti) is the <a href="https://www.secure-resumption.com/">Triple Handshake Attack</a> which makes it possible for an active attacker to intercept and modify traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '16, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span> </br></br></p></div></div><div id="comments-container-48853" class="comments-container"></div><div id="comment-tools-48853" class="comment-tools"></div><div class="clear"></div><div id="comment-48853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

