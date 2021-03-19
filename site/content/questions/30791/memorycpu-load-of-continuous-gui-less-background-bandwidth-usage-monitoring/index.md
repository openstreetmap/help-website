+++
type = "question"
title = "Memory/CPU load of continuous GUI-less background bandwidth usage monitoring"
description = '''I&#x27;d like to log my Internet usage in such a way that I can see how much I&#x27;ve uploaded, and how much I&#x27;ve downloaded, to each port on each host/IP I visit. The machine I would be using to do this is an 800MHz Duron with 640MB of RAM, and this box is also used for quite a few other tasks (it typically...'''
date = "2014-03-14T00:46:00Z"
lastmod = "2014-03-14T00:54:00Z"
weight = 30791
keywords = [ "performance", "traffic-analysis", "monitoring", "background" ]
aliases = [ "/questions/30791" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Memory/CPU load of continuous GUI-less background bandwidth usage monitoring](/questions/30791/memorycpu-load-of-continuous-gui-less-background-bandwidth-usage-monitoring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to log my Internet usage in such a way that I can see how much I've uploaded, and how much I've downloaded, to each port on each host/IP I visit.</p><p>The machine I would be using to do this is an 800MHz Duron with 640MB of RAM, and this box is also used for quite a few other tasks (it typically has about 150MB of RAM free, and an average of 60-80% CPU usage), so I'd like to know how responsive the system would be with Wireshark constantly running in the background on such a system. (For some unusual and involved technical reasons, upgrading this system or using another is currently not possible.)</p><p>Also, since just about everything that works with a domain name is going to do a DNS lookup to find the IP address, would it be possible to sniff for the DNS lookup response and use that to associate IP addresses with hostnames, rather than making an extra, technically superfluous, DNS lookup?</p></div><div id="question-tags" class="tags-container tags">performance traffic-analysis monitoring background</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '14, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/5afde66cd49d8af6e708316bead67dcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="i336_&#39;s gravatar image" /><p>i336_<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="i336_ has no accepted answers">0%</span></p></div></div><div id="comments-container-30791" class="comments-container"></div><div id="comment-tools-30791" class="comment-tools"></div><div class="clear"></div><div id="comment-30791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30792"></span>

<div id="answer-container-30792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30792-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is not a lot of RAM, and no matter how much RAM you put in you will still run into trouble after a while. Wireshark is unable to capture nonstop, so if you plan on doing a continuous capture you should use dumpcap instead. See <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">this blog post</a> for more information on long time captures.</p><p>Regarding DNS: Wireshark uses DNS answers found in capture files to do name resolution. It will only do DNS lookups if there is no answer found to a given IP address, and only if you use network name resolution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '14, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30792" class="comments-container"><span id="30794"></span><div id="comment-30794" class="comment"><div id="post-30794-score" class="comment-score"></div><div class="comment-text"><p>I see, thanks for that information; I'll give dumpcap a look. What's its performance like, CPU/RAM-wise? Is dumpcap a kind of intelligent framework that adds to libpcap, or is it just a thin layer that brings the functionality required into Wireshark?</p><p>Also, it's nice to know I'm not the only one who thought of the spurious-DNS thing :P</p></div><div id="comment-30794-info" class="comment-info"><span class="comment-age">(14 Mar '14, 01:38)</span> i336_</div></div><span id="30795"></span><div id="comment-30795" class="comment"><div id="post-30795-score" class="comment-score"></div><div class="comment-text"><p>dumpcap has no intelligence when it comes to analyzing packets, its single job is to grab frames from the network card and write them to a file. So it's memory footprint should be pretty small; similar to what TCPdump does.</p><p>Actually, when Wireshark is capturing data it is not doing it itself. Wireshark spawns a dumpcap process and keeps reloading the file while it is written by dumpcap.</p></div><div id="comment-30795-info" class="comment-info"><span class="comment-age">(14 Mar '14, 01:54)</span> Jasper ♦♦</div></div></div><div id="comment-tools-30792" class="comment-tools"></div><div class="clear"></div><div id="comment-30792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

