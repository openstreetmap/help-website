+++
type = "question"
title = "Wireshark join a multicast"
description = '''I have a server playing out 24 multi-cast streams on three GbE ports (8 per port), which are connected to a switch. When I connect directly to one of the GbE ports I am able to capture all the multicast streams. When I connect to the switch I have to set-up TSReader (or StreamXpert) to join to a mul...'''
date = "2012-05-29T08:31:00Z"
lastmod = "2012-05-31T06:39:00Z"
weight = 11445
keywords = [ "udp", "multicast", "join" ]
aliases = [ "/questions/11445" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark join a multicast](/questions/11445/wireshark-join-a-multicast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11445-score" class="post-score" title="current number of votes">0</div><span id="post-11445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a server playing out 24 multi-cast streams on three GbE ports (8 per port), which are connected to a switch. When I connect directly to one of the GbE ports I am able to capture all the multicast streams.</p><p>When I connect to the switch I have to set-up TSReader (or StreamXpert) to join to a multicast before Wireshark will display the packets</p><p>Is there a way that wireshark can make a join request to a multicast therefore cutting out the need to use TSReader?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-join" rel="tag" title="see questions tagged &#39;join&#39;">join</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/0537fb2feaea0a16e638b604e497fae6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krobinson&#39;s gravatar image" /><p><span>krobinson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krobinson has no accepted answers">0%</span></p></div></div><div id="comments-container-11445" class="comments-container"></div><div id="comment-tools-11445" class="comment-tools"></div><div class="clear"></div><div id="comment-11445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11447"></span>

<div id="answer-container-11447" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11447-score" class="post-score" title="current number of votes">0</div><span id="post-11447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Only by changing the Wireshark code (which would be a non-starter IMO) :)</p><p>What's wrong with separately issuing the join request before starting the Wireshark capture ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 May '12, 08:42</strong> </span></p></div></div><div id="comments-container-11447" class="comments-container"><span id="11448"></span><div id="comment-11448" class="comment"><div id="post-11448-score" class="comment-score"></div><div class="comment-text"><p>Just being lazy.</p><p>I need to check the TTL on a couple of different streams, so I was hoping to have a easier and faster way.</p></div><div id="comment-11448-info" class="comment-info"><span class="comment-age">(29 May '12, 08:59)</span> <span class="comment-user userinfo">krobinson</span></div></div></div><div id="comment-tools-11447" class="comment-tools"></div><div class="clear"></div><div id="comment-11447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11488"></span>

<div id="answer-container-11488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11488-score" class="post-score" title="current number of votes">0</div><span id="post-11488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That would require to implement (part of) the multicast host requirements in Wireshark.</p><ul><li>Transmitting of packets (which Wireshark doesn't do, at all)</li><li>Creating the group join in IGMP v1, or v2, or v3</li><li>Putting it out on the correct link / vlan / circuit</li><li>Wait for the IGMP v1 / v2 / v3 querier to reconfirm the group membership.</li><li>Terminate group membership when capture stops</li></ul><p>As you can see from the list, the generic solution is rather large. Therefore I don't see it happening in the near future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11488" class="comments-container"></div><div id="comment-tools-11488" class="comment-tools"></div><div class="clear"></div><div id="comment-11488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

