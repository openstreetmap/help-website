+++
type = "question"
title = "Foundry FDP Capture Filter"
description = '''I have found a capture filter for CDP and was hoping this would work for FDP too. Can you help me find one that will work for FDP please. The CDP one which works is : ether[12:2] &amp;lt;= 1500 &amp;amp;&amp;amp; ether[14:2] == 0xAAAA &amp;amp;&amp;amp; ether[16:1] == 0x03 &amp;amp;&amp;amp;  ether[17:2] == 0x0000 &amp;amp;&amp;amp; e...'''
date = "2013-11-26T09:56:00Z"
lastmod = "2013-11-26T14:29:00Z"
weight = 27436
keywords = [ "fdp", "capture-filter", "capture" ]
aliases = [ "/questions/27436" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Foundry FDP Capture Filter](/questions/27436/foundry-fdp-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27436-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found a capture filter for CDP and was hoping this would work for FDP too. Can you help me find one that will work for FDP please. The CDP one which works is : ether[12:2] &lt;= 1500 &amp;&amp; ether[14:2] == 0xAAAA &amp;&amp; ether[16:1] == 0x03 &amp;&amp; ether[17:2] == 0x0000 &amp;&amp; ether[19:1] == 0x0C &amp;&amp; ether[20:2] == 0x2000</p><p>thanks</p><p>Chris Chambers BBC London</p></div><div id="question-tags" class="tags-container tags">fdp capture-filter capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/2f699de077f665e0954acdf06703bc06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20C&#39;s gravatar image" /><p>Chris C<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris C has no accepted answers">0%</span></p></div></div><div id="comments-container-27436" class="comments-container"><span id="27440"></span><div id="comment-27440" class="comment"><div id="post-27440-score" class="comment-score">1</div><div class="comment-text"><p>If you can provide a capture file (with some frames, not just one), someone here might be able to help.</p></div><div id="comment-27440-info" class="comment-info"><span class="comment-age">(26 Nov '13, 10:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27436" class="comment-tools"></div><div class="clear"></div><div id="comment-27436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27453"></span>

<div id="answer-container-27453" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27453-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That filter is checking for SNAP frames with an OUI of 00:00:0C and a PID of 0x2000.</p><p>For FDP, the OUI is 00:E0:52, which is an OUI for Foundry, and the PID is again 0x2000.</p><p>Therefore, the filter would be</p><pre><code>ether[12:2] &lt;= 1500 &amp;&amp; ether[14:2] == 0xAAAA &amp;&amp; ether[16:1] == 0x03 &amp;&amp; ether[17:2] == 0x00E0 &amp;&amp; ether[19:1] == 0x52 &amp;&amp; ether[20:2] == 0x2000</code></pre><p>(I really need to add a "snap" filter primitive to libpcap, so you can do something such as "snap 00:e0:52-2000" or something such as that, or maybe "snapoui 00:e0:52 snappid 0x2000", in a capture filter.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27453" class="comments-container"><span id="27454"></span><div id="comment-27454" class="comment"><div id="post-27454-score" class="comment-score">1</div><div class="comment-text"><p>(BTW, some slightly more efficient filters would be</p><pre><code>ether[12:2] &lt;= 1500 &amp;&amp; ether[14:4] == 0xAAAA0300 &amp;&amp; ether[18:4] == 0x000C2000</code></pre><p>for CDP and</p><pre><code>ether[12:2] &lt;= 1500 &amp;&amp; ether[14:4] == 0xAAAA0300 &amp;&amp; ether[18:4] == 0xE0522000</code></pre><p>for FDP - fewer BPF instructions interpreted per packet, but that might not make a huge difference in capture performance.)</p></div><div id="comment-27454-info" class="comment-info"><span class="comment-age">(26 Nov '13, 14:31)</span> Guy Harris ♦♦</div></div><span id="27703"></span><div id="comment-27703" class="comment"><div id="post-27703-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy, all working perfectly, much appreciated</p></div><div id="comment-27703-info" class="comment-info"><span class="comment-age">(03 Dec '13, 05:38)</span> Chris C</div></div><span id="27705"></span><div id="comment-27705" class="comment"><div id="post-27705-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-27705-info" class="comment-info"><span class="comment-age">(03 Dec '13, 05:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27453" class="comment-tools"></div><div class="clear"></div><div id="comment-27453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

