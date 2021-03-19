+++
type = "question"
title = "Difference in HTTP and HTTP/XML"
description = '''Hello, I am sending two XMLs with same HTTP headers. But for one, wireshark shows HTTP under Protocol column and for other it shows HTTP/XML. Why is it so? Is it dependent on the XML header or some other parameter defined by wireshark? I just want to know when wireshark shows HTTP(and HTTP/XML) unde...'''
date = "2015-10-16T01:56:00Z"
lastmod = "2015-10-16T03:22:00Z"
weight = 46601
keywords = [ "http" ]
aliases = [ "/questions/46601" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Difference in HTTP and HTTP/XML](/questions/46601/difference-in-http-and-httpxml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am sending two XMLs with same HTTP headers. But for one, wireshark shows HTTP under Protocol column and for other it shows HTTP/XML. Why is it so? Is it dependent on the XML header or some other parameter defined by wireshark?</p><p>I just want to know when wireshark shows HTTP(and HTTP/XML) under Protocol column?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/dd53ffcd0309998e1333522517765a31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsuser&#39;s gravatar image" /><p>wsuser<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsuser has no accepted answers">0%</span></p></div></div><div id="comments-container-46601" class="comments-container"></div><div id="comment-tools-46601" class="comment-tools"></div><div class="clear"></div><div id="comment-46601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46604"></span>

<div id="answer-container-46604" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46604-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Whether '/XML' get's appended to the protocol column or not, depends on the media type your are using in the HTTP request, like "text/xml", "application/soap+xml" and some others. You'll find a list of them in packet-xml.c in the Wireshark source code.</p><p>You say, that you are using the "same" HTTP headers. If that's the case, both frames should have "HTTP/XML" in the protocol column. Please upload a sample capture file somewhere and post the link here, so we can check.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46604" class="comments-container"></div><div id="comment-tools-46604" class="comment-tools"></div><div class="clear"></div><div id="comment-46604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

