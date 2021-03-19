+++
type = "question"
title = "G723 or G723.1 over RTP"
description = '''hi. Is wireshark support G723.1 over RTP?in RTP protocol , payloay.type ==4 assign for g723 or g723.1? '''
date = "2017-05-30T02:33:00Z"
lastmod = "2017-05-30T02:58:00Z"
weight = 61691
keywords = [ "g723", "rtp", "g723.1" ]
aliases = [ "/questions/61691" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [G723 or G723.1 over RTP](/questions/61691/g723-or-g7231-over-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61691-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi. Is wireshark support G723.1 over RTP?in RTP protocol , payloay.type ==4 assign for g723 or g723.1?</p></div><div id="question-tags" class="tags-container tags">g723 rtp g723.1</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '17, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '17, 06:10</p></div></div><div id="comments-container-61691" class="comments-container"></div><div id="comment-tools-61691" class="comment-tools"></div><div class="clear"></div><div id="comment-61691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61692"></span>

<div id="answer-container-61692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61692-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Currently? No. In future, maybe.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '17, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61692" class="comments-container"><span id="61694"></span><div id="comment-61694" class="comment"><div id="post-61694-score" class="comment-score"></div><div class="comment-text"><p>thank you. i see if payloay.type ==4(G.723) then after RTP, G723.1 dissect remaining data? is it correct? in packet-g723.c i see :</p><p>dissector_add_uint("rtp.pt", PT_G723, g723_handle);</p><p>col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, "G.723.1");</p><p>in RTP protocol , payloay.type ==4 assign for g723 or g723.1?</p></div><div id="comment-61694-info" class="comment-info"><span class="comment-age">(30 May '17, 04:16)</span> ghader</div></div></div><div id="comment-tools-61692" class="comment-tools"></div><div class="clear"></div><div id="comment-61692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

