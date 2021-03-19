+++
type = "question"
title = "Time sequence stevens graph question"
description = '''I&#x27;m using Wireshark 1.6.7 and 1.5.0, and I noticed an anomaly. After loading a capture file that consists of 300K+ packets, I use the Expert Info feature to check the file for retransmits, duplicate ACK&#x27;s and other warnings or errors within a TCP stream. It shows no errors or warnings. Then, I use t...'''
date = "2012-05-15T13:49:00Z"
lastmod = "2012-05-16T06:57:00Z"
weight = 11001
keywords = [ "graph", "expert-info", "sequence", "time", "stevens" ]
aliases = [ "/questions/11001" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Time sequence stevens graph question](/questions/11001/time-sequence-stevens-graph-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11001-score" class="post-score" title="current number of votes">0</div><span id="post-11001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark 1.6.7 and 1.5.0, and I noticed an anomaly. After loading a capture file that consists of 300K+ packets, I use the Expert Info feature to check the file for retransmits, duplicate ACK's and other warnings or errors within a TCP stream. It shows no errors or warnings. Then, I use the TCP Stream Time sequence (Stevens<sup>♔</sup>) feature to generate a time sequence diagram. On my first captured file, I see a nice straight line starting from lower left and moving to upper right corner. Everything looks good. In my 2nd, 3rd, 4th files, I see a straight line at the top of the graph with NO sequence number scale on the left side of graph.</p><p>Now here is the anomaly: If I skip to the bottom of the file or wait for some unknown period of time and then regenerate the time sequence (Stevens<sup>♔</sup>) graph for the same file, it actually turns out to be a line starting from the lower left and moving upward to the upper right...like I would expect it to be. Further, the Expert Info for these shows no errors and no warnings. Any ideas?</p><hr /><p>♔ <sub>Time-Sequence Graph (Stevens): a graph of TCP sequence numbers versus time. This helps us see if traffic is moving along without interruption, packet loss or long delays. <em>Reference: TCP/IP Illustrated by W. Richard Stevens</em><br />
<a href="http://sharkfest.wireshark.org/sharkfest.09/bu-9-tompkins-gearbit-wireshark_charts_&amp;_io_graphs-sharkfest09.pdf">http://sharkfest.wireshark.org/sharkfest.09/bu-9-tompkins-gearbit-wireshark_charts_&amp;_io_graphs-sharkfest09.pdf</a></sub></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-stevens" rel="tag" title="see questions tagged &#39;stevens&#39;">stevens</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/60889bf3601ab32f6b8477e8e68fa1f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rascheri&#39;s gravatar image" /><p><span>rascheri</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rascheri has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '12, 15:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11001" class="comments-container"><span id="11003"></span><div id="comment-11003" class="comment"><div id="post-11003-score" class="comment-score"></div><div class="comment-text"><p>It seems that I can repeat this every time I open the file. I seem to have to wait for some unknown period of time. Sometimes when I jump to the bottom using &lt;ctrl&gt;&lt;home&gt; and regenerate the time sequence (stevens) diagram it display the graph correctly. Other times I have to wait longer and retry. Oh, I'm doing all of this on Windows XP SP3.</p></div><div id="comment-11003-info" class="comment-info"><span class="comment-age">(15 May '12, 15:00)</span> <span class="comment-user userinfo">rascheri</span></div></div><span id="11008"></span><div id="comment-11008" class="comment"><div id="post-11008-score" class="comment-score"></div><div class="comment-text"><p>This issue is resolved. Thanks for the helpful suggestions.</p><p>Just remember, when you are using the TCP Stream Time Sequence Graphing features. You should first select a packet that is coming from the client to the server. If you pick the packet which carries only the ACK then you will only see a straight line as indicated in the previous messages.</p><p>Thanks everyone. Rick</p></div><div id="comment-11008-info" class="comment-info"><span class="comment-age">(15 May '12, 16:13)</span> <span class="comment-user userinfo">rascheri</span></div></div><span id="11020"></span><div id="comment-11020" class="comment"><div id="post-11020-score" class="comment-score"></div><div class="comment-text"><p>Rick, good to hear your feedback that the issue has been resolved. Could you accept the answer that made you resolve your issue by clicking on the check-mark next to it? That is the way this site works best (see the FAQ). I also converted your answer to a comment, as it was a comment and not a new answer to your question :-)</p></div><div id="comment-11020-info" class="comment-info"><span class="comment-age">(15 May '12, 23:28)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="11047"></span><div id="comment-11047" class="comment"><div id="post-11047-score" class="comment-score"></div><div class="comment-text"><p>SYN-BIT, I did click on the thumbs up icon after I verified what Jasper reported was in fact true. He was the first to respond with the correct answer. I also just awarded points to him as well. Is there anything else I need to do?</p></div><div id="comment-11047-info" class="comment-info"><span class="comment-age">(16 May '12, 06:51)</span> <span class="comment-user userinfo">rascheri</span></div></div><span id="11048"></span><div id="comment-11048" class="comment"><div id="post-11048-score" class="comment-score">1</div><div class="comment-text"><p>If you want to accept an answer you can "activate" the round checkmark icon just below the thumbs up/down icons ;-)</p></div><div id="comment-11048-info" class="comment-info"><span class="comment-age">(16 May '12, 06:57)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-11001" class="comment-tools"></div><div class="clear"></div><div id="comment-11001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11004"></span>

<div id="answer-container-11004" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11004-score" class="post-score" title="current number of votes">5</div><span id="post-11004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rascheri has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to keep in mind that the TCP Stream graphs are NOT bidirectional, so depending on what packet you had selected when opening a graph you'll see either the direction from client to server or vice versa. You can tell by looking at the window caption; it will always tell you from what IP to what IP the transfer is drawn.</p><p>If you have a communication (like an FTP download) where one node only acknowledges and never sends anything else you'll see the horizontal line you mentioned.</p><p>So try to select a packet WITH content (easy to find, just don't click at those 60 byte packets), and you'll see you always get a line that is not horizontal. In your case it it probably just a case of luck which direction the packets are full and which direction they're just ACK'ing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11004" class="comments-container"></div><div id="comment-tools-11004" class="comment-tools"></div><div class="clear"></div><div id="comment-11004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

