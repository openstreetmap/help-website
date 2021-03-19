+++
type = "question"
title = "How to blocked specific packet or payload?"
description = '''How to blocked specific packet or payload? I saw a packet that would crash the application which I don&#x27;t have control. is there a way to drop this specific packet? Thanks'''
date = "2015-12-03T04:07:00Z"
lastmod = "2015-12-03T07:29:00Z"
weight = 48221
keywords = [ "tcp", "packet" ]
aliases = [ "/questions/48221" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to blocked specific packet or payload?](/questions/48221/how-to-blocked-specific-packet-or-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48221-score" class="post-score" title="current number of votes">0</div><span id="post-48221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to blocked specific packet or payload? I saw a packet that would crash the application which I don't have control. is there a way to drop this specific packet? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '15, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/b28e4bba49352b3b1e2f015d72556540?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmguy&#39;s gravatar image" /><p><span>mmguy</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmguy has no accepted answers">0%</span></p></div></div><div id="comments-container-48221" class="comments-container"></div><div id="comment-tools-48221" class="comment-tools"></div><div class="clear"></div><div id="comment-48221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="48222"></span>

<div id="answer-container-48222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48222-score" class="post-score" title="current number of votes">0</div><span id="post-48222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a Packet Analyzer, not a firewall or proxy. You'll need some other software for that sort of functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '15, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48222" class="comments-container"></div><div id="comment-tools-48222" class="comment-tools"></div><div class="clear"></div><div id="comment-48222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48223"></span>

<div id="answer-container-48223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48223-score" class="post-score" title="current number of votes">0</div><span id="post-48223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are able to identify this packet from it's IP address or transport protocol port number you could setup a capture filter to prevent the packet from reaching Wireshark at all. But I doubt that could be made specific enough.</p><p>If you found a packet which crashed the application we would welcome a bug report at <a href="https://bugs.wireshark.org">bugs.wireshark.org</a>, including the relevant details of the Wireshark version used and most importantly a sample capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '15, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-48223" class="comments-container"></div><div id="comment-tools-48223" class="comment-tools"></div><div class="clear"></div><div id="comment-48223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48227"></span>

<div id="answer-container-48227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48227-score" class="post-score" title="current number of votes">0</div><span id="post-48227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is really hard to understand what exactly you have in mind, which is why you get answers varying up to what people guess you are really asking.</p><p><em>My</em> guess is that you have already identified, using Wireshark, a packet which kills some application different from Wireshark, and you already know how the packet looks like. And now you are looking for a way to prevent the packet from reaching the application.</p><p>If the application runs on a Linux machine, netfilter (aka iptables) may help you, but ONLY if the packet is really unrelated to any existing stream. If so, you may set up a netfilter rule to drop the packet. You can also put a linux box between the machine you need to protect and the rest of the network. On Windows I currently don't know about any routinely used equivalent of netfilter; some firewall appliances may be able to go so deep into packet's contents as to allow you to describe in deep detail which packets to drop.</p><p>If I am right in my decoding of your question, please publish a capture which contains not only the killer packet but also a continuous piece of normal communication before the killer packet has arrived and give a link to it and the frame number of the killer packet here. Only doing so will allow folks here to say whether dropping this packet is possible or whether it would make things worse.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '15, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48227" class="comments-container"><span id="48231"></span><div id="comment-48231" class="comment"><div id="post-48231-score" class="comment-score"></div><div class="comment-text"><p>Indeed, what is this magical 'the application'?? For sure it's Wireshark? Or, how far off-topic are we going?</p></div><div id="comment-48231-info" class="comment-info"><span class="comment-age">(03 Dec '15, 07:29)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-48227" class="comment-tools"></div><div class="clear"></div><div id="comment-48227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

