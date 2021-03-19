+++
type = "question"
title = "RST message for program request"
description = '''Hi, I;m Using program where it Requests data from a remote server and it gives data. (see Link)  I have written a Custom Program to above remote server where it sends request but doesn&#x27;t get data . It send a RST and drops the session.  (see Link) Please let me know what is the issue (WireShark Logs ...'''
date = "2013-03-05T03:46:00Z"
lastmod = "2013-03-05T11:10:00Z"
weight = 19145
keywords = [ "rst", "dropping", "session", "packet", "wireshark" ]
aliases = [ "/questions/19145" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RST message for program request](/questions/19145/rst-message-for-program-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19145-score" class="post-score" title="current number of votes">0</div><span id="post-19145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I;m Using program where it Requests data from a remote server and it gives data. <a href="http://cloudshark.org/captures/74105fe6138c?filter=ip.addr%3D%3D211.154.136.219">(see Link)</a></p><p>I have written a Custom Program to above remote server where it sends request but doesn't get data . It send a RST and drops the session. <a href="http://cloudshark.org/captures/f5bef0aeba06?filter=ip.addr%3D%3D211.154.136.219">(see Link)</a></p><p>Please let me know what is the issue (WireShark Logs are attached in the Links)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-dropping" rel="tag" title="see questions tagged &#39;dropping&#39;">dropping</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '13, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/47050f603ff32c64a34a83fe723500b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irsh&#39;s gravatar image" /><p><span>Irsh</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irsh has no accepted answers">0%</span></p></div></div><div id="comments-container-19145" class="comments-container"></div><div id="comment-tools-19145" class="comment-tools"></div><div class="clear"></div><div id="comment-19145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19147"></span>

<div id="answer-container-19147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19147-score" class="post-score" title="current number of votes">0</div><span id="post-19147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your second (faulty) capture the client sends one packet of data to the server and the server sends a FIN at frame 438 approx 7 seconds after the client data indicating it's closing the connection. All the client can do now is close the connection from its side and open a new one. The client attempting to send further data after the FIN (frame frame 440) will cause the server to send the RST as it's not interested.</p><p>Looking at your good capture the client data sent to the server seems to be a little different from the bad capture, and the client sends two items of data (frames 775, 789) before the server responds with data (frame 790).</p><p>So, your client stack needs to behave properly on receipt of a FIN and the client application needs to send the correct data to the server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19147" class="comments-container"></div><div id="comment-tools-19147" class="comment-tools"></div><div class="clear"></div><div id="comment-19147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19164"></span>

<div id="answer-container-19164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19164-score" class="post-score" title="current number of votes">0</div><span id="post-19164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Please let me know what is the issue</p></blockquote><p>If I compare the two connections I see this:</p><p>In W2.pcapng (session that gets closed quickly):</p><ul><li>the client sends data in frame 314</li><li>the server ACKs that data</li><li>Then there is <strong>no communication</strong> for 6.9 seconds <strong>from the client</strong></li><li>The server closes the connection with a FIN</li><li>The rest is 'standard' TCP connection tear down</li></ul><p>As there is no such (large) time gap in W1.pcapng, I guess the server application closes the connection as it runs into an application specific timeout. Please check, why your client application stops sending data after the first chunk of data.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19164" class="comments-container"></div><div id="comment-tools-19164" class="comment-tools"></div><div class="clear"></div><div id="comment-19164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

