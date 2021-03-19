+++
type = "question"
title = "Looking on recommendations/best practices on WS deployment at large Data Centers"
description = '''Hi WS community Willing to get references/best practices/experience on WS deployment at large data centers. Looking to understand what type of configurations/arranges have worked well, which not, which tools for process/automate data collection, etc. Thanks vey much -f'''
date = "2015-11-23T08:25:00Z"
lastmod = "2015-11-23T11:18:00Z"
weight = 47868
keywords = [ "data", "center", "wireshark" ]
aliases = [ "/questions/47868" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Looking on recommendations/best practices on WS deployment at large Data Centers](/questions/47868/looking-on-recommendationsbest-practices-on-ws-deployment-at-large-data-centers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi WS community Willing to get references/best practices/experience on WS deployment at large data centers. Looking to understand what type of configurations/arranges have worked well, which not, which tools for process/automate data collection, etc. Thanks vey much -f</p></div><div id="question-tags" class="tags-container tags">data center wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/4f7098448a7582633b026ad9d55769d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fturriaf&#39;s gravatar image" /><p>fturriaf<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fturriaf has no accepted answers">0%</span></p></div></div><div id="comments-container-47868" class="comments-container"><span id="47871"></span><div id="comment-47871" class="comment"><div id="post-47871-score" class="comment-score"></div><div class="comment-text"><p>please define "large data center" and what you are trying to do.</p></div><div id="comment-47871-info" class="comment-info"><span class="comment-age">(23 Nov '15, 09:28)</span> Kurt Knochner ♦</div></div><span id="47873"></span><div id="comment-47873" class="comment"><div id="post-47873-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt I referring to DC with 10-20 row with 32 racks per row and typically 15 servers per rack, so about 10,000 servers (30% of them bare metal, rest running hypervisors). basically, looking to be able to monitor any server by mirroring network ports at ToR. Initially, thinking to deploy a small cluster of servers running Wireshark per Row, but not sure if this is a good approach or there are smarter ways to do this. Thanks</p></div><div id="comment-47873-info" class="comment-info"><span class="comment-age">(23 Nov '15, 09:35)</span> fturriaf</div></div></div><div id="comment-tools-47868" class="comment-tools"></div><div class="clear"></div><div id="comment-47868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47877"></span>

<div id="answer-container-47877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47877-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>for an environment like that, Wireshark will work if the capturing devices (ToR) are fast machines (CPU, RAM, disk IO) and you don't have to capture at full speed 10Gig.</p><p>But operating a distributed capturing architecture is not easy. Wirshark won't help you here (let's ignore remote capturing), so you will end up with a lot of a manual processing. Please think about:</p><ul><li>start/stop capturing</li><li>copying/archiving capture files</li><li>searching in a large amount of capture files for certain data and/or patterns</li><li>loading very large capturing files, (several Gbyte)</li><li>etc.</li></ul><p>Maybe a commercial capturing system would fit better into a data center environment of that size.</p><p>I'm <strong>not</strong> saying, that it's impossible with Wireshark, it's just a lot more manual work than with a commercial solution.</p><p>Maybe the following Open Source projects can help or give some ideas.</p><blockquote><p><a href="http://www.openfpc.org/">http://www.openfpc.org/</a><br />
<a href="https://github.com/aol/moloch">https://github.com/aol/moloch</a><br />
<a href="https://github.com/RIPE-NCC/hadoop-pcap">https://github.com/RIPE-NCC/hadoop-pcap</a></p></blockquote><p>There was also a Sharkfest talk about a similar matter</p><blockquote><p><a href="https://sharkfest.wireshark.org/assets/presentations/A6.pptx">https://sharkfest.wireshark.org/assets/presentations/A6.pptx</a></p></blockquote><p>You could try to contact the authors, maybe they can give some more hints.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '15, 14:49</p></div></div><div id="comments-container-47877" class="comments-container"><span id="47882"></span><div id="comment-47882" class="comment"><div id="post-47882-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. Any recommendation on commercial solutions with proven experience in Datacenter environments?</p></div><div id="comment-47882-info" class="comment-info"><span class="comment-age">(23 Nov '15, 11:29)</span> fturriaf</div></div><span id="47891"></span><div id="comment-47891" class="comment"><div id="post-47891-score" class="comment-score"></div><div class="comment-text"><ul><li>Riverbed (SteelCentral)</li><li>Savvius Omnipeek</li><li>Fluke</li><li>Endace</li><li>Netscout</li><li>Niksun (NetOmni)</li><li>AppDynamics</li><li>many more.</li></ul><p>"Network Performance Management" and "Application Performance Management" are they search keywords @ google.</p></div><div id="comment-47891-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:11)</span> Kurt Knochner ♦</div></div><span id="47892"></span><div id="comment-47892" class="comment"><div id="post-47892-score" class="comment-score"></div><div class="comment-text"><p>Yes, and additionally I would say...<br />
The best solution depends on your specific requirements.</p></div><div id="comment-47892-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:19)</span> Christian_R</div></div><span id="47894"></span><div id="comment-47894" class="comment"><div id="post-47894-score" class="comment-score"></div><div class="comment-text"><p>as always ;-)</p></div><div id="comment-47894-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:27)</span> Kurt Knochner ♦</div></div><span id="47899"></span><div id="comment-47899" class="comment"><div id="post-47899-score" class="comment-score"></div><div class="comment-text"><p>@Kurt: I liked your list.<br />
I just wanted to underline, that there is no general All in One Perfect Tool and so this list is the best answer to the question of @fturiaf.</p></div><div id="comment-47899-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:50)</span> Christian_R</div></div><span id="47905"></span><div id="comment-47905" class="comment not_top_scorer"><div id="post-47905-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I just wanted to underline, that there is no general All in One Perfect Tool</p></blockquote><p>That's how I understood your comment :-)</p></div><div id="comment-47905-info" class="comment-info"><span class="comment-age">(23 Nov '15, 16:46)</span> Kurt Knochner ♦</div></div><span id="47942"></span><div id="comment-47942" class="comment not_top_scorer"><div id="post-47942-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for advice. Best Regards</p></div><div id="comment-47942-info" class="comment-info"><span class="comment-age">(24 Nov '15, 14:10)</span> fturriaf</div></div><span id="47946"></span><div id="comment-47946" class="comment not_top_scorer"><div id="post-47946-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47946-info" class="comment-info"><span class="comment-age">(24 Nov '15, 16:49)</span> Kurt Knochner ♦</div></div><span id="48004"></span><div id="comment-48004" class="comment not_top_scorer"><div id="post-48004-score" class="comment-score"></div><div class="comment-text"><p>We are actually looking into an Network Performance Monitoring and diagnostic (NPMD) tool for our 2 DCs and we've seen demos of products from various brands, but do you want to monitor server- or network performance? All depend your requirements and budget. I agree with Kurt; using WS for that is not optimal, (Riverbed is using WS actually as deep packet analyzer) you'd need a tool that is doing analysis &amp; stats on live traffic, and can store it for some time so that you can do historic analysis. There are 2 different kind of tools on the market that can do this; 1. a network packet capturing and storing tool; you need to put in-line taps on network links or span traffic to monitor sessions in a switch/router 2. a Netflow collector, which uses Netflow traffic, but these will not give you performance stats and analysis; they are however cheaper and good for Security monitoring</p><p>Below are some additional brands for NPMD tools (add them to Kurt's list) that fall in the first category (but some can do also the 2nd one); Corvil Viavi solutions (formerly Network Instruments) SevOne Packet Design You probably might want to add a network capture aggregation layer, below some brands: Gigamon Ixia Arista</p><p>Other very interesting tools that are somehow doing analysis and statistics as well, but in a complete differnt way as packet capturing/analysing tools (for network) are listed below, take a look at their websites, it's worth while; LiveAction Netbrain</p><p>and other specials; Accedian Emelux</p><p>Good luck!</p></div><div id="comment-48004-info" class="comment-info"><span class="comment-age">(26 Nov '15, 07:30)</span> profke</div></div></div><div id="comment-tools-47877" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-47877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47879"></span>

<div id="answer-container-47879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47879-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or look at the right hand side column of this page. Riverbed, providing a home for Wireshark, may have solutions you seek.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-47879" class="comments-container"></div><div id="comment-tools-47879" class="comment-tools"></div><div class="clear"></div><div id="comment-47879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

