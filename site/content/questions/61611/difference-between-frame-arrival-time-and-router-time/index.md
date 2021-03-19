+++
type = "question"
title = "Difference between frame arrival time and Router time"
description = '''Hi everyone, I have a doubt regarding the frame time. I was using -e frame.time field in tshark inorder to capture time stamp but i was confused about the frame time, it this the time when packet was generated? or it is the arrival time of the packet? Can we calculate the router timestamp? because f...'''
date = "2017-05-24T15:33:00Z"
lastmod = "2017-05-24T21:59:00Z"
weight = 61611
keywords = [ "timestamp", "frame", "wireshark", "tshark", "time" ]
aliases = [ "/questions/61611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between frame arrival time and Router time](/questions/61611/difference-between-frame-arrival-time-and-router-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61611-score" class="post-score" title="current number of votes">0</div><span id="post-61611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I have a doubt regarding the frame time. I was using -e frame.time field in tshark inorder to capture time stamp but i was confused about the frame time, it this the time when packet was generated? or it is the arrival time of the packet? Can we calculate the router timestamp? because for example if a packet was sent by server to router at 6:00 AM but the packet arrived to the router at 6:02 AM, i want to calculate router time(i.e.,6:01 AM time), till now i am assuming frame.time is the packet arrival time, please correct me if i was wrong. If wrong is there any filter in tshark to find the router timestamp?</p><p>Thanks in advance :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '17, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/3c5efc7cfe5ef8e05bd2f756df40afa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreenu19&#39;s gravatar image" /><p><span>sreenu19</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreenu19 has no accepted answers">0%</span></p></div></div><div id="comments-container-61611" class="comments-container"></div><div id="comment-tools-61611" class="comment-tools"></div><div class="clear"></div><div id="comment-61611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61612"></span>

<div id="answer-container-61612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61612-score" class="post-score" title="current number of votes">0</div><span id="post-61612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A quick search turns up a lot of information:</p><ul><li><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimestamps.html">Wiresahark Users Guide</a></li><li><a href="https://wiki.wireshark.org/Timestamps">Wireshark Wiki</a></li><li><a href="https://stackoverflow.com/questions/16676095/when-does-wireshark-timestamp-captured-packets">Stack Overflow</a></li><li><a href="https://www.elvidence.com.au/understanding-time-stamps-in-packet-capture-data-pcap-files/">Elvidence</a></li></ul><p>In short: packets are stamped (somewhere near) packet arrival time. If you want 'Router time' as you call it, you'll need capture and time stamping in the router itself.</p><p>BTW: A retention time of 2 minutes is ridiculously long. Microseconds is more likely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '17, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61612" class="comments-container"></div><div id="comment-tools-61612" class="comment-tools"></div><div class="clear"></div><div id="comment-61612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

