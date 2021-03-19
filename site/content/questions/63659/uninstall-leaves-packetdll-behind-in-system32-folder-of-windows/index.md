+++
type = "question"
title = "Uninstall leaves packet.dll behind in system32 folder of Windows"
description = '''1.I uninstalled Wireshark from my Windows 10 Laptop but I see packet.dll still installed. I tried the following: C:&#92;Windows&#92;System32&amp;gt;driverquery | findstr /i winpcap  WPRO_41_2001 WinPcap Packet Driver Kernel 11/7/2011 4:04:48 PM C:&#92;Windows&#92;System32&amp;gt;del Packet.dll  C:&#92;Windows&#92;System32&#92;Packet.d...'''
date = "2017-09-27T11:23:00Z"
lastmod = "2017-09-27T15:15:00Z"
weight = 63659
keywords = [ "remove", "uninstall" ]
aliases = [ "/questions/63659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Uninstall leaves packet.dll behind in system32 folder of Windows](/questions/63659/uninstall-leaves-packetdll-behind-in-system32-folder-of-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1.I uninstalled Wireshark from my Windows 10 Laptop but I see packet.dll still installed. I tried the following:</p><p>C:\Windows\System32&gt;driverquery | findstr /i winpcap WPRO_41_2001 WinPcap Packet Driver Kernel 11/7/2011 4:04:48 PM</p><p>C:\Windows\System32&gt;del Packet.dll C:\Windows\System32\Packet.dll Access is denied.</p><p>I tried to reinstall Wireshark then Winpcap and uninstall it, nothing helped. Can you please tell me how to get rid of driver</p></div><div id="question-tags" class="tags-container tags">remove uninstall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '17, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/ecf27b798470bd00b0a540aec9f080c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="relahi&#39;s gravatar image" /><p>relahi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="relahi has no accepted answers">0%</span></p></div></div><div id="comments-container-63659" class="comments-container"></div><div id="comment-tools-63659" class="comment-tools"></div><div class="clear"></div><div id="comment-63659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63660"></span>

<div id="answer-container-63660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63660-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet.dll is usually installed by WinPcap, but can sometimes be installed by other applications that may have "borrowed" or re-implemented it (e.g. Npcap).</p><p>Have you tried uninstalling WinPcap on its own? Do you have other capture drivers installed, e.g. Npcap which is part of Nmap?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '17, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63660" class="comments-container"><span id="63661"></span><div id="comment-63661" class="comment"><div id="post-63661-score" class="comment-score"></div><div class="comment-text"><p>I did reinstall winpcap and removed it, but packet.dll stays there. I currently do not have any other packet capturing software installed.</p><p>Thanks Rahat</p></div><div id="comment-63661-info" class="comment-info"><span class="comment-age">(28 Sep '17, 07:16)</span> relahi</div></div><span id="63662"></span><div id="comment-63662" class="comment"><div id="post-63662-score" class="comment-score"></div><div class="comment-text"><p>The digital signature tab of the properties screen says, it is signed by Riverbed Technologies Inc.</p></div><div id="comment-63662-info" class="comment-info"><span class="comment-age">(28 Sep '17, 07:18)</span> relahi</div></div><span id="63663"></span><div id="comment-63663" class="comment"><div id="post-63663-score" class="comment-score"></div><div class="comment-text"><p>I suspect this is installed by something other than WinPcap, possibly something from Riverbed (or another licencee) that uses "WinPCap Pro" the commercial version.</p><p>In WinPcap, packet.dll is the user mode portion of the packet capture API and isn't installed as a driver and so does not show up in driverquery. The WinPcap driver is npf.sys that shows up as <code>NPF NetGroup Packet Filter Kernel 01/03/2013 01:31:24</code>.</p><p>Try using <a href="https://github.com/lostindark/DriverStoreExplorer">Driver Store Explorer</a>(RAPR) (with care) and see what that says about the issue. RAPR can also remove drivers.</p></div><div id="comment-63663-info" class="comment-info"><span class="comment-age">(28 Sep '17, 08:21)</span> grahamb ♦</div></div><span id="63664"></span><div id="comment-63664" class="comment"><div id="post-63664-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response, I just tested that on another system, installed winpcap only and uninstall winpcap leaves packet.dll behind as well. I have sent the same question to Riverbed Technologies.</p><p>Using RAPR on my system does not list packet.dll installed. It does not list anything from Riverbed Technologies.</p><p>Thanks Rahat</p></div><div id="comment-63664-info" class="comment-info"><span class="comment-age">(28 Sep '17, 09:11)</span> relahi</div></div><span id="63665"></span><div id="comment-63665" class="comment"><div id="post-63665-score" class="comment-score"></div><div class="comment-text"><p>Can you move (or delete) the packet.dll file on the other system you tested on?</p></div><div id="comment-63665-info" class="comment-info"><span class="comment-age">(28 Sep '17, 09:26)</span> grahamb ♦</div></div><span id="63666"></span><div id="comment-63666" class="comment not_top_scorer"><div id="post-63666-score" class="comment-score"></div><div class="comment-text"><p>I just tried uninstalling Winpcap on my system and packet.dll was left behind, but it could be deleted, so there does seem to be an uninstaller issue.</p><p>The issue is unlikely to be fixed, all work on WinPCap has ceased.</p></div><div id="comment-63666-info" class="comment-info"><span class="comment-age">(28 Sep '17, 09:42)</span> grahamb ♦</div></div><span id="63667"></span><div id="comment-63667" class="comment not_top_scorer"><div id="post-63667-score" class="comment-score"></div><div class="comment-text"><p>It was Windows Server 2012 I was able to delete it.</p><p>I went back to Win 10, started command prompt with "run as" Administrator and was able to delete there as well.</p><p>Issue resolved.</p><p>Thanks for your help.</p><p>Rahat</p></div><div id="comment-63667-info" class="comment-info"><span class="comment-age">(28 Sep '17, 09:58)</span> relahi</div></div></div><div id="comment-tools-63660" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-63660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

