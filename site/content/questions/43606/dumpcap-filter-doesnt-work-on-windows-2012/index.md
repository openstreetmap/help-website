+++
type = "question"
title = "Dumpcap filter doesn&#x27;t work on Windows 2012"
description = '''Hi, I recently installed the latest Wireshark &amp;amp; Winpcap on a Windows 2012 server. When I want to use the dumpcap command straight from the dos prompt and add a filter, it is not capturing any packets (while I know the filter should provide packets). There is no syntax error.  Same dumpcap under ...'''
date = "2015-06-27T14:41:00Z"
lastmod = "2015-06-29T07:47:00Z"
weight = 43606
keywords = [ "capture-filter", "dumpcap" ]
aliases = [ "/questions/43606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap filter doesn't work on Windows 2012](/questions/43606/dumpcap-filter-doesnt-work-on-windows-2012)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I recently installed the latest Wireshark &amp; Winpcap on a Windows 2012 server. When I want to use the dumpcap command straight from the dos prompt and add a filter, it is not capturing any packets (while I know the filter should provide packets). There is no syntax error.</p><p>Same dumpcap under either W7 or W2008R2 works fine.</p><p>I tried to run the DOS box under admin rights, but no difference.</p><p>Any ideas?</p><p>Thanks Marc</p></div><div id="question-tags" class="tags-container tags">capture-filter dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '15, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/a9fbf0d7d0306d5552b6adebfb69892b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mlaporte74&#39;s gravatar image" /><p>mlaporte74<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mlaporte74 has no accepted answers">0%</span></p></div></div><div id="comments-container-43606" class="comments-container"><span id="43607"></span><div id="comment-43607" class="comment"><div id="post-43607-score" class="comment-score"></div><div class="comment-text"><p>Does <a href="http://www.winpcap.org/windump/default.htm">WinDump</a> work? Can Wireshark capture with the same filter? If not, this is probably a WinPcap problem.</p></div><div id="comment-43607-info" class="comment-info"><span class="comment-age">(27 Jun '15, 15:00)</span> Guy Harris ♦♦</div></div><span id="43608"></span><div id="comment-43608" class="comment"><div id="post-43608-score" class="comment-score"></div><div class="comment-text"><p>What are your dumpcap CLI options and what is the output of <strong>dumpcap -D -M</strong>?</p></div><div id="comment-43608-info" class="comment-info"><span class="comment-age">(27 Jun '15, 15:07)</span> Kurt Knochner ♦</div></div><span id="43662"></span><div id="comment-43662" class="comment"><div id="post-43662-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for the responses so far. Here's the requested info...</p><p>Windump doesn't work on W2012, so I can't install this to test it with.</p><p>Yes, I can capture with Wireshark with the same filter, and get expected output.</p><pre><code>E:\Program Files (x86)\Wireshark&gt;dumpcap -i 1 -b duration:600 -f &quot;host 172.23.66.83&quot; -w &quot;E:\Dumpfiles\capture.pcap&quot;
Capturing on &#39;VLAN 194&#39;
File: E:\Dumpfiles\capture_00001_20150629154350.pcap
Packets captured: 0
Packets received/dropped on interface &#39;VLAN 194&#39;: 0/0 (pcap:0/dumpcap:0/flushed:0/ps_ifdrop:0) (0.0%)

E:\Program Files (x86)\Wireshark&gt;dumpcap -D -M
1. \Device\NPF_{175C0321-A028-4589-9373-70FAA304CE05}   VMware vmxnet3 virtual network device   VLAN 194        8       fe80::e03b:c307:2efc:2639,172.22.36.91        network</code></pre></div><div id="comment-43662-info" class="comment-info"><span class="comment-age">(29 Jun '15, 06:51)</span> mlaporte74</div></div><span id="43683"></span><div id="comment-43683" class="comment"><div id="post-43683-score" class="comment-score"></div><div class="comment-text"><p>Correction: I <em>cannot</em> use the capture filter on wireshark either.</p><p>If it's a winpcap issue, what to do?</p><p>Using suggested filter (vlan and host) makes no difference</p><p>dumpcap -i 1 -b duration:600 -f "vlan and host 172.23.66.83" -w "E:\Dumpfiles\capture.pcap"</p></div><div id="comment-43683-info" class="comment-info"><span class="comment-age">(29 Jun '15, 12:42)</span> mlaporte74</div></div></div><div id="comment-tools-43606" class="comment-tools"></div><div class="clear"></div><div id="comment-43606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43664"></span>

<div id="answer-container-43664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43664-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The name of the interface (VLAN 194) implies, that there is a VLAN configured on that interface.</p><p>Please try the following:</p><blockquote><p>dumpcap -i 1 -b duration:600 -f "<strong>vlan and</strong> host 172.23.66.83" -w "E:\Dumpfiles\capture.pcap"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43664" class="comments-container"></div><div id="comment-tools-43664" class="comment-tools"></div><div class="clear"></div><div id="comment-43664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

