+++
type = "question"
title = "How to identify RTP delay"
description = '''Hello Forum, Assume following workflow, Client1 made a SIP call -&amp;gt; (network) -&amp;gt; clien2 We have encountered a delay in hearing the voice in client2. I have captured the RTP packets from Client1 and Client2. However I am not able to find a way to identify the delay by compering the RTP packets. ...'''
date = "2013-09-06T05:07:00Z"
lastmod = "2013-09-09T08:58:00Z"
weight = 24420
keywords = [ "rtp" ]
aliases = [ "/questions/24420" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify RTP delay](/questions/24420/how-to-identify-rtp-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Forum,</p><p>Assume following workflow, Client1 made a SIP call -&gt; (network) -&gt; clien2</p><p>We have encountered a delay in hearing the voice in client2. I have captured the RTP packets from Client1 and Client2. However I am not able to find a way to identify the delay by compering the RTP packets. May be I do not know how to do it. Please help me, how can I identify the delay by studying the packets.</p><p>Regards Rajib Siemens India.</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/457bb334d6450e55df562520a57938b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajib&#39;s gravatar image" /><p>Rajib<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajib has no accepted answers">0%</span></p></div></div><div id="comments-container-24420" class="comments-container"><span id="24434"></span><div id="comment-24434" class="comment"><div id="post-24434-score" class="comment-score"></div><div class="comment-text"><p>What does (network) constitute of? A layer 2/3 network? WAN connections? VoIP gateways?</p></div><div id="comment-24434-info" class="comment-info"><span class="comment-age">(06 Sep '13, 09:07)</span> Jaap ♦</div></div></div><div id="comment-tools-24420" class="comment-tools"></div><div class="clear"></div><div id="comment-24420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24483"></span>

<div id="answer-container-24483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24483-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>We have encountered a <strong>delay in hearing the voice in client2</strong>. I have captured the RTP packets from Client1 and Client2. However I am not able to find a way to identify the delay by compering the RTP packets.</p></blockquote><p>This could be caused by the use of jitter buffers (at the receiver) and some problems in the network (packet reodering, packet loss, varying latency). Jitter buffers are used to compensate those network problems.</p><p><strong>The advantage:</strong> You will hear the full stream, even if there is varying delay and/or out of order packets (at least to some extent)<br />
<strong>The disadvantage:</strong> The receiving device will have to delay the audio/video output for a while, until the jitter buffer fills with enough data.</p><p>If the jitter buffer is to large (buffering more than ~ 100-150 ms), you may/will hear that.</p><p>Unfortunately, you cannot see anything in the capture files, as the jitter buffer is just an internal mechanism within the receiving VoIP client.</p><p>What you might see are 'increased' values for: jitter and/or skew and/or delay and/or lost packets in the RTP statistics.</p><p>Please open the capture file taken at the receiver side (jitter can only be calculated correctly at the receiver side!) and run the following stats.</p><blockquote><p>Telephony -&gt; RTP -&gt; Show all Streams</p></blockquote><p>What are the values for <strong>Lost</strong>, <strong>Max. Delta</strong>, <strong>Mean Jitter",</strong> Max. Jitter**?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '13, 08:58</p></div></div><div id="comments-container-24483" class="comments-container"><span id="24504"></span><div id="comment-24504" class="comment"><div id="post-24504-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your inputs. I can see the following,</p><pre><code>Max delta = 155.55 ms at packet no. 6989 
Max jitter = 15.60 ms. Mean jitter = 1.29 ms.
Max skew = 142.47 ms.
Total RTP packets = 3938   (expected 3938)   Lost RTP packets = 7 (0.18%)   Sequence errors = 7 
Duration 78.60 s (158 ms clock drift, corresponding to 8016 Hz (+0.20%)</code></pre><p>Can the delay be occurred in our audio processor? We use to write the streams into six different devices after receiving it from the RTP stack.</p><p>Regards Rajib</p></div><div id="comment-24504-info" class="comment-info"><span class="comment-age">(09 Sep '13, 23:51)</span> Rajib</div></div><span id="24505"></span><div id="comment-24505" class="comment"><div id="post-24505-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can the delay be occurred in our audio processor?</p></blockquote><p>sure and I guess, the problem is more likely a software/hardware problem than a network problem.</p></div><div id="comment-24505-info" class="comment-info"><span class="comment-age">(09 Sep '13, 23:57)</span> Kurt Knochner ♦</div></div><span id="24510"></span><div id="comment-24510" class="comment"><div id="post-24510-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, Looks like the delay does not occur if we reduce the number of devices attached to our application. So we are sure, the problem is in our code. Regards Rajib</p></div><div id="comment-24510-info" class="comment-info"><span class="comment-age">(10 Sep '13, 00:49)</span> Rajib</div></div><span id="24513"></span><div id="comment-24513" class="comment"><div id="post-24513-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-24513-info" class="comment-info"><span class="comment-age">(10 Sep '13, 01:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24483" class="comment-tools"></div><div class="clear"></div><div id="comment-24483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

