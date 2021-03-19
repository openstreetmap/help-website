+++
type = "question"
title = "Measuring Jitter, Twitch.tv video stream"
description = '''I want to measure the jitter in the packet stream that I receive from watching a twitch.tv stream since I receive huge performance degredation as the day progresses. Since I can&#x27;t use any of the telephony tools since it isn&#x27;t streamed over RTP is there any way to do this with a normal(TCP/UDP) packe...'''
date = "2013-06-26T08:40:00Z"
lastmod = "2013-06-26T08:57:00Z"
weight = 22364
keywords = [ "jitter", "analysis", "tcp", "wireshark" ]
aliases = [ "/questions/22364" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Measuring Jitter, Twitch.tv video stream](/questions/22364/measuring-jitter-twitchtv-video-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22364-score" class="post-score" title="current number of votes">0</div><span id="post-22364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to measure the jitter in the packet stream that I receive from watching a twitch.tv stream since I receive huge performance degredation as the day progresses. Since I can't use any of the telephony tools since it isn't streamed over RTP is there any way to do this with a normal(TCP/UDP) packet stream?</p><p>I've done some looking but all the answers seem to be for VoIP services.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/5032e6783aeacbd305a38c0bb622b329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blackdragon1400&#39;s gravatar image" /><p><span>Blackdragon1400</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blackdragon1400 has no accepted answers">0%</span></p></div></div><div id="comments-container-22364" class="comments-container"></div><div id="comment-tools-22364" class="comment-tools"></div><div class="clear"></div><div id="comment-22364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22365"></span>

<div id="answer-container-22365" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22365-score" class="post-score" title="current number of votes">2</div><span id="post-22365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Blackdragon1400 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually, by concept, you cannot calculate (real) jitter values if you look at the traffic at only one point. See my answer to a similar question for an explanation why.</p><blockquote><p><a href="http://ask.wireshark.org/questions/12837/udp-packets-jitter-and-delay">http://ask.wireshark.org/questions/12837/udp-packets-jitter-and-delay</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '13, 08:52</strong> </span></p></div></div><div id="comments-container-22365" class="comments-container"><span id="22366"></span><div id="comment-22366" class="comment"><div id="post-22366-score" class="comment-score"></div><div class="comment-text"><p>Your analysis makes sense, I'm going to give jperf a try. Thanks for the help.</p></div><div id="comment-22366-info" class="comment-info"><span class="comment-age">(26 Jun '13, 08:57)</span> <span class="comment-user userinfo">Blackdragon1400</span></div></div></div><div id="comment-tools-22365" class="comment-tools"></div><div class="clear"></div><div id="comment-22365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

