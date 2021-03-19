+++
type = "question"
title = "tshark BYTES (stats) does not match wireshark &quot;Cumulative Bytes&quot;"
description = '''Basically I&#x27;m trying to get a total amount of bytes transferred per port (22, 5900, 5901, etc) but tshark does not seem to give the same results as wireshark... what am I doing wrong? I&#x27;ve tested this with wireshark/tshark 1.12.5 on win7 and tshark 1.10.6 on Ubuntu linux, same results. All tests rea...'''
date = "2015-05-19T13:19:00Z"
lastmod = "2015-05-19T21:48:00Z"
weight = 42561
keywords = [ "bytes", "cumulative", "stats", "tshark" ]
aliases = [ "/questions/42561" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark BYTES (stats) does not match wireshark "Cumulative Bytes"](/questions/42561/tshark-bytes-stats-does-not-match-wireshark-cumulative-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42561-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Basically I'm trying to get a total amount of bytes transferred per port (22, 5900, 5901, etc) but tshark does not seem to give the same results as wireshark... what am I doing wrong? I've tested this with wireshark/tshark 1.12.5 on win7 and tshark 1.10.6 on Ubuntu linux, same results. All tests reading from the same pcap file.</p><p>I added "Cumulative Bytes" as a column then applied a filter: "tcp.port==22". Cumulative bytes at the bottom for this filter is 396974.</p><p>Tshark gives me 71578 bytes from the same data:</p><pre><code>tshark.exe -r tcpdump.pcap -qz io,stat,0,,&quot;BYTES()tcp.port==22&quot;</code></pre><p>Using tshark, how can I get a statistical dump of the total tx/rx bytes per port (tcp.port) from the entire file based on a list of ~ 20 specific ports ? (it would be lot faster then running wireshark filters manually then copying the last "Cumulative Bytes" value each time)</p></div><div id="question-tags" class="tags-container tags">bytes cumulative stats tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '15, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/adabc519e456c74ff57f176e4a4685a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CptFuzzy&#39;s gravatar image" /><p>CptFuzzy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CptFuzzy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '15, 16:05</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-42561" class="comments-container"><span id="42563"></span><div id="comment-42563" class="comment"><div id="post-42563-score" class="comment-score">1</div><div class="comment-text"><p>Can you post a sample capture file, to <a href="https://appliance.cloudshark.org/upload/">cloudshark</a> for example?</p></div><div id="comment-42563-info" class="comment-info"><span class="comment-age">(19 May '15, 14:19)</span> cmaynard ♦♦</div></div><span id="42564"></span><div id="comment-42564" class="comment"><div id="post-42564-score" class="comment-score"></div><div class="comment-text"><p>I can't post the file I'm working on as it has real IP's in it... I'll try and create another file that i can share and reproduce the problem. Is "BYTES()tcp.port==22" the correct method to get all the traffic for that port?</p></div><div id="comment-42564-info" class="comment-info"><span class="comment-age">(19 May '15, 15:44)</span> CptFuzzy</div></div><span id="42565"></span><div id="comment-42565" class="comment"><div id="post-42565-score" class="comment-score">1</div><div class="comment-text"><p><em>Is "BYTES()tcp.port==22" the correct method to get all the traffic for that port?</em></p><p>I don't know. If there's IP fragmentation occurring, for example, it might not be. Or maybe it is and there's a Wireshark bug. Or perhaps there's a Wireshark preference setting that needs to be changed. Or maybe running <code>tshark</code> with other options, such as the <code>-2</code> option, for example, might give you the output you need. It's hard [for me] to say without looking at a sample capture file.</p></div><div id="comment-42565-info" class="comment-info"><span class="comment-age">(19 May '15, 16:04)</span> cmaynard ♦♦</div></div><span id="42580"></span><div id="comment-42580" class="comment"><div id="post-42580-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comments. I'll try to get a 'clean' capture file and start again. Thanks for the cloudshark link - could be useful.</p></div><div id="comment-42580-info" class="comment-info"><span class="comment-age">(20 May '15, 07:44)</span> CptFuzzy</div></div><span id="42581"></span><div id="comment-42581" class="comment"><div id="post-42581-score" class="comment-score"></div><div class="comment-text"><p>@CptFuzzy</p><p>You can use <a href="https://www.tracewrangler.com/">TraceWrangler</a> to anonymize your capture file and then post the anonymized one.</p></div><div id="comment-42581-info" class="comment-info"><span class="comment-age">(20 May '15, 07:51)</span> grahamb ♦</div></div></div><div id="comment-tools-42561" class="comment-tools"></div><div class="clear"></div><div id="comment-42561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42567"></span>

<div id="answer-container-42567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general it works (same values in the GUI and tshark). I just tested with 1.12.1 on Win7. So, the problem could be related to your capture file.</p><p>Can you please test with the following test file to see if you get the same result as I do.</p><p>Test file: <a href="https://www.cloudshark.org/captures/60efe7c0e18b">https://www.cloudshark.org/captures/60efe7c0e18b</a></p><pre><code>tshark.exe -r http.pcapng -qz io,stat,0,,&quot;BYTES()tcp.port==80&quot;,&quot;BYTES
()tcp.srcport==80&quot;,&quot;BYTES()tcp.dstport==80&quot;

==========================================
| IO Statistics                          |
|                                        |
| Duration: 0.688 secs                   |
| Interval: 0.688 secs                   |
|                                        |
| Col 1: BYTES()tcp.port==80             |
|     2: BYTES()tcp.srcport==80          |
|     3: BYTES()tcp.dstport==80          |
|----------------------------------------|
|                |1      |2      |3      |
| Interval       | BYTES | BYTES | BYTES |
|----------------------------------------|
| 0.000 &lt;&gt; 0.688 | 11409 | 10443 |   966 |
==========================================</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/http.pcapng_Conversations.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '15, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '15, 21:49</p></div></div><div id="comments-container-42567" class="comments-container"><span id="42579"></span><div id="comment-42579" class="comment"><div id="post-42579-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answers. I will try a few things and post results. In the mean-time, is there a way to validate my pcap file? perhaps remove incomplete/invalid records?</p></div><div id="comment-42579-info" class="comment-info"><span class="comment-age">(20 May '15, 07:42)</span> CptFuzzy</div></div><span id="42635"></span><div id="comment-42635" class="comment"><div id="post-42635-score" class="comment-score"></div><div class="comment-text"><blockquote><p>is there a way to validate my pcap file? perhaps remove incomplete/invalid records?</p></blockquote><p>Hard to tell without access to the capture file.</p></div><div id="comment-42635-info" class="comment-info"><span class="comment-age">(24 May '15, 02:47)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42567" class="comment-tools"></div><div class="clear"></div><div id="comment-42567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

