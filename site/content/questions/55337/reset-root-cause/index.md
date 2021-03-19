+++
type = "question"
title = "Reset root cause"
description = '''Hi, Server A = 192.168.5.113 ( node no 3 under load balancer), Virtual IP = 192.168.5.18 Server B = 10.12.229.56  Based on below screenshot we can see that both server said the Reset from other END. How to know the root cause for Reset below. From which side the Reset coming ? Capture at SERVER A  C...'''
date = "2016-09-05T18:27:00Z"
lastmod = "2016-09-05T23:21:00Z"
weight = 55337
keywords = [ "reset" ]
aliases = [ "/questions/55337" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reset root cause](/questions/55337/reset-root-cause)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55337-score" class="post-score" title="current number of votes">0</div><span id="post-55337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Server A = 192.168.5.113 ( node no 3 under load balancer), Virtual IP = 192.168.5.18 Server B = 10.12.229.56<br />
</p><p>Based on below screenshot we can see that both server said the Reset from other END. How to know the root cause for Reset below. From which side the Reset coming ?</p><p>Capture at SERVER A <img src="https://osqa-ask.wireshark.org/upfiles/MK.jpg" alt="alt text" /></p><p>Capture at SERVER B</p><p><img src="https://osqa-ask.wireshark.org/upfiles/AM.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '16, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/b8cbaa9ee7d5bf40e4c8f703e3197880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suarez123&#39;s gravatar image" /><p><span>suarez123</span><br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suarez123 has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-55337" class="comments-container"><span id="55339"></span><div id="comment-55339" class="comment"><div id="post-55339-score" class="comment-score"></div><div class="comment-text"><p>To me it looks like the load balancer is inserting a RST both ways.</p></div><div id="comment-55339-info" class="comment-info"><span class="comment-age">(05 Sep '16, 23:21)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-55337" class="comment-tools"></div><div class="clear"></div><div id="comment-55337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

