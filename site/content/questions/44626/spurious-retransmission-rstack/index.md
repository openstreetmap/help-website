+++
type = "question"
title = "Spurious Retransmission RST,ACK"
description = '''We are experiencing an issue when uploading a file to a sFTP server. Most of the time the upload is a success, however occasionally it fails. Running Wireshark we discovered we are sending a SYN frame and receiving a RST,ACK seemingly from destination (but I have doubts about that). Looking at the f...'''
date = "2015-07-30T05:19:00Z"
lastmod = "2015-07-30T11:52:00Z"
weight = 44626
keywords = [ "spurious", "retransmissions", "rst+ack" ]
aliases = [ "/questions/44626" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Spurious Retransmission RST,ACK](/questions/44626/spurious-retransmission-rstack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44626-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are experiencing an issue when uploading a file to a sFTP server. Most of the time the upload is a success, however occasionally it fails. Running Wireshark we discovered we are sending a SYN frame and receiving a RST,ACK seemingly from destination (but I have doubts about that). Looking at the failed trace I see where we try and establish connection multiple times before giving up. One thing I note as odd is the response time between frames, they're approximately 0.000733 seconds on the failed connection. For the successful connection the response times are approximately 0.031923 seconds. I've included a screenshot of both the failure and success.</p><p><strong>Notes</strong></p><ul><li>When this occurs we can usually correct it by logging into the source server via RDP and it instantly begins working.</li><li>We've moved this process to another source server but continue to have the problem.</li><li>I'm not seeing any of this traffic in my ASA</li><li>Source: Windows 2012 R2 (We also tried running on Windows 2008 R2)</li><li>I have no control over destination, furthermore they have told me we are the only ones with this problem</li></ul><p><strong><a href="http://i.imgur.com/tTzc3l0.png">Failure Screenshot</a> <img src="http://i.imgur.com/tTzc3l0.png" alt="Failure Screenshot" /></strong></p><p><strong><a href="http://i.imgur.com/pv0GODo.png">Success Screenshot</a> <img src="http://i.imgur.com/pv0GODo.png" alt="Success Screenshot" /></strong></p><p><strong>Network Topology</strong></p><p>[ Source Server ] ---- [ Web Filter (only port 80) ] ---- [ ASA w/ IPS Module ] ---- [ Link Balancer ] ---- [ Internet ] ---- [ Destination]</p></div><div id="question-tags" class="tags-container tags">spurious retransmissions rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/cc3ebb4ccc3c300af10662cb6439db09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlpitch&#39;s gravatar image" /><p>tlpitch<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlpitch has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44626" class="comments-container"><span id="44648"></span><div id="comment-44648" class="comment"><div id="post-44648-score" class="comment-score"></div><div class="comment-text"><p>I noticed the ECN flag as well and thought that could be the issue, however it is something that MS enabled in Windows 2012. We're running this process on a Windows 2008 box at the moment and the Wireshark during the failures shows it is not present. Additionally I have traces that show successful connection with ECN enabled.</p><p>I like you thought the same thing, so upon researching I found that I could disable ECN but that didn't help on the Windows 2012.</p><p>When we are having failures I've run traces from the ASA and I don't see any traffic during the times where we have a failure.</p><p><strong>ECN</strong> <a href="http://serverfault.com/questions/526377/is-ecn-explicit-congestion-notification-turned-on-by-default-on-windows-server">http://serverfault.com/questions/526377/is-ecn-explicit-congestion-notification-turned-on-by-default-on-windows-server</a></p></div><div id="comment-44648-info" class="comment-info"><span class="comment-age">(30 Jul '15, 12:47)</span> tlpitch</div></div><span id="44649"></span><div id="comment-44649" class="comment"><div id="post-44649-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the following outputs?</p><pre><code>netsh int tcp show global output?</code></pre><p>And the following Powershell displays at the Win2012.</p><pre><code>Get-NetAdapter
Get-NetAdapterAdvancedProperty
Get-NetAdapterHardwareInfo
Get-NetTCPSetting</code></pre><p>If you say, that you have succesfull traces with a ECN inside, do you mean to that sFTP server?</p></div><div id="comment-44649-info" class="comment-info"><span class="comment-age">(30 Jul '15, 13:01)</span> Christian_R</div></div><span id="44650"></span><div id="comment-44650" class="comment"><div id="post-44650-score" class="comment-score"></div><div class="comment-text"><p>I've included two server outputs. The 2008 is the one the application folks move the process for testing. The 2012 box is the one we started using and ultimately wish to use- both produce the same failures.</p><p>On the Windows 2008 (the current system) TCP Global Parameters</p><hr /><p>Receive-Side Scaling State : enabled Chimney Offload State : automatic NetDMA State : enabled Direct Cache Acess (DCA) : disabled Receive Window Auto-Tuning Level : normal Add-On Congestion Control Provider : ctcp ECN Capability : disabled RFC 1323 Timestamps : disabled</p><p>On the Windows 2012 (the desired system) TCP Global Parameters</p><hr /><p>Receive-Side Scaling State : enabled Chimney Offload State : disabled NetDMA State : disabled Direct Cache Access (DCA) : disabled Receive Window Auto-Tuning Level : normal Add-On Congestion Control Provider : none ECN Capability : disabled RFC 1323 Timestamps : disabled Initial RTO : 3000 Receive Segment Coalescing State : enabled Non Sack Rtt Resiliency : disabled Max SYN Retransmissions : 2</p></div><div id="comment-44650-info" class="comment-info"><span class="comment-age">(30 Jul '15, 13:13)</span> tlpitch</div></div><span id="44670"></span><div id="comment-44670" class="comment"><div id="post-44670-score" class="comment-score"></div><div class="comment-text"><p>maybe you have to set the congestion control provider to ctcp like the win2008</p></div><div id="comment-44670-info" class="comment-info"><span class="comment-age">(31 Jul '15, 01:25)</span> Christian_R</div></div></div><div id="comment-tools-44626" class="comment-tools"></div><div class="clear"></div><div id="comment-44626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44643"></span>

<div id="answer-container-44643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44643-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi I can´t remember that I have seen a packet like Frame #7, (SYN,ECN,CWR) and maybe your FW/IPS eitehr not. So if I were you, I would take a trace at the last point of my network, so that I can see if the packet left my network correctly.</p><hr /><p>Edit:</p><p>Ok at least I found that the Syn in frame 7 is correct see here: <a href="https://tools.ietf.org/html/rfc3168">https://tools.ietf.org/html/rfc3168</a></p><p>Also it can be seen that Frame 7 starts with rfc3168 feature than goes back to to rfc1323 and ends in the old tcp syn request. This is like an normal behaviour. So I guess that the most probable cause for the failure is in or next to your FW or IPS (Maybe it is a bug of this device)</p><hr /><p>See similar question here: <a href="https://ask.wireshark.org/questions/29758/syn-with-ecn-flag-set-on-certain-port-number">https://ask.wireshark.org/questions/29758/syn-with-ecn-flag-set-on-certain-port-number</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '15, 01:22</p></div></div><div id="comments-container-44643" class="comments-container"></div><div id="comment-tools-44643" class="comment-tools"></div><div class="clear"></div><div id="comment-44643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

