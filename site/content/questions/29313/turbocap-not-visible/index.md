+++
type = "question"
title = "turbocap / not visible"
description = '''I&#x27;ve employed several Turbocap boards, under Win7, and they just work: slide the card in, power on the machine, run the installer, and presto: both dumpcap and Wireshark see three additional ports (A, B, and the Aggregating function). But I&#x27;m stumbling on my latest install. TurboCap-1.4.1843.846 Tur...'''
date = "2014-01-30T06:21:00Z"
lastmod = "2014-03-05T22:10:00Z"
weight = 29313
keywords = [ "turbocap", "install", "wireshark" ]
aliases = [ "/questions/29313" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [turbocap / not visible](/questions/29313/turbocap-not-visible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've employed several Turbocap boards, under Win7, and they just work: slide the card in, power on the machine, run the installer, and presto: both dumpcap and Wireshark see three additional ports (A, B, and the Aggregating function).</p><p>But I'm stumbling on my latest install.</p><p>TurboCap-1.4.1843.846 TurboCap2 board Win7 64-bit Winpcap 4.1.3</p><p>The installation log reports success:</p><pre><code>[000007D0] 2014-01-30 06:11:48 LOG Event: 1, ENTER:  DriverPackageInstallW
[000007D0] 2014-01-30 06:11:48 LOG Event: 2, DRIVER_PACKAGE_LEGACY_MODE flag set but not supported on Plug and Play driver on VISTA. Flag will be ignored.
[000007D0] 2014-01-30 06:11:55 LOG Event: 1, Installing INF file &#39;C:\Program Files (x86)\CACE Technologies\TurboCap\driver\tc.inf&#39; (Plug and Play).
[000007D0] 2014-01-30 06:11:55 LOG Event: 1, Looking for Model Section [CACE.NTAMD64]...
[000007D0] 2014-01-30 06:11:55 LOG Event: 1, Installing devices with Id &quot;PCI\VEN_CACE&amp;DEV_0001&amp;SUBSYS_125E8086&amp;REV_06&quot; using INF &quot;C:\Windows\System32\DriverStore\FileRepository\tc.inf_amd64_neutral_be36f37d1431884a\tc.inf&quot;.
[000007D0] 2014-01-30 06:11:55 LOG Event: 1, Will force install because driver is not better and force flag is set.
[000007D0] 2014-01-30 06:11:55 LOG Event: 1, ENTER UpdateDriverForPlugAndPlayDevices...
[000007D0] 2014-01-30 06:11:58 LOG Event: 0, RETURN UpdateDriverForPlugAndPlayDevices.
[000007D0] 2014-01-30 06:11:58 LOG Event: 1, Installation was successful.
[000007D0] 2014-01-30 06:11:58 LOG Event: 1, Installing devices with Id &quot;PCI\VEN_CACE&amp;DEV_0002&amp;SUBSYS_125E8086&amp;REV_06&quot; using INF &quot;C:\Windows\System32\DriverStore\FileRepository\tc.inf_amd64_neutral_be36f37d1431884a\tc.inf&quot;.
[000007D0] 2014-01-30 06:11:58 LOG Event: 1, Will force install because driver is not better and force flag is set.
[000007D0] 2014-01-30 06:11:58 LOG Event: 1, ENTER UpdateDriverForPlugAndPlayDevices...
[000007D0] 2014-01-30 06:12:00 LOG Event: 0, RETURN UpdateDriverForPlugAndPlayDevices.
[000007D0] 2014-01-30 06:12:00 LOG Event: 1, Installation was successful.
[000007D0] 2014-01-30 06:12:00 LOG Event: 0, Install completed
[000007D0] 2014-01-30 06:12:00 LOG Event: 1, RETURN: DriverPackageInstallW  (0x0)</code></pre><p>The ControlPanel.exe utility sees the board fine, along with link and autonegotiation results.</p><p>The Windows Control Panel 'Programs &amp; Features' sees the 'TurboCap Software v1.4' installed (I've uninstalled / re-installed / rebooted several times).</p><p>But neither Wireshark nor dumpcap see the board</p><pre><code>C:\Program Files\Wireshark&gt;dumpcap -D
1. \Device\NPF_{B3EFF398-88EE-4C69-A344-8379C033DD49} (Blueberry)
2. \Device\NPF_{E4DA7718-7F06-452A-9DAD-B4E7D565EF80} (Ethernet)
3. \Device\NPF_{FEA06F85-4BB7-420E-B346-250379942856} (VMware Network Adapter VMnet1)
4. \Device\NPF_{D21C44E5-AEBA-4106-99CA-0FBF265AC63B} (Swampnet)
5. \Device\NPF_{113837E6-DDDD-4547-BEC8-0C2EB40E3BBA} (VMware Network Adapter VMnet8)
C:\Program Files\Wireshark&gt;</code></pre><p>Nor does tcdump.exe</p><pre><code>C:\Program Files (x86)\CACE Technologies\TurboCap&gt;tcdump foo.pcap
No ports found! Make sure Turbocap is installed.
C:\Program Files (x86)\CACE Technologies\TurboCap&gt;</code></pre><p>Anyone have tips on persuading Win7 to see a Turbocap board?</p><p>--sk</p><p>Stuart Kendrick</p></div><div id="question-tags" class="tags-container tags">turbocap install wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '14, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '14, 07:10</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-29313" class="comments-container"><span id="29315"></span><div id="comment-29315" class="comment"><div id="post-29315-score" class="comment-score"></div><div class="comment-text"><p>maybe the card is broken. Did you try to switch cards between two systems?</p></div><div id="comment-29315-info" class="comment-info"><span class="comment-age">(30 Jan '14, 06:38)</span> Kurt Knochner ♦</div></div><span id="29372"></span><div id="comment-29372" class="comment"><div id="post-29372-score" class="comment-score"></div><div class="comment-text"><p>Dang, that's an obvious step to take, and I haven't tried it yet, thanx</p></div><div id="comment-29372-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:46)</span> skendric</div></div><span id="29396"></span><div id="comment-29396" class="comment"><div id="post-29396-score" class="comment-score"></div><div class="comment-text"><p>I'm curious about the results :-)</p></div><div id="comment-29396-info" class="comment-info"><span class="comment-age">(03 Feb '14, 08:08)</span> Kurt Knochner ♦</div></div><span id="30319"></span><div id="comment-30319" class="comment"><div id="post-30319-score" class="comment-score"></div><div class="comment-text"><p>Turns out the board works fine in another PC (Dell Optiplex 755, running the same Windows SKU: Win7 Pro 64 bit)</p><p>So, something about the hardware/software of this Shuttle PC (SZ77R5) ... I'm stuck, so I'll turn my attention elsewhere for a while</p></div><div id="comment-30319-info" class="comment-info"><span class="comment-age">(02 Mar '14, 06:33)</span> skendric</div></div><span id="30322"></span><div id="comment-30322" class="comment"><div id="post-30322-score" class="comment-score"></div><div class="comment-text"><p>is that a dual-port or quad-port TurboCap?</p></div><div id="comment-30322-info" class="comment-info"><span class="comment-age">(02 Mar '14, 07:41)</span> Kurt Knochner ♦</div></div><span id="30323"></span><div id="comment-30323" class="comment not_top_scorer"><div id="post-30323-score" class="comment-score"></div><div class="comment-text"><p>My money is on the PCIe slot of the shuttle being reduced to graphics card compatibility only. If I remember correctly a 16 lane PCIe slot designed for gfx cards does not always allow running 8 or 4 lane NICs in them.</p></div><div id="comment-30323-info" class="comment-info"><span class="comment-age">(02 Mar '14, 07:59)</span> Jasper ♦♦</div></div><span id="30324"></span><div id="comment-30324" class="comment not_top_scorer"><div id="post-30324-score" class="comment-score"></div><div class="comment-text"><p>Had the same idea ;-)) The SZ77R5 has two PCIe slots. One limited to graphics cards (x16) and one for all-purpose use (x4). Maybe the OP installed the TurboCap in the wrong slot...</p></div><div id="comment-30324-info" class="comment-info"><span class="comment-age">(02 Mar '14, 08:18)</span> Kurt Knochner ♦</div></div><span id="30330"></span><div id="comment-30330" class="comment not_top_scorer"><div id="post-30330-score" class="comment-score"></div><div class="comment-text"><p>dual-port card</p></div><div id="comment-30330-info" class="comment-info"><span class="comment-age">(02 Mar '14, 11:02)</span> skendric</div></div><span id="30331"></span><div id="comment-30331" class="comment not_top_scorer"><div id="post-30331-score" class="comment-score"></div><div class="comment-text"><p>what about the x16 versus x4 PCIe port? Did you try both (if the card fits into both)?</p></div><div id="comment-30331-info" class="comment-info"><span class="comment-age">(02 Mar '14, 11:03)</span> Kurt Knochner ♦</div></div><span id="30442"></span><div id="comment-30442" class="comment not_top_scorer"><div id="post-30442-score" class="comment-score"></div><div class="comment-text"><p>Dual-port</p><p>Same issue regardless of which slot (pci-e x4 or pci-e x16) hosts the card</p></div><div id="comment-30442-info" class="comment-info"><span class="comment-age">(05 Mar '14, 05:49)</span> skendric</div></div></div><div id="comment-tools-29313" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-29313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30460"></span>

<div id="answer-container-30460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30460-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Same issue regardless of which slot (pci-e x4 or pci-e x16) hosts the card</p></blockquote><p>Well, then the conclusion would be: Either your Shuttle PC is broken (like damaged PCIe slot, low voltage, etc.) or there is some piece of software on the Shuttle that causes the problems, like AV, Endpoint Security or even Malware...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '14, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30460" class="comments-container"></div><div id="comment-tools-30460" class="comment-tools"></div><div class="clear"></div><div id="comment-30460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

