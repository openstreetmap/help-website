+++
type = "question"
title = "no capture mpls frame"
description = '''Hello I have a network for testing MPLS protocol.(PC-Switch-RouterLER1-Sw-LSR1-Sw-RLSR2-sw-RLER2-sw-PC)  I have monitoring each segment to see MPLS label with Wireshark. Last year this pratice operate! This year Wireshark capture packet except the frame with MPLS label. How configure Wireshark to ca...'''
date = "2012-11-20T05:58:00Z"
lastmod = "2012-11-21T09:24:00Z"
weight = 16112
keywords = [ "mpls" ]
aliases = [ "/questions/16112" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [no capture mpls frame](/questions/16112/no-capture-mpls-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16112-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have a network for testing MPLS protocol.(PC-Switch-RouterLER1-Sw-LSR1-Sw-RLSR2-sw-RLER2-sw-PC) I have monitoring each segment to see MPLS label with Wireshark.</p><p>Last year this pratice operate!</p><p>This year Wireshark capture packet except the frame with MPLS label.</p><p>How configure Wireshark to capture frame with MPLS?</p><p>Christophe Varin</p></div><div id="question-tags" class="tags-container tags">mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/edad779b7fc3b6e32ecd6fc12ccec1bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christophe85&#39;s gravatar image" /><p>Christophe85<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christophe85 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '12, 06:27</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-16112" class="comments-container"><span id="16114"></span><div id="comment-16114" class="comment"><div id="post-16114-score" class="comment-score"></div><div class="comment-text"><p>Last year you had a different PC to capture with?</p></div><div id="comment-16114-info" class="comment-info"><span class="comment-age">(20 Nov '12, 06:28)</span> Jaap ♦</div></div><span id="16157"></span><div id="comment-16157" class="comment"><div id="post-16157-score" class="comment-score"></div><div class="comment-text"><p>Wireshark for linux operate normally with mpls! But not with os windows</p></div><div id="comment-16157-info" class="comment-info"><span class="comment-age">(21 Nov '12, 05:53)</span> Christophe85</div></div><span id="16165"></span><div id="comment-16165" class="comment"><div id="post-16165-score" class="comment-score">1</div><div class="comment-text"><p>this may be a nic driver issue then...</p></div><div id="comment-16165-info" class="comment-info"><span class="comment-age">(21 Nov '12, 08:58)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16112" class="comment-tools"></div><div class="clear"></div><div id="comment-16112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16168"></span>

<div id="answer-container-16168" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16168-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems you have changed hardware and Operating System compared to last years experiment. Especially on Windows you are very dependent on the capabilities and settings of the network card and its driver with respect to how much you can get of the original frame present on the wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '12, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16168" class="comments-container"><span id="16210"></span><div id="comment-16210" class="comment"><div id="post-16210-score" class="comment-score"></div><div class="comment-text"><p>Now with os linux is operate normally , with os window 2 stations operate normally and capture frame mpls and 2 stations exactly the same don't capture mpls frame. Probably a difference is operating mode.</p><p>i stop the analys for the year!</p><p>Thank</p></div><div id="comment-16210-info" class="comment-info"><span class="comment-age">(22 Nov '12, 05:19)</span> Christophe85</div></div></div><div id="comment-tools-16168" class="comment-tools"></div><div class="clear"></div><div id="comment-16168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

