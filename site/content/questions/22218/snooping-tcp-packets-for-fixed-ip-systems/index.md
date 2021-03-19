+++
type = "question"
title = "Snooping TCP packets for fixed IP systems"
description = '''I am not an expert in networking but I am trying to connect two embedded systems in a network to snoop the TCP packets. Both the systems(lets say A and B) has fixed IP address and they communicate on a dedicated port. I am using PC (lets say system C) and Wireshark to snoop the TCP packets for debug...'''
date = "2013-06-21T02:14:00Z"
lastmod = "2013-06-21T10:35:00Z"
weight = 22218
keywords = [ "packets", "snooping", "tcp" ]
aliases = [ "/questions/22218" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Snooping TCP packets for fixed IP systems](/questions/22218/snooping-tcp-packets-for-fixed-ip-systems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22218-score" class="post-score" title="current number of votes">0</div><span id="post-22218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not an expert in networking but I am trying to connect two embedded systems in a network to snoop the TCP packets. Both the systems(lets say A and B) has fixed IP address and they communicate on a dedicated port. I am using PC (lets say system C) and Wireshark to snoop the TCP packets for debugging.</p><p>1) When I connected these systems(A,B and C) through a switch, I couldn't see any data on Wireshark. After some Googling I found that now a days switches are smart and they do flow control, that's the reason I couldn't see any data on the Wireshark.</p><p>2) I connected both the embedded systems (A and B) via USB to Ethernet adapters(one for each system) to a PC(system C) on which I was running wireshark. In Windows 7 there is an option to link both the network adapters via bridge, which I did by right clicking both the adapters and creating a bridge. I couldn't ping from system A to system B or vice-verse.</p><p>I just want to snoop the TCP packets on wireshark from these systems on a PC with out any switches(external hardware), is there any other way I can snoop the packets easily ? Your help would be appreciated tremendously and thanks in advance.</p><p>Emb</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-snooping" rel="tag" title="see questions tagged &#39;snooping&#39;">snooping</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/6e5543ecd3c597e3d692bb92920ec5d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="embdsp&#39;s gravatar image" /><p><span>embdsp</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="embdsp has no accepted answers">0%</span></p></div></div><div id="comments-container-22218" class="comments-container"></div><div id="comment-tools-22218" class="comment-tools"></div><div class="clear"></div><div id="comment-22218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22221"></span>

<div id="answer-container-22221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22221-score" class="post-score" title="current number of votes">1</div><span id="post-22221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a>.</p><p>If you have two network adaptors in the Win 7 system (one should not be a USB one), then you can bridge the two and capture on the non-USB NIC.</p><p>In this sort of situation the easiest method is to buy a switch that will span or mirror a port to a monitoring port. The Netgear ProSafe Plus GS105E can be picked up cheaply from Ebay (other models of switches are available) and will do this. If buying a switch for this purpose make sure it can span or mirror, a basic switch won't do this, hence the need to pay a little more. The switch will come in handy for all sorts of things in the future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22221" class="comments-container"><span id="22223"></span><div id="comment-22223" class="comment"><div id="post-22223-score" class="comment-score"></div><div class="comment-text"><p>I will buy the switch which you ahve recommended. This seem to be hassle free idea. Thanks for your help.</p><p>Cheers! Emb</p></div><div id="comment-22223-info" class="comment-info"><span class="comment-age">(21 Jun '13, 09:39)</span> <span class="comment-user userinfo">embdsp</span></div></div><span id="22224"></span><div id="comment-22224" class="comment"><div id="post-22224-score" class="comment-score"></div><div class="comment-text"><p>I got mine from an EU ebay seller for GBP 28 delivered. A bargain.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-22224-info" class="comment-info"><span class="comment-age">(21 Jun '13, 09:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="22227"></span><div id="comment-22227" class="comment"><div id="post-22227-score" class="comment-score"></div><div class="comment-text"><p>Million thanks for you suggestion, I will go for the switch. Thanks again. Cheers! Emb</p></div><div id="comment-22227-info" class="comment-info"><span class="comment-age">(21 Jun '13, 10:35)</span> <span class="comment-user userinfo">embdsp</span></div></div></div><div id="comment-tools-22221" class="comment-tools"></div><div class="clear"></div><div id="comment-22221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

