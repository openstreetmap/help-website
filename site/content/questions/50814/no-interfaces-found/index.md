+++
type = "question"
title = "no interfaces found ..."
description = '''I do not have enough &quot;karma&quot; to upload files, so no screenshots, sorry.... I was running wireshark fine with NPCAP just a week ago. This morning starting it as administrator it shows no interfaces to be selected for capture. I Uninstalled it. Made sure every program data/program files forlder where ...'''
date = "2016-03-11T01:05:00Z"
lastmod = "2016-03-18T18:02:00Z"
weight = 50814
keywords = [ "interface" ]
aliases = [ "/questions/50814" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no interfaces found ...](/questions/50814/no-interfaces-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I do not have enough "karma" to upload files, so no screenshots, sorry....</p><p>I was running wireshark fine with NPCAP just a week ago. This morning starting it as administrator it shows no interfaces to be selected for capture.</p><p>I Uninstalled it. Made sure every program data/program files forlder where removed, rebooted, reinstalled ( it detected npcap during install), rebooted, started as administrator... Same problem.</p><p>If I use rawcap I can see these interfaces:</p><pre><code>0.     169.254.39.183  vEthernet (Internal Switch)     Ethernet
1.     192.168.6.52    vEthernet (commutateur virtuel 1)       Ethernet
2.     169.254.110.185 Npcap Loopback Adapter  Ethernet
3.     192.168.56.1    VirtualBox Host-Only Network    Ethernet
4.     127.0.0.1       Loopback Pseudo-Interface 1     Loopback</code></pre><p>I'm using windows 8.1 64 bits and wireshark 2.0.2 for win64.</p><p>Any idea, so far i'm simply using rawcap to save to a file I open with wireshark, but it is annoying.</p><hr /><p>Trying to build on the first answer. I uninstalled NPCAP, then removed the driver service as follows:</p><pre><code>    pnputil -e
...
Published name :            oem12.inf
Driver package provider :   Nmap Project
Class :                     Network Service
Driver date and version :   02/24/2016 23.40.33.73
Signer name :               Insecure.Com LLC
...

pnputil -d oem12.inf</code></pre><p>I had to remove two of them oem12.inf and oem16.inf from Insecure.Com LLC. Then I rebooted, ran iterativelly CCLeaner just to get rid of some registry keys in any case then reinstalled the latest version of NPCAP as admin.</p><p>===&gt; It "fails to install driver service"...</p></div><div id="question-tags" class="tags-container tags">interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '16, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/ffb5b88113560c98da7600da5dd3bc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rapha&#39;s gravatar image" /><p>rapha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rapha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '16, 04:55</p></div></div><div id="comments-container-50814" class="comments-container"></div><div id="comment-tools-50814" class="comment-tools"></div><div class="clear"></div><div id="comment-50814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50818"></span>

<div id="answer-container-50818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50818-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The enumeration of interfaces isn't handled by Wireshark at all, rather the capture mechanism, which in your case is npcap or WinPcap, so reinstalling Wireshark isn't likely to help.</p><p>Presumably you're using npcap as you wish to capture on the loopback interface. If not, you might better off using WinPcap at the moment.</p><p>Which version of npcap are you using? Try uninstalling npcap, reboot, check for traces, e.g. %WINDIR%\System32\Drivers\npcap.sys or npf,sys, and then reinstall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50818" class="comments-container"><span id="50819"></span><div id="comment-50819" class="comment"><div id="post-50819-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'm indeed debugging a client server program locally this is why I need the loopback. I edited my question.</p></div><div id="comment-50819-info" class="comment-info"><span class="comment-age">(11 Mar '16, 04:56)</span> rapha</div></div><span id="50820"></span><div id="comment-50820" class="comment"><div id="post-50820-score" class="comment-score"></div><div class="comment-text"><p>There have been some ongoing issues for some when installing npcap which haven't yet been resolved. A more appropriate forum for npcap issues would be the <a href="https://nmap.org/mailman/listinfo/dev">nmap dev mailing list</a>.</p></div><div id="comment-50820-info" class="comment-info"><span class="comment-age">(11 Mar '16, 05:33)</span> grahamb ♦</div></div><span id="50875"></span><div id="comment-50875" class="comment"><div id="post-50875-score" class="comment-score"></div><div class="comment-text"><p>thanks, I'll check there. So far, I have my workaround with rawcap.</p></div><div id="comment-50875-info" class="comment-info"><span class="comment-age">(14 Mar '16, 01:26)</span> rapha</div></div></div><div id="comment-tools-50818" class="comment-tools"></div><div class="clear"></div><div id="comment-50818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51041"></span>

<div id="answer-container-51041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51041-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi.</p><p>Please try the latest Npcap 0.06 R10 here: <a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a></p><p>Don't change options if you don't know what they mean.</p><p>Let me know if there're any issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '16, 18:02</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-51041" class="comments-container"></div><div id="comment-tools-51041" class="comment-tools"></div><div class="clear"></div><div id="comment-51041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

