+++
type = "question"
title = "How to filter SNMP packets by oid?"
description = '''Has this possibility been removed? I think in previous versions it was possible to do the following filter: &quot;snmp.ObjectName == ...&quot; However, this is not supported. Also snmp.value.oid does not support the == operator. What is wrong here?'''
date = "2012-07-12T05:28:00Z"
lastmod = "2012-07-12T07:50:00Z"
weight = 12657
keywords = [ "snmp" ]
aliases = [ "/questions/12657" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter SNMP packets by oid?](/questions/12657/how-to-filter-snmp-packets-by-oid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12657-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Has this possibility been removed? I think in previous versions it was possible to do the following filter: "snmp.ObjectName == ..." However, this is not supported. Also snmp.value.oid does not support the == operator. What is wrong here?</p></div><div id="question-tags" class="tags-container tags">snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '12, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/3a1eaf8d4b730fc363d37384991b5800?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gubbanoa&#39;s gravatar image" /><p>gubbanoa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gubbanoa has no accepted answers">0%</span></p></div></div><div id="comments-container-12657" class="comments-container"></div><div id="comment-tools-12657" class="comment-tools"></div><div class="clear"></div><div id="comment-12657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12659"></span>

<div id="answer-container-12659" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12659-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>snmp.ObjectName may have changed. I can find snmp.name in Wireshark 1.8.0.</p><p>Both (snmp.name and snmp.value.oid) do work on my system (Win7_64) with Wireshark 1.8.0. I can apply filters (== and contains). I do get the expected result.</p><p>Can you please add more details (your wireshark version, system, error messages).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '12, 07:51</p></div></div><div id="comments-container-12659" class="comments-container"><span id="12695"></span><div id="comment-12695" class="comment"><div id="post-12695-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt! For instance "snmp.name == 1.3.6.1.2.1.1.2.0" does the trick, thanks. However, snmp.value.oid does not return any results. Yes my system configuration is the exact same as yours. Have a nice summer!</p></div><div id="comment-12695-info" class="comment-info"><span class="comment-age">(13 Jul '12, 00:51)</span> gubbanoa</div></div></div><div id="comment-tools-12659" class="comment-tools"></div><div class="clear"></div><div id="comment-12659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

