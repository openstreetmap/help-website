+++
type = "question"
title = "interface Linkspeed"
description = '''Hi, we have an HP G6 DL380 running window7 SP1, we have the Intel X520D-2 (10GIG NIC) installed, the OS &amp;amp; router both indicated link speed 10g full duplex, but the wireshark interface detail stated it&#x27;s only a 1410mbps link speed.  we are using wireshark version 1.11.2 Rev 53411 (64 bits) ; WinP...'''
date = "2014-01-29T12:47:00Z"
lastmod = "2014-01-30T05:36:00Z"
weight = 29288
keywords = [ "interface", "speed", "link" ]
aliases = [ "/questions/29288" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [interface Linkspeed](/questions/29288/interface-linkspeed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29288-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, we have an HP G6 DL380 running window7 SP1, we have the Intel X520D-2 (10GIG NIC) installed, the OS &amp; router both indicated link speed 10g full duplex, but the wireshark interface detail stated it's only a 1410mbps link speed. we are using wireshark version 1.11.2 Rev 53411 (64 bits) ; WinPcap 4.1.3</p><p>any suggestion ??</p><p>Thanks in advance Anh</p></div><div id="question-tags" class="tags-container tags">interface speed link</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/50c7fb43ecfb7d6016dd649b771c98df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Texamau&#39;s gravatar image" /><p>Texamau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Texamau has no accepted answers">0%</span></p></div></div><div id="comments-container-29288" class="comments-container"></div><div id="comment-tools-29288" class="comment-tools"></div><div class="clear"></div><div id="comment-29288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29309"></span>

<div id="answer-container-29309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29309-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This could be a driver problem or a WinPcap problem (from where Wireshark gets the information about the NIC speed), or even a Wireshark bug (which I don't believe).</p><p>To get closer to the answer, please post the output of the following commands:</p><blockquote><p>dumpcap -D -M<br />
</p></blockquote><p>plus</p><blockquote><p>wmic NIC where NetEnabled=true list full<br />
</p></blockquote><p>or</p><blockquote><p>wmic NIC where NetEnabled=true get Name, Speed</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '14, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '14, 07:32</p></div></div><div id="comments-container-29309" class="comments-container"><span id="29316"></span><div id="comment-29316" class="comment"><div id="post-29316-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Here's the results:</p><pre><code>C:\Program Files\Wireshark&gt;dumpcap -D -M
1. \Device\NPF_{C2B5CD33-AF50-4E37-8719-2B03B7A3DE61}   Broadcom L2 NDIS client
driver  ALU135 MB eth#1 0       fe80::cd2d:8d8f:423:db0b,135.112.74.80  network
2. \Device\NPF_{9FC40E92-445D-4CA0-9F03-0B29CE55F2B3}   Intel(R) Ethernet Server
 Adapter X520-2 PDN3-10-1-12    0       fe80::801:188f:cd23:c191,fe80::801:188f:
cd23:c191       network
3. \Device\NPF_{13E4F5A6-2670-4F88-9AF8-F2115100AD89}   Broadcom L2 NDIS client
driver  5-2-19 pdncore-4 MB eth#3       0       fe80::58f4:1c93:9f14:b3f4,11.11.
11.2    network
4. \Device\NPF_{EFBA455E-5AE7-4741-AF00-7999CA77F034}   Broadcom L2 NDIS client
driver  5-2-19 pdncore-3 MB eth#4       0       fe80::1046:5fbb:adb6:c1f9,3.3.3.
2       network
5. \Device\NPF_{039367CD-0BAD-4446-84D0-C812295D6C38}   Broadcom L2 NDIS client
driver  2-1-3 pdncore1 MB eth#2 0       fe80::211a:2793:8e3b:c5c7,10.10.10.2
network
6. \Device\NPF_{D59296F6-A407-4D5B-818B-C7985286605E}   Intel(R) Ethernet Server
 Adapter X520-2 PDN4-10-1-12    0       fe80::a05b:4860:bdf7:d4f1,4.4.4.4
network

C:\Program Files\Wireshark&gt;</code></pre></div><div id="comment-29316-info" class="comment-info"><span class="comment-age">(30 Jan '14, 07:10)</span> Texamau</div></div><span id="29317"></span><div id="comment-29317" class="comment"><div id="post-29317-score" class="comment-score"></div><div class="comment-text"><p>what about the <code>wmic</code> command (see my answer)?</p></div><div id="comment-29317-info" class="comment-info"><span class="comment-age">(30 Jan '14, 07:17)</span> Kurt Knochner ♦</div></div><span id="29325"></span><div id="comment-29325" class="comment"><div id="post-29325-score" class="comment-score"></div><div class="comment-text"><p>here the wmic cmd:</p><pre><code>C:\Program Files\Wireshark&gt;
C:\Program Files\Wireshark&gt;wmic NIC where NetEnabled=true get NAme, Speed
Name                                                      Speed
Broadcom BCM5709C NetXtreme II GigE (NDIS VBD Client)     1000000000
Broadcom BCM5709C NetXtreme II GigE (NDIS VBD Client) #2  1000000000
Broadcom BCM5709C NetXtreme II GigE (NDIS VBD Client) #3  1000000000
Broadcom BCM5709C NetXtreme II GigE (NDIS VBD Client) #4  100000000
Intel(R) Ethernet Server Adapter X520-2                   10000000000

C:\Program Files\Wireshark&gt;</code></pre></div><div id="comment-29325-info" class="comment-info"><span class="comment-age">(30 Jan '14, 11:29)</span> Texamau</div></div><span id="29327"></span><div id="comment-29327" class="comment"><div id="post-29327-score" class="comment-score"></div><div class="comment-text"><p>O.K. as windows shows the correct value, it's most certainly a WinPcap problem. Please report the bug to the WinPcap folks at www.winpcap.org</p></div><div id="comment-29327-info" class="comment-info"><span class="comment-age">(30 Jan '14, 11:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29309" class="comment-tools"></div><div class="clear"></div><div id="comment-29309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

