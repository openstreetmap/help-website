+++
type = "question"
title = "Tshark get rtp stream statistics in realtime"
description = '''I need to get statistics on sip streams for a large test. I have 2 sipp generators one sender and one receiver, the receiver has the switch port mirrored to another machine used for analysis. For now on the &quot;analyzer&quot; I am saving data to a file: tshark &quot;host 1.1.1.1 and host 2.2.2.2&quot; -i3 -w test_cal...'''
date = "2016-11-17T03:32:00Z"
lastmod = "2016-11-17T05:02:00Z"
weight = 57441
keywords = [ "sip", "qos", "tshark" ]
aliases = [ "/questions/57441" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark get rtp stream statistics in realtime](/questions/57441/tshark-get-rtp-stream-statistics-in-realtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to get statistics on sip streams for a large test. I have 2 sipp generators one sender and one receiver, the receiver has the switch port mirrored to another machine used for analysis. For now on the "analyzer" I am saving data to a file:</p><pre><code>tshark &quot;host 1.1.1.1 and host 2.2.2.2&quot; -i3 -w test_calls.pcap #(no other filters needed as this is only sip traffic, streams)</code></pre><p>After this i analyze the pcap file:</p><pre><code>tshark -r test_calls.pcap -qz rtp,streams</code></pre><p>All is good and showing ok but on capture after a few minutes I have a few GB of data in the file, as I make cycles of 1000 2 minutes calls with 30 sec pause between cycles. Is there a way to get statistics with no saving to disk, I mean after a call ended show statistics and forget the data because I need to make some tests for 4-8 hours. Something like this:</p><pre><code>tshark &quot;host 1.1.1.1 and host 2.2.2.2&quot; -i3 -qz rtp,streams (not a working command)</code></pre></div><div id="question-tags" class="tags-container tags">sip qos tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '16, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/b4287260fae8bc69f6d54a48e6a05071?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rift85&#39;s gravatar image" /><p>rift85<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rift85 has no accepted answers">0%</span></p></div></div><div id="comments-container-57441" class="comments-container"></div><div id="comment-tools-57441" class="comment-tools"></div><div class="clear"></div><div id="comment-57441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57442"></span>

<div id="answer-container-57442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57442-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use dumpcap to capture the traffic with multiple files, e.g. the <code>-b</code> option, then using scripting to detect a new file and run tshark over that file to get the stats.</p><p>The tricky bit will be arranging the file capture and call to overlap so a complete call is contained within each capture file, you have options for duration and file size to limit a capture file.</p><p>Running tshark for long periods with high-volume data runs the risk of the tshark process running out of memory due to the state that's maintained.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '16, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57442" class="comments-container"></div><div id="comment-tools-57442" class="comment-tools"></div><div class="clear"></div><div id="comment-57442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57443"></span>

<div id="answer-container-57443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57443-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you say you generate calls in "campaigns" clearly bordered in time, you can synchronize individual runs of tshark with those campaigns, can't you? That way, you wouldn't need to save the data to disk at all, just redirect the statistics output of tshark to a text file.</p><p>Trouble would begin if the memory of the capturing machine would be insufficient to handle the complete campaign, but that does not seem to be your case currently.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57443" class="comments-container"></div><div id="comment-tools-57443" class="comment-tools"></div><div class="clear"></div><div id="comment-57443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

