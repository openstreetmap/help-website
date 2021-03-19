+++
type = "question"
title = "how works TCP Flow"
description = '''Hi  I&#x27;m trying to find a performance issue with wireshark I have a capture where the start request (a HTTP POST request) is the packet n° 14481  This request is acked in the packet 423239 66.05 seconds later These start and ack packets have the TCP Stream n° : 106 Between i have thousan of mysql req...'''
date = "2016-01-28T01:27:00Z"
lastmod = "2016-01-28T02:58:00Z"
weight = 49575
keywords = [ "flow", "tcp", "wireshark" ]
aliases = [ "/questions/49575" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how works TCP Flow](/questions/49575/how-works-tcp-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49575-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm trying to find a performance issue with wireshark</p><p>I have a capture where the start request (a HTTP POST request) is the packet n° 14481 This request is acked in the packet 423239 66.05 seconds later These start and ack packets have the TCP Stream n° : 106</p><p>Between i have thousan of mysql requests but in the TCP Stream n° : 2</p><p>My question is :</p><p>As the TCP Stream of the mysql request (2) is less than the TCP Stream of the HTTP requests (106), can i suppose that they are not part of my HTTP request ?</p><p>And if yes how can i filter in order or only have the ones that where executed between my HTTP request ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">flow tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '16, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/928a31ed339a11393f9fc35098c61176?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jojoRoro40&#39;s gravatar image" /><p>jojoRoro40<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jojoRoro40 has no accepted answers">0%</span></p></div></div><div id="comments-container-49575" class="comments-container"><span id="49585"></span><div id="comment-49585" class="comment"><div id="post-49585-score" class="comment-score"></div><div class="comment-text"><p>I am not sure, if I understand your question correct. But maybe this two articles can help you a little bit:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p><p><a href="https://blog.packet-foo.com/2015/05/port-numbers-reused/">https://blog.packet-foo.com/2015/05/port-numbers-reused/</a></p></div><div id="comment-49585-info" class="comment-info"><span class="comment-age">(28 Jan '16, 03:16)</span> Christian_R</div></div></div><div id="comment-tools-49575" class="comment-tools"></div><div class="clear"></div><div id="comment-49575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49582"></span>

<div id="answer-container-49582" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49582-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ul><li><p>If tcp is used to transport http, both the http request and the response to it always use exactly one tcp session. But the same tcp session may be used by several request/response pairs - more than that, it is almost always the case.</p></li><li><p><code>tcp.stream</code> is not a field you could find in the packet contents. It is a "virtual" or "pseudo" field, i.e. an attribute of a frame which Wireshark generates, in order to make packet analysis easier, by aggregating several real packet fields together. It is the order number of the beginning of that particular tcp session in that particular capture; if you would modify a capture file by removing all packets matching display filter <code>tcp.stream == N</code> from it, stream N+1 from the original file would become stream N in the modified file.</p></li></ul><p>To finish the answer, I need you to explain more precisely what you had in mind when writing</p><blockquote><p>how can i filter in order or only have the ones that where executed between my HTTP request ?</p></blockquote><p>If you had in mind "I want to see all packets, no matter to what tcp session they belong, which have been captured between the http request in tcp stream 106 and the response to it", then you can use a display filter <code>frame.number &gt;= N and frame.number &lt;= M</code>, where N would be the frame number (the leftmost column in default layout of the packet list pane) of the http request, and M would be the frame number of the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '16, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49582" class="comments-container"></div><div id="comment-tools-49582" class="comment-tools"></div><div class="clear"></div><div id="comment-49582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

