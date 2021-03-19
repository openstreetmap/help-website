+++
type = "question"
title = "network stack Wireshark driver placement"
description = '''How can I list the order of drivers in the Windows network stack. For example, when installing Wireshark winpcap will place itself before the NIC driver. I&#x27;m asking because I was reading that in case of VPN solutions sometimes Wireshark won&#x27;t be able to capture frames because of how the driver was w...'''
date = "2016-08-10T00:43:00Z"
lastmod = "2016-08-11T11:12:00Z"
weight = 54712
keywords = [ "wireshark" ]
aliases = [ "/questions/54712" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [network stack Wireshark driver placement](/questions/54712/network-stack-wireshark-driver-placement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54712-score" class="post-score" title="current number of votes">0</div><span id="post-54712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>How can I list the order of drivers in the Windows network stack. For example, when installing Wireshark winpcap will place itself before the NIC driver. I'm asking because I was reading that in case of VPN solutions sometimes Wireshark won't be able to capture frames because of how the driver was written so per my understanding the VPN's driver needs to be before winpcap and the physical NIC driver , correct?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '16, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '16, 00:46</strong> </span></p></div></div><div id="comments-container-54712" class="comments-container"></div><div id="comment-tools-54712" class="comment-tools"></div><div class="clear"></div><div id="comment-54712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54722"></span>

<div id="answer-container-54722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54722-score" class="post-score" title="current number of votes">2</div><span id="post-54722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Npcap is the NDIS 6 fork of WinPcap. And there is a sequence for all filter drivers in NDIS 6 stack. Some of the filters in my Win10 is here:<br />
</p><pre><code>Service Name  Description                                 FilterClass                 Inf File
MsBridge      Microsoft MAC Bridge                        ms_implatform               netbrdg.inf
WfpLwfs       WFP 802.3 MAC Layer LightWeight Filter      ms_firewall_upper           wfplwfs.inf  
WfpLwfs       WFP Native MAC Layer LightWeight Filter     ms_medium_converter_bottom  wfplwfs.inf  
WfpLwfs       Microsoft Windows Filtering Platform        ms_switch_filter            wfplwfs.inf  
vwififlt      Virtual WiFi Filter Driver                  ms_medium_converter_128     netvwififlt.inf  
npf           Npcap Packet Driver (NPCAP)                 compression                 npf.inf  
Psched        QoS Packet Scheduler                        scheduler                   netpacer.inf  
NativeWifiP   NativeWiFi Filter                           ms_medium_converter_top     netnwifi.inf  
NdisCap       Microsoft NDIS Capture                      ms_switch_capture           ndiscap.inf  
jnprns        Juniper Network Service                     NULL                        jnprns.inf  
VBoxNetLwf    VirtualBox NDIS6 Bridged Networking Driver  compression                 VBoxNetLwf.inf</code></pre><p>The most important part is the FilterClass. It determines the filter sequence. It's defined <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545161%28v=vs.85%29.aspx?f=255&amp;MSPPError=-2147217396">here</a>.</p><p>The sequence is:</p><pre><code>ms_firewall_upper
scheduler
encryption
compression
vpn
loadbalance
failover
diagnostic
custom
provider_address
ms_implatform
ms_switch_capture
ms_switch_filter
ms_switch_reserved
ms_switch_forward
ms_firewall_lower
ms_medium_converter_top
ms_medium_converter_128
ms_medium_converter_bottom</code></pre><p>Npcap's FilterClass is compression. So it will be higher than all "vpn" filters and lower than "encryption" filters.</p><p>But I don't quite know VPN drivers, you can't think they are using the "vpn" FilterClass. Because when you capture on Wireshark with Npcap, you can still see VPN encrypted packets. So it means that Npcap is lower than VPN softwares.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '16, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p><span>Yang Luo</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '16, 02:01</strong> </span></p></div></div><div id="comments-container-54722" class="comments-container"><span id="54727"></span><div id="comment-54727" class="comment"><div id="post-54727-score" class="comment-score"></div><div class="comment-text"><p>So the Npcap driver is a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545161(v=vs.85).aspx"><em>modifying</em> filter driver</a> rather than a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545162(v=vs.85).aspx"><em>monitoring</em> filter driver</a>?</p></div><div id="comment-54727-info" class="comment-info"><span class="comment-age">(10 Aug '16, 17:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="54728"></span><div id="comment-54728" class="comment"><div id="post-54728-score" class="comment-score">1</div><div class="comment-text"><p><span></span><span>@Guy Harris</span>, yes. Npcap has been a modifying LWF from the very beginning. Because a monitoring filter can't originate its own packets into the NDIS stack, but Npcap needs to send packets in the Tx way.</p></div><div id="comment-54728-info" class="comment-info"><span class="comment-age">(10 Aug '16, 17:39)</span> <span class="comment-user userinfo">Yang Luo</span></div></div><span id="54734"></span><div id="comment-54734" class="comment"><div id="post-54734-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure i got it all right, but wouldn't that mean that a network capture using NETSH would capture the greatest amount of packets?</p></div><div id="comment-54734-info" class="comment-info"><span class="comment-age">(11 Aug '16, 01:14)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="54737"></span><div id="comment-54737" class="comment"><div id="post-54737-score" class="comment-score"></div><div class="comment-text"><p>On what do you base such conclusion? Do you know which of the filter classes <code>netsh</code> is using to capture?</p></div><div id="comment-54737-info" class="comment-info"><span class="comment-age">(11 Aug '16, 01:37)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54749"></span><div id="comment-54749" class="comment"><div id="post-54749-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> That's the point. Maybe I'm wrong I don't know I just try to understand. I have the following filters on my Windows 7: Filter Count: 9 Filter List:</p><p>Description : Virtual WiFi Filter Driver PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{5CBF81BF-5055-47CD-9055-A76B2B4E3698}</p><p>Description : Microsoft Network Monitor 3 Driver PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{6E022F38-AB31-44C5-8206-2EB023EFF145}</p><p>Description : Symantec Endpoint Protection Firewall PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{72891E7B-0A3D-4541-BDCB-3DA62E25B6A8}</p><p>Description : QoS Packet Scheduler PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{B5F4D659-7DAA-4565-8E41-BE220ED60542}</p><p>Description : WFP Lightweight Filter PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{B70D6460-3635-4D42-B866-B8AB1A24454C}</p><p>Description : Microsoft PEF NDIS ETW Provider Driver PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{BD583A2D-7410-4BD1-B9C0-ECA0E65E6980}</p><p>Description : Juniper Network Service PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{C02D1E54-FBAB-46BB-8052-BE25AB90C99A}</p><p>Description : NativeWiFi Filter PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{E475CF9A-60CD-4439-A75F-0079CE0E18A1}</p><p>Description : NDIS Capture LightWeight Filter PSPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\system\currentcontrolset\control\network{4d36e974 -e325-11ce-bfc1-08002be10318}{EA24CD6C-D17A-4348-9190-09F0D5BE83DD}</p><p>Microsoft Network Monitor 3 Driver was installed because I’ve installed NetMon. I can see one for Juniper (it’s my VPN). Is there a way to list the preferred order of which filter is going to be used ?</p></div><div id="comment-54749-info" class="comment-info"><span class="comment-age">(11 Aug '16, 07:49)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="54751"></span><div id="comment-54751" class="comment not_top_scorer"><div id="post-54751-score" class="comment-score"></div><div class="comment-text"><p>Adam, some months ago <span>@Yang Luo</span> gave me a link to a <a href="http://www.nirsoft.net/utils/installed_drivers_list.html">software which allows to list all drivers</a>. That software, if I remember right, shows the FilterClass of the driver. Or you can use <code>regedit</code> to find the FilterClass, using one of the long hexadecimal IDs as a search key.</p></div><div id="comment-54751-info" class="comment-info"><span class="comment-age">(11 Aug '16, 08:09)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54753"></span><div id="comment-54753" class="comment not_top_scorer"><div id="post-54753-score" class="comment-score"></div><div class="comment-text"><p>If you mean InstalledDriversList, it probably doesn't show you the FilterClass, because it's not only for NDIS filter drivers. There is no ready way to get the existing filters' sequence automatically. You can write a program to read the registry key to do that. Read their FilterClass, then match them with MSDN's sequence.</p></div><div id="comment-54753-info" class="comment-info"><span class="comment-age">(11 Aug '16, 09:07)</span> <span class="comment-user userinfo">Yang Luo</span></div></div></div><div id="comment-tools-54722" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-54722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54713"></span>

<div id="answer-container-54713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54713-score" class="post-score" title="current number of votes">1</div><span id="post-54713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This document: "Fulvio Risso, Loris Degioanni, <a href="https://winpcap.org/docs/iscc01-wpcap.pdf">An Architecture for High Performance Network Analysis</a>, Proceedings of the 6th IEEE Symposium on Computers and Communications (ISCC 2001), Hammamet, Tunisia, July 2001", contains the most detailed description there is on this subject, especially section 4.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '16, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54713" class="comments-container"><span id="54716"></span><div id="comment-54716" class="comment"><div id="post-54716-score" class="comment-score">1</div><div class="comment-text"><p>The npcap project aims at replacing winpcap with a more modern driver <a href="https://github.com/nmap/npcap">https://github.com/nmap/npcap</a></p></div><div id="comment-54716-info" class="comment-info"><span class="comment-age">(10 Aug '16, 03:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="54755"></span><div id="comment-54755" class="comment"><div id="post-54755-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The npcap project aims at replacing winpcap with a more modern driver</p></blockquote><p>See <span>@Yang Luo</span>'s answer above for some information about it. (The more modern driver only works on Windows Vista and later, as it requires NDIS 6.)</p></div><div id="comment-54755-info" class="comment-info"><span class="comment-age">(11 Aug '16, 11:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-54713" class="comment-tools"></div><div class="clear"></div><div id="comment-54713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

