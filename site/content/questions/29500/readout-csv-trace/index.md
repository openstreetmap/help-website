+++
type = "question"
title = "Readout CSV trace"
description = '''Hello, I would like to readout a Wireshark CSV file and detect the received and lost RTP packets. Is that even possible with Wireshark? Many thanks in advance. :)'''
date = "2014-02-06T14:29:00Z"
lastmod = "2014-02-07T09:51:00Z"
weight = 29500
keywords = [ "wireshark" ]
aliases = [ "/questions/29500" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Readout CSV trace](/questions/29500/readout-csv-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29500-score" class="post-score" title="current number of votes">0</div><span id="post-29500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to readout a Wireshark CSV file and detect the received and lost RTP packets. Is that even possible with Wireshark? Many thanks in advance. :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '14, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/0010523346f0f58caac17a8d216ab7dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kvmannila&#39;s gravatar image" /><p><span>kvmannila</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kvmannila has no accepted answers">0%</span></p></div></div><div id="comments-container-29500" class="comments-container"><span id="29515"></span><div id="comment-29515" class="comment"><div id="post-29515-score" class="comment-score"></div><div class="comment-text"><p>What is a Wireshark CSV file?</p></div><div id="comment-29515-info" class="comment-info"><span class="comment-age">(06 Feb '14, 23:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29516"></span><div id="comment-29516" class="comment"><div id="post-29516-score" class="comment-score"></div><div class="comment-text"><p>It's a trace exported as a csv file. But any "readable" file format would be OK.</p></div><div id="comment-29516-info" class="comment-info"><span class="comment-age">(07 Feb '14, 00:08)</span> <span class="comment-user userinfo">kvmannila</span></div></div></div><div id="comment-tools-29500" class="comment-tools"></div><div class="clear"></div><div id="comment-29500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29519"></span>

<div id="answer-container-29519" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29519-score" class="post-score" title="current number of votes">0</div><span id="post-29519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kvmannila has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are just interested in the amount of lost RTP frames, you can use the Wireshark statistics.</p><p><strong>Wireshark GUI:</strong><br />
</p><p>Take a look at the RTP statistics.</p><blockquote><p>Telephony -&gt; RTP -&gt; Show all Streams</p></blockquote><p>The output of that contains information about</p><ul><li>different RTP streams</li><li>number of frames received</li><li>number of lost frames</li><li>jitter</li><li>etc.</li></ul><p>The same can be achieved with tshark</p><p><strong>tshark:</strong><br />
</p><blockquote><p>tshark -nr sip_rtp.pcap -z rtp,streams</p></blockquote><p>Output:</p><pre><code>========================= RTP Streams ========================
    Src IP addr  Port    Dest IP addr  Port       SSRC          Payload  Pkts         Lost   Max Delta(ms)  Max Jitter(ms) Mean Jitter(ms) P
roblems?
   200.57.7.204  8000    200.57.7.196 40376 0xD2BD4E3E ITU-T G.711 PCMA   548     0 (0.0%)         5843.74            7.41            2.60
   200.57.7.196 40376    200.57.7.204  8000 0x58F33DEA ITU-T G.711 PCMA   891     0 (0.0%)          379.90            0.25            0.10
   200.57.7.202 30000    200.57.7.196 40362 0x00002E3D ITU-T G.711 PCMA     6     0 (0.0%)           30.04            0.64            1.74
==============================================================</code></pre><p>If that is sufficient for you, consider it as my answer to your question.</p><p>If you want to know exactly which RTP frame is missing (based on the sequence number), I suggest to use tshark</p><blockquote><p>tshark -nr sip_rtp.pcap -R "rtp" -T fields -e frame.number -e ip.src -e ip.dst -e udp.srcport -e udp.dstport -e rtp.seq -e rtp.extseq -E header=y -E separator=;</p></blockquote><p>Output:</p><pre><code>frame.number;ip.src;ip.dst;udp.srcport;udp.dstport;rtp.seq;rtp.extseq
499;200.57.7.204;200.57.7.196;8000;40376;1;65537
500;200.57.7.204;200.57.7.196;8000;40376;2;65538
515;200.57.7.204;200.57.7.196;8000;40376;3;65539
522;200.57.7.196;200.57.7.204;40376;8000;11331;76867
524;200.57.7.204;200.57.7.196;8000;40376;4;65540
528;200.57.7.196;200.57.7.204;40376;8000;11332;76868
530;200.57.7.204;200.57.7.196;8000;40376;5;65541
534;200.57.7.196;200.57.7.204;40376;8000;11333;76869
535;200.57.7.204;200.57.7.196;8000;40376;6;65542
538;200.57.7.196;200.57.7.204;40376;8000;11334;76870
540;200.57.7.196;200.57.7.204;40376;8000;11335;76871</code></pre><p>Then parse the output with a script (perl, python, whatever) and check if there is a frame missing for a certain RTP stream. You can use the IP addresses and the ports to distinguish streams and the sequence numbers to find missing frames (sequence number missing).</p><p>Obviously you can do the same with your exported CSV file, but the tshark output is easier to parse as it only contains what you need. And you can always add new fields to the output as you need them ( tshark -e xxxx)</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/r/rtp.html">http://www.wireshark.org/docs/dfref/r/rtp.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '14, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Feb '14, 03:11</strong> </span></p></div></div><div id="comments-container-29519" class="comments-container"><span id="29538"></span><div id="comment-29538" class="comment"><div id="post-29538-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that seems to be exactly what I want.</p></div><div id="comment-29538-info" class="comment-info"><span class="comment-age">(07 Feb '14, 08:37)</span> <span class="comment-user userinfo">kvmannila</span></div></div><span id="29541"></span><div id="comment-29541" class="comment"><div id="post-29541-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-29541-info" class="comment-info"><span class="comment-age">(07 Feb '14, 09:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-29519" class="comment-tools"></div><div class="clear"></div><div id="comment-29519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

