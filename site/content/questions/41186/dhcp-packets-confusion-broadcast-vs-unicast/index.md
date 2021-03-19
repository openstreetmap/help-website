+++
type = "question"
title = "DHCP - Packets confusion - Broadcast vs Unicast"
description = '''Hello, Was checking out the DHCP packet capture on Wireshark-  It is evident that only the 1st packet has dest IP addr. 255.255.255.255 i.e. is broadcast and rest 3 packets are unicast. But the Microsoft article on DHCP mentions that all 4 packet are broadcast-  Kindly advise. Thanks, Rahil'''
date = "2015-04-04T05:44:00Z"
lastmod = "2015-04-04T08:13:00Z"
weight = 41186
keywords = [ "dhcp" ]
aliases = [ "/questions/41186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP - Packets confusion - Broadcast vs Unicast](/questions/41186/dhcp-packets-confusion-broadcast-vs-unicast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41186-score" class="post-score" title="current number of votes">1</div><span id="post-41186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Was checking out the DHCP packet capture on Wireshark-</p><p><img src="https://osqa-ask.wireshark.org/upfiles/DHCP.PNG" alt="alt text" /></p><p>It is evident that only the 1st packet has dest IP addr. 255.255.255.255 i.e. is broadcast and rest 3 packets are unicast. But the Microsoft article on <a href="http://support.microsoft.com/en-us/kb/169289">DHCP</a> mentions that all 4 packet are broadcast- <img src="https://osqa-ask.wireshark.org/upfiles/DHCP_1.PNG" alt="alt text" /></p><p>Kindly advise.</p><p>Thanks,</p><p>Rahil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '15, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/42ac24bbf384d2f8ab78e2ee28c743c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahil&#39;s gravatar image" /><p><span>Rahil</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahil has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '15, 08:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-41186" class="comments-container"></div><div id="comment-tools-41186" class="comment-tools"></div><div class="clear"></div><div id="comment-41186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41188"></span>

<div id="answer-container-41188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41188-score" class="post-score" title="current number of votes">2</div><span id="post-41188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://www.ietf.org/rfc/rfc2131.txt">RFC 2131</a>. The MS KB article you link to only really covers RFC 1541 which was superseded by 2131, and also only covers up to Win 95 and NT 4.0, so is really old.</p><p>The first message (DHCP Discover) is a broadcast as the client doesn't know where the DHCP servers are (or if there are any around).</p><p>The second message (DHCP Offer) is unicast to the IP address that the DHPC server is offering. This is as per the RFC where the client did not set the broadcast bit in the DHCP Discover message.</p><p>The third message (DHCP Request) is broadcast by the client as it is SELECTing the offer, other DHPC servers on the subnet need to know which offer has been selected.</p><p>The fourth message (DHCP Ack) is unicast by the server to the client at the IP address the client requested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '15, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41188" class="comments-container"></div><div id="comment-tools-41188" class="comment-tools"></div><div class="clear"></div><div id="comment-41188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

