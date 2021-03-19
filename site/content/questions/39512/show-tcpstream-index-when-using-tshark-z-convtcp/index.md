+++
type = "question"
title = "Show tcp.stream index when using tshark -z conv,tcp"
description = '''Is there anyway to show the tcp.stream index using the tshark &quot;-z conv,tcp&quot; option?'''
date = "2015-01-30T14:52:00Z"
lastmod = "2015-07-01T23:00:00Z"
weight = 39512
keywords = [ "statistics", "tshark" ]
aliases = [ "/questions/39512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show tcp.stream index when using tshark -z conv,tcp](/questions/39512/show-tcpstream-index-when-using-tshark-z-convtcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39512-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyway to show the tcp.stream index using the tshark "-z conv,tcp" option?</p></div><div id="question-tags" class="tags-container tags">statistics tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/661d763914fceef62409df8cb9087cdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="heathm&#39;s gravatar image" /><p>heathm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="heathm has no accepted answers">0%</span></p></div></div><div id="comments-container-39512" class="comments-container"><span id="39514"></span><div id="comment-39514" class="comment"><div id="post-39514-score" class="comment-score"></div><div class="comment-text"><p>I'm running Wireshark 1.99.1 downloaded Jan. 30, 2015. The output of tshark -z conv,tcp is pretty useless for tracking down problems since it doesn't show any TCP ports nor does it show the TCP stream. If I see something odd in a particular stream, how do I then track down the details of that stream?</p></div><div id="comment-39514-info" class="comment-info"><span class="comment-age">(30 Jan '15, 15:31)</span> heathm</div></div><span id="43805"></span><div id="comment-43805" class="comment"><div id="post-43805-score" class="comment-score"></div><div class="comment-text"><p>In my 1.99.7 version it's displaying the TCP ports like seen below</p><p>D:\Traces&gt;tshark -r test.pcap -qz conv,tcp | more</p><p>TCP Conversations Filter:&lt;no filter=""&gt; [...]</p><p>172.16.0.130:51534 &lt;-&gt; 172.16.0.251:80</p></div><div id="comment-43805-info" class="comment-info"><span class="comment-age">(02 Jul '15, 00:24)</span> Landi</div></div></div><div id="comment-tools-39512" class="comment-tools"></div><div class="clear"></div><div id="comment-39512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43804"></span>

<div id="answer-container-43804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43804-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With Tshark 1.8.2, GNU sed 4.2.1 (well, you could do without), GNU awk 4.0.1 (nothing fancy here as well) in the GNU bash 4.2.37 (and nothing fancy here as well), the following hack "works for me", but is neither fast nor pretty, but can be written as a one-liner...</p><pre><code>tshark -nr input.pcap -z conv,tcp -q | sed &#39;1,5d;$d&#39; | awk -F &#39;:| +&#39; &#39;{print $1 &quot; &quot; $2 &quot; &quot; $4 &quot; &quot; $5 &quot; &quot; $11 &quot; &quot; $12 &quot; &quot; $0}&#39; | while read src sport dst dport total start all ; do stream=`tshark -nr input.pcap -R &quot;ip.addr eq $src and ip.addr eq $dst and tcp.port eq $sport and tcp.port eq $dport and frame.time_relative eq $start&quot; -T fields -e tcp.stream` ; echo &quot;$all $stream&quot; ; done</code></pre><p>It is very slow (the second tshark call reads the whole file again, each time), and rather error-prone, but you might get the idea.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '15, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/789bc3035c46d76083997737ba561d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nrs01&#39;s gravatar image" /><p>nrs01<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nrs01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '15, 00:12</p></div></div><div id="comments-container-43804" class="comments-container"></div><div id="comment-tools-43804" class="comment-tools"></div><div class="clear"></div><div id="comment-43804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

