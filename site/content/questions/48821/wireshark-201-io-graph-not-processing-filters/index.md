+++
type = "question"
title = "Wireshark 2.0.1  -   I/O  Graph not processing filters"
description = '''I just finished a packet capture. I&#x27;m trying to save an I/O Graph with bandwidth usage information. During the packet capture, I set some filters.  The view filter I set in the packet list view during capture is ip.addr == 10.149.21.79 and !tcp.port == 22  The capture is taking place from a differen...'''
date = "2016-01-04T00:50:00Z"
lastmod = "2016-01-04T02:53:00Z"
weight = 48821
keywords = [ "filter", "graph" ]
aliases = [ "/questions/48821" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.1 - I/O Graph not processing filters](/questions/48821/wireshark-201-io-graph-not-processing-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just finished a packet capture. I'm trying to save an I/O Graph with bandwidth usage information.</p><p>During the packet capture, I set some filters.</p><p>The view filter I set in the packet list view during capture is</p><pre><code>ip.addr == 10.149.21.79 and !tcp.port == 22</code></pre><p>The capture is taking place from a different host than 10.149.21.79, so there's a lot of other packets captured.</p><p>For the I/O Graph I'm trying to create of traffic coming from 10.149.21.79 I want to filter out all other traffic.</p><p>I created some filters to use in the I/O Graph tool (same ones worked in the previous version of Wireshark)</p><pre><code>ip.addr == 10.149.21.79 and tcp.port == 5678
ip.addr == 10.149.21.79 and icmp
ip.addr == 10.149.21.79</code></pre><p>And so on.</p><p>Even though the bandwidth usage is completely different between icmp traffic and the traffic I'm capturing from port 5678, the graph remains identical.</p><p>This issue started since I installed the new version 2.0.1 this morning.</p><p>I could try and set capture filters, but that would mean I have to perform three or more captures</p><p>Have there been changes in the filter mechanism or is this a bug?</p></div><div id="question-tags" class="tags-container tags">filter graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '16, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/96194b6046dffad3676d973415271cdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amx&#39;s gravatar image" /><p>amx<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '16, 00:52</p></div></div><div id="comments-container-48821" class="comments-container"></div><div id="comment-tools-48821" class="comment-tools"></div><div class="clear"></div><div id="comment-48821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48827"></span>

<div id="answer-container-48827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seems to work for me. I'm presuming you are using the Qt version, not the legacy GTK version?</p><p>Can you provide a capture file in a public share somewhere, e.g. Google Drive, Dropbox etc.?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '16, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48827" class="comments-container"><span id="48830"></span><div id="comment-48830" class="comment"><div id="post-48830-score" class="comment-score"></div><div class="comment-text"><p>I'm not 100% sure, but I checked the About section in Wireshark and it says it's compiled with QT.</p><p><a href="https://www.hidrive.strato.com/lnk/34grm4j4">https://www.hidrive.strato.com/lnk/34grm4j4</a></p><p>I included a capture with traffic between localhost and 10.149.21.79. there is 21% SSH traffic, but I still cannot exclude that traffic in the I/O graph</p></div><div id="comment-48830-info" class="comment-info"><span class="comment-age">(04 Jan '16, 03:25)</span> amx</div></div><span id="48831"></span><div id="comment-48831" class="comment"><div id="post-48831-score" class="comment-score"></div><div class="comment-text"><p>Never mind.</p><p>This was a user error.</p><p>I did not check the columns correctly, and was filling in the display filter in the Name column.</p><p>Obviously it's working now.</p></div><div id="comment-48831-info" class="comment-info"><span class="comment-age">(04 Jan '16, 03:42)</span> amx</div></div><span id="48832"></span><div id="comment-48832" class="comment"><div id="post-48832-score" class="comment-score"></div><div class="comment-text"><p>It was not a Wireshark problem, thanks for helping anyway Graham!</p></div><div id="comment-48832-info" class="comment-info"><span class="comment-age">(04 Jan '16, 03:47)</span> amx</div></div><span id="48833"></span><div id="comment-48833" class="comment"><div id="post-48833-score" class="comment-score"></div><div class="comment-text"><p>I've created the graph showing the total traffic, icmp, port 5678 and ssh to\from the host. Looks OK to me.</p><p><img src="http://s4.postimg.org/g03noz64t/test_capture.png" alt="IO Graph" /></p></div><div id="comment-48833-info" class="comment-info"><span class="comment-age">(04 Jan '16, 04:04)</span> grahamb ♦</div></div></div><div id="comment-tools-48827" class="comment-tools"></div><div class="clear"></div><div id="comment-48827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

