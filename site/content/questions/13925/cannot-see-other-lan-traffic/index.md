+++
type = "question"
title = "Cannot see other LAN traffic"
description = '''I have three machines on my VLAN- A, B and C, all running Ubuntu. If I run Wireshark in promiscuous mode on, say, machine B, I am unable to see the traffic between machine A/C and the internet. The LAN traffic between them is detected fine. Where am I going wrong?'''
date = "2012-08-28T02:23:00Z"
lastmod = "2012-08-28T02:28:00Z"
weight = 13925
keywords = [ "vlan", "traffic" ]
aliases = [ "/questions/13925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot see other LAN traffic](/questions/13925/cannot-see-other-lan-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13925-score" class="post-score" title="current number of votes">0</div><span id="post-13925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have three machines on my VLAN- A, B and C, all running Ubuntu. If I run Wireshark in promiscuous mode on, say, machine B, I am unable to see the traffic between machine A/C and the internet. The LAN traffic between them is detected fine. Where am I going wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/be46a5c5bfe9818e55a16624203bc673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnp&#39;s gravatar image" /><p><span>pnp</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnp has no accepted answers">0%</span></p></div></div><div id="comments-container-13925" class="comments-container"></div><div id="comment-tools-13925" class="comment-tools"></div><div class="clear"></div><div id="comment-13925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13927"></span>

<div id="answer-container-13927" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13927-score" class="post-score" title="current number of votes">2</div><span id="post-13927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pnp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're capturing at a switch, and a switch will not push all packets to all ports like a hub used to do. That means that the conversation between A and C is bypassing your link to B, which is why it can't see the traffic.</p><p>Please take a look at <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13927" class="comments-container"></div><div id="comment-tools-13927" class="comment-tools"></div><div class="clear"></div><div id="comment-13927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

