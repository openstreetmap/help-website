+++
type = "question"
title = "Comunication over VPN (2 Servers)"
description = '''Hey guys, I have a little problem and only wanted to know if I&#x27;m right. MachineA: 192.168.11.17 - http://www.cloudshark.org/captures/d93b8cda3ebd Sorry for Checksum Offload here! MachineB: 192.168.13.17 - http://www.cloudshark.org/captures/6fec5b3aa134 There&#x27;s only the one stream in my trace file. W...'''
date = "2013-01-11T08:06:00Z"
lastmod = "2013-01-15T05:17:00Z"
weight = 17604
keywords = [ "vpn", "trace" ]
aliases = [ "/questions/17604" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Comunication over VPN (2 Servers)](/questions/17604/comunication-over-vpn-2-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17604-score" class="post-score" title="current number of votes">0</div><span id="post-17604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I have a little problem and only wanted to know if I'm right.</p><p>MachineA: 192.168.11.17 - <a href="http://www.cloudshark.org/captures/d93b8cda3ebd">http://www.cloudshark.org/captures/d93b8cda3ebd</a></p><p>Sorry for Checksum Offload here!</p><p>MachineB: 192.168.13.17 - <a href="http://www.cloudshark.org/captures/6fec5b3aa134">http://www.cloudshark.org/captures/6fec5b3aa134</a></p><p>There's only the one stream in my trace file. What's going on there?</p><p>Regards Leo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/942654ab74b247e619da6cbe23d83720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DasLeo&#39;s gravatar image" /><p><span>DasLeo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DasLeo has no accepted answers">0%</span></p></div></div><div id="comments-container-17604" class="comments-container"><span id="17606"></span><div id="comment-17606" class="comment"><div id="post-17606-score" class="comment-score"></div><div class="comment-text"><p>What exactly is the question ?</p><p>It looks like the captures are of a connection between the two machines as seen at each machine.</p></div><div id="comment-17606-info" class="comment-info"><span class="comment-age">(11 Jan '13, 08:26)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-17604" class="comment-tools"></div><div class="clear"></div><div id="comment-17604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17618"></span>

<div id="answer-container-17618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17618-score" class="post-score" title="current number of votes">1</div><span id="post-17618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>There's only the one stream in my trace file. What's going on there?</p></blockquote><p>Well, there are some differences. Some minor, some major.</p><p><strong>Minor:</strong> Some frames with the same IP ID are different in length: #3,#5,#8. However, that's not a problem, as the difference is due to removed <strong>padding bytes</strong> in the ethernet frame.</p><p><strong>Major:</strong> Frame #18 (MachineA) was not transmitted over the VPN tunnel, as the size was too large (4192 bytes) <strong>and</strong> the <strong>don't fragment flag</strong> was set in that segment.</p><p>If your question is: How to fix the 'major' problem?</p><p>My answer would be: Check the MTU size of the involved systems and adjust it to the requirements of your VPN, or allow IP fragmentation.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17618" class="comments-container"><span id="17683"></span><div id="comment-17683" class="comment"><div id="post-17683-score" class="comment-score"></div><div class="comment-text"><p>Thx Kurt, that's what I needed to know!</p></div><div id="comment-17683-info" class="comment-info"><span class="comment-age">(14 Jan '13, 23:18)</span> <span class="comment-user userinfo">DasLeo</span></div></div><span id="17695"></span><div id="comment-17695" class="comment"><div id="post-17695-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>HINT: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-17695-info" class="comment-info"><span class="comment-age">(15 Jan '13, 05:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17618" class="comment-tools"></div><div class="clear"></div><div id="comment-17618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

