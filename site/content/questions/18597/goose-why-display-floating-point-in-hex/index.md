+++
type = "question"
title = "GOOSE: Why display floating-point in hex?"
description = '''Feature request: When displaying the data of a GOOSE packet, could you please display the value of the floating number to the right of the hex value? I have to admit I am a little slow to convert in my head so I can see that 0840600000 is f3.5 :=) Thanks'''
date = "2013-02-13T09:05:00Z"
lastmod = "2013-02-13T09:12:00Z"
weight = 18597
keywords = [ "floating", "display", "point" ]
aliases = [ "/questions/18597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GOOSE: Why display floating-point in hex?](/questions/18597/goose-why-display-floating-point-in-hex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18597-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Feature request:</p><p>When displaying the data of a GOOSE packet, could you please display the value of the floating number to the right of the hex value? I have to admit I am a little slow to convert in my head so I can see that 0840600000 is f3.5 :=)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">floating display point</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/4025240b8c0475c260d9cb7529e827c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecs1749&#39;s gravatar image" /><p>ecs1749<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecs1749 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '13, 10:07</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-18597" class="comments-container"></div><div id="comment-tools-18597" class="comment-tools"></div><div class="clear"></div><div id="comment-18597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18599"></span>

<div id="answer-container-18599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18599-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To request a new feature, go to <a href="https://bugs.wireshark.org/bugzilla/">the Wireshark bugzilla</a> and enter an enhancement request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-18599" class="comments-container"><span id="18607"></span><div id="comment-18607" class="comment"><div id="post-18607-score" class="comment-score"></div><div class="comment-text"><p>I guess it's this defenition in the Goose asn1 specification. FloatingPoint ::= OCTET STRING as it's defined as OCTET STRING it will be displayed in hex. One could pssibly redifine the field in the .cnf file to FT_FLOAT but as there is no size constraint the OCTET STRING can be of arbitarry length.</p></div><div id="comment-18607-info" class="comment-info"><span class="comment-age">(13 Feb '13, 11:37)</span> Anders ♦</div></div><span id="18661"></span><div id="comment-18661" class="comment"><div id="post-18661-score" class="comment-score"></div><div class="comment-text"><p>Which .cnf file? I am pretty new to GOOSE &amp; Wireshark in general. What I am seeing when I look at the goosePdu -&gt; allData, it displays something like Data: floating-point (7) and then "floating-point: 0840900000". Now, it's obvious to me Wireshark knows it's a float and that the value is 4090 0000. Why can it just say: "floating-point: 0840900000 (+4.500000e+00)"?</p></div><div id="comment-18661-info" class="comment-info"><span class="comment-age">(15 Feb '13, 09:47)</span> ecs1749</div></div><span id="18666"></span><div id="comment-18666" class="comment"><div id="post-18666-score" class="comment-score"></div><div class="comment-text"><p>The GOOSE dissector in Wireshark is auto-generated from an asn1 definition of the protocol. As @Anders says, in that definition it defines FloatingPoint types as an unlimited length string of bytes.</p><p>The .cnf file allows "overrides" of the definition but as it appears to be of unlimited length it might not be correct to just do that.</p><p>Someone with access to the (not free) protocol spec (IEC61850-x-x) should check the latest definition of the type.</p><p>Note there there also seems to be issues on this type: <a href="http://tissues.iec61850.com/tissue.mspx?issueid=817">http://tissues.iec61850.com/tissue.mspx?issueid=817</a></p></div><div id="comment-18666-info" class="comment-info"><span class="comment-age">(16 Feb '13, 00:09)</span> grahamb ♦</div></div></div><div id="comment-tools-18599" class="comment-tools"></div><div class="clear"></div><div id="comment-18599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

