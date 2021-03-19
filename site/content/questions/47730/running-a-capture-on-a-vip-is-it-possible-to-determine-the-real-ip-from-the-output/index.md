+++
type = "question"
title = "Running a capture on a VIP, is it possible to determine the real IP from the output?"
description = '''I ran a capture for a customer who has a server farm sitting behind an F5 load balancer. Based on my position in the network, I captured all traffic to/from the VIP but am unable to find a way to see the actual IP of the server in the farm that sent any particular packet. I&#x27;m not sure it&#x27;s possible ...'''
date = "2015-11-18T14:27:00Z"
lastmod = "2015-11-19T03:55:00Z"
weight = 47730
keywords = [ "vip", "f5", "load-balancer503" ]
aliases = [ "/questions/47730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Running a capture on a VIP, is it possible to determine the real IP from the output?](/questions/47730/running-a-capture-on-a-vip-is-it-possible-to-determine-the-real-ip-from-the-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47730-score" class="post-score" title="current number of votes">0</div><span id="post-47730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran a capture for a customer who has a server farm sitting behind an F5 load balancer. Based on my position in the network, I captured all traffic to/from the VIP but am unable to find a way to see the actual IP of the server in the farm that sent any particular packet. I'm not sure it's possible from a capture, but we did see a lot of TCP window full messages from the VIP, so I'm trying to see if it is the F5 sending the window full message, or if there's a way to see which server is sending it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vip" rel="tag" title="see questions tagged &#39;vip&#39;">vip</span> <span class="post-tag tag-link-f5" rel="tag" title="see questions tagged &#39;f5&#39;">f5</span> <span class="post-tag tag-link-load-balancer503" rel="tag" title="see questions tagged &#39;load-balancer503&#39;">load-balancer503</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/0259ac537ba567c6247b356765efa8e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fnngswk&#39;s gravatar image" /><p><span>fnngswk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fnngswk has no accepted answers">0%</span></p></div></div><div id="comments-container-47730" class="comments-container"></div><div id="comment-tools-47730" class="comment-tools"></div><div class="clear"></div><div id="comment-47730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47745"></span>

<div id="answer-container-47745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47745-score" class="post-score" title="current number of votes">0</div><span id="post-47745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>or if there's a way to see which server is sending it.</p></blockquote><p>it depends :-)</p><p>In general it is hard to identify a node behind a loadbalancer, especially if the loadbalancer terminates the connection, meaning it is using a TCP proxy and/or any other proxy (HTTP, SMTP, etc.). But, sometimes even then the real servers reveal themselves by using their name in HTTP headers or individual timestamps in the protocols (combined with a time glitch on the real servers) etc.</p><p>In your case, it depends on the F5 configuration. If it's 'pure' TCP balancing, without any advanced TCP features enabled on the loadbalancer it's going to be hard to tell which node it is. The best you can do is to caputre on the F5 itself on the external and internal interface in parallel. By comparing the two capture files, you should be able to match an external connection to an internal one.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '15, 03:57</strong> </span></p></div></div><div id="comments-container-47745" class="comments-container"></div><div id="comment-tools-47745" class="comment-tools"></div><div class="clear"></div><div id="comment-47745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

