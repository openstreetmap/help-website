+++
type = "question"
title = "Unreadable TCP stream"
description = '''When I follow a tcp stream, the data in the &quot;Follow TCP Stream&quot; dialog box is unreadable even though it is in ASCII. I don&#x27;t know how to read it, and what I can do.'''
date = "2016-12-13T12:05:00Z"
lastmod = "2016-12-13T12:11:00Z"
weight = 58050
keywords = [ "tcpstream", "stream", "tcp" ]
aliases = [ "/questions/58050" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unreadable TCP stream](/questions/58050/unreadable-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58050-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I follow a tcp stream, the data in the "Follow TCP Stream" dialog box is unreadable even though it is in ASCII. I don't know how to read it, and what I can do.</p></div><div id="question-tags" class="tags-container tags">tcpstream stream tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/a95003a0476c498118ae808723fff6f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hansvish&#39;s gravatar image" /><p>Hansvish<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hansvish has no accepted answers">0%</span></p></div></div><div id="comments-container-58050" class="comments-container"></div><div id="comment-tools-58050" class="comment-tools"></div><div class="clear"></div><div id="comment-58050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58051"></span>

<div id="answer-container-58051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58051-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just because Wireshark's display is set to ASCII, doesn't mean that the TCP stream is actually a stream of ASCII bytes. Unless the protocol that you are following communicates using ASCII readable text (like IRC, for example, or FTP requests and responses), the data will not be readable. The TCP stream might be a stream of binary bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-58051" class="comments-container"></div><div id="comment-tools-58051" class="comment-tools"></div><div class="clear"></div><div id="comment-58051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

