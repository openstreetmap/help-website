+++
type = "question"
title = "Measuring Bandwidth Speed"
description = '''Is it possible to get an accurate calculation of download speed using wireshark, and how is this done? I am streaming a video and each time the video changes quality (automatically) I want to see what the bandwidth speed was at that point in time. Thanks in advance. '''
date = "2014-03-28T15:47:00Z"
lastmod = "2014-03-28T21:56:00Z"
weight = 31267
keywords = [ "streaming", "bandwidth", "speed", "connection.speed" ]
aliases = [ "/questions/31267" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Measuring Bandwidth Speed](/questions/31267/measuring-bandwidth-speed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31267-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to get an accurate calculation of download speed using wireshark, and how is this done?</p><p>I am streaming a video and each time the video changes quality (automatically) I want to see what the bandwidth speed was at that point in time.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">streaming bandwidth speed connection.speed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/140fe8da9d189e180c3927c9a61dc09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimmy967&#39;s gravatar image" /><p>jimmy967<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimmy967 has no accepted answers">0%</span></p></div></div><div id="comments-container-31267" class="comments-container"></div><div id="comment-tools-31267" class="comment-tools"></div><div class="clear"></div><div id="comment-31267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31278"></span>

<div id="answer-container-31278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31278-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a trace running as you stream the video go to Statistics - IO Graph draw a graph in the outbound direction only. Change the Y-axis to bits/tick if you want to see bandwidth. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_001.jpeg" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-31278" class="comments-container"><span id="31281"></span><div id="comment-31281" class="comment"><div id="post-31281-score" class="comment-score"></div><div class="comment-text"><p>I have that done, I am also outputting when the quality change has occured and which bitrate the video has changed to.</p><p>When I am comparing the two, they do not match. Some of the reading i get are 0. why is this?</p></div><div id="comment-31281-info" class="comment-info"><span class="comment-age">(29 Mar '14, 09:29)</span> jimmy967</div></div><span id="31282"></span><div id="comment-31282" class="comment"><div id="post-31282-score" class="comment-score"></div><div class="comment-text"><p>Hard to say without more details... Which software, which protocol etc...? Can you paste a trace snippet to <a href="http://cloudshar.org">http://cloudshar.org</a> ?</p></div><div id="comment-31282-info" class="comment-info"><span class="comment-age">(29 Mar '14, 11:00)</span> mrEEde2</div></div><span id="31284"></span><div id="comment-31284" class="comment"><div id="post-31284-score" class="comment-score"></div><div class="comment-text"><p>Im using Microsoft Smooth Streaming, which is requesting the segmented video file using a HTTP GET request and TCP for delivering the video files.</p></div><div id="comment-31284-info" class="comment-info"><span class="comment-age">(29 Mar '14, 11:57)</span> jimmy967</div></div><span id="31285"></span><div id="comment-31285" class="comment"><div id="post-31285-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Some of the reading i get are 0. why is this?</p></blockquote><p>Maybe due to prefetching and buffering in the client application.</p></div><div id="comment-31285-info" class="comment-info"><span class="comment-age">(29 Mar '14, 12:15)</span> Kurt Knochner ♦</div></div><span id="31286"></span><div id="comment-31286" class="comment"><div id="post-31286-score" class="comment-score"></div><div class="comment-text"><p>So TCP protocol being used. Anything outstanding with tcp.analysis.flags filter? What is the windowsize offering of the client? What is the RTT of the connection? Where do you see the most significant delays frame.time_delay? Just a few questions to get you started ;-)</p></div><div id="comment-31286-info" class="comment-info"><span class="comment-age">(29 Mar '14, 15:44)</span> mrEEde2</div></div></div><div id="comment-tools-31278" class="comment-tools"></div><div class="clear"></div><div id="comment-31278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

