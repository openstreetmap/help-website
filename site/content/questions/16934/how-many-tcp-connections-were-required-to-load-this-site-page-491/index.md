+++
type = "question"
title = "How many TCP connections were required to load this site - page 491"
description = '''Ch.20 - page 491 - http-google2011.pcapng  says we browsed to www,google.com. How Many TCP connections were required to load this site. My Ans. is 6 tcp connections or packets 1-6 is that correct? to verify I checked client http request: packet #4 GET / HTTP/1.1 details show: Host: www.google.com  a...'''
date = "2012-12-15T12:06:00Z"
lastmod = "2012-12-17T00:55:00Z"
weight = 16934
keywords = [ "tcp" ]
aliases = [ "/questions/16934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How many TCP connections were required to load this site - page 491](/questions/16934/how-many-tcp-connections-were-required-to-load-this-site-page-491)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16934-score" class="post-score" title="current number of votes">0</div><span id="post-16934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ch.20 - page 491 - http-google2011.pcapng says we browsed to www,<a href="http://google.com">google.com</a>. How Many TCP connections were required to load this site.</p><p>My Ans. is 6 tcp connections or packets 1-6 is that correct? to verify I checked client http request: packet #4 GET / HTTP/1.1 details show: Host: <a href="http://www.google.com">www.google.com</a> and packet 6 (server response shows) HTTP/1.1 200 OK.</p><p>I also did a right-click on any of the TCP packets, selected TCP Flow Stream to see traffic flow from client in Red and response traffic from web-Server in Blue for same above?</p><p>Let me know if I ma On the right track for Ans above for this question?<br />
Thanks Sarkis</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '12, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/0d284f502ddd68ff954a9facd4b30189?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarkis&#39;s gravatar image" /><p><span>Sarkis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarkis has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-16934" class="comments-container"></div><div id="comment-tools-16934" class="comment-tools"></div><div class="clear"></div><div id="comment-16934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16935"></span>

<div id="answer-container-16935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16935-score" class="post-score" title="current number of votes">1</div><span id="post-16935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My Ans. is 6 tcp connections or packets 1-6 is that correct?</p></blockquote><p>I don't believe that there are 6 different TCP connections in packets 1-6 (for your scenario). If you load a web page, you first get the SYN,SYN-ACK,ACK (3 packets) then the HTML code (a variable number of packets). Then the browser will parse the HTML code and fetch the 'objects' in the HTML code (CSS, images, javascript, etc.). So, your 6 TCP connections cannot be within the first 6 packets.</p><p>HINT: Look for packets with a SYN flag that 'go' to the google server (IP destination). Then count the number of those packets and you will get the number of connections, right? There are several ways to do that. As I don't want to spoil the fun of discovering that yourself, I suggest you first try it yourself and come back if you want/need the next hint ;-)</p><p>BTW: What book are you referring to?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '12, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16935" class="comments-container"><span id="16937"></span><div id="comment-16937" class="comment"><div id="post-16937-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for the Hint and Make me understand the Qn. better. working with trace: http-google2011.pcapng in page 491 top Question.</p><p>I did some research and used display filter: tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 and it found only 3 packets (1, 25, 39)with TCP session/connections to web-server IP 74.125.224.81 and 224.96.</p><p>So Ans = 3 TCP Connections/sessions with SYN set to 1 to load <a href="http://www.google.com">www.google.com</a> page Hope I am right now and understand TCP connections.</p><p>BTW, I was refering to page 491 in - The Official Wireshark Certified Network Analyst Study Guide - Second Edition Book (ISBN 978-1-893939-94-30)</p><p>Let me know how I did :) Sarkis</p></div><div id="comment-16937-info" class="comment-info"><span class="comment-age">(15 Dec '12, 14:37)</span> <span class="comment-user userinfo">Sarkis</span></div></div><span id="16939"></span><div id="comment-16939" class="comment"><div id="post-16939-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I did some research and used display filter: tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 and it found only 3 packets</p></blockquote><p>O.K. to verify that, you could use: <code>Statistics -&gt; Conversations</code><br />
</p><blockquote><p>So Ans = 3 TCP Connections/sessions with SYN set to 1 to load <a href="http://www.google.com">www.google.com</a> page</p></blockquote><p>It depends, if those connections are all for a google server. Did you check the HTTP Host header?</p></div><div id="comment-16939-info" class="comment-info"><span class="comment-age">(15 Dec '12, 15:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16951"></span><div id="comment-16951" class="comment"><div id="post-16951-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><blockquote><p>O.K. to verify that, you could use: Statistics -&gt; Conversations</p></blockquote><p>I verified Statistics &gt; Conversation | TCP tab shows TCP:3, which matches my Ans. 3.</p><blockquote><p>It depends, if those connections are all for a google server. Did you check the HTTP Host header?</p></blockquote><p>Well, I verified all three connections under the Packet Details Pane by expanding the HTTP tab with GET requests,each connx showed Host: <a href="http://www.google.com">www.google.com</a>\r\n</p><p>Hope this is what you meant. Or Could I verify same... by Right, Click (on each of those 3-Connection packets 1,25,39) and select "Follow TCP Stream" instead?<br />
</p><p>Thanks Sarkis</p><p>(yesterday)Kurt</p></div><div id="comment-16951-info" class="comment-info"><span class="comment-age">(16 Dec '12, 19:26)</span> <span class="comment-user userinfo">Sarkis</span></div></div><span id="16956"></span><div id="comment-16956" class="comment"><div id="post-16956-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Hope this is what you meant.</p></blockquote><p>Yes. You successfully verified the number of connections.</p><blockquote><p>by Right, Click (on each of those 3-Connection packets 1,25,39) and select "Follow TCP Stream" instead?</p></blockquote><p>sure. There are many ways to find the answer to that question.</p></div><div id="comment-16956-info" class="comment-info"><span class="comment-age">(17 Dec '12, 00:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16935" class="comment-tools"></div><div class="clear"></div><div id="comment-16935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

