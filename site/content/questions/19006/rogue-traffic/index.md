+++
type = "question"
title = "Rogue Traffic"
description = '''Hi , we have captured some wire shark traces from our equipment which is connected on L3 switch.  in the logs We are able to see the other devices communication/traffic (TCP messages) which is connected in same L3 switch. Is this generic ...? or gives some idea about traffic flow on L3 Switch with p...'''
date = "2013-02-28T20:31:00Z"
lastmod = "2013-03-01T09:18:00Z"
weight = 19006
keywords = [ "rogue", "traffic", "tcp" ]
aliases = [ "/questions/19006" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rogue Traffic](/questions/19006/rogue-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19006-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>we have captured some wire shark traces from our equipment which is connected on L3 switch.</p><p>in the logs We are able to see the other devices communication/traffic (TCP messages) which is connected in same L3 switch.</p><p>Is this generic ...?</p><p>or gives some idea about traffic flow on L3 Switch with protocols.</p></div><div id="question-tags" class="tags-container tags">rogue traffic tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/4d9b861e062e5c63e056d362e22108e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lokanadhareddy&#39;s gravatar image" /><p>Lokanadhareddy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lokanadhareddy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 02:33</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19006" class="comments-container"></div><div id="comment-tools-19006" class="comment-tools"></div><div class="clear"></div><div id="comment-19006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19035"></span>

<div id="answer-container-19035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this generic ?</p></blockquote><p>as I understand your question:</p><ul><li>You have a 'standard' switch (<strong>not</strong> a hub).</li><li>Your Wireshark machine is connected to a 'regular' switch port (access port).</li><li>You <strong>do</strong> see TCP traffic that is not related to your Wireshark machine</li></ul><p>If that is all true, here are my guesses</p><ul><li>You believe to have a switch, while you have a hub. In that case, you will see the <strong>whole</strong> network traffic.</li><li>The switch operates in <strong>fail-open mode</strong> and sends all packets to all ports. The reason for fail-open mode might be another system flooding the switch to be able to capture traffic. See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet.">http://wiki.wireshark.org/CaptureSetup/Ethernet.</a> In that case, you will see the <strong>whole</strong> network traffic.</li><li>The switch port you are connected to is incidentally/accidentally a SAPN/mirror port. In that case you will see whatever traffic is mirrored to that port. Please check the switch configuration</li><li>You are seeing only those TCP packets that the switch needs to flood to all ports, as its MAC/CAM table timed out the entry for those MAC addresses. In that case, you should <strong>not</strong> see the whole TCP communication, but rather single packets.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19035" class="comments-container"></div><div id="comment-tools-19035" class="comment-tools"></div><div class="clear"></div><div id="comment-19035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

