+++
type = "question"
title = "Internet disconnects when I run monitor mode"
description = '''My Internet disconnects when I run monitor mode. Why? Thank you.'''
date = "2014-05-02T06:23:00Z"
lastmod = "2014-05-02T06:51:00Z"
weight = 32391
keywords = [ "wpa2" ]
aliases = [ "/questions/32391" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Internet disconnects when I run monitor mode](/questions/32391/internet-disconnects-when-i-run-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32391-score" class="post-score" title="current number of votes">0</div><span id="post-32391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Internet disconnects when I run monitor mode. Why? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/eeca75356089d0569c63dfc514d7f19d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tttttttttttt2&#39;s gravatar image" /><p><span>tttttttttttt2</span><br />
<span class="score" title="34 reputation points">34</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tttttttttttt2 has no accepted answers">0%</span></p></div></div><div id="comments-container-32391" class="comments-container"></div><div id="comment-tools-32391" class="comment-tools"></div><div class="clear"></div><div id="comment-32391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32393"></span>

<div id="answer-container-32393" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32393-score" class="post-score" title="current number of votes">1</div><span id="post-32393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tttttttttttt2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Monitor mode is probably setting your adapter to "receive-only mode", which means that you cannot send any more requests to the internet. Remember that wireless adapters are not full duplex adapters; they can either send or receive but not both at the same time. So if you tell it to monitor (meaning: receive everything, all the time) it doesn't have "time" to send anything anymore.</p><p>This is the reason why many WiFi analysts use an additional, dedicated monitor mode adapter for the capture while using the regular WiFi adapter to communicate with the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '14, 06:33</strong> </span></p></div></div><div id="comments-container-32393" class="comments-container"><span id="32394"></span><div id="comment-32394" class="comment"><div id="post-32394-score" class="comment-score"></div><div class="comment-text"><p>I used airmon-ng and it seems it works now</p></div><div id="comment-32394-info" class="comment-info"><span class="comment-age">(02 May '14, 06:35)</span> <span class="comment-user userinfo">tttttttttttt2</span></div></div></div><div id="comment-tools-32393" class="comment-tools"></div><div class="clear"></div><div id="comment-32393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32400"></span>

<div id="answer-container-32400" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32400-score" class="post-score" title="current number of votes">0</div><span id="post-32400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You didn't provide so much information... I'm assuming you are talking about Wifi and Linux...</p><p>Possibly because you need to configure differently your WiFi card: To do monitor mode and STA mode (AP client) at the same time, you need to bind two virtual interfaces (STA and monitor) to one physical interface (your wifi card).</p><p>I suggest you to try doing this by hand, before running wireshark. You will need to use the "iw" tool in order to do this.</p><p>Gave a look here (chapter "Adding interfaces with iw") <a href="http://wireless.kernel.org/en/users/Documentation/iw">http://wireless.kernel.org/en/users/Documentation/iw</a></p><p>Andrea</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/96076cb0346f60280e33f1964e316475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrea&#39;s gravatar image" /><p><span>Andrea</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrea has no accepted answers">0%</span></p></div></div><div id="comments-container-32400" class="comments-container"></div><div id="comment-tools-32400" class="comment-tools"></div><div class="clear"></div><div id="comment-32400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

