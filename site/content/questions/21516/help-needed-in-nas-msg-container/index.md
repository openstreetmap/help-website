+++
type = "question"
title = "Help needed in NAS msg container"
description = '''I am using wireshark Version 1.8.7. In case of SGsAP Uplink Unitdata or SGsAP Downlink Unitdata packet in NAS msg container IE for TP-MTI in TPDU SMS-SUBMIT-REPORT the spec says the field TP-Failure-Cause is mandatory.But the wireshark does not show so.It never show TP-Failure-Causs field.Is it righ...'''
date = "2013-05-28T00:56:00Z"
lastmod = "2013-05-28T20:51:00Z"
weight = 21516
keywords = [ "nas", "message", "container" ]
aliases = [ "/questions/21516" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help needed in NAS msg container](/questions/21516/help-needed-in-nas-msg-container)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark Version 1.8.7. In case of SGsAP Uplink Unitdata or SGsAP Downlink Unitdata packet in NAS msg container IE for TP-MTI in TPDU SMS-SUBMIT-REPORT the spec says the field TP-Failure-Cause is mandatory.But the wireshark does not show so.It never show TP-Failure-Causs field.Is it right?</p></div><div id="question-tags" class="tags-container tags">nas message container</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '13, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/5aae92c75bcf159f9da5092d5e7e99a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swap&#39;s gravatar image" /><p>swap<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swap has no accepted answers">0%</span></p></div></div><div id="comments-container-21516" class="comments-container"></div><div id="comment-tools-21516" class="comment-tools"></div><div class="clear"></div><div id="comment-21516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21518"></span>

<div id="answer-container-21518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21518-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TP-Failure-Cause field is only present in case of RP-ERROR. In case of RP-ACK it is not present. Are you in the RP-ERROR case? Can you share a pcap file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-21518" class="comments-container"></div><div id="comment-tools-21518" class="comment-tools"></div><div class="clear"></div><div id="comment-21518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21551"></span>

<div id="answer-container-21551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21551-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is the specific scenario being referenced? As per 3GPP TS 23.040 section 9.2.2.2, Pascal is correct on spec (TP-Failure-Cause is only mandatory in SMS-SUBMIT-REPORT for RP-ERROR). First I suggest you double-check the message container to see if it falls under the IE breakdown of 9.2.2.2a(i) or 9.2.2.2a(ii) tables in 3GPP TS 23.040.</p><p>Barring that, you mention this is specific to an SGs interface trace. Have you followed this message through at a MAP level, or compared it to an unciphered NAS message container from an S1-MME or Iu trace to say that a TP-Failure-Cause was being decoded by Wireshark elsewhere for this NAS message? The .pcaps would be very helpful here if you are able to share them though considering this is carrier SMS I'm guessing you cannot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21551" class="comments-container"></div><div id="comment-tools-21551" class="comment-tools"></div><div class="clear"></div><div id="comment-21551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

