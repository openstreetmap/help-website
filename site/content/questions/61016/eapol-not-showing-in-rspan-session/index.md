+++
type = "question"
title = "EAPoL not showing in RSPAN session"
description = '''Hello experts, I hope that you can help me figuring out why am I not able to see any EAPoL messages on my remote SPAN port configuration, this is my scenario: Laptop (authenticating) -- Switch1 -- Switch2 -- Laptop (Monitor) For more detail scenario Laptop -- &amp;lt;port g0=&quot;&quot; 2=&quot;&quot;&amp;gt; Switch1 (Cisco 3...'''
date = "2017-04-24T11:37:00Z"
lastmod = "2017-04-24T13:47:00Z"
weight = 61016
keywords = [ "eapol" ]
aliases = [ "/questions/61016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [EAPoL not showing in RSPAN session](/questions/61016/eapol-not-showing-in-rspan-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello experts,</p><p>I hope that you can help me figuring out why am I not able to see any EAPoL messages on my remote SPAN port configuration, this is my scenario:</p><p>Laptop (authenticating) -- Switch1 -- Switch2 -- Laptop (Monitor)</p><p>For more detail scenario Laptop -- &lt;port g0="" 2=""&gt; Switch1 (Cisco 3560-CG) &lt;port g0="" 10=""&gt; -- &lt;port g1="" 0="" 15=""&gt; Switch2 (Cisco 3750G) &lt;port g2="" 0="" 2=""&gt;</p><p>The configuration from switch1: monitor session 1 source interface Gi0/1 - 7 monitor session 1 destination remote vlan 101</p><p>The configuration from Switch2: monitor session 2 destination interface Gi2/0/2 monitor session 2 source remote vlan 101</p><p>AS you can see I'm using remote span configuration and using remote vlan 101 to carry all my traffic.</p><p>When I turn on tshark or wireshark and make a filter eapol or eth.type == 0x888e I can't see anything, no packets coming to that port.</p><p>Now what's important to mention is that if I use a local port on the 3560-CG, without any remote span am able to see all the packets, eapol and eth.type... What am I missing, should the cisco SPAN port forward all packets? There are no other commands for the cisco to configure special fields.</p><p>Thanks and I hope that someone can help me.</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '17, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/fe3fd7a72e9a708a6467f0b25caac329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="payala&#39;s gravatar image" /><p>payala<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="payala has no accepted answers">0%</span></p></div></div><div id="comments-container-61016" class="comments-container"></div><div id="comment-tools-61016" class="comment-tools"></div><div class="clear"></div><div id="comment-61016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61021"></span>

<div id="answer-container-61021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61021-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would seriously look into the details of the Cisco equipment at hand. EAPoL is specifically destined for 'The Nearest Bridge', that means your switch port. With a local monitor port it's probably capable of capturing frames low enough near the Phy to get even the EAPoL frames, while an RSPAN probably latches on to the switching fabric, where EAPoL frames are nowhere to be found.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61021" class="comments-container"><span id="61369"></span><div id="comment-61369" class="comment"><div id="post-61369-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the clarification, now makes sense. If I want to check EAPoL messages then I should make them locally, there is no way to transport over RSPAN or ERSPAN. Thanks again</p></div><div id="comment-61369-info" class="comment-info"><span class="comment-age">(12 May '17, 07:33)</span> payala</div></div></div><div id="comment-tools-61021" class="comment-tools"></div><div class="clear"></div><div id="comment-61021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

