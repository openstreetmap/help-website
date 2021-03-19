+++
type = "question"
title = "Why do I see TCP packets on the network?"
description = '''This is a question more related to the fundamentals of networking rather than wireshark itself. I&#x27;ve been trying to learn networking from some videos on the internet and if I understand correctly each layer of the network model is encapsulated by the layer below it. Why do I see TCP and UDP packets ...'''
date = "2013-10-31T11:20:00Z"
lastmod = "2013-10-31T13:13:00Z"
weight = 26597
keywords = [ "ip", "networking", "network", "tcp" ]
aliases = [ "/questions/26597" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do I see TCP packets on the network?](/questions/26597/why-do-i-see-tcp-packets-on-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26597-score" class="post-score" title="current number of votes">0</div><span id="post-26597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a question more related to the fundamentals of networking rather than wireshark itself. I've been trying to learn networking from some videos on the internet and if I understand correctly each layer of the network model is encapsulated by the layer below it. Why do I see TCP and UDP packets on the network then? Shouldn't they be encapsulated by IP packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '13, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/be17b92e8b1944961d5f77df07534b5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_delta_&#39;s gravatar image" /><p><span>_delta_</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_delta_ has no accepted answers">0%</span></p></div></div><div id="comments-container-26597" class="comments-container"></div><div id="comment-tools-26597" class="comment-tools"></div><div class="clear"></div><div id="comment-26597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26598"></span>

<div id="answer-container-26598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26598-score" class="post-score" title="current number of votes">1</div><span id="post-26598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you looking in the Protocol column in Wireshark's Packet List pane? In this column, Wirehark lists the highest level protocol that it can identify, which is why you see TCP instead of IP. Yes, the TCP and UDP packets are encapsulated in IP, which is in turn encapsulated in Ethernet.</p><p>If you look in the Packet Details pane, you'll see the entire packet: TCP or UDP, IP, and Ethernet. And if the TCP or UDP packet contains data, you'll see the higher-level protocol, such as HTTP or SMTP, if Wireshark can identify it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-26598" class="comments-container"><span id="26599"></span><div id="comment-26599" class="comment"><div id="post-26599-score" class="comment-score"></div><div class="comment-text"><p>Okay so if I understand correctly, Wireshark sometimes can't identify higher than a certain level like TCP. Why is that?</p></div><div id="comment-26599-info" class="comment-info"><span class="comment-age">(31 Oct '13, 11:52)</span> <span class="comment-user userinfo">_delta_</span></div></div><span id="26601"></span><div id="comment-26601" class="comment"><div id="post-26601-score" class="comment-score"></div><div class="comment-text"><p>There may not be a higher level. Some TCP packets are just acknowledgments; they do not contain any data.</p></div><div id="comment-26601-info" class="comment-info"><span class="comment-age">(31 Oct '13, 13:13)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-26598" class="comment-tools"></div><div class="clear"></div><div id="comment-26598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

