+++
type = "question"
title = "Capture between two ip addresses"
description = '''Team I&#x27;m a newbie to wireshark, can someone tell me how to capture packets between two ip addresses from a different host? Example: I&#x27;m using a Mac and want to capture packets from two remote windows pcs between those two windows pcs while not including any data from my mac.  Thanks Technolust'''
date = "2016-05-09T13:09:00Z"
lastmod = "2016-05-10T07:41:00Z"
weight = 52366
keywords = [ "ip", "capture", "between" ]
aliases = [ "/questions/52366" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture between two ip addresses](/questions/52366/capture-between-two-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52366-score" class="post-score" title="current number of votes">0</div><span id="post-52366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Team</p><p>I'm a newbie to wireshark, can someone tell me how to capture packets between two ip addresses from a different host?</p><p>Example: I'm using a Mac and want to capture packets from two remote windows pcs between those two windows pcs while not including any data from my mac.</p><p>Thanks</p><p>Technolust</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-between" rel="tag" title="see questions tagged &#39;between&#39;">between</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '16, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/33629cedbae0425f09b7818d5e5bbdcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Technolust&#39;s gravatar image" /><p><span>Technolust</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Technolust has no accepted answers">0%</span></p></div></div><div id="comments-container-52366" class="comments-container"><span id="52367"></span><div id="comment-52367" class="comment"><div id="post-52367-score" class="comment-score"></div><div class="comment-text"><p>Is this on a wired network (such as an Ethernet) or a Wi-Fi network?</p></div><div id="comment-52367-info" class="comment-info"><span class="comment-age">(09 May '16, 13:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="52368"></span><div id="comment-52368" class="comment"><div id="post-52368-score" class="comment-score"></div><div class="comment-text"><p>This is on a wired network and using Wireshark 2.0.3</p></div><div id="comment-52368-info" class="comment-info"><span class="comment-age">(09 May '16, 13:25)</span> <span class="comment-user userinfo">Technolust</span></div></div></div><div id="comment-tools-52366" class="comment-tools"></div><div class="clear"></div><div id="comment-52366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52369"></span>

<div id="answer-container-52369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52369-score" class="post-score" title="current number of votes">0</div><span id="post-52369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This is on a wired network</p></blockquote><p>OK, that could be difficult if not impossible, depending on what the machines are plugged into.</p><p>Ethernet was originally a passive network, and every host on the network could, if its adapter was in promiscuous mode, see all the traffic sent on the network, including traffic sent neither to nor from that host.</p><p>However, modern Ethernets tend to be switched networks, and the switch usually only sends to a host the traffic it thinks is intended for the host to see - either broadcast traffic, multicast traffic, or traffic sent to that host.</p><p>See <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark Wiki article on Ethernet capture</a> for details on this and on how to try to overcome those problems with switched networks.</p><p><em>If</em> you manage to set up the network in that fashion, then you will want to 1) make sure you're capturing in promiscuous mode and 2) use a capture filter such as "host A and B", where "A" and "B" are the IP addresses of the two hosts whose traffic you're trying to capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '16, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '16, 13:33</strong> </span></p></div></div><div id="comments-container-52369" class="comments-container"><span id="52394"></span><div id="comment-52394" class="comment"><div id="post-52394-score" class="comment-score"></div><div class="comment-text"><p>I had a feeling that was going to be the case, thank you for your response. Well clarifying things up.</p></div><div id="comment-52394-info" class="comment-info"><span class="comment-age">(10 May '16, 07:41)</span> <span class="comment-user userinfo">Technolust</span></div></div></div><div id="comment-tools-52369" class="comment-tools"></div><div class="clear"></div><div id="comment-52369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

