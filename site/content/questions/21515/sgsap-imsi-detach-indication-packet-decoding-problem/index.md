+++
type = "question"
title = "SGsAP IMSI DETACH INDICATION packet decoding problem"
description = '''I am using Wireshark Version 1.8.7. In SGsAP IMSI DETACH INDICATION packet in IMSI detach from non-EPS service type IE the IEI and length is correct but the content is wrong.It says IMSI detach from EPS service type: UE initiated IMSI detach from EPS services (2),but it should be IMSI detach from No...'''
date = "2013-05-28T00:49:00Z"
lastmod = "2013-05-28T02:45:00Z"
weight = 21515
keywords = [ "sgsap" ]
aliases = [ "/questions/21515" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SGsAP IMSI DETACH INDICATION packet decoding problem](/questions/21515/sgsap-imsi-detach-indication-packet-decoding-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark Version 1.8.7. In SGsAP IMSI DETACH INDICATION packet in IMSI detach from non-EPS service type IE the IEI and length is correct but the content is wrong.It says IMSI detach from EPS service type: UE initiated IMSI detach from EPS services (2),but it should be IMSI detach from Non EPS service type: Combined UE initiated IMSI detach from EPS and Non EPS services (2).</p><p>Please look into this.</p></div><div id="question-tags" class="tags-container tags">sgsap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '13, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/5aae92c75bcf159f9da5092d5e7e99a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swap&#39;s gravatar image" /><p>swap<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swap has no accepted answers">0%</span></p></div></div><div id="comments-container-21515" class="comments-container"></div><div id="comment-tools-21515" class="comment-tools"></div><div class="clear"></div><div id="comment-21515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21517"></span>

<div id="answer-container-21517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21517-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>this bug is fixed in Wireshark 1.10.0rc2 and I just added it to the backport list for 1.8.8 and 1.6.16. In the meantime i suggest you to switch to 1.10.0 release candidate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-21517" class="comments-container"></div><div id="comment-tools-21517" class="comment-tools"></div><div class="clear"></div><div id="comment-21517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

