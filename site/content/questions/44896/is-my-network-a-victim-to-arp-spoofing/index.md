+++
type = "question"
title = "Is my network a victim to ARP Spoofing?"
description = '''Hi All, I am not too familiar with understanding wireshark logs, but have tried to diagnose a recent network connectivity issue that is crippling our speeds. I have been reading up on issues around the large amount of duplicate IP and ARP transactions, with a lot of resources saying its related to a...'''
date = "2015-08-05T18:23:00Z"
lastmod = "2015-08-06T16:30:00Z"
weight = 44896
keywords = [ "dump", "wireshark" ]
aliases = [ "/questions/44896" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is my network a victim to ARP Spoofing?](/questions/44896/is-my-network-a-victim-to-arp-spoofing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44896-score" class="post-score" title="current number of votes">0</div><span id="post-44896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am not too familiar with understanding wireshark logs, but have tried to diagnose a recent network connectivity issue that is crippling our speeds.</p><p>I have been reading up on issues around the large amount of duplicate IP and ARP transactions, with a lot of resources saying its related to an ARP Spoofing attack. Would someone with a bit more experience on the matter be able to let me know if thats the case?</p><p>Here is the dump: <a href="https://www.cloudshark.org/captures/dc90369489a0">https://www.cloudshark.org/captures/dc90369489a0</a></p><p>I really appreciate the support, thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 18:23</strong></p><img src="https://secure.gravatar.com/avatar/06952c2ddd62ace58bf65eb9f17983f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danr&#39;s gravatar image" /><p><span>danr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danr has no accepted answers">0%</span></p></div></div><div id="comments-container-44896" class="comments-container"></div><div id="comment-tools-44896" class="comment-tools"></div><div class="clear"></div><div id="comment-44896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44898"></span>

<div id="answer-container-44898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44898-score" class="post-score" title="current number of votes">1</div><span id="post-44898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks indeed a little bit strange. There is a suspicious system in your trace, at least from my point of view.</p><p>The IP is 192.168.16.10 with the Mac 00:04:23:e1:2F:77 It sends always a an direct ARP Answer to all the devices and it als o sends constantly DHCP ACKs. This makes the system supsicious. There is another MAC the 00:04.23:e1:2f:76 with the IP Address 192.168.16.10.</p><p>If I were you, I would investigate this behaviour. But maybe it is just a new art of ARP and teaming implementation?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 21:47</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '15, 22:19</strong> </span></p></div></div><div id="comments-container-44898" class="comments-container"><span id="44899"></span><div id="comment-44899" class="comment"><div id="post-44899-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your input Christian.</p></div><div id="comment-44899-info" class="comment-info"><span class="comment-age">(05 Aug '15, 22:04)</span> <span class="comment-user userinfo">danr</span></div></div><span id="44900"></span><div id="comment-44900" class="comment"><div id="post-44900-score" class="comment-score"></div><div class="comment-text"><p>But it has an FCS checksum of 0x0 so it be the system with the trace. Oh and I oversaw, that he is maybe the real DHCP server.</p></div><div id="comment-44900-info" class="comment-info"><span class="comment-age">(05 Aug '15, 22:23)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44911"></span><div id="comment-44911" class="comment"><div id="post-44911-score" class="comment-score"></div><div class="comment-text"><p>Correct, both MAC's are the adapters on the DHCP. Which I wasn't aware of at the time.</p></div><div id="comment-44911-info" class="comment-info"><span class="comment-age">(06 Aug '15, 16:30)</span> <span class="comment-user userinfo">danr</span></div></div></div><div id="comment-tools-44898" class="comment-tools"></div><div class="clear"></div><div id="comment-44898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

