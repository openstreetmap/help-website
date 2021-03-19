+++
type = "question"
title = "about calculate TCP performance"
description = '''Hello  I captured file download logs in wireshark. Now I want calculate this metrics :  TCP throughput, capacity, round-trip time,... download time, response time, time to complete task, ...  I don&#x27;t find this metrics values in wireshark. How I can calculate this metrics by my TCP logs in wireshark ...'''
date = "2016-04-08T13:37:00Z"
lastmod = "2016-04-11T07:45:00Z"
weight = 51522
keywords = [ "performance", "throughput", "homework", "tcp" ]
aliases = [ "/questions/51522" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [about calculate TCP performance](/questions/51522/about-calculate-tcp-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51522-score" class="post-score" title="current number of votes">0</div><span id="post-51522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I captured file download logs in wireshark. Now I want calculate this metrics :</p><ol><li>TCP throughput, capacity, round-trip time,...</li><li>download time, response time, time to complete task, ...</li></ol><p>I don't find this metrics values in wireshark. How I can calculate this metrics by my TCP logs in wireshark ? please help me completely , because I am beginner in wireshark.</p><p>Thank You</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-homework" rel="tag" title="see questions tagged &#39;homework&#39;">homework</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/8b36fb27165d1d8a03e434c58a629176?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abdorreza&#39;s gravatar image" /><p><span>abdorreza</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abdorreza has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Apr '16, 03:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51522" class="comments-container"><span id="51526"></span><div id="comment-51526" class="comment"><div id="post-51526-score" class="comment-score"></div><div class="comment-text"><p>HELP me please !</p></div><div id="comment-51526-info" class="comment-info"><span class="comment-age">(09 Apr '16, 00:15)</span> <span class="comment-user userinfo">abdorreza</span></div></div></div><div id="comment-tools-51522" class="comment-tools"></div><div class="clear"></div><div id="comment-51522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51554"></span>

<div id="answer-container-51554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51554-score" class="post-score" title="current number of votes">1</div><span id="post-51554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I'll try to give you some guidance. I'll assume that you are using Wireshark 2.</p><p><strong>TCP Throughput</strong></p><p>I'm not completely sure what you mean by this but if you want to know the data rate on a particular TCP connection you can do this by selecting a particular TCP stream. As an example I'll use TCP Stream 0 to an SMB file server (on TCP Port 445):</p><ul><li>Go to Menu &gt; Statistics &gt; IO Graph</li><li>Click on the + button in the bottom left of the graph window</li><li>Name the new plot TCP Stream 0 Tx</li><li>In the Display Filter field enter tcp.stream==0 &amp;&amp; tcp.dstport==445</li><li>In the Y Axis field select Bits/s</li><li>Check the box next to the name to display the result (uncheck all plots)</li><li>Click on the + button in the bottom left of the graph window</li><li>Name the new plot TCP Stream 0 Tx</li><li>In the Display Filter field enter tcp.stream==0 &amp;&amp; tcp.srcport==445</li><li>In the Y Axis field select Bits/s</li><li>Check the box next to the name to display the result</li></ul><p><strong>Capacity</strong></p><p>Not sure what you mean. You could measure apparent capacity by plotting Bits/s in the Tx and Rx directions and looking for the maximum value.</p><p><strong>Round Trip Time</strong></p><p>I think most people measure this by looking at the delta between a SYN and a SYN/ACK. You can do this by sorting the trace by tcp.stream, filtering for packets with the SYN flag set and adding the column <em>Time delta from previously displayed frame</em>. Export the Summary Line into CSV and then fiddling around with the CSV in Excel.</p><p>A much quicker way is to use the TRANSUM plugin - see <a href="http://www.tribelab.com/transum:">http://www.tribelab.com/transum:</a></p><ul><li>Start Wireshark with TRANSUM</li><li>Open the trace file</li><li>Set a display filter tcp.flags.syn==1 &amp;&amp; transum</li><li>Expand the TRANSUM RTE Data tree in the packet detail frame</li><li>Right click on APDU Response Time and Apply as Column</li><li>You should now see the SYN to SYN/ACK delays and hence the nominal RTT</li></ul><p>I'll deal with the remaining points in little later - have to get off the train I'm on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '16, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-51554" class="comments-container"><span id="51555"></span><div id="comment-51555" class="comment"><div id="post-51555-score" class="comment-score"></div><div class="comment-text"><p><strong>Download Time, Response Time, Time to Complete Task</strong></p><p>Many of the dissectors include response time values. Look out for values in headers such as <em>Time from request</em>. To study I would add the value as a column and then export to CSV, although you can probably also do a lot with the built-in graphing.</p><p>TRANSUM is also a big help here and the TRANSUM User Guide gives a lot of detail about extracting response time information from Wireshark traces.</p></div><div id="comment-51555-info" class="comment-info"><span class="comment-age">(11 Apr '16, 07:45)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-51554" class="comment-tools"></div><div class="clear"></div><div id="comment-51554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

