+++
type = "question"
title = "wireshark syn ack fin get"
description = '''I&#x27;m new to wireshark and I&#x27;m trying really hard to understand. What do SYN, ACK, FIN, and GET mean in wireshark? What are they and what do they do? Thank you'''
date = "2014-11-06T16:51:00Z"
lastmod = "2014-11-07T11:48:00Z"
weight = 37630
keywords = [ "ack", "get", "fin", "syn", "wireshark" ]
aliases = [ "/questions/37630" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark syn ack fin get](/questions/37630/wireshark-syn-ack-fin-get)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37630-score" class="post-score" title="current number of votes">0</div><span id="post-37630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to wireshark and I'm trying really hard to understand. What do SYN, ACK, FIN, and GET mean in wireshark? What are they and what do they do? Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '14, 16:51</strong></p><img src="https://secure.gravatar.com/avatar/416a674ed40560b7da546111781bff02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolf1937&#39;s gravatar image" /><p><span>wolf1937</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolf1937 has no accepted answers">0%</span></p></div></div><div id="comments-container-37630" class="comments-container"></div><div id="comment-tools-37630" class="comment-tools"></div><div class="clear"></div><div id="comment-37630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37661"></span>

<div id="answer-container-37661" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37661-score" class="post-score" title="current number of votes">2</div><span id="post-37661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wolf1937 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, this is really hard to answer in a Q&amp;A but I'll give it a try.</p><p>SYN ACK and FIN are bits in the TCP Header as defined in the <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">Transmission Control Protocol</a></p><ul><li>A SYN is used to indicate the start a TCP session<br />
</li><li>A FIN is used to indicate the termination of a TCP session</li><li>The ACK bit is used to indicate that that the ACK number in the TCP header is acknowledging data</li></ul><p>The GET is a <a href="http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol">Hypertext Transfer Protocol</a> command to ask for data from an HTTP Server<br />
I'm sure there are many other 'GET' commands beside this one ...</p><p>You see, this is not really a wireshark related question but more a general TCP/IP question which opens up more questions that it actually answers.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-37661" class="comments-container"></div><div id="comment-tools-37661" class="comment-tools"></div><div class="clear"></div><div id="comment-37661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

