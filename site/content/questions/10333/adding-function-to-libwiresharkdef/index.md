+++
type = "question"
title = "Adding function to libwireshark.def"
description = '''Hi,  Is it possible to add to file &#x27;libwireshark.def&#x27; function &#x27;de_ms_cm_3 &#x27; as there are &#x27;de_ms_cm_1 &#x27; and &#x27;de_ms_cm_2 &#x27;? Symbol &#x27;_de_ms_cm_3 &#x27; isn&#x27;t appears in &#x27;wireshark.lib&#x27; and since I was linking with this library I&#x27;ve got error below. packet-rrc.obj : error LNK2019: unresolved external symbol...'''
date = "2012-04-20T01:54:00Z"
lastmod = "2012-04-20T02:35:00Z"
weight = 10333
keywords = [ "radek" ]
aliases = [ "/questions/10333" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding function to libwireshark.def](/questions/10333/adding-function-to-libwiresharkdef)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10333-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Is it possible to add to file 'libwireshark.def' function 'de_ms_cm_3 ' as there are 'de_ms_cm_1 ' and 'de_ms_cm_2 '? Symbol '_de_ms_cm_3 ' isn't appears in 'wireshark.lib' and since I was linking with this library I've got error below.</p><p>packet-rrc.obj : error LNK2019: unresolved external symbol _de_ms_cm_3 referenced in function _dissect_rrc_GSM_Classmark3</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">radek</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '12, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/d610ed43d63bbfc938588c89d3e62224?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ringo&#39;s gravatar image" /><p>ringo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ringo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Apr '12, 01:55</p></div></div><div id="comments-container-10333" class="comments-container"></div><div id="comment-tools-10333" class="comment-tools"></div><div class="clear"></div><div id="comment-10333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10338"></span>

<div id="answer-container-10338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10338-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've added this and committed it in r42154.</p><p>Note that Ask Wireshark isn't really the place for this sort of request, better to email the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">dev</a> mailing list, or raise an enhancement request on the Wireshark <a href="https://bugs.wireshark.org/">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10338" class="comments-container"></div><div id="comment-tools-10338" class="comment-tools"></div><div class="clear"></div><div id="comment-10338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

