+++
type = "question"
title = "Problem with http dissector on 204 with Content-type"
description = '''Hello, I&#x27;m facing a problem I don&#x27;t understand and I hope that someone here can help me. I managed to reduce it to a simple pcap (available here: http://dl.free.fr/eheNlphr1) which is only a few KB. If I run: tshark -r weird-204.pcap -T fields -e frame.number -e frame.time -e ip.src -e http.response...'''
date = "2016-11-09T10:18:00Z"
lastmod = "2016-11-09T13:16:00Z"
weight = 57217
keywords = [ "dissector", "http" ]
aliases = [ "/questions/57217" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with http dissector on 204 with Content-type](/questions/57217/problem-with-http-dissector-on-204-with-content-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57217-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm facing a problem I don't understand and I hope that someone here can help me.</p><p>I managed to reduce it to a simple pcap (available here: <a href="http://dl.free.fr/eheNlphr1)">http://dl.free.fr/eheNlphr1)</a> which is only a few KB.</p><p>If I run:</p><pre><code>tshark -r weird-204.pcap -T fields -e frame.number -e frame.time -e ip.src -e http.response.code -e http.time</code></pre><p>I get this output:</p><pre><code>1   Nov  9, 2016 17:45:55.453409000 CET 176.31.224.85       
2   Nov  9, 2016 17:45:55.490626000 CET 46.228.164.12       
3   Nov  9, 2016 17:45:55.490644000 CET 176.31.224.85       
4   Nov  9, 2016 17:45:56.633395000 CET 176.31.224.85       
5   Nov  9, 2016 17:45:56.653943000 CET 46.228.164.12       
6   Nov  9, 2016 17:45:56.653959000 CET 176.31.224.85       
7   Nov  9, 2016 17:46:11.330837000 CET 176.31.224.85       
8   Nov  9, 2016 17:46:11.350015000 CET 46.228.164.12   204,204 14.716620000
9   Nov  9, 2016 17:46:11.350034000 CET 176.31.224.85</code></pre><p>What I don't understand is that packet 8 seems to have 2 204 responses. If you look carefully at the packets, you will see that: packet 1 is the HTTP request, packet 2 is an HTTP response 204 (the first one), packet 3 is an ack for packet 2, packet 4 is the second HTTP request, etc.</p><p>I was expecting to have packet 2 dissected as an HTTP response with status 204 but it is not.</p><p>At this point, I suspect this is linked to the presence of Content-type (which, admittedly is weird for a 204 but not forbidden). If it is the reason, is there any way to change the behavior and have the packet 2 dissected as an HTTP response.</p><p>Apologies if my terminology around dissection and packets/frames/PDU is not correct.</p><p>And thanks to any help anyone could provide.</p><p>Antoine.</p></div><div id="question-tags" class="tags-container tags">dissector http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '16, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/e903777d9a45d1a81d38719dbd2fcc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antoine-sticky&#39;s gravatar image" /><p>antoine-sticky<br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antoine-sticky has no accepted answers">0%</span></p></div></div><div id="comments-container-57217" class="comments-container"></div><div id="comment-tools-57217" class="comment-tools"></div><div class="clear"></div><div id="comment-57217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57223"></span>

<div id="answer-container-57223" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57223-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To me, the problem is not so much the presence of the Content-Type header in a 204 response as the absence of any actual content in a PDU bearing this header.</p><p>If I get right what happens, the absence of contents where it is expected due to presence of Content-Type header somehow makes the HTTP dissector return "not enough data" when it is offered frame 2, causing the TCP dissector to continue reassembly and offer the contents of frame 2 to the HTTP dissector once more, concatenated with the contents of frame 5, with the same result (HTTP dissector doesn't find any content even here so it returns "not enough data" again).</p><p>Only the zero size of the TCP payload which comes in frame 8 somehow makes the HTTP dissector process both the previously received PDUs properly, probably because it analyses them into deeper detail than in the previous passes, and render them as two distinct PDUs in a single reassembled segment.</p><p>I recommend you to <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a bug</a> as the HTTP dissector is clearly able to handle the (weird!) data properly, except that it is "lazy" to do that already during the initial "fast scan" phase.</p><p>If that may help you continue analysis of a particular scenario, unticking the (ticked by default) HTTP dissector preference <code>Reassemble HTTP bodies spanning multiple TCP segments</code> will cause these 204s with Content-Type header to be dissected properly, but it will break analysis of 200s with bodies which exceed the size of a single TCP segment. Closing Wireshark saves the setting into the preferences file in the profile which tshark uses as well, or you may override the default setting only for a single run of tshark, i.e. without saving it to the preferences file, by adding <code>-o "http.desegment_body:FALSE"</code> to your command line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '16, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '16, 00:42</p></div></div><div id="comments-container-57223" class="comments-container"><span id="57226"></span><div id="comment-57226" class="comment"><div id="post-57226-score" class="comment-score"></div><div class="comment-text"><p>Hello Sindy,</p><p>Thanks for your time and response. I followed your reco and posted a bug (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13116).">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13116).</a></p><p>You seem to imply that this is due to the "fast scan" phase. Is there a way to enable a slower (more in-depth) scan phase that would return the appropriate segments ? My original purpose was to measure http.time and see if a delay in http responses could explain some of the problematic behaviors I'm seeing in my application. Obviously with this bug I cannot get appropriate numbers.</p><p>The workaround seems to be working fine. At least it's enough for me to pursue my original analysis.</p><p>Thanks for your precious help, I really appreciate it.</p><p>A.</p></div><div id="comment-57226-info" class="comment-info"><span class="comment-age">(09 Nov '16, 13:47)</span> antoine-sticky</div></div></div><div id="comment-tools-57223" class="comment-tools"></div><div class="clear"></div><div id="comment-57223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

