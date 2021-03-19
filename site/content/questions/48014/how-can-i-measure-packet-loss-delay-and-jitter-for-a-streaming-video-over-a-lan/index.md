+++
type = "question"
title = "How can I measure packet loss, delay and jitter for a streaming video over a LAN?"
description = '''Hi.! if anyone can help me, exactly I need to know how to measure parameters such as packet loss, jitter and delay over a LAN on which runs the service streaming video, as currently I tried filtering UDP packets and when analyzing the statistics and the summary does not meet the above parameters, th...'''
date = "2015-11-26T14:10:00Z"
lastmod = "2015-11-27T02:10:00Z"
weight = 48014
keywords = [ "delay", "videostreaming", "packet-loss", "jitter" ]
aliases = [ "/questions/48014" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I measure packet loss, delay and jitter for a streaming video over a LAN?](/questions/48014/how-can-i-measure-packet-loss-delay-and-jitter-for-a-streaming-video-over-a-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48014-score" class="post-score" title="current number of votes">0</div><span id="post-48014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.! if anyone can help me, exactly I need to know <em>how to measure parameters such as packet loss, jitter and delay over a LAN on which runs the service streaming video, as currently I tried filtering UDP packets and when analyzing the statistics and the summary does not meet the above parameters, this might doing wrong ??</em> I forgot to mention that there is also over this LAN VoIP and file transfer services but need only evaluate these parameters in the video streaming service, two questions: - It is possible to obtain these parameters if I send streaming video on the RTP protocol, if possible, how to avoid confusion with the telephony service? - I can use Telephony&gt; RTP&gt; "stream analysis" to analyze streaming video?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-videostreaming" rel="tag" title="see questions tagged &#39;videostreaming&#39;">videostreaming</span> <span class="post-tag tag-link-packet-loss" rel="tag" title="see questions tagged &#39;packet-loss&#39;">packet-loss</span> <span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '15, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/c836acb03cca56cf0f90986d0861c01a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fer1006&#39;s gravatar image" /><p><span>Fer1006</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fer1006 has no accepted answers">0%</span></p></div></div><div id="comments-container-48014" class="comments-container"></div><div id="comment-tools-48014" class="comment-tools"></div><div class="clear"></div><div id="comment-48014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48018"></span>

<div id="answer-container-48018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48018-score" class="post-score" title="current number of votes">0</div><span id="post-48018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are two distinct issues to deal with:</p><ul><li><p>separation of the of the video traffic from other RTP traffic. Unless the IP telephony server is the same machine as the video streamer, the source IP address should be a sufficient identifier of a video stream.</p></li><li><p>precision of the measurement, especially of jitter.</p></li></ul><p>To the first point - yes, you may use "RTP stream analysis" to analyse streamed video if it is really properly encapsulated as RTP with all the headers. But be careful:</p><ul><li>to analyse packet loss, you have to analyse only the capture from the receiving machine, not from the sending one, so that you could see the real loss (caused by e.g. overbooking of the available connection bandwidth).</li><li>to measure delay, you need to capture at both the source and the destination machines simultaneously, because there is no absolute information about departure time inside the packet.</li><li>to measure jitter, you should compare both captures because to determine the jitter caused by the LAN alone, you have to subtract the amount of jitter coming already from the sending machine itself and from the machines running the capture - see below.</li></ul><p>The precision of measurement is another issue. According to common sense and also <a href="https://ask.wireshark.org/questions/45464/tshark-htpp-jitter-statistics-capabilities-question">this answer</a>, the jitter is calculated as variation of difference between the RTP timestamp of the packet (which is written into the RTP packet by its sender) and the packet capture timestamp (which is added to the packet badge by the capturing machine). And both precision and resolution of the capture timestamps depend on the operating system and load of the machine running the capture, which may easily contribute much more jitter than the LAN: unless you use a specialized hardware, the capture timestamp is not assigned at the moment when the packet physically arrives over the wire and is stored to RAM but at the moment when the operating system notices that it has arrived. So the capturing machine should run a "real time" operating system, use "real" Ethernet ports (not USB - Ethernet adaptors) and preferably do nothing else but capture. So capturing directly on sending and receiving machine is not a good idea, you should use a tap or a SPAN port of a switch and a separate (physical, not virtual!) machine for capturing. Only if you'll see a difference between the mean jitter value of a given stream captured at source and the mean jitter value of exactly the same stream captured at destination (and for several such measurements, the mean jitter value is consistently higher in the captures taken at receiving side), you can consider the difference to be the jitter contributed by the LAN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '15, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Nov '15, 14:18</strong> </span></p></div></div><div id="comments-container-48018" class="comments-container"></div><div id="comment-tools-48018" class="comment-tools"></div><div class="clear"></div><div id="comment-48018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

