+++
type = "question"
title = "ASN2WRS does not create PDU (which is specified in .cnf file)"
description = '''Hi, I have a with creating my asn1 dissector. I used the plugin template and there is a toyasn1.cnf file included. The PDU in this file is specified:  #.PDU TOYASN1-MESSAGE In my Template i use the function : dissect_TOYASN1_MESSAGE_PDU(tvb,pinfo,toyasn1_tree) Now i have the issue, while starting wi...'''
date = "2014-09-15T23:34:00Z"
lastmod = "2014-09-16T03:05:00Z"
weight = 36352
keywords = [ "asn2wrs", "asn1", "plugin" ]
aliases = [ "/questions/36352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ASN2WRS does not create PDU (which is specified in .cnf file)](/questions/36352/asn2wrs-does-not-create-pdu-which-is-specified-in-cnf-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36352-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a with creating my asn1 dissector. I used the plugin template and there is a toyasn1.cnf file included. The PDU in this file is specified:</p><p><code>#.PDU TOYASN1-MESSAGE</code></p><p>In my Template i use the function : <code>dissect_TOYASN1_MESSAGE_PDU(tvb,pinfo,toyasn1_tree)</code></p><p>Now i have the issue, while starting wireshark i get the following error:</p><p><code>undefined Symbol: dissect_TOYASN1_MESSAGE_PDU</code></p><p>The second thing i noticed is, that there is no <code>static int hf_toyasn1_MESSAGE_PDU = -1</code> created in packet-toyasn1-hf.c</p><p>So, can someone tell me how that cnf file works? I thought i only have to put my PDU name in #.PDU and the main dissector function will be created automatically?</p></div><div id="question-tags" class="tags-container tags">asn2wrs asn1 plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '14, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/f65ac046295141d9f33ce4ac1770b5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venturina&#39;s gravatar image" /><p>Venturina<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venturina has no accepted answers">0%</span></p></div></div><div id="comments-container-36352" class="comments-container"></div><div id="comment-tools-36352" class="comment-tools"></div><div class="clear"></div><div id="comment-36352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36356"></span>

<div id="answer-container-36356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36356-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For the record this has been discussed and solved in <a href="https://www.wireshark.org/lists/wireshark-dev/201409/msg00066.html">this thread</a> on the wireshark-dev mailing list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-36356" class="comments-container"></div><div id="comment-tools-36356" class="comment-tools"></div><div class="clear"></div><div id="comment-36356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

