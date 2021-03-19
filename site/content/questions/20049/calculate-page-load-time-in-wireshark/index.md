+++
type = "question"
title = "Calculate page load time in Wireshark?"
description = '''Hello! I am trying to measure page load performance from a mobile smartphone. I have installed tpacketcapture on my Android phone, I then navigate to a particular website and stop capturing. I then load the .pcap files into wireshark. But how can I determine the total load time for a particular webp...'''
date = "2013-04-03T04:16:00Z"
lastmod = "2013-04-03T07:11:00Z"
weight = 20049
keywords = [ "webpage", "mobile", "speed", "http", "time" ]
aliases = [ "/questions/20049" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate page load time in Wireshark?](/questions/20049/calculate-page-load-time-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20049-score" class="post-score" title="current number of votes">0</div><span id="post-20049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I am trying to measure page load performance from a mobile smartphone. I have installed tpacketcapture on my Android phone, I then navigate to a particular website and stop capturing. I then load the .pcap files into wireshark. But how can I determine the total load time for a particular webpage from Wireshark?</p><p>Thanks, I do know much about Wireshark, any help would be much appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webpage" rel="tag" title="see questions tagged &#39;webpage&#39;">webpage</span> <span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/89c1a852827b0b4f9def05bf2bdc48a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sham123&#39;s gravatar image" /><p><span>Sham123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sham123 has no accepted answers">0%</span></p></div></div><div id="comments-container-20049" class="comments-container"></div><div id="comment-tools-20049" class="comment-tools"></div><div class="clear"></div><div id="comment-20049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20054"></span>

<div id="answer-container-20054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20054-score" class="post-score" title="current number of votes">1</div><span id="post-20054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First use this Display Filter: http.request or http.response</p><p>Then go to the first HTTP request to the host you are interested in (IP address and/or HTTP Host: header). Set a time reference (CTRL-T). Go to the last HTTP response (HTTP/1.0 xxx or HTTP/1.1 xxx). The time you see in the <strong>Time column</strong> is (more or less) the "page load time".</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20054" class="comments-container"></div><div id="comment-tools-20054" class="comment-tools"></div><div class="clear"></div><div id="comment-20054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

