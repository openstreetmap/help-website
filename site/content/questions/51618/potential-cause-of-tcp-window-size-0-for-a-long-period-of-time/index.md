+++
type = "question"
title = "Potential cause of TCP window size 0 for a long period of time"
description = '''In the first pcap (2016-03-17-other-Angler-EK-after-localtasteblog.com.pcap ) from page,  for the TCP session that starts with packet 209, there is a long period of about 7 seconds (from packet 371 to packet 822), the client side has TCP window size of 0.  My guess is that the client is trying to do...'''
date = "2016-04-12T20:40:00Z"
lastmod = "2016-04-13T00:34:00Z"
weight = 51618
keywords = [ "wireshark" ]
aliases = [ "/questions/51618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Potential cause of TCP window size 0 for a long period of time](/questions/51618/potential-cause-of-tcp-window-size-0-for-a-long-period-of-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the first pcap (2016-03-17-other-Angler-EK-after-localtasteblog.com.pcap ) from <a href="http://www.malware-traffic-analysis.net/2016/03/18/index.html">page</a>, for the TCP session that starts with packet 209, there is a long period of about 7 seconds (from packet 371 to packet 822), the client side has TCP window size of 0.</p><p>My guess is that the client is trying to do gunzip while receiving the server response data, but even that doesn't explain the long period of NULL tcp window on client side. Wonder what are the possible causes for it.</p><p>Thanks Jin</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 20:40</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-51618" class="comments-container"></div><div id="comment-tools-51618" class="comment-tools"></div><div class="clear"></div><div id="comment-51618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51620"></span>

<div id="answer-container-51620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51620-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The client is busy doing something that doesn't give it time to empty the window buffer. What exactly can only be guessed. Usually it's an I/O intensive operation, but it may also be some sort of calculation or the client is using all it's memory (leading to paging -&gt; I/O).</p><p>I've seen zero window situations longer than a minute caused by client resource problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51620" class="comments-container"><span id="51624"></span><div id="comment-51624" class="comment"><div id="post-51624-score" class="comment-score"></div><div class="comment-text"><p>I'll just emphasize that the client activity may be completely unrelated to the TCP session you are interested in.</p></div><div id="comment-51624-info" class="comment-info"><span class="comment-age">(13 Apr '16, 01:45)</span> sindy</div></div><span id="51653"></span><div id="comment-51653" class="comment"><div id="post-51653-score" class="comment-score"></div><div class="comment-text"><p>This traffic is from a malware running a sandbox. Given this fact, I wonder if it's because the malware, in the middle of getting HTTP response data, started another HTTP request to "hxxp://161.averoncapital.info/?x=&amp;i=i0bnwGUkE&amp;v=i6orgt&amp;s=vZ6sD0f&amp;q=qxLNvg&amp;l=wcqMSQi&amp;a=sDi&amp;b=TMnHdLxar&amp;h=t" starting at packet 378. That would explain it didn't drain all the packets from the TCP session (causing the TCP window size of 0). Thanks.</p></div><div id="comment-51653-info" class="comment-info"><span class="comment-age">(13 Apr '16, 14:48)</span> pktUser1001</div></div></div><div id="comment-tools-51620" class="comment-tools"></div><div class="clear"></div><div id="comment-51620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

