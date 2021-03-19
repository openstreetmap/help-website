+++
type = "question"
title = "Tick interval question"
description = '''Hello. I am doing some testing of UDP video streams that are being multicasted. I am playing back 8 streams while capturing with wireshark. When I generate an IO graph using a tick interval of 1sec, I get the expected avg of just under 140Mbps (8 streams @ ~17Mbps each). I am playing around with the...'''
date = "2012-12-26T11:57:00Z"
lastmod = "2012-12-26T11:57:00Z"
weight = 17245
keywords = [ "graph", "bandwidth", "video", "bandwidthutilization" ]
aliases = [ "/questions/17245" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tick interval question](/questions/17245/tick-interval-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17245-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I am doing some testing of UDP video streams that are being multicasted. I am playing back 8 streams while capturing with wireshark. When I generate an IO graph using a tick interval of 1sec, I get the expected avg of just under 140Mbps (8 streams @ ~17Mbps each). I am playing around with the tick interval and I don't understand why the bandwidth seems to increase with every decrease of the tick interval? So if I set the tick interval to .001, I am seeing spikes well over 1 000 000 bits. If I understand the relationship between bits and tick interval that equals 1 000 000 000 bits/second, or 1Gbps. If this is incorrect could somebody please set me straight on this? If it is correct, how is this possible, since the video streams really shouldn't be going anywhere near that high, and to boot my NIC is only 1Gbps. I'm very confused here.</p><p>Thanks! Mike</p></div><div id="question-tags" class="tags-container tags">graph bandwidth video bandwidthutilization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '12, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/25d5676bb1d93e3f4c72b25a63439d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acedreds&#39;s gravatar image" /><p>acedreds<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acedreds has no accepted answers">0%</span></p></div></div><div id="comments-container-17245" class="comments-container"><span id="17259"></span><div id="comment-17259" class="comment"><div id="post-17259-score" class="comment-score"></div><div class="comment-text"><p>can you please post the screenshots for the intervals of 1,0.1,0.001?</p><p>BTW: What is your Wireshark version and OS (wireshark -v)?</p></div><div id="comment-17259-info" class="comment-info"><span class="comment-age">(27 Dec '12, 01:34)</span> Kurt Knochner ♦</div></div><span id="17403"></span><div id="comment-17403" class="comment"><div id="post-17403-score" class="comment-score"></div><div class="comment-text"><p>Mike, remember, there are only two utilization states. Zero percent utilized and 100% utilized. Either the packet is on the wire, or it's not. So as you make your avg interval smaller, the utilization will go up. I can't speak for the validity of the graph in Wireshark, but the fact that utilization goes up when you average it over a smaller time slot is perfectly normal and expected. Google for "network microburst" and you will get a more detailed answer.</p></div><div id="comment-17403-info" class="comment-info"><span class="comment-age">(02 Jan '13, 16:26)</span> hansangb</div></div></div><div id="comment-tools-17245" class="comment-tools"></div><div class="clear"></div><div id="comment-17245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

