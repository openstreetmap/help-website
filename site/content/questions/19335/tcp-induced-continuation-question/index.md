+++
type = "question"
title = "TCP- induced “Continuation” question."
description = '''My homework is asking this question: Are there any HTTP status lines in the transmitted data associated with a TCP- induced “Continuation”? The text previous to the question states: In the packet-listing window, you should see your HTTP GET message, followed by a multiple-packet response to your HTT...'''
date = "2013-03-09T18:48:00Z"
lastmod = "2013-03-09T21:08:00Z"
weight = 19335
keywords = [ "continuation", "tcp" ]
aliases = [ "/questions/19335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP- induced “Continuation” question.](/questions/19335/tcp-induced-continuation-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19335-score" class="post-score" title="current number of votes">0</div><span id="post-19335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My homework is asking this question: Are there any HTTP status lines in the transmitted data associated with a TCP- induced “Continuation”? The text previous to the question states: In the packet-listing window, you should see your HTTP GET message, followed by a multiple-packet response to your HTTP GET request. This multiple-packet response deserves a bit of explanation. Recall from Section 2.2 (see Figure 2.9 in the text) that the HTTP response message consists of a status line, followed by header lines, followed by a blank line, followed by the entity body. In the case of our HTTP GET, the entity body in the response is the entire requested HTML file. In our case here, the HTML file is rather long, and at 4500 bytes is too large to fit in one TCP packet. The single HTTP response message is thus broken into several pieces by TCP, with each piece being contained within a separate TCP segment (see Figure 1.24 in the text). Each TCP segment is recorded as a separate packet by Wireshark, and the fact that the single HTTP response was fragmented across multiple TCP packets is indicated by the “Continuation” phrase displayed by Wireshark. We stress here that there is no “Continuation” message in HTTP!</p><p>I do not see any thing that says "Continuation" displayed by WireShark in any of the status lines for the TCP traffic but there must be something that Im missing. Will I see the word Continuation or can the Continuation look like something else? I see my GET request and then TCP traffic and finally the 200 OK response from the server. Is the TCP traffic the Continuation? Here is a CloudShark link to the data: <a href="http://www.cloudshark.org/captures/dd413b6a1b45?filter=tcp">http://www.cloudshark.org/captures/dd413b6a1b45?filter=tcp</a></p><p>So #s 36 - 42 is what Im looking at. First 36 is my GET request, then 37 - 41 is TCP traffic and finaly 42 is the server saying 200 OK telling me that the request was fulfilled. Is the 37 - 41 the Continuation?</p><p>Thanks for the help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-continuation" rel="tag" title="see questions tagged &#39;continuation&#39;">continuation</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '13, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/ac2dcd40c310eb0cb72e5d599bcec1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SydneyLebowitz&#39;s gravatar image" /><p><span>SydneyLebowitz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SydneyLebowitz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '13, 18:59</strong> </span></p></div></div><div id="comments-container-19335" class="comments-container"></div><div id="comment-tools-19335" class="comment-tools"></div><div class="clear"></div><div id="comment-19335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19336"></span>

<div id="answer-container-19336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19336-score" class="post-score" title="current number of votes">0</div><span id="post-19336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Select any TCP packet. In the Packet Details pane, right-click on the "Transmission Control Protocol" summary line, select "Protocol Preferences" and uncheck "Allow subdissector to reassemble TCP streams."</p><p>You can do the same thing by going to Edit &gt; Preferences &gt; Protocols &gt; TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19336" class="comments-container"></div><div id="comment-tools-19336" class="comment-tools"></div><div class="clear"></div><div id="comment-19336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

