+++
type = "question"
title = "Ethernet address display filter on 802.11 frames"
description = '''For example, I want to capture traffic between an AP (00:00:00:11:11:11) and a terminal (00:00:00:22:22:22.) by the AirPCap I have been able to capture all 802.11 frames by defining capture filter: (ether src host 00:00:00:11:11:11 and ether dst host 00:00:00:22:22:22) or   (ether dst host 00:00:00:...'''
date = "2012-03-16T07:17:00Z"
lastmod = "2012-03-16T09:28:00Z"
weight = 9585
keywords = [ "filter", "ethernet", "display" ]
aliases = [ "/questions/9585" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet address display filter on 802.11 frames](/questions/9585/ethernet-address-display-filter-on-80211-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example, I want to capture traffic between an AP (00:00:00:11:11:11) and a terminal (00:00:00:22:22:22.) by the AirPCap</p><p>I have been able to capture all 802.11 frames by defining capture filter:</p><p>(ether src host 00:00:00:11:11:11 and ether dst host 00:00:00:22:22:22) or (ether dst host 00:00:00:11:11:11 and ether src host 00:00:00:22:22:22)</p><p>However, when I try to capture all frames without this capture filter and later on apply "display filter" below, I see no frames are displayed...??? I guess both filters are of same meaning?</p><p>(eth.src == 00:00:00:11:11:11 and eth.dst == 00:00:00:22:22:22) || (eth.dst == 00:00:00:11:11:11 and eth.src == 00:00:00:22:22:22)</p><p>Strange is...even I apply display filter eth.src == 00:00:00:11:11:11...I see no frame?</p><p>I am keen to learn the Wireshark...just installed for 2 days.</p><p>Can anyone teach me ...if my display filter syntax incorrect?<br />
</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">filter ethernet display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '12, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/ee6b9c3fe51323d681ae7514a89cae62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WiresharkJW&#39;s gravatar image" /><p>WiresharkJW<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WiresharkJW has one accepted answer">100%</span> </br></p></div></div><div id="comments-container-9585" class="comments-container"></div><div id="comment-tools-9585" class="comment-tools"></div><div class="clear"></div><div id="comment-9585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9588"></span>

<div id="answer-container-9588" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9588-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have got the answer from someone...just to share for beginner if you want to capture 802.11 frames</p><p>For capture filter: use "ether src host" / "ether dst host" For display filter: use "wlan.sa" / "wlan.da"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '12, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/ee6b9c3fe51323d681ae7514a89cae62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WiresharkJW&#39;s gravatar image" /><p>WiresharkJW<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WiresharkJW has one accepted answer">100%</span></p></div></div><div id="comments-container-9588" class="comments-container"></div><div id="comment-tools-9588" class="comment-tools"></div><div class="clear"></div><div id="comment-9588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

