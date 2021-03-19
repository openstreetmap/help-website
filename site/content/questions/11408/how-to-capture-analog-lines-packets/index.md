+++
type = "question"
title = "how to capture analog lines packets?"
description = '''Can I use wireshark to capture analog lines&#x27; voice traffic? And if yes, how?'''
date = "2012-05-27T12:50:00Z"
lastmod = "2012-05-27T13:22:00Z"
weight = 11408
keywords = [ "wireshark", "analog", "mark" ]
aliases = [ "/questions/11408" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture analog lines packets?](/questions/11408/how-to-capture-analog-lines-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use wireshark to capture analog lines' voice traffic? And if yes, how?</p></div><div id="question-tags" class="tags-container tags">wireshark analog mark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '12, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/2e9ca7d554f1c1cdf7d66d6827884742?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markkarp&#39;s gravatar image" /><p>markkarp<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markkarp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '12, 13:02</p></div></div><div id="comments-container-11408" class="comments-container"></div><div id="comment-tools-11408" class="comment-tools"></div><div class="clear"></div><div id="comment-11408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11410"></span>

<div id="answer-container-11410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a network sniffer. To sniff analog phone lines, you would need a device that "captures" data on those lines and converts it to something wireshark can read. There are several call recording tools available on the market, however I don't know if they can export the captured data in a wireshark readable format (e.g. SIP/RTP). Search google for: <strong>analog call recording</strong>.</p><p>However, you could connect your analog phone to a VoIP adapter and then sniff the Voip traffic.</p><p><a href="http://www.voiplink.com/VoIP_Adapter_s/3.htm">http://www.voiplink.com/VoIP_Adapter_s/3.htm</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '12, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '12, 13:24</p></div></div><div id="comments-container-11410" class="comments-container"><span id="11431"></span><div id="comment-11431" class="comment"><div id="post-11431-score" class="comment-score"></div><div class="comment-text"><p>thank you Kurt</p></div><div id="comment-11431-info" class="comment-info"><span class="comment-age">(28 May '12, 20:59)</span> markkarp</div></div></div><div id="comment-tools-11410" class="comment-tools"></div><div class="clear"></div><div id="comment-11410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

