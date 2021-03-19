+++
type = "question"
title = "Can someone help me interpret these SSDP packets?"
description = '''Hi all, I use a VPN so a lot of what Wireshark shows me on my network is encrypted. I&#x27;m a total n00b to network analysis and Wireshark but was hoping someone could explain what&#x27;s happening with SSDP Packets? The SSDP packets are not encrypted (I can clearly read the text contained in the packet alon...'''
date = "2016-12-03T08:22:00Z"
lastmod = "2016-12-03T14:09:00Z"
weight = 57816
keywords = [ "encryption", "ssdp" ]
aliases = [ "/questions/57816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can someone help me interpret these SSDP packets?](/questions/57816/can-someone-help-me-interpret-these-ssdp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57816-score" class="post-score" title="current number of votes">0</div><span id="post-57816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I use a VPN so a lot of what Wireshark shows me on my network is encrypted.</p><p>I'm a total n00b to network analysis and Wireshark but was hoping someone could explain what's happening with SSDP Packets?</p><p>The SSDP packets are not encrypted (I can clearly read the text contained in the packet along the right-hand side of the 'Packet Bytes' window). They mention my Router's MAC address and another MAC address of unknown origin.</p><p>Since the packets aren't encrypted and this communication is occurring with a MAC not on my network, should I be suspicious? Does this represent remote Router Configuration access (i.e. hacking or remote manipulation)?</p><p>Essentially, what's the explanation for this? Can I disable this functionality without compromising internet useability?</p><p>Thanks a ton for all this help! I'll start helping others as soon as I'm up-to-speed with the program!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-ssdp" rel="tag" title="see questions tagged &#39;ssdp&#39;">ssdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '16, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/e5be3f3b963ac091b204c64d8c7e82f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arianax&#39;s gravatar image" /><p><span>Arianax</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arianax has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '16, 08:23</strong> </span></p></div></div><div id="comments-container-57816" class="comments-container"></div><div id="comment-tools-57816" class="comment-tools"></div><div class="clear"></div><div id="comment-57816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57823"></span>

<div id="answer-container-57823" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57823-score" class="post-score" title="current number of votes">1</div><span id="post-57823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a description of SSDP on the Wireshark wiki: <a href="https://wiki.wireshark.org/SSDP">https://wiki.wireshark.org/SSDP</a></p><p>That "other unknown MAC address" is likely the multicast address (see also the picture linked above). If your host is part of a multicast group, then it will receive this traffic.</p><p>SSDP is normally used for device discovery in the network (think of media devices to which you can stream data). If you do not need this functionality (I do not), then you could just disable it without any bad side-effects.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '16, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-57823" class="comments-container"></div><div id="comment-tools-57823" class="comment-tools"></div><div class="clear"></div><div id="comment-57823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

