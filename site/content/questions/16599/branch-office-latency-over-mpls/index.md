+++
type = "question"
title = "Branch office latency over MPLS"
description = '''Note: fairly green at Wireshark Scenario: We have branch offices connected to our main office via MPLS VPN. Branch offices use thin clients and VoIP phones. Users RDP to virtual desktop on ESX Server. On random days and random times these branch offices have one minute outages where their RDP sessio...'''
date = "2012-12-05T09:44:00Z"
lastmod = "2012-12-05T12:39:00Z"
weight = 16599
keywords = [ "latency", "mpls", "rdp", "branch" ]
aliases = [ "/questions/16599" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Branch office latency over MPLS](/questions/16599/branch-office-latency-over-mpls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Note: fairly green at Wireshark</p><p>Scenario: We have branch offices connected to our main office via MPLS VPN. Branch offices use thin clients and VoIP phones. Users RDP to virtual desktop on ESX Server.</p><p>On random days and random times these branch offices have one minute outages where their RDP session will say "Reconnecting" and the voice call is lost. After a minute the RDP sessions and VoIP are fine.</p><p>Is it possible to capture this latency even though I don't know when it will happen again? The time range is from 815am-2pm.</p><p>I've verified the WAN circuit hasn't dropped and calls to Cisco indicate a LAN issue between the edge router &gt; firewall &gt; switch &gt; ESX Server.</p><p>I'd like to capture packets remotely and locally but don't know where to start.</p></div><div id="question-tags" class="tags-container tags">latency mpls rdp branch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/e5e8587e540ff45ccb1aa1f99f529407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jtlg&#39;s gravatar image" /><p>jtlg<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jtlg has no accepted answers">0%</span></p></div></div><div id="comments-container-16599" class="comments-container"></div><div id="comment-tools-16599" class="comment-tools"></div><div class="clear"></div><div id="comment-16599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16611"></span>

<div id="answer-container-16611" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16611-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you don't know when it happens, you can only capture with a ring buffer of files and stop the capture as soon as the problem was detected.</p><ul><li>Configure port mirroring on the switch, where your ESX server is connected</li><li>Attach a capture PC to the mirrored port</li><li>run dumpcap</li></ul><blockquote><p><code>dumpcap -ni 1 -w mpls_error.cap -s 200 -b filesize:150000 -b files:50 -f "port 3389 and (net 10.1.0.0/24 or net 10.2.0.0/24)"</code><br />
</p></blockquote><p>This will write 50 files, named mpls_error_xxxxx.cap (xxxxxx will be replaced by a time stamp). Each file will have a size of 150 MByte. If dumpcap reaches file nr. 50, it will overwrite file nr. 1, etc.</p><p>So, you will have a circular ring buffer of 50 files, each with 150 Mbyte size. As the packets are truncated at 200 bytes (-s 200), you will be able to capture a lot of sessions. This will consume max. 7.5 Gbyte on your disk, no matter how long it runs.</p><p>Comments:<br />
</p><ul><li>10.1.0.0/24 and 10.2.0.0/24 are the networks of your remote offices.</li><li>figure out the interface for option -i with: <strong><code>dumpcap -D -M</code></strong></li><li>you might have to use different values for <strong>filesize</strong> and <strong>files</strong>, depending on the amount of data in your network</li></ul><p>Now, as soon as the problem was detected, you or the network people need to <strong>stop dumpcap rather quickly</strong>, to prevent it from overwriting the part where the problem occurred. How quick you have to do it, depends on how much data is captured. Just observe how long it takes to write 10 of those 150 MByte files and then possibly adjust the options <strong>filesize</strong> and <strong>files</strong> to have enough time to stop dumpcap after the problem has been reported.</p><p>If you let the people record the exact time of the problem (and your capture PC is configured with the "real time"), you will easily find the capture file and within that file, the time frame where the problem occurred.</p><p>That was easy. Now you will have to walk through the captured data and try to figure out what went wrong. Maybe the capture filter (optione: -f) needs to be extended, if you can't identify the problem in the first tests.</p><blockquote><p>I'd like to capture packets remotely and locally but don't know where to start.</p></blockquote><p>yes, good idea. Please repeat the above steps for the remote location. Mirror the port where your MPLS router is connected to the network of the remote location.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 12:56</p></div></div><div id="comments-container-16611" class="comments-container"><span id="16679"></span><div id="comment-16679" class="comment"><div id="post-16679-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'll work my way through your steps</p></div><div id="comment-16679-info" class="comment-info"><span class="comment-age">(07 Dec '12, 06:47)</span> jtlg</div></div><span id="16684"></span><div id="comment-16684" class="comment"><div id="post-16684-score" class="comment-score"></div><div class="comment-text"><p>you're welcome.</p><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-16684-info" class="comment-info"><span class="comment-age">(07 Dec '12, 07:44)</span> Kurt Knochner ♦</div></div><span id="16803"></span><div id="comment-16803" class="comment"><div id="post-16803-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>I have this up and running on the LAN side. Thanks for your help!</p></div><div id="comment-16803-info" class="comment-info"><span class="comment-age">(12 Dec '12, 07:44)</span> jtlg</div></div></div><div id="comment-tools-16611" class="comment-tools"></div><div class="clear"></div><div id="comment-16611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

