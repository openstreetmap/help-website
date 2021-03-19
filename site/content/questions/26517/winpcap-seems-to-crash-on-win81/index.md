+++
type = "question"
title = "Winpcap seems to crash on Win8.1"
description = '''Hi all, I recently upgraded my HP Envy laptop (1 month old version) to Win8.1. Following that upgrade launching Wireshark would hang and not be able to close properly. A background file call dump was running and I actually had to reboot the system in order to close it. It seems the winpcap was causi...'''
date = "2013-10-29T09:14:00Z"
lastmod = "2013-11-26T05:57:00Z"
weight = 26517
keywords = [ "winpcap" ]
aliases = [ "/questions/26517" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Winpcap seems to crash on Win8.1](/questions/26517/winpcap-seems-to-crash-on-win81)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26517-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I recently upgraded my HP Envy laptop (1 month old version) to Win8.1. Following that upgrade launching Wireshark would hang and not be able to close properly. A background file call dump was running and I actually had to reboot the system in order to close it.</p><p>It seems the winpcap was causing problems so I deinstalled it and then reinstalled Wireshark. After that it seems to operate fine.</p><p>Just wanted to let you know.</p></div><div id="question-tags" class="tags-container tags">winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '13, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/6e068813c3016826e3581941f1b452ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Glen%20Gerhard&#39;s gravatar image" /><p>Glen Gerhard<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Glen Gerhard has no accepted answers">0%</span></p></div></div><div id="comments-container-26517" class="comments-container"><span id="26799"></span><div id="comment-26799" class="comment"><div id="post-26799-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have encountered exactly the same behavior after my upgrade to windows 8.1. Dumpcap hangs when it tries to list interfaces via winpcap. I came to the same solution, uninstall winpcap, but in fact I can't tell if the problem comes from winpcap itself or dumpcap.</p><p>Now I can't capture traffic anymore which is quite annoying.</p></div><div id="comment-26799-info" class="comment-info"><span class="comment-age">(09 Nov '13, 03:58)</span> Marc Sabatier</div></div><span id="27039"></span><div id="comment-27039" class="comment"><div id="post-27039-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem with an Acer Aspire running Windoze 8.1. WS will run standalone without winpcap but it hangs when pcap is installed. Searches have come up empty so far. After force closing WS, dumpcap stays active as a process and can only be stopped by a reboot.</p></div><div id="comment-27039-info" class="comment-info"><span class="comment-age">(15 Nov '13, 11:27)</span> johnnyp10704</div></div></div><div id="comment-tools-26517" class="comment-tools"></div><div class="clear"></div><div id="comment-26517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="27282"></span>

<div id="answer-container-27282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27282-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am also having the same problem (Hang!) on wireshark and also GNS3 cloud service! I found out that the problem is because WinPCap did not auto start after upgraded to Windows 8.1. It will work after reinstallation of winPCap. However, after restarting windows, it will not work again!</p><p>These are the steps that I have taken and it is working fine now!</p><ol><li>In the registry, change HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NPF\Start to 0x3 (SERVICE_DEMAND_START)</li><li>Run your program (i.e., wireshark, gns3, ...) as Administrator! (Run as Administrator)(You can also change it to always run as administrator!)</li></ol><p>and it works again and again even after restart windows 8.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/cbd17bc6425c8afe9e16a697c127e1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ling&#39;s gravatar image" /><p>Ling<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ling has no accepted answers">0%</span></p></div></div><div id="comments-container-27282" class="comments-container"><span id="39038"></span><div id="comment-39038" class="comment"><div id="post-39038-score" class="comment-score"></div><div class="comment-text"><p>Although this may fix your issues, running Wireshark with elevated privileges is not recommended. There are millions of lines of unaudited code in Wireshark and a great deal of work has been undertaken to allow Wireshark to run without elevating privs.</p></div><div id="comment-39038-info" class="comment-info"><span class="comment-age">(11 Jan '15, 03:54)</span> grahamb ♦</div></div><span id="43699"></span><div id="comment-43699" class="comment"><div id="post-43699-score" class="comment-score"></div><div class="comment-text"><p>"It Lives, again!": I recently deleted searched files from the registry for uninstalled programs one of them included a program called netScan! I think it removed an important dll from the registry! Will changing this entry form 2 to 3 make anything less secure? if so what would be the proper way to ... Win8.1 Centrino wireless adapter + rtl drivers</p></div><div id="comment-43699-info" class="comment-info"><span class="comment-age">(29 Jun '15, 22:06)</span> fred57</div></div></div><div id="comment-tools-27282" class="comment-tools"></div><div class="clear"></div><div id="comment-27282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27040"></span>

<div id="answer-container-27040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27040-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of <a href="http://www.winpcap.org/install/default.htm">WinPcap</a> are you folks running? If you're not running the latest version, currently 4.1.3, then you you might try upgrading to that version. If you are running the latest version, and if similar problems also occur when running <a href="http://www.winpcap.org/windump/default.htm">WinDump</a>, then it's very likely a WinPcap problem and not a Wireshark problem, per se, in which case the best bet would probably be to <a href="http://www.winpcap.org/contact.htm">contact the WinPcap developers</a> for support/advice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '13, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27040" class="comments-container"><span id="27046"></span><div id="comment-27046" class="comment"><div id="post-27046-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am using winpcap 4.1.3. I just tested with windump and it is hanging when trying to capture on my AR8131 Gigabit Ethernet interface. So I think you are right it is more a WinPcap problem.</p><p>Thanks, Marc</p></div><div id="comment-27046-info" class="comment-info"><span class="comment-age">(16 Nov '13, 03:44)</span> Marc Sabatier</div></div></div><div id="comment-tools-27040" class="comment-tools"></div><div class="clear"></div><div id="comment-27040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27420"></span>

<div id="answer-container-27420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27420-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I was googling around as I faced a similar problem while trying to capture traffic off a gns3 topology. Wireshard would simply crash with the "Dumpcap has stopped working" error. I am also using Windows 8</p><p>I made sure I am running both GNS3 and Wireshark as "administrator". Still the problem persisted.</p><p>What fixed this for me was setting the compatibility mode to Windows 7</p><ul><li>Write click Wireshark and select Properties -&gt; Compatibility tab</li><li>Set the compatibility mode for windows 7</li></ul><p>Hope this helps someone having the same problem under Windows 8</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/7ea637318b43f3a89c39cd0614af0a57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nimal&#39;s gravatar image" /><p>Nimal<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nimal has no accepted answers">0%</span></p></div></div><div id="comments-container-27420" class="comments-container"></div><div id="comment-tools-27420" class="comment-tools"></div><div class="clear"></div><div id="comment-27420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

