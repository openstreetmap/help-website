+++
type = "question"
title = "Query over the Protocal name"
description = '''hello all i am fresher to the networking field. i am working on switch working. i connected 3 PCs to a switch by ethernet cables. i am able to ping all the 3 machines, one from the other. wireshark is running on all the three. suppose, when i run a simple server and client on 2 machines..i.e sending...'''
date = "2012-04-25T00:00:00Z"
lastmod = "2012-04-25T06:33:00Z"
weight = 10427
keywords = [ "protocol" ]
aliases = [ "/questions/10427" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query over the Protocal name](/questions/10427/query-over-the-protocal-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10427-score" class="post-score" title="current number of votes">0</div><span id="post-10427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello all</p><p>i am fresher to the networking field. i am working on switch working.</p><p>i connected 3 PCs to a switch by ethernet cables. i am able to ping all the 3 machines, one from the other. wireshark is running on all the three. suppose, when i run a simple server and client on 2 machines..i.e sending a message from one to other; in what form i.e by what protocol, will wireshark grasp the information ?</p><p>if 2 machines are interaction, will the 3rd machine access the info over wireshark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '12, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/a1fa900778de0a4200d907fc770b2dc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manju1438&#39;s gravatar image" /><p><span>manju1438</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manju1438 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '12, 00:02</strong> </span></p></div></div><div id="comments-container-10427" class="comments-container"></div><div id="comment-tools-10427" class="comment-tools"></div><div class="clear"></div><div id="comment-10427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10435"></span>

<div id="answer-container-10435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10435-score" class="post-score" title="current number of votes">0</div><span id="post-10435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're sending data from one machine to the other the switch will forward it directly, so the third machine won't see it at all (except the occasional unicast flood to learn MAC addresses, but that's a bit too much detail at the moment). So no, Wireshark will not see anything usefull, unless you can tell your switch to give a copy of the packets between the other machines to the capturing machine. For that you need a manageable switch with a monitor port feature.</p><p>And regarding the protocol: Wireshark will capture whatever the machines use and show it. It is not a decision made by Wireshark, but by the applications that send the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10435" class="comments-container"></div><div id="comment-tools-10435" class="comment-tools"></div><div class="clear"></div><div id="comment-10435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

