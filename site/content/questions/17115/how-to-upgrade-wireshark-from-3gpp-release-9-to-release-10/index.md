+++
type = "question"
title = "How to upgrade wireshark from 3gpp release 9 to release 10?"
description = '''I want to upgrade my wireshark to support LTE Release 10. Please guide me how to start ?'''
date = "2012-12-20T21:11:00Z"
lastmod = "2013-01-15T15:11:00Z"
weight = 17115
keywords = [ "3gpp", "release10", "lte" ]
aliases = [ "/questions/17115" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to upgrade wireshark from 3gpp release 9 to release 10?](/questions/17115/how-to-upgrade-wireshark-from-3gpp-release-9-to-release-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to upgrade my wireshark to support LTE Release 10. Please guide me how to start ?</p></div><div id="question-tags" class="tags-container tags">3gpp release10 lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '12, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/35b8afb49fb326994d65a5125c7d60dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scorp&#39;s gravatar image" /><p>Scorp<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scorp has no accepted answers">0%</span></p></div></div><div id="comments-container-17115" class="comments-container"></div><div id="comment-tools-17115" class="comment-tools"></div><div class="clear"></div><div id="comment-17115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17121"></span>

<div id="answer-container-17121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17121-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I think the development version mostly does that. But basically you would have to compare all the dissectors for the LTE protocols with the respective protocol specification and make updates where needed. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-17121" class="comments-container"><span id="17218"></span><div id="comment-17218" class="comment"><div id="post-17218-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Anders.If I wish to upgrade only the ASN1 from one release to another, I will upgrade the packet-lte-rrc.c and the same for s1ap and x2ap. Will any change be required in packet-mac-lte.c/packet-pdcp-lte.c/packet-rlc-lte.c</p></div><div id="comment-17218-info" class="comment-info"><span class="comment-age">(23 Dec '12, 23:02)</span> Scorp</div></div><span id="17219"></span><div id="comment-17219" class="comment"><div id="post-17219-score" class="comment-score"></div><div class="comment-text"><p>I don't know, but probably. You would have to check.</p></div><div id="comment-17219-info" class="comment-info"><span class="comment-age">(23 Dec '12, 23:47)</span> Anders ♦</div></div></div><div id="comment-tools-17121" class="comment-tools"></div><div class="clear"></div><div id="comment-17121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17707"></span>

<div id="answer-container-17707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17707-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>NAS EPS/RRC/PDCP/RLC/MAC LTE dissectors are already Release 11 compliant in current development version. S1AP and X2AP dissectors are still based on v10.3.0.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '13, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-17707" class="comments-container"></div><div id="comment-tools-17707" class="comment-tools"></div><div class="clear"></div><div id="comment-17707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

