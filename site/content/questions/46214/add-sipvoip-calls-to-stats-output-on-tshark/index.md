+++
type = "question"
title = "Add sip,voip-calls to stats output on tshark"
description = '''Tshark is able to produce stats from a capture file using the -z switch. One of these options is &#x27;sip,stat&#x27; where it gives a break down of SIP methods/responses seen in the file. I would like to request that a new option be added &#x27;sip,voip-calls&#x27; that produces a similar output to the &#x27;Telephony - VO...'''
date = "2015-09-28T03:19:00Z"
lastmod = "2015-09-28T07:36:00Z"
weight = 46214
keywords = [ "voipcalls", "feature-request", "tshark" ]
aliases = [ "/questions/46214" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Add sip,voip-calls to stats output on tshark](/questions/46214/add-sipvoip-calls-to-stats-output-on-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46214-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tshark is able to produce stats from a capture file using the -z switch. One of these options is 'sip,stat' where it gives a break down of SIP methods/responses seen in the file. I would like to request that a new option be added 'sip,voip-calls' that produces a similar output to the 'Telephony - VOIP Calls' option in the Wireshark application, and produce a list of SIP calls discovered in the file and their call state. The logic to do this is already there in Wireshark, I would just like this logic applied in TShark also please. Pretty please?</p></div><div id="question-tags" class="tags-container tags">voipcalls feature-request tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '15, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/13434718a8ed6f82f6c90be14d9acec6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boidy&#39;s gravatar image" /><p>Boidy<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boidy has no accepted answers">0%</span></p></div></div><div id="comments-container-46214" class="comments-container"></div><div id="comment-tools-46214" class="comment-tools"></div><div class="clear"></div><div id="comment-46214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46219"></span>

<div id="answer-container-46219" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46219-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check for an existing request first, and if not found raise an "enhancement" request on the Wireshark <a href="https://bugs.wireshark.org/">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46219" class="comments-container"><span id="46222"></span><div id="comment-46222" class="comment"><div id="post-46222-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham. I hadn't realised that was the preferred channel for enhancement requests. Last time I requested an enhancement it was in a hot tub in Mountain View :o) I've added my '+1' to the enhancement request on bugzilla now.</p><p>Thanks.</p></div><div id="comment-46222-info" class="comment-info"><span class="comment-age">(28 Sep '15, 09:08)</span> Boidy</div></div></div><div id="comment-tools-46219" class="comment-tools"></div><div class="clear"></div><div id="comment-46219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

