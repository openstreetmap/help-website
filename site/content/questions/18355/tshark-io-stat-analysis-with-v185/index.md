+++
type = "question"
title = "Tshark IO stat analysis with v1.8.5"
description = '''I&#x27;m using a command such as the following to: tshark.exe -q -z &quot;io,stat,60,ip.src==myhost.co.uk&quot; -r Monday.pcap &amp;gt; MonOutboundStats.txt With the aim of determining how much traffic is going out from &quot;myhost.co.uk&quot;. However, when I look at the resulting stats file it doesn&#x27;t add up. The first few r...'''
date = "2013-02-06T02:18:00Z"
lastmod = "2013-02-06T06:36:00Z"
weight = 18355
keywords = [ "stat", "tshark", "io" ]
aliases = [ "/questions/18355" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark IO stat analysis with v1.8.5](/questions/18355/tshark-io-stat-analysis-with-v185)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18355-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a command such as the following to:</p><p><code>tshark.exe -q -z "io,stat,60,ip.src==myhost.co.uk" -r Monday.pcap &gt; MonOutboundStats.txt</code></p><p>With the aim of determining how much traffic is going out from "myhost.co.uk". However, when I look at the resulting stats file it doesn't add up. The first few rows make sense but then I get the same figure repeated in column 2 (118799631). If I understand correctly, the first column is unfiltered and should show me the total IO (both in and outbound). Therefore my second filtered column you would not expect to see values that are greater than the first column.</p><p>| Interval | Frames | Bytes | Frames | Bytes |</p><p>|---------------------------------------------------------|</p><p>...</p><p>| 44940 &lt;&gt; 45000 | 69 | 9922 | 36 | 4470 |</p><p>...</p><p>| 121140 &lt;&gt; 121200 | 4 | 336 | 0 | 118799631 |</p><p>| 121200 &lt;&gt; 121260 | 1 | 243 | 0 | 118799631 |</p><p>| 121260 &lt;&gt; 121320 | 0 | 0 | 0 | 118799631 |</p><p>| 121320 &lt;&gt; 121380 | 0 | 0 | 0 | 118799631 |</p><p>| 121380 &lt;&gt; 121440 | 0 | 0 | 0 | 118799631 |</p><p>| 121440 &lt;&gt; 121500 | 0 | 0 | 0 | 118799631 |</p><p>...</p><p>Have I missed something here?</p><p>I'd like to end up with a command I can used to see how much traffic is going in and out from my host, similar to:</p><p><code>tshark.exe -q -z "io,stat,60,ip.src==myhost.co.uk,ip.dst==myhost.co.uk" -r Monday.pcap &gt; MonOutboundStats.txt</code></p></div><div id="question-tags" class="tags-container tags">stat tshark io</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '13, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/a011be3874d7902d8904b8e239bdd201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billbofagends&#39;s gravatar image" /><p>billbofagends<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billbofagends has no accepted answers">0%</span></p></div></div><div id="comments-container-18355" class="comments-container"><span id="18357"></span><div id="comment-18357" class="comment"><div id="post-18357-score" class="comment-score"></div><div class="comment-text"><p>A similar experiment works for me, can you share your capture file?</p></div><div id="comment-18357-info" class="comment-info"><span class="comment-age">(06 Feb '13, 04:24)</span> grahamb ♦</div></div></div><div id="comment-tools-18355" class="comment-tools"></div><div class="clear"></div><div id="comment-18355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18359"></span>

<div id="answer-container-18359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18359-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug in tshark-1.8.x (i know because I filed it!) You can learn more here:<br />
</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8066">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8066</a></p><p>Dropping back to 1.6 will solve the <code>io,stat</code> issue, but then you won't have all the goodies that come with 1.8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span> </br></p></div></div><div id="comments-container-18359" class="comments-container"></div><div id="comment-tools-18359" class="comment-tools"></div><div class="clear"></div><div id="comment-18359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

