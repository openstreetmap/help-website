+++
type = "question"
title = "Bad SSL response from server"
description = '''Hi,  I would like to ask to my issue. I cannot decode the SSL packet from server. I can see that Client sent Client Hello packet. Server sent &quot;some&quot; SSL response. After this response SSL handshake not continue. So I don&#x27;t know where could be issue. here&#x27;s my pcap:  https://www.cloudshark.org/capture...'''
date = "2015-05-20T02:01:00Z"
lastmod = "2015-05-20T03:29:00Z"
weight = 42571
keywords = [ "ssl", "handshake", "ssl_decrypt" ]
aliases = [ "/questions/42571" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bad SSL response from server](/questions/42571/bad-ssl-response-from-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42571-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to ask to my issue. I cannot decode the SSL packet from server. I can see that Client sent Client Hello packet. Server sent "some" SSL response. After this response SSL handshake not continue. So I don't know where could be issue. here's my pcap:</p><blockquote><p><a href="https://www.cloudshark.org/captures/7abdbca762de">https://www.cloudshark.org/captures/7abdbca762de</a></p></blockquote><p>Thanks</p><p>Patrick</p></div><div id="question-tags" class="tags-container tags">ssl handshake ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/7b58cd002998f5e289c00b47f8c00c10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patrik%20Kristel&#39;s gravatar image" /><p>Patrik Kristel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patrik Kristel has no accepted answers">0%</span></p></div></div><div id="comments-container-42571" class="comments-container"></div><div id="comment-tools-42571" class="comment-tools"></div><div class="clear"></div><div id="comment-42571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42572"></span>

<div id="answer-container-42572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42572-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some data is missing from the capture. In the 5 Second gap between frames 5 and 6 the server has sent some data that isn't in the capture. The clue is in the message "TCP previous segment not captured" message in frame 6.</p><p>Looking at the sequence number for frame 6, it's 2725, that means 2724 bytes of data are missing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '15, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42572" class="comments-container"><span id="42573"></span><div id="comment-42573" class="comment"><div id="post-42573-score" class="comment-score"></div><div class="comment-text"><p>thanks for answer, but is there any reason that some data in capture missing?</p></div><div id="comment-42573-info" class="comment-info"><span class="comment-age">(20 May '15, 03:45)</span> Patrik Kristel</div></div><span id="42575"></span><div id="comment-42575" class="comment"><div id="post-42575-score" class="comment-score"></div><div class="comment-text"><p>Where did you take this capture? Span Port, Client ...</p></div><div id="comment-42575-info" class="comment-info"><span class="comment-age">(20 May '15, 03:53)</span> Christian_R</div></div></div><div id="comment-tools-42572" class="comment-tools"></div><div class="clear"></div><div id="comment-42572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

