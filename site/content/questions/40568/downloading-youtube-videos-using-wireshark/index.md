+++
type = "question"
title = "Downloading youtube videos using Wireshark"
description = '''Hi, There is lot of tutorials how ho use wireshark to download youtube videos. (search for http GET packet, use follow TCP stream and you have the link) However it is not working. There is not a single http packet when you launch youtube video. Any hints? THX'''
date = "2015-03-15T03:58:00Z"
lastmod = "2015-03-18T11:56:00Z"
weight = 40568
keywords = [ "download", "video", "wireshark", "youtube", "using" ]
aliases = [ "/questions/40568" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading youtube videos using Wireshark](/questions/40568/downloading-youtube-videos-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40568-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>There is lot of tutorials how ho use wireshark to download youtube videos. (search for http GET packet, use follow TCP stream and you have the link)</p><p>However it is not working. There is not a single http packet when you launch youtube video.</p><p>Any hints?</p><p>THX</p></div><div id="question-tags" class="tags-container tags">download video wireshark youtube using</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '15, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/63638b9f69913ff1b4bc7cca10495ad6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mirrax&#39;s gravatar image" /><p>mirrax<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mirrax has no accepted answers">0%</span></p></div></div><div id="comments-container-40568" class="comments-container"><span id="40615"></span><div id="comment-40615" class="comment"><div id="post-40615-score" class="comment-score"></div><div class="comment-text"><p>I guess when google bought the youtube they changed the way of broadcasting? Might this be the case: <a href="https://ask.wireshark.org/questions/36967/decoding-spdy-after-protocol-switch">https://ask.wireshark.org/questions/36967/decoding-spdy-after-protocol-switch</a></p></div><div id="comment-40615-info" class="comment-info"><span class="comment-age">(16 Mar '15, 06:25)</span> mirrax</div></div><span id="40661"></span><div id="comment-40661" class="comment"><div id="post-40661-score" class="comment-score"></div><div class="comment-text"><p>Does the URL start with https?</p></div><div id="comment-40661-info" class="comment-info"><span class="comment-age">(18 Mar '15, 08:07)</span> Roland</div></div><span id="40663"></span><div id="comment-40663" class="comment"><div id="post-40663-score" class="comment-score"></div><div class="comment-text"><p>yes it does and https goes red when trying to filter</p></div><div id="comment-40663-info" class="comment-info"><span class="comment-age">(18 Mar '15, 08:34)</span> mirrax</div></div></div><div id="comment-tools-40568" class="comment-tools"></div><div class="clear"></div><div id="comment-40568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40669"></span>

<div id="answer-container-40669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40669-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the URL starts with https it means the connection is encrypted, You can't filter for https, you have to use ssl. And you have to decrypt the traffic before you can see any http request. Your best option would be to intercept the traffic with Fiddler.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-40669" class="comments-container"></div><div id="comment-tools-40669" class="comment-tools"></div><div class="clear"></div><div id="comment-40669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

