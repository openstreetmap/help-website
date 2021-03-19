+++
type = "question"
title = "udp traffic analyzer"
description = '''hi..i want to know something about wireshark.pls tell me how i can analyize udp traffic in wireshark i want to measure packet delay,thrughput,jitter n packet loss from source to destination.i think wireshark is best tool for tcp traffic.plzz help me if its possible in wireshark.plz i&#x27;m totaly intere...'''
date = "2013-01-01T01:41:00Z"
lastmod = "2013-01-11T04:25:00Z"
weight = 17369
keywords = [ "udp", "traffic" ]
aliases = [ "/questions/17369" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [udp traffic analyzer](/questions/17369/udp-traffic-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17369-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi..i want to know something about wireshark.pls tell me how i can analyize udp traffic in wireshark i want to measure packet delay,thrughput,jitter n packet loss from source to destination.i think wireshark is best tool for tcp traffic.plzz help me if its possible in wireshark.plz i'm totaly interested in udp traffic.plzz ans me</p></div><div id="question-tags" class="tags-container tags">udp traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '13, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/d9eab83a46d6ed52ec3facf57108fee5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahsan&#39;s gravatar image" /><p>ahsan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahsan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '13, 12:18</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-17369" class="comments-container"></div><div id="comment-tools-17369" class="comment-tools"></div><div class="clear"></div><div id="comment-17369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17386"></span>

<div id="answer-container-17386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17386-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i want to measure packet delay,thrughput,jitter n packet loss from source to destination</p></blockquote><p>for all of those values, you need a capture point near the sender and a second capture point near the receiver. Only then you would be able to calculate those values. Unfortunately, there is no support within Wireshark to read both capture files and calculate the values automatically, so you will have to do that yourself with scripting (parse tshark output) or with a <a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">Lua Listener</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17386" class="comments-container"><span id="17436"></span><div id="comment-17436" class="comment"><div id="post-17436-score" class="comment-score"></div><div class="comment-text"><p>thnkss alot kurt.. is dere any video tutorial for this..??</p></div><div id="comment-17436-info" class="comment-info"><span class="comment-age">(04 Jan '13, 05:33)</span> ahsan</div></div><span id="17437"></span><div id="comment-17437" class="comment"><div id="post-17437-score" class="comment-score"></div><div class="comment-text"><p>kurt can u do this for me plzz i dnt know how to do this plzz m very new in wirshrk.:(</p></div><div id="comment-17437-info" class="comment-info"><span class="comment-age">(04 Jan '13, 05:50)</span> ahsan</div></div><span id="17440"></span><div id="comment-17440" class="comment"><div id="post-17440-score" class="comment-score"></div><div class="comment-text"><blockquote><p>thnkss alot kurt.. is dere any video tutorial for this..??</p></blockquote><p>I don't think so.</p><blockquote><p>kurt can u do this for me plzz i dnt know how to do this plzz m very new in wirshark.:(</p></blockquote><p>I'm sorry, but I don't have time for that kind of public "support", as it would be a lot of work.</p><p>If I knew a tutorial or an available tool, I would post it here, but unfortunately I don't know either.</p><p>If I had to do it, I would most certainly use Perl or Python together with a pcap library to extract the required data. For your requirements, the functionality of wireshark/tshark would not be necessary.</p></div><div id="comment-17440-info" class="comment-info"><span class="comment-age">(04 Jan '13, 06:48)</span> Kurt Knochner ♦</div></div><span id="17492"></span><div id="comment-17492" class="comment"><div id="post-17492-score" class="comment-score"></div><div class="comment-text"><p>thnkss kurt.</p></div><div id="comment-17492-info" class="comment-info"><span class="comment-age">(07 Jan '13, 05:56)</span> ahsan</div></div><span id="17495"></span><div id="comment-17495" class="comment"><div id="post-17495-score" class="comment-score"></div><div class="comment-text"><p>you're welcome</p></div><div id="comment-17495-info" class="comment-info"><span class="comment-age">(07 Jan '13, 07:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-17386" class="comment-tools"></div><div class="clear"></div><div id="comment-17386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17594"></span>

<div id="answer-container-17594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to measure UDP throughput, packet loss and jitter between server and client it's best to use</p><p>nuttcp</p><p>( iperf is also ok but not as robust ).</p><p>Pick latest version from here: <a href="http://www.wcisd.hpc.mil/nuttcp/">http://www.wcisd.hpc.mil/nuttcp/</a></p><p>And here you can find tutorial</p><p><a href="http://www.wcisd.hpc.mil/nuttcp/Nuttcp-HOWTO.html">http://www.wcisd.hpc.mil/nuttcp/Nuttcp-HOWTO.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-17594" class="comments-container"></div><div id="comment-tools-17594" class="comment-tools"></div><div class="clear"></div><div id="comment-17594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

