+++
type = "question"
title = "how do you capture all packets on network?"
description = '''We have a network with a Cisco Lan/WLAN router and ethernet unmanaged Netgear 100MB and 1GB switches. Computers are Win XP Pro and Win 7 Pro. Need to capture all packets and discover cause of problem with POP3 emails intermittent send and recieve errors. We have isolated the problem to something on ...'''
date = "2013-08-08T07:05:00Z"
lastmod = "2013-08-11T18:18:00Z"
weight = 23647
keywords = [ "pop3" ]
aliases = [ "/questions/23647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how do you capture all packets on network?](/questions/23647/how-do-you-capture-all-packets-on-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23647-score" class="post-score" title="current number of votes">0</div><span id="post-23647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a network with a Cisco Lan/WLAN router and ethernet unmanaged Netgear 100MB and 1GB switches. Computers are Win XP Pro and Win 7 Pro. Need to capture all packets and discover cause of problem with POP3 emails intermittent send and recieve errors. We have isolated the problem to something on network is interfering with POP3. New to wireshark capturing. What is the best method to capture all packets on network? Where on network should we put the Win7 Pro machine with Wireshark to capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pop3" rel="tag" title="see questions tagged &#39;pop3&#39;">pop3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '13, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/027e6b3c334d22294718fa26e5672f76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sacn&#39;s gravatar image" /><p><span>sacn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sacn has no accepted answers">0%</span></p></div></div><div id="comments-container-23647" class="comments-container"></div><div id="comment-tools-23647" class="comment-tools"></div><div class="clear"></div><div id="comment-23647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23702"></span>

<div id="answer-container-23702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23702-score" class="post-score" title="current number of votes">0</div><span id="post-23702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your computers are connected to switched Ethernet network. Inherently this offers a point to multipoint service - it looks a little like a broadcast, the network devices manage who gets to see the traffic. Thus there isn't one point that sees <em>all</em> of the traffic. So either you have to arrange to have all enduser devices to connect to one big switch, or do the capture in multiple places. Also with unmanaged switches, you are not going to able to configure them to perform a port-mirroring role (which sends a copy of traffic to a single monitoring port). You maybe able to configure your Cisco to do this, but again it would only be able to mirror traffic that passes through it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '13, 18:18</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-23702" class="comments-container"></div><div id="comment-tools-23702" class="comment-tools"></div><div class="clear"></div><div id="comment-23702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

