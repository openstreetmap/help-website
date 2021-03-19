+++
type = "question"
title = "Problem with Absolute Time"
description = '''Hello everybody! I have a &quot;little&quot; problem with Wireshark timestamps. I have one column with &quot;Time&quot;, which starts at 0.0, but I want to get the absolute time (=system time) like &quot;2013-11-05 09:39:02&quot;. I have selected &quot;Absolute date and time&quot; option for a new column and I get something like &quot;1970-01-...'''
date = "2013-11-05T00:44:00Z"
lastmod = "2013-11-05T05:40:00Z"
weight = 26673
keywords = [ "date", "epoch", "time", "absolute" ]
aliases = [ "/questions/26673" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with Absolute Time](/questions/26673/problem-with-absolute-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26673-score" class="post-score" title="current number of votes">0</div><span id="post-26673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody! I have a "little" problem with Wireshark timestamps. I have one column with "Time", which starts at 0.0, but I want to get the absolute time (=system time) like "2013-11-05 09:39:02". I have selected "Absolute date and time" option for a new column and I get something like "1970-01-01 1:00:10" -&gt; Epoch time :( How can I change this date-time?</p><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-date" rel="tag" title="see questions tagged &#39;date&#39;">date</span> <span class="post-tag tag-link-epoch" rel="tag" title="see questions tagged &#39;epoch&#39;">epoch</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-absolute" rel="tag" title="see questions tagged &#39;absolute&#39;">absolute</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '13, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/783208052cae351d09ee832cc9b96d70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoseA&#39;s gravatar image" /><p><span>JoseA</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoseA has no accepted answers">0%</span></p></div></div><div id="comments-container-26673" class="comments-container"><span id="26675"></span><div id="comment-26675" class="comment"><div id="post-26675-score" class="comment-score"></div><div class="comment-text"><p>What OS and Wireshark Version are you using? "Absolute Date and Time" should give you the absolute date and time of the packets adjusted to your time zone settings (meaning, they should be the same time your system showed when capturing the packets).</p></div><div id="comment-26675-info" class="comment-info"><span class="comment-age">(05 Nov '13, 02:47)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26673" class="comment-tools"></div><div class="clear"></div><div id="comment-26673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26679"></span>

<div id="answer-container-26679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26679-score" class="post-score" title="current number of votes">0</div><span id="post-26679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have one column with "Time", which <strong>starts at 0.0</strong><br />
I have selected "Absolute date and time" option for a new column and <strong>I get something like "1970-01-01 1:00:10"</strong></p></blockquote><p>Sounds like the date/time in your capture file is really 0.00, hence you get 1970-01-01 etc. if you display the full date time.</p><p>If you run <a href="http://www.wireshark.org/docs/man-pages/capinfos.html">capinfos</a>, what do you see in the rows 'Start time' and 'End time'?</p><blockquote><p>capinfos input.pcap</p></blockquote><pre><code>File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 65535 bytes
Number of packets:   12 k
File size:           4147 kB
Data size:           3941 kB
Capture duration:    67 seconds
Start time:         Wed Feb 02 16:37:29 2011
End time:           Wed Feb 02 16:38:36 2011</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '13, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26679" class="comments-container"></div><div id="comment-tools-26679" class="comment-tools"></div><div class="clear"></div><div id="comment-26679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

