+++
type = "question"
title = "High tcp.delta_time client or server?"
description = '''Hi, I am looking at a trace with the following information (stream is applied as filter): client_pc(source) -&amp;gt; Server(dest) -&amp;gt;Delta Time=0.552-&amp;gt;tcp.time_delta=30.277237000 I can interpret this as such: RTT (Delta Time)bit slow but meh, server in US me in germany, it happens. tcp.delta_time ...'''
date = "2014-10-01T14:20:00Z"
lastmod = "2014-10-02T05:34:00Z"
weight = 36764
keywords = [ "tcp.time_delta" ]
aliases = [ "/questions/36764" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [High tcp.delta\_time client or server?](/questions/36764/high-tcpdelta_time-client-or-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36764-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am looking at a trace with the following information (stream is applied as filter):</p><p>client_pc(source) -&gt; Server(dest) -&gt;Delta Time=0.552-&gt;tcp.time_delta=30.277237000</p><p>I can interpret this as such: RTT (Delta Time)bit slow but meh, server in US me in germany, it happens. tcp.delta_time extremely slow, probably a timeout fetching data or someother major problem.</p><p>Question is. Should I be looking for the problem in the client application or on the server? I Know tcp.time_delta is the time from end of previous tcp packet in stream to end of current. But I am not sure if this means the tcp delay is on this packet and the client is slow or it is on the previous and the server is slow.</p><p>I just need to know if the client is waiting on the server or the server on the client: does the tcp.time_delta refer to the current frame and indicate delay on the client in this case?</p><p>I am pretty sure the delay is on the client, but that just kinda doesn't make an sense to me..<img src="https://osqa-ask.wireshark.org/upfiles/2014-10-01_23_10_47-Clipboard.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcp.time_delta</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></img></div></div><div id="comments-container-36764" class="comments-container"><span id="36782"></span><div id="comment-36782" class="comment"><div id="post-36782-score" class="comment-score"></div><div class="comment-text"><p>Can I try this one then slightly differently..</p><p><code> 2253 indicates everything from client to server is okay 2277 indicates the client was just waiting around for 30 seconds 2278 indicates traffic form client to server inside the send window 2279 indicates traffic form client to server inside the send window 2280 indicates server responds to previous packet after 160ms (roughly rtt + 20ms)</code></p><p>The delay was on the client either waiting for or working on the data received and I should be looking at whatever it is the client is doing during this pause?</p><p>Sound about right?</p></div><div id="comment-36782-info" class="comment-info"><span class="comment-age">(02 Oct '14, 05:16)</span> DarrenWright</div></div></div><div id="comment-tools-36764" class="comment-tools"></div><div class="clear"></div><div id="comment-36764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36783"></span>

<div id="answer-container-36783" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36783-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As usual analysis by screenshot is fraught with issues as we can't see acks, connection setup, etc.</p><p>Assuming your annotation of source and dest in the diagram is correct, then it does look as though the client is waiting for 30 secs to transmit the data contained in the 3 frames 2277, 2278 &amp; 2279 (probably one application message spread over three tcp segments looking at the relative times) and the server is quick to respond given the likely RTT.</p><p>What I can't tell is what the client was doing between 2253 &amp; 2277, knowledge of the application would be needed there. I guess that 2253 is a client ack to data from the server in 2252, again due to the very short relative time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36783" class="comments-container"><span id="36791"></span><div id="comment-36791" class="comment"><div id="post-36791-score" class="comment-score"></div><div class="comment-text"><p>If the security team is concerned with disclosing confident information in traces have them look at TraceWrangler (<a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a>). It's really easy to obfuscate IP addresses and cut away sensitive payloads with it, and usually the results are still usable to do TCP troubleshooting where no exact application behavior is needed.</p></div><div id="comment-36791-info" class="comment-info"><span class="comment-age">(02 Oct '14, 09:49)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36783" class="comment-tools"></div><div class="clear"></div><div id="comment-36783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

