+++
type = "question"
title = "iperf and 64K window size"
description = '''I did an iperf test across my 200Mb WAN line... I got 50Mb/s Next I did another iperf test, same source, destination but added -w 64KB... I got 140Mb/s The obvious answer is that the calculated window size was larger in the second test right? But it wasn&#x27;t. I capture both iperf runs and both had 64K...'''
date = "2014-04-29T13:51:00Z"
lastmod = "2014-05-01T16:13:00Z"
weight = 32297
keywords = [ "iperf", "tcpwindowsize" ]
aliases = [ "/questions/32297" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [iperf and 64K window size](/questions/32297/iperf-and-64k-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32297-score" class="post-score" title="current number of votes">0</div><span id="post-32297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did an iperf test across my 200Mb WAN line... I got 50Mb/s</p><p>Next I did another iperf test, same source, destination but added -w 64KB... I got 140Mb/s</p><p>The obvious answer is that the calculated window size was larger in the second test right? But it wasn't. I capture both iperf runs and both had 64K CALCULATED window size. How is this possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iperf" rel="tag" title="see questions tagged &#39;iperf&#39;">iperf</span> <span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/4236f30a4fa840a16a367eb6364c022b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uncleboarder&#39;s gravatar image" /><p><span>uncleboarder</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uncleboarder has no accepted answers">0%</span></p></div></div><div id="comments-container-32297" class="comments-container"><span id="32359"></span><div id="comment-32359" class="comment"><div id="post-32359-score" class="comment-score"></div><div class="comment-text"><p>Window size is 64K (both directions) for ~99% of the traffic... both captures.</p><p><strong>Packet length (iperf 1):</strong><br />
40-79 23%<br />
1280-2559 63% (max packet length captured is 1514)<br />
(all other lengths are less than 1%)</p><p>99.99% of capture is 64K calculated WinSize<br />
20,351 total packets</p><p><strong>Packet length (iperf 2):</strong><br />
40-79 27%<br />
1280-2559 69% (max packet length captured is 1514)<br />
(all other lenghts are less than 1%)</p><p>98.7% of capture is 64K calculated WinSize (only 30 packets are less than 30K)<br />
48,810 total packets</p><p>Suggestions?</p></div><div id="comment-32359-info" class="comment-info"><span class="comment-age">(01 May '14, 10:34)</span> <span class="comment-user userinfo">uncleboarder</span></div></div><span id="32366"></span><div id="comment-32366" class="comment"><div id="post-32366-score" class="comment-score"></div><div class="comment-text"><p>I guess the capture files are too large to upload them. If so, can you please add the following screenshots for both capture files?</p><blockquote><p>Statistics -&gt; TCP StreamGraph -&gt; Round Trip Time Graph<br />
Statistics -&gt; TCP StreamGraph -&gt; Window Scaling Graph<br />
Statistics -&gt; TCP StreamGraph -&gt; Throughput Graph<br />
Statistics -&gt; TCP StreamGraph -&gt; Time-Sequence Graph (tcptrace)<br />
</p></blockquote><p>Please consider, that these graphs will report different things if you calculate them while a frame from A -&gt; B (e.g. SYN) was selected versus B -&gt; A (e.g. SYN-ACK)!</p></div><div id="comment-32366-info" class="comment-info"><span class="comment-age">(01 May '14, 16:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32297" class="comment-tools"></div><div class="clear"></div><div id="comment-32297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32298"></span>

<div id="answer-container-32298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32298-score" class="post-score" title="current number of votes">0</div><span id="post-32298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a lot more to TCP throughput than Window Size - it's not a magic bullet to look at the calculated Window size.</p><p>Check packet sizes, delta times between packets, delay on the sender side to prepare the next batch, serialization delay, buffering delay etc etc. If one throughput is less than the other find out why by looking at the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '14, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-32298" class="comments-container"><span id="32299"></span><div id="comment-32299" class="comment"><div id="post-32299-score" class="comment-score"></div><div class="comment-text"><p>Packet sizes and delta times are visually similar but I don't know how to make a direct comparison and identify why one is 3 times faster than the other.</p><p>This is repeatable. The source, destination, and path are unchanged. The only change I make is using the iperf window size setting (which apparently doesn't change the window size).</p><p>What is the iperf setting changing that makes this difference?</p><p>I can see one is slower than the other by looking at the capture, but I don't know how to identify why. I've been researching and reading and the best culprit seemed to be window size. But now I'm doubting that answer. Need help in how to identify the cause of the througput difference.</p></div><div id="comment-32299-info" class="comment-info"><span class="comment-age">(29 Apr '14, 14:15)</span> <span class="comment-user userinfo">uncleboarder</span></div></div><span id="32300"></span><div id="comment-32300" class="comment"><div id="post-32300-score" class="comment-score"></div><div class="comment-text"><p>The iperf window size setting does not affect the TCP window size last time I checked, because that is still something the TCP stack of the OS controls. What the setting does is send more or less blocks of data in one go to the TCP stack for transmission, so it's an application level setting.</p><p>If you put give the TCP stack more data to transfer it can push it out as fast as possible, without saying less often to the application "ok, this batch was done, give me more", which causes delay.</p></div><div id="comment-32300-info" class="comment-info"><span class="comment-age">(29 Apr '14, 14:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="32301"></span><div id="comment-32301" class="comment"><div id="post-32301-score" class="comment-score"></div><div class="comment-text"><p>That would suggest that the application is the bottleneck in this particular test. However the same iperf settings on the same iperf server can deliver around 600Mb/s on my LAN so this doesn't make sense to me.</p><p>My goal is to determine why I can't fill my 200Mb (5ms) pipe. At that spec, 200Mb/5ms, I can only have about 100Mb in flight with a 64K window size. So... it's difficult to NOT associate window size since that's a break point for the math. I used iperf to "prove" that it was not a window size problem but perhaps I haven't done that.</p><p>I know iperf can deliver a lot faster... around 600Mb/s on my LAN. So how do I determine why a single transfer across my WAN is stuck around 100Mb?</p><p>I need a suggestion.</p></div><div id="comment-32301-info" class="comment-info"><span class="comment-age">(29 Apr '14, 14:53)</span> <span class="comment-user userinfo">uncleboarder</span></div></div><span id="32302"></span><div id="comment-32302" class="comment"><div id="post-32302-score" class="comment-score">1</div><div class="comment-text"><p>Uhm, if it was my test I would read the trace file to see where the delays are...</p></div><div id="comment-32302-info" class="comment-info"><span class="comment-age">(29 Apr '14, 14:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="32338"></span><div id="comment-32338" class="comment"><div id="post-32338-score" class="comment-score"></div><div class="comment-text"><p>It seems you have a lot more experience than I do and you think that reading the trace to find delays is an obvious answer. For an average Wireshark user, it is not.<br />
</p><p>I'm posting here because I've already read/reasearched to my ability level and need help. I can read through the trace. I know delta times look very similar but I don't know how to do a 100% comparison so have I missed something? I don't know. I can see that packet size distribution is very similar by visually scanning the trace files. And I don't know how to check the delays that you mentioned. (batch prep, serialization, buffering).</p><p>Can I get a little more help than "read the trace file".</p></div><div id="comment-32338-info" class="comment-info"><span class="comment-age">(01 May '14, 05:40)</span> <span class="comment-user userinfo">uncleboarder</span></div></div><span id="32340"></span><div id="comment-32340" class="comment not_top_scorer"><div id="post-32340-score" class="comment-score"></div><div class="comment-text"><p>okay, two options:</p><ol><li><p>try doing ftp transfers instead of iperf and measure throughput using Wireshark, e.g. by leveraging the conversation statistics/TCP tab. Ftp sends all data in one go, so its usually good for testing throughput</p></li><li><p>put your iperf captures up at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> so I/we can take a look and give you more detailed feedback.</p></li></ol></div><div id="comment-32340-info" class="comment-info"><span class="comment-age">(01 May '14, 06:29)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-32298" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32349"></span>

<div id="answer-container-32349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32349-score" class="post-score" title="current number of votes">0</div><span id="post-32349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and both had 64K CALCULATED window size. How is this possible?</p></blockquote><p>There is a Window size for <strong>both directions</strong> of the connection. Are you sure you were checking the correct window size? Additionally I have noticed that iperf options sometimes behave differently than one might expect (depends on the OS).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '14, 07:30</strong> </span></p></div></div><div id="comments-container-32349" class="comments-container"></div><div id="comment-tools-32349" class="comment-tools"></div><div class="clear"></div><div id="comment-32349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

