+++
type = "question"
title = "Blacklist an Interface"
description = '''I was wondering whether it is possible to blacklist an interface and stop Wireshark from scanning it? We have a user who is wanting to create virtual network adapters with Mininet, they will need wireshark to debug and check packets are moving between virtual adapters. The problem is we have a fairl...'''
date = "2017-04-24T08:40:00Z"
lastmod = "2017-04-26T03:30:00Z"
weight = 61010
keywords = [ "mininet" ]
aliases = [ "/questions/61010" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Blacklist an Interface](/questions/61010/blacklist-an-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61010-score" class="post-score" title="current number of votes">0</div><span id="post-61010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering whether it is possible to blacklist an interface and stop Wireshark from scanning it?</p><p>We have a user who is wanting to create virtual network adapters with Mininet, they will need wireshark to debug and check packets are moving between virtual adapters.</p><p>The problem is we have a fairly strict network policy which states port scanning and packet scanning is not allowed.</p><p>I was hoping that there was some config that would let me blacklist wireshark from using the main physical network adapter and restrict the ability of a user scanning packets on the network.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mininet" rel="tag" title="see questions tagged &#39;mininet&#39;">mininet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '17, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/240d695652f32af8c8504bd826286f5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fyberoptik&#39;s gravatar image" /><p><span>fyberoptik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fyberoptik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '17, 08:44</strong> </span></p></div></div><div id="comments-container-61010" class="comments-container"><span id="61013"></span><div id="comment-61013" class="comment"><div id="post-61013-score" class="comment-score"></div><div class="comment-text"><p>Why is that a problem if all is inside a VM? What platform are we talking about?</p></div><div id="comment-61013-info" class="comment-info"><span class="comment-age">(24 Apr '17, 09:37)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61026"></span><div id="comment-61026" class="comment"><div id="post-61026-score" class="comment-score"></div><div class="comment-text"><p>The main issue with a VM type solution is that it would give users free reign to install other unmanaged operating systems on a network which closely managed.</p><p>This solution is needed for a Linux/Ubuntu 16.04 machine.</p></div><div id="comment-61026-info" class="comment-info"><span class="comment-age">(25 Apr '17, 02:11)</span> <span class="comment-user userinfo">fyberoptik</span></div></div><span id="61046"></span><div id="comment-61046" class="comment"><div id="post-61046-score" class="comment-score"></div><div class="comment-text"><p>I still wonder how you would manage mininet in such context anyway. Attaching a real network interface to the topology can have some interesting consequences.</p></div><div id="comment-61046-info" class="comment-info"><span class="comment-age">(25 Apr '17, 07:14)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-61010" class="comment-tools"></div><div class="clear"></div><div id="comment-61010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61047"></span>

<div id="answer-container-61047" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61047-score" class="post-score" title="current number of votes">0</div><span id="post-61047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fyberoptik has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the short and fast answer is: no, it's not possible to blacklist an interface. Even if you select to 'hide' an interface, the user can 'unhide' it, and the traffic will still show up on the 'All' interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '17, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61047" class="comments-container"><span id="61058"></span><div id="comment-61058" class="comment"><div id="post-61058-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help Jaap, I think I will have to admit defeat on this one.</p></div><div id="comment-61058-info" class="comment-info"><span class="comment-age">(26 Apr '17, 03:30)</span> <span class="comment-user userinfo">fyberoptik</span></div></div></div><div id="comment-tools-61047" class="comment-tools"></div><div class="clear"></div><div id="comment-61047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

