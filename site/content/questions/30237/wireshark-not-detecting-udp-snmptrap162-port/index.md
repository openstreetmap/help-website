+++
type = "question"
title = "Wireshark not detecting udp snmptrap/162 port"
description = '''Hi Can someone please advise how I can trace udp snmptrap/162 port on a Windows 7 PRO system using wireshark as I never see anything, using udp.port==162 filter or no filter (capturing everything). Using Windows sysinternals process monitor I can see the following when monitoring SNMP trap snmptrap....'''
date = "2014-02-27T09:00:00Z"
lastmod = "2014-02-28T07:22:00Z"
weight = 30237
keywords = [ "snmptrap", "udp", "port", "162" ]
aliases = [ "/questions/30237" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not detecting udp snmptrap/162 port](/questions/30237/wireshark-not-detecting-udp-snmptrap162-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30237-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Can someone please advise how I can trace udp snmptrap/162 port on a Windows 7 PRO system using wireshark as I never see anything, using udp.port==162 filter or no filter (capturing everything).</p><p>Using Windows sysinternals process monitor I can see the following when monitoring SNMP trap snmptrap.exe service:</p><pre><code>Date: 27/02/2014 16:28:58
Thread: 0
Class: Network
Operation: UDP Receive
Result: SUCCESS
Path: FQDN:snmptrap -&gt; FQDN:49589
Duration: 0.000000

Length: 43
seqnum: 0
connid: 0</code></pre><p>Any ideas please,</p><p>I can see the trap using snmputil.exe from windows resource kit:</p><pre><code>Incoming Trap:
  generic    = 6
  specific   = 1
  enterprise = .iso.org.dod.internet.private.enterprises.2854
  agent      = 192.168.154.114
  source IP  = 192.168.154.114
  community  = public</code></pre><p>Thank you,</p><p>Best Regards - Colin</p></div><div id="question-tags" class="tags-container tags">snmptrap udp port 162</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/d28e7a8f671e1a0d79e3e7b2b9f631d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Colin&#39;s gravatar image" /><p>Colin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Colin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '14, 07:10</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30237" class="comments-container"></div><div id="comment-tools-30237" class="comment-tools"></div><div class="clear"></div><div id="comment-30237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30268"></span>

<div id="answer-container-30268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30268-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you did not say where and how you captured the traffic, I'll have to assume several things, which is not good. It would have been better, if you had added that information in the first place ;-)</p><p><strong>Case #1:</strong> You captured on the SNMP client<br />
In this case, <strong>you're not seeing outgoing traffic</strong> (SNMP trap sender -&gt; SNMP trap receiver). This has been reported in many other cases. Very often the problem has been some interfering software like AV, IDS, VPN client, Firewall, Endpoint Security (especially Symantec). If there is any security software running on the capturing system, try to disable or uninstall that software and then repeat your tests. If disabling/uninstalling is not an option, you need a different system (without that software) to capture traffic, like a bootable Linux CDROM or USB flash drive (see <a href="http://kali.org">Kali Linux</a>).</p><p>See also: <a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a></p><p><strong>Case #2:</strong> You captured on the SNMP <strong>server</strong>, aka SNMP trap receiver<br />
In this case, you're not seeing <strong>incoming traffic</strong> (SNMP traps coming in). Well, it could be interfering software as well, so see case #1. But more often the problem is that the traffic is simply not reaching the target system. Please double check that everything is setup correctly.</p><p><strong>Case #3:</strong> You captured on a system where you sent SNMP traps <strong>to the same system</strong> (localhost) for testing.<br />
In this case, you <strong>cannot see</strong> that traffic in Wireshark, as WinPcap is unable to capture localhost traffic. What you need is <a href="http://www.netresec.com/?page=RawCap">RawCap</a>.</p><p>If none of the above cases apply, please add more details about your environment.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '14, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-30268" class="comments-container"><span id="30337"></span><div id="comment-30337" class="comment"><div id="post-30337-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thank you for your reply. I'm running everything locally on a Windows 7 PRO PC, trapgen.exe -d 192.168.154.114 (third party tool) to generate trap and snmputil.exe (Windows resource kit) trap to capture; Microsoft Sysinternals Windows Process explorer to doubly verify.</p><p>I've repeated my test with rawcap.exe capturing the local lan interface, not localhost as that has static IP 192.168.154.114 bound and I specify that IP in my trap test, I'm pleased to report that rawcap.exe consistently captures the snmptrap; but with wireshark and its default winpcap it does not appear to capture snmptrap; latest stable and development releases tried.</p><p>I do have Symantec Endpoint Protection (SEP) enforced by GPO, can’t disable it even though I’m a member of local administrator group, :-(.</p><p>Best Regards - Colin</p></div><div id="comment-30337-info" class="comment-info"><span class="comment-age">(02 Mar '14, 23:22)</span> Colin</div></div><span id="30338"></span><div id="comment-30338" class="comment"><div id="post-30338-score" class="comment-score"></div><div class="comment-text"><p>I’m fairly sure, but need to double check, that windows netmon tool also didn't capture snmptrap, so interesting to find that rawcap.exe did.</p></div><div id="comment-30338-info" class="comment-info"><span class="comment-age">(02 Mar '14, 23:27)</span> Colin</div></div><span id="30340"></span><div id="comment-30340" class="comment"><div id="post-30340-score" class="comment-score"></div><div class="comment-text"><p>WinPCap does not capture "localhost" traffic, the OS doesn't allow the traffic to get down the stack to the point where WinPCap can see it. See the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback capture</a> wiki page for more info.</p></div><div id="comment-30340-info" class="comment-info"><span class="comment-age">(03 Mar '14, 02:04)</span> grahamb ♦</div></div><span id="30345"></span><div id="comment-30345" class="comment"><div id="post-30345-score" class="comment-score"></div><div class="comment-text"><p>Aha I think I understand, I have confused reference to "localhost" with "loopback" 127.0.0.1; "localhost" refers to all interfaces on localhost. Thank you.</p></div><div id="comment-30345-info" class="comment-info"><span class="comment-age">(03 Mar '14, 03:38)</span> Colin</div></div><span id="30351"></span><div id="comment-30351" class="comment"><div id="post-30351-score" class="comment-score"></div><div class="comment-text"><p>Actually 'localhost' refers to intra system traffic, regardless of the IP address used (127.0.0.1 or 192.168.154.114), as long as the sender and recipient is the same system.</p></div><div id="comment-30351-info" class="comment-info"><span class="comment-age">(03 Mar '14, 10:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30268" class="comment-tools"></div><div class="clear"></div><div id="comment-30268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

