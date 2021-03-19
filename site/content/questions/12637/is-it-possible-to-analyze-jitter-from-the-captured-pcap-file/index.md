+++
type = "question"
title = "Is it possible to Analyze Jitter from the captured pcap file?"
description = '''Hi All, I have captured the logs at both ends for a end-to-end Wi-Fi call using two phones. They have mainly SIP and RTP packets. I am getting jitter between 5-15 ms for reverse and forward directions. I have a local router which isn&#x27;t connected to LAN.  My question is: Is it possible to analyze jit...'''
date = "2012-07-11T12:16:00Z"
lastmod = "2012-07-12T00:45:00Z"
weight = 12637
keywords = [ "wifi", "jitter", "calls" ]
aliases = [ "/questions/12637" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to Analyze Jitter from the captured pcap file?](/questions/12637/is-it-possible-to-analyze-jitter-from-the-captured-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have captured the logs at both ends for a end-to-end Wi-Fi call using two phones. They have mainly SIP and RTP packets. I am getting jitter between 5-15 ms for reverse and forward directions. I have a local router which isn't connected to LAN.<br />
My question is: Is it possible to analyze jitter and find the possible root cause of why it is occurring?<br />
Please let me know if any detail i am missing.</p><p>Any help is greatly appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags">wifi jitter calls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '12, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/605d70d2a09cf6f80f885269114d0bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vibgyor2nee&#39;s gravatar image" /><p>vibgyor2nee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vibgyor2nee has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-12637" class="comments-container"><span id="28768"></span><div id="comment-28768" class="comment"><div id="post-28768-score" class="comment-score"></div><div class="comment-text"><p>In addition to the main question: is it possible to get jitter or other voice quality metrics via command line?</p></div><div id="comment-28768-info" class="comment-info"><span class="comment-age">(10 Jan '14, 04:25)</span> Alex Voron</div></div><span id="28907"></span><div id="comment-28907" class="comment"><div id="post-28907-score" class="comment-score"></div><div class="comment-text"><p>Please try this:</p><blockquote><p>tshark -nr rtp.pcap -q -z rtp,streams</p></blockquote><p>The output will also show jitter values.</p><p>Regards<br />
Kurt</p></div><div id="comment-28907-info" class="comment-info"><span class="comment-age">(15 Jan '14, 06:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12637" class="comment-tools"></div><div class="clear"></div><div id="comment-12637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12649"></span>

<div id="answer-container-12649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12649-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.8</p><blockquote><p><code>Telephony -&gt; RTP -&gt; Show All Streams</code><br />
</p></blockquote><p>This will show all RTP streams and Min/Max Jitter for each stream (scroll to the right).</p><p>Then select one stream and click on <strong><code>Analyze</code></strong> (same as Option: Telephony -&gt; RTP -&gt; Stream Analysis). You will get a much more detailed view of that stream.</p><p><strong>UPDATE</strong>:</p><blockquote><p>Any idea what is the permissible value of Jitter for an end-to-end wi-fi call?</p></blockquote><p>Well, it depends ... Some network providers offer <a href="http://www.verizonbusiness.com/terms/us/products/advantage/">SLAs with 0.5 - 2 ms max jitter</a>. That's pretty good. Others (e.g. Avaja, Cisco) say, 10-20 ms is acceptable. Furthermore there are compensations techniques, like <a href="http://www.voiptroubleshooter.com/indepth/jittersources.html">jitter buffers</a>. So a jitter value of 15 ms can cause problems (crippled audio) in one environment and no problems at all in another environment (with jitter buffers).</p><p>As I mentioned, <a href="http://www.voiptroubleshooter.com/indepth/jittersources.html">Jitter can be caused by numerous factors</a>. Even the VoIP devices (especially soft phones) can cause jitter due to process scheduling in the device. So, if there are no signs of other network problems, you should consider the VoIP devices as a possible source.</p><p>As you mentioned that the VoIP endpoints are connected via Wifi, I suggest to check that connection first. A Wifi link can also cause jitter, especially if the network is "crowded" or if there are other interfering radio signals. You can test the jitter of the network with <a href="http://code.google.com/p/xjperf/">xjperf (UDP tests)</a>. I'm not sure how iperf calculates the jitter value, so it may not be comparable with the VoIP jitter value! However, it's something to start with.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '12, 20:40</p></div></div><div id="comments-container-12649" class="comments-container"><span id="12662"></span><div id="comment-12662" class="comment"><div id="post-12662-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt</p><p>I got that. That's how i know the jitter values. I need to analyze it and find the reason of occurrence. Is there any way we can do so?</p></div><div id="comment-12662-info" class="comment-info"><span class="comment-age">(12 Jul '12, 10:08)</span> vibgyor2nee</div></div><span id="12664"></span><div id="comment-12664" class="comment"><div id="post-12664-score" class="comment-score"></div><div class="comment-text"><p>you can save the the jitter values as CSV, then use Excel to chart the values together with the frame/packet number. If there are any spikes in the jitter values, go to that packet number any check if there are any signs of general network problems within +/- 10 seconds in the capture file. Unfortunately it's hard to give any detailed advice what to look for, as it may be anything or nothing if it's a problem on the VoIP client itself.</p></div><div id="comment-12664-info" class="comment-info"><span class="comment-age">(12 Jul '12, 11:46)</span> Kurt Knochner ♦</div></div><span id="12672"></span><div id="comment-12672" class="comment"><div id="post-12672-score" class="comment-score"></div><div class="comment-text"><p>Any idea what is the permissible value of Jitter for an end-to-end wi-fi call?</p></div><div id="comment-12672-info" class="comment-info"><span class="comment-age">(12 Jul '12, 14:32)</span> vibgyor2nee</div></div><span id="12682"></span><div id="comment-12682" class="comment"><div id="post-12682-score" class="comment-score"></div><div class="comment-text"><p>see UPDATE in my answer.</p></div><div id="comment-12682-info" class="comment-info"><span class="comment-age">(12 Jul '12, 20:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12649" class="comment-tools"></div><div class="clear"></div><div id="comment-12649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

