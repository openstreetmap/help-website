+++
type = "question"
title = "does pack drop reported by tshark really means packet drop?"
description = '''Hi experts, Would this kind of cases happen? - large amounts of data coming into the NIC. The NIC was cable of processing such amounts of data, but tshark, even dumpcap was not capable of handling this.  We saw packet drop reported by tshark when capturing, does it really mean that we have data drop...'''
date = "2014-08-17T20:44:00Z"
lastmod = "2014-08-18T00:36:00Z"
weight = 35521
keywords = [ "packet_drop" ]
aliases = [ "/questions/35521" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [does pack drop reported by tshark really means packet drop?](/questions/35521/does-pack-drop-reported-by-tshark-really-means-packet-drop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35521-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts,</p><p>Would this kind of cases happen? - large amounts of data coming into the NIC. The NIC was cable of processing such amounts of data, but tshark, even dumpcap was not capable of handling this.</p><p>We saw packet drop reported by tshark when capturing, does it really mean that we have data drop here? How to determine if the packet drop reported by tshark or dumpcap is real?</p><p>thank you!</p></div><div id="question-tags" class="tags-container tags">packet_drop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '14, 20:44</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-35521" class="comments-container"></div><div id="comment-tools-35521" class="comment-tools"></div><div class="clear"></div><div id="comment-35521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35523"></span>

<div id="answer-container-35523" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35523-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually if tshark/dumpcap report dropped packets, there are dropped packets. You can manually verify this if you have lots of TCP packets, because you'll often see messages like "previous segment not captured" and "acked unseen segment". The first tells you that there is something missing (which could also be normal packet loss, of course), but the second tells you that Wireshark saw acknowledge packets for packets it doesn't have in the capture - those are usually dropped packets, as long as you have at least a few packets going both directions (otherwise you could suffer from asynchronous routing).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35523" class="comments-container"><span id="35549"></span><div id="comment-35549" class="comment"><div id="post-35549-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Sorry in advance if I misunderstood your answer above.</p><p>These two situation you mentioned could also due to huge amounts of incoming packets that tshark just cannot keep pace with it for capturing, but those packets were actually not dropped from the NIC's perspective. tshark said "I got packet drop", but the NIC do have sent the packets to the destination successfully. In this case, we cannot just conclude that we are having packets drop, right?</p></div><div id="comment-35549-info" class="comment-info"><span class="comment-age">(18 Aug '14, 22:40)</span> SteveZhou</div></div><span id="35551"></span><div id="comment-35551" class="comment"><div id="post-35551-score" class="comment-score">1</div><div class="comment-text"><p>Okay, I think you're talking about a system capturing its own traffic (which is not a good idea, but sometimes it can't be helped). You need to distinguish between the normal send/receive and the additional capture process - drops are packets missing from the <strong>capture</strong> process, not the normal NIC operation. They don't affect normal communication, so packets will be sent and received even if the capture does not pick them up.</p></div><div id="comment-35551-info" class="comment-info"><span class="comment-age">(18 Aug '14, 22:53)</span> Jasper ♦♦</div></div><span id="35554"></span><div id="comment-35554" class="comment"><div id="post-35554-score" class="comment-score"></div><div class="comment-text"><p>correct, that's what I'm talking about!</p><p>I think we can look at the captured trace and see if we got duplicate Ack and/or retransmissions. If that was the case, then we are hitting a real packet drop situation. Are you think so?</p></div><div id="comment-35554-info" class="comment-info"><span class="comment-age">(19 Aug '14, 02:39)</span> SteveZhou</div></div></div><div id="comment-tools-35523" class="comment-tools"></div><div class="clear"></div><div id="comment-35523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

