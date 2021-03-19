+++
type = "question"
title = "Read LZO compressed payload in pcap file"
description = '''I am using Wireshark 1.10.6 to analyse my pcap file. pcap is human readable once loaded in wireshark but the &quot;payload&quot; is not. It has been compressed using LZO algorithm and I intent to use a utility that could decompress the LZO payload and change it to human readable format. Currently it is in hex...'''
date = "2017-01-21T01:03:00Z"
lastmod = "2017-01-21T05:53:00Z"
weight = 58929
keywords = [ "payload", "decompress" ]
aliases = [ "/questions/58929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Read LZO compressed payload in pcap file](/questions/58929/read-lzo-compressed-payload-in-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.10.6 to analyse my pcap file. pcap is human readable once loaded in wireshark but the "payload" is not. It has been compressed using LZO algorithm and I intent to use a utility that could decompress the LZO payload and change it to human readable format. Currently it is in hexa format, as shown in the picture below<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2017-01-21_14:23:29.png" alt="alt text" /></p><p>The data is from NSE Exchange. Steps for decompression have been given on <a href="https://www.nseindia.com/content/press/Realtime_CM_L1.pdf">https://www.nseindia.com/content/press/Realtime_CM_L1.pdf</a> page#29</p><p>What would be the best way to make the whole pcap file human readable, I am sure this is a pretty common procedure used by many hft firms to track their orders</p><p>Update 1: I dumped the log as C arrays file, which looks something like below, and my aim is to make it readable.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2017-01-23_16:41:39.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">payload decompress</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/32ddf7b73f88565b33c0ffb19926d18a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hftguy&#39;s gravatar image" /><p>hftguy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hftguy has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '17, 03:38</p></div></div><div id="comments-container-58929" class="comments-container"></div><div id="comment-tools-58929" class="comment-tools"></div><div class="clear"></div><div id="comment-58929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58930"></span>

<div id="answer-container-58930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58930-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is a dissector for the payload, these a a fundamental aspect of Wireshark, that's how the rest of the data in the packet (Ethernet/IP/TCP) can be displayed in "human readable format".</p><p>See the wiki page on <a href="https://wiki.wireshark.org/Development">Development</a>, then decide how you will create your dissector. You can use C (all the "built-in" dissectors use C), <a href="https://wiki.wireshark.org/Lua">Lua</a> or for simpler protocols <a href="http://wsgd.free.fr/">WSGD</a>.</p><p>If you're able to program in C, then using that will produce the highest performing dissector (load and filter times will be faster), else start with Lua.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '17, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-58930" class="comments-container"></div><div id="comment-tools-58930" class="comment-tools"></div><div class="clear"></div><div id="comment-58930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

