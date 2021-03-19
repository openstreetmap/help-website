+++
type = "question"
title = "capture on bundled port(4 port part of  etherchannel)"
description = '''Is it possible to capture on bundled ports accurately,capturing 4 gb on 1 bg interface looks not feasible but still how?'''
date = "2013-07-05T02:25:00Z"
lastmod = "2013-07-22T15:38:00Z"
weight = 22687
keywords = [ "etherchannel" ]
aliases = [ "/questions/22687" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture on bundled port(4 port part of etherchannel)](/questions/22687/capture-on-bundled-port4-port-part-of-etherchannel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22687-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to capture on bundled ports accurately,capturing 4 gb on 1 bg interface looks not feasible but still how?</p></div><div id="question-tags" class="tags-container tags">etherchannel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-22687" class="comments-container"></div><div id="comment-tools-22687" class="comment-tools"></div><div class="clear"></div><div id="comment-22687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23262"></span>

<div id="answer-container-23262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23262-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends where you want to capture.</p><p>If you want to capture on a switch, you will have a hard time, because it does not make sense to mirror 4 ports to only one capturing port, as the capturing link can be flooded in case of massive traffic. You can however use a capturing system with 4 interfaces and mirror each of the aggregated (etherchannel) ports to one mirror/monitoring port.</p><p>If you want to capture on the system that is directly connected to the switch with four adapters (aggregated by the driver - sometimes called adapter teaming), you can try to capture on the aggregated virtual device that will be provided by the driver (run <code>dumpcap -D -M</code> to see that device). Alternatively you can capture on all 4 interfaces with a recent version of Wireshark, by specifying the option -i several times.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23262" class="comments-container"></div><div id="comment-tools-23262" class="comment-tools"></div><div class="clear"></div><div id="comment-23262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

