+++
type = "question"
title = "Question about mean jitter"
description = '''I am trying to learn about how are the jitter and mean jitter calculated. I downloaded an example pcap file from http://wiki.wireshark.org/SampleCaptures#head-6f6128a524888c86ee322aa7cbf0d7b7a8fdf353 named aaa.pcap. Actually, this pcap file was used as the example on wiki.wireshark RTP_statistics se...'''
date = "2015-02-03T09:14:00Z"
lastmod = "2015-02-09T15:32:00Z"
weight = 39611
keywords = [ "jitter", "rtp" ]
aliases = [ "/questions/39611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question about mean jitter](/questions/39611/question-about-mean-jitter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to learn about how are the jitter and mean jitter calculated. I downloaded an example pcap file from <a href="http://wiki.wireshark.org/SampleCaptures#head-6f6128a524888c86ee322aa7cbf0d7b7a8fdf353">http://wiki.wireshark.org/SampleCaptures#head-6f6128a524888c86ee322aa7cbf0d7b7a8fdf353</a> named aaa.pcap. Actually, this pcap file was used as the example on wiki.wireshark RTP_statistics section to calculate the jitter. When I used the RTP Stream Analysis, it will show some information about every RTP packet including jitter. My question is: Max jitter is 7.80ms, why the Mean jitter is 18.02ms? How does Mean jitter = 18.02ms come from?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/aaa-pcap.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">jitter rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '15, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/4215c52a96b1064a8b64a3eb5724088c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Antibes&#39;s gravatar image" /><p>Antibes<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Antibes has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 Feb '15, 09:21</p></div></div><div id="comments-container-39611" class="comments-container"></div><div id="comment-tools-39611" class="comment-tools"></div><div class="clear"></div><div id="comment-39611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39723"></span>

<div id="answer-container-39723" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39723-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is: Max jitter is 7.80ms, why the Mean jitter is 18.02ms?</p></blockquote><p>to my understanding, the <strong>mean</strong> value should not be larger than the <strong>max</strong> value. Looks like a bug to me. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39723" class="comments-container"></div><div id="comment-tools-39723" class="comment-tools"></div><div class="clear"></div><div id="comment-39723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

