+++
type = "question"
title = "I can get GVCP packet,but I can not get GVSP packet"
description = '''Hi, I am trying to dissect the ethernet (GVSP) packets coming from GigE vision camera. I use wirshark version 2.0.3 with windows 7 64bit.When I open the GigE vision camera, I can get a lot of GVCP packet, but I can not get GVSP packet when the image upload normally.I have seen a solution(https://ask...'''
date = "2016-08-10T03:23:00Z"
lastmod = "2016-08-10T03:23:00Z"
weight = 54714
keywords = [ "gige", "gvcp", "gvsp" ]
aliases = [ "/questions/54714" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I can get GVCP packet,but I can not get GVSP packet](/questions/54714/i-can-get-gvcp-packetbut-i-can-not-get-gvsp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to dissect the ethernet (GVSP) packets coming from GigE vision camera. I use wirshark version 2.0.3 with windows 7 64bit.When I open the GigE vision camera, I can get a lot of GVCP packet, but I can not get GVSP packet when the image upload normally.I have seen a solution(<a href="https://ask.wireshark.org/questions/46869/adding-c-dissector-to-wireshark),but">https://ask.wireshark.org/questions/46869/adding-c-dissector-to-wireshark),but</a> I still do not konw how to do.</p></div><div id="question-tags" class="tags-container tags">gige gvcp gvsp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '16, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/7d722022dd5811563b569e753676953c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yyz1988&#39;s gravatar image" /><p>yyz1988<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yyz1988 has no accepted answers">0%</span></p></div></div><div id="comments-container-54714" class="comments-container"><span id="54715"></span><div id="comment-54715" class="comment"><div id="post-54715-score" class="comment-score"></div><div class="comment-text"><p>A step-by-step instruction for what @Pascal Quantin wrote in the answer you refer to:</p><ul><li><p>right-click a packet in the packet list which is dissected as GVCP while you know it is a GVSP one, and choose <code>Decode as</code> from the context menu which appears. Doing so will open a new window.</p></li><li><p>in the table in that window, there should be a single line which begins with <code>UDP port</code> in column <code>Field</code>, while the last column, <code>Current</code>, is empty. Choose <code>GVSP</code> from the drop-down menu in that column, and press <code>OK</code>.</p></li></ul><p>After that, the packets previously dissected as GVCP should be dissected as GVSP.</p></div><div id="comment-54715-info" class="comment-info"><span class="comment-age">(10 Aug '16, 03:37)</span> sindy</div></div></div><div id="comment-tools-54714" class="comment-tools"></div><div class="clear"></div><div id="comment-54714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

