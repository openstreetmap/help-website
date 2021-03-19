+++
type = "question"
title = "VOIP quality issues----how do I use wireshark to identify the problem"
description = '''Dear All, I work with for a TDM/VOIP carrier and I have this customer who complains about quality issues on our TDM/VOIP switch which interconnects with his on VOIP switch over IP. My boss has adviced me to use wireshark to determine if the issue is with our ISP provider. We have a 100G connection t...'''
date = "2011-06-03T05:15:00Z"
lastmod = "2011-06-04T20:33:00Z"
weight = 4362
keywords = [ "beginner", "voip", "troubleshooting" ]
aliases = [ "/questions/4362" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VOIP quality issues----how do I use wireshark to identify the problem](/questions/4362/voip-quality-issues-how-do-i-use-wireshark-to-identify-the-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>I work with for a TDM/VOIP carrier and I have this customer who complains about quality issues on our TDM/VOIP switch which interconnects with his on VOIP switch over IP. My boss has adviced me to use wireshark to determine if the issue is with our ISP provider. We have a 100G connection to our ISP but his thinking we might be having some bandwidth or latency issues. I am new to wireshark and don't know how to go about it. Please can you help me? I have installed wireshark on my PC in the office.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">beginner voip troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '11, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/db05b98c5a90e043c071ee620a50520c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dollyp&#39;s gravatar image" /><p>dollyp<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dollyp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 04 Jun '11, 17:09</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4362" class="comments-container"></div><div id="comment-tools-4362" class="comment-tools"></div><div class="clear"></div><div id="comment-4362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4378"></span>

<div id="answer-container-4378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4378-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>100G ? I hope that is a typo because at that rate you need very expensive capture solutions.</p><p>In general, at high speeds such investigations are a mix of traffic analysis followed by protocol analysis. Wireshark is a bit level protocol analyzer. So it is a fairly big hammer to bring on as a first tool when dealing with network performance issues.</p><p>First check if there are any issues at the traffic level. Monitor the link using a tool like ntop/trisul and verify if the end customer is 1) getting adequate bandwidth and 2) if there is unwanted (other) traffic on the link that is causing the voip traffic to be squeezed out. In order to do this, you can either enable port spanning or netflow on your end. At 100G port spanning is not feasible so Netflow is the way to go. You may have to monitor for an hour or two around the time when the customer usually complains.</p><p>Once traffic issues are ruled out, use Wireshark to dive into the protocol level. You can use a capture filter to do so. Again if you are on 10x10G things get a lot more complicated. In Wireshark you can view a list of calls and plot jitter/throughput and take it from there. You can also debug signalling issues with wireshark, maybe the end points are failing to negotiate a wideband codec or something like that.</p><p>HTH,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '11, 20:33</strong></p><img src="https://secure.gravatar.com/avatar/69ac745d2d90272605b1847ea5fe451f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vivekrj&#39;s gravatar image" /><p>vivekrj<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vivekrj has no accepted answers">0%</span></p></div></div><div id="comments-container-4378" class="comments-container"></div><div id="comment-tools-4378" class="comment-tools"></div><div class="clear"></div><div id="comment-4378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

