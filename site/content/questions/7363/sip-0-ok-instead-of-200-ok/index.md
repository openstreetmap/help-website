+++
type = "question"
title = "SIP 0 OK instead of 200 OK"
description = '''Wireshark version: &quot;Version 1.4.3 (SVN Rev 35482 from /trunk-1.4)&quot; When two SIP messages in one packet (sip request INFO for fast update picture AND sip response 200 OK) Graph Analysis will show &quot;0 OK&quot; status instead of &quot;200 OK&quot;, see screenshot: http://xmages.net/i/3200261 '''
date = "2011-11-10T02:32:00Z"
lastmod = "2011-11-10T06:06:00Z"
weight = 7363
keywords = [ "200", "sip", "ok" ]
aliases = [ "/questions/7363" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP 0 OK instead of 200 OK](/questions/7363/sip-0-ok-instead-of-200-ok)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7363-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark version: "Version 1.4.3 (SVN Rev 35482 from /trunk-1.4)" When two SIP messages in one packet (sip request INFO for fast update picture AND sip response 200 OK) Graph Analysis will show "0 OK" status instead of "200 OK", see screenshot: http://xmages.net/i/3200261</p><p><img src="http://xmages.net/i/3200261" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">200 sip ok</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '11, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/ed1f596bf4fc383f8ca4527c80cc8be7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%D0%9A%D0%BE%D1%81%D1%82%D1%8F%20%D0%A2%D1%80%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2&#39;s gravatar image" /><p>Костя Трушников<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Костя Трушников has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '11, 02:33</p></div></div><div id="comments-container-7363" class="comments-container"></div><div id="comment-tools-7363" class="comment-tools"></div><div class="clear"></div><div id="comment-7363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7369"></span>

<div id="answer-container-7369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a bug. If you could file a bug report at bugs.wirshark.org including this capture file then it could be picked up by someone working the code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '11, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7369" class="comments-container"><span id="7371"></span><div id="comment-7371" class="comment"><div id="post-7371-score" class="comment-score"></div><div class="comment-text"><p>Sorry, can not connect to <strong>http://bugs.wirshark.org/</strong></p><p>can resolve by nslookup:</p><p><strong>google-public-dns-a.google.com</strong></p><p>Address: 8.8.8.8</p><p>bugs.wireshark.org</p><p>Addresses: 2607:f0d0:2001:e:1::123</p><p><strong>67.228.110.123</strong></p><p>And can do "<em>telnet 67.228.110.123 80</em>", but browsers don't show me the page</p></div><div id="comment-7371-info" class="comment-info"><span class="comment-age">(10 Nov '11, 06:15)</span> Костя Трушников</div></div><span id="7372"></span><div id="comment-7372" class="comment"><div id="post-7372-score" class="comment-score"></div><div class="comment-text"><p>Try <a href="https://bugs.wireshark.org">https</a></p></div><div id="comment-7372-info" class="comment-info"><span class="comment-age">(10 Nov '11, 06:28)</span> grahamb ♦</div></div></div><div id="comment-tools-7369" class="comment-tools"></div><div class="clear"></div><div id="comment-7369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

