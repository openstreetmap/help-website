+++
type = "question"
title = "CCX sniffing"
description = '''Does the AirPcap and wireshark sniff CCX? or do you need the upgraded AirPcap NX?'''
date = "2011-07-05T07:10:00Z"
lastmod = "2011-07-06T16:38:00Z"
weight = 4905
keywords = [ "ccx" ]
aliases = [ "/questions/4905" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CCX sniffing](/questions/4905/ccx-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does the AirPcap and wireshark sniff CCX? or do you need the upgraded AirPcap NX?</p></div><div id="question-tags" class="tags-container tags">ccx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/91e210367995c3353d652b7b0f745381?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aplatek&#39;s gravatar image" /><p>aplatek<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aplatek has no accepted answers">0%</span></p></div></div><div id="comments-container-4905" class="comments-container"></div><div id="comment-tools-4905" class="comment-tools"></div><div class="clear"></div><div id="comment-4905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4937"></span>

<div id="answer-container-4937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4937-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I presume CCX are <a href="http://www.cisco.com/web/partners/pr46/pr147/partners_pgm_concept_home.html">Cisco Compatible eXtensions</a> rather than, say, the <a href="https://www.theice.com/ccx.jhtml">Chicago Climate eXchange</a> or <a href="http://www.koenigsegg.com/our-cars-yesterday/all-cars/ccx/">this little economy car</a>.</p><p>It sounds as if, at the network protocol layer, CCX is just some additional protocols and additions to existing Wi-Fi protocols, so any device capable of receiving arbitrary 802.11 packets, such as an AirPcap device, could capture that traffic. Whether Wireshark can <em>recognize</em> those extensions and dissect them, rather than just showing them as unknown protocols/TLVs/etc., is another matter.</p><p>What the AirPcap Nx provides is support for 802.11n; you won't be able to capture on an 802.11n network with an AirPcap Classic or AirPcap Tx, regardless of whether CCX is being used on the network or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4937" class="comments-container"></div><div id="comment-tools-4937" class="comment-tools"></div><div class="clear"></div><div id="comment-4937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

