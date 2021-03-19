+++
type = "question"
title = "Remote Capture in Windows XP"
description = '''I&#x27;m using Wireshark 1.4.4 and the remote system is installed with WinPcap rpcapd version (4.1.2). rpcapd.exe -n is running in the remote pc and the corresponding service is ON too. Many options I tried to do a &#x27;remote capture&#x27; from Wireshark as below, but nothing seems to be working fine.  Interface...'''
date = "2011-03-05T04:27:00Z"
lastmod = "2011-03-20T22:35:00Z"
weight = 2673
keywords = [ "remote" ]
aliases = [ "/questions/2673" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Capture in Windows XP](/questions/2673/remote-capture-in-windows-xp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2673-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark 1.4.4 and the remote system is installed with WinPcap rpcapd version (4.1.2). rpcapd.exe -n is running in the remote pc and the corresponding service is ON too. Many options I tried to do a 'remote capture' from Wireshark as below, but nothing seems to be working fine.</p><p>Interface: Remote &amp; tried the below options rpcap://IPADDRESS/DeviceNPF_{INTERFACE INFORMATION} rpcap://IPADDRESS//DeviceNPF_{INTERFACE INFORMATION} - another try ://IPADDRESS//DeviceNPF_{INTERFACE INFORMATION} - another try &amp; many more tries.</p><p>In the pop-up window for Host information I tried both the IP &amp; Hostname information with 2002 port &amp; without that also. I have admin rights as well, I'm getting the error "Can't get the list of interfaces: Logon failure - unknown username/pwd (I'm using the domain admin pwd and not local admin- hope this will work). I'm able to telnet to 2002 port on the destination pc. Could any of you provide some clue to make this work? Should I try some other version of WinpCap or Wireshark? Any known issues in capturing remotely?</p></div><div id="question-tags" class="tags-container tags">remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '11, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/33ae172a39b60392624a390279320038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joes77&#39;s gravatar image" /><p>joes77<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joes77 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '11, 04:30</p></div></div><div id="comments-container-2673" class="comments-container"></div><div id="comment-tools-2673" class="comment-tools"></div><div class="clear"></div><div id="comment-2673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2707"></span>

<div id="answer-container-2707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2707-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's a setup that I use, which you might try (Instructions are based on Windows XP Professional SP3 using Wireshark 1.4.2, and WinPcap 4.1.2):</p><p>On the machine running the remote packet capture daemon:</p><ol><li>Create a local user account for remote capture authentication: Start -&gt; Control Panel -&gt; User Accounts -&gt; Create a new account -&gt; Advanced -&gt; Advanced -&gt; Users (right-click) -&gt; New User -&gt; [Fill in details] -&gt; Create.</li><li>Configure rpacpd as a service: Start -&gt; Administrator Tools -&gt; Services -&gt; Remote Packet Capture Protocol v.0 (experimental) (right-click) -&gt; Properties -&gt; Log On -&gt; This account -&gt; [Fill in the account details from step 1] -&gt; OK.</li><li>Start rpcapd as a service: Start -&gt; Administrator Tools -&gt; Services -&gt; Remote Packet Capture Protocol v.0 (experimental) (right-click) -&gt; Start.</li></ol><p>On the machine running Wireshark:</p><ol><li>Configure the capture options: Capture -&gt; Options -&gt; Interface -&gt; Remote -&gt; [Fill in details]* -&gt; OK.</li><li>Choose the remote interface: On the capture options window, the remote interfaces are in the drop-down list in the upper right corner. Pick the one you need.</li><li>Choose the remainder of your capture options, including remote settings, as needed, then choose Start.</li></ol><p>*NOTES:</p><ul><li>The Host is filled in as the remote IP address only, with no <code>rpacp://</code> prefix or anything else.</li><li>It is not necessary to fill out the port unless you have changed it on the remote machine from the default of 2002.</li><li>Choose Password Authentication, then fill in the remote username and password credentials.</li></ul><p>For more information on WinPcap remote packet capturing, try <a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2707" class="comments-container"></div><div id="comment-tools-2707" class="comment-tools"></div><div class="clear"></div><div id="comment-2707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2674"></span>

<div id="answer-container-2674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try this:<br />
rpcap://IPADDRESS/\Device\NPF_{INTERFACE INFORMATION}<br />
<br />
BTW<br />
I'm running Wireshark version 1.5.0 and WinPcap version 4.1.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '11, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '11, 07:50</p></div></div><div id="comments-container-2674" class="comments-container"></div><div id="comment-tools-2674" class="comment-tools"></div><div class="clear"></div><div id="comment-2674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2676"></span>

<div id="answer-container-2676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2676-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>...the error "Can't get the list of interfaces: Logon failure - <strong>unknown username/pwd</strong> (I'm using the domain admin pwd and not local admin- hope this will work).</p></blockquote><p>Sound like a clue, doesn't it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '11, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-2676" class="comments-container"></div><div id="comment-tools-2676" class="comment-tools"></div><div class="clear"></div><div id="comment-2676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2962"></span>

<div id="answer-container-2962" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2962-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hey Guys, It worked. Wireshark 1.4.4 &amp; rpcap 4.1.0.2001. Not sure why it did not work before, I ran the Wireshark as Admin from a normal user account before. this time i logged in as Admin. May be because of this. Thanks anyways for your help</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/33ae172a39b60392624a390279320038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joes77&#39;s gravatar image" /><p>joes77<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joes77 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '11, 22:36</p></div></div><div id="comments-container-2962" class="comments-container"></div><div id="comment-tools-2962" class="comment-tools"></div><div class="clear"></div><div id="comment-2962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

