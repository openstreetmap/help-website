+++
type = "question"
title = "Wireshark process runs but the GUI window never opens."
description = '''Hi, I just installed WireShark today and the installer popped an error on uninstalling the older version of WinPCap. The installer continued anyway and said it completed. When I start it now I get a few little popups that show WireShark trying to load but the GUI never comes up. I can see the wiresh...'''
date = "2013-08-12T20:20:00Z"
lastmod = "2013-08-14T14:05:00Z"
weight = 23725
keywords = [ "nogui" ]
aliases = [ "/questions/23725" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark process runs but the GUI window never opens.](/questions/23725/wireshark-process-runs-but-the-gui-window-never-opens)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23725-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I just installed WireShark today and the installer popped an error on uninstalling the older version of WinPCap. The installer continued anyway and said it completed. When I start it now I get a few little popups that show WireShark trying to load but the GUI never comes up. I can see the wireshark process in ProcessExplorer but nothing else happens. I uninstalled wireshark, rebooted and uninstalled WinPCap, rebooted and reinstalled the package but I get the same results; popups go by, process starts, no GUI. Any thoughts or suggestions?</p></div><div id="question-tags" class="tags-container tags">nogui</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '13, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/359803e8fe725a8f8b8edf0ea85480f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charlieagiii&#39;s gravatar image" /><p>charlieagiii<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charlieagiii has one accepted answer">100%</span></p></div></div><div id="comments-container-23725" class="comments-container"><span id="23733"></span><div id="comment-23733" class="comment"><div id="post-23733-score" class="comment-score"></div><div class="comment-text"><p>Independent from wireshark - if someone knows this problem I'd be very interested in that too because aside from wireshark I've had this issue with a few other applications</p></div><div id="comment-23733-info" class="comment-info"><span class="comment-age">(13 Aug '13, 00:26)</span> Landi</div></div><span id="23741"></span><div id="comment-23741" class="comment"><div id="post-23741-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'd be very interested in that too because aside from wireshark I've had this issue with a few other applications</p></blockquote><p>me too. And I have a strong feeling that it is related to <a href="http://en.wikipedia.org/wiki/User_Account_Control">UAC</a>.</p></div><div id="comment-23741-info" class="comment-info"><span class="comment-age">(13 Aug '13, 04:30)</span> Kurt Knochner ♦</div></div><span id="23747"></span><div id="comment-23747" class="comment"><div id="post-23747-score" class="comment-score"></div><div class="comment-text"><p>Or possibly <a href="http://en.wikipedia.org/wiki/Data_Execution_Prevention">DEP</a>-related? As a test, you could try adding a <a href="http://www.0xc0000005.com/dep-exceptions.html">DEP exception</a>.</p></div><div id="comment-23747-info" class="comment-info"><span class="comment-age">(13 Aug '13, 08:27)</span> cmaynard ♦♦</div></div><span id="23749"></span><div id="comment-23749" class="comment"><div id="post-23749-score" class="comment-score"></div><div class="comment-text"><p>I think a DEP related issue would just cause an exception with the resultant error dialog, rather than allowing the process to continue to run silently.</p></div><div id="comment-23749-info" class="comment-info"><span class="comment-age">(13 Aug '13, 09:06)</span> grahamb ♦</div></div></div><div id="comment-tools-23725" class="comment-tools"></div><div class="clear"></div><div id="comment-23725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23784"></span>

<div id="answer-container-23784" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23784-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, this is embarrassing. It turns out that I use a utility called MultiMon Taskbar to allow me to "throw" Windows Media Player onto my TV with a keyboard shortcut. The TV is treated like a second monitor. I had the TV's input set to TV instead of PC so I was not seeing that Wireshark had decided to open in the second monitor which has it's own independent taskbar where the Wireshark program was showing up instead of it showing up on the taskbar of the primary monitor. It would appear that it was there the whole time but I was unable to see it until I change the TV's input to PC. Thanks to everyone who participated in helping me troubleshoot this one. Sorry for the inconvenience, Charlieagiii</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/359803e8fe725a8f8b8edf0ea85480f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charlieagiii&#39;s gravatar image" /><p>charlieagiii<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charlieagiii has one accepted answer">100%</span></p></div></div><div id="comments-container-23784" class="comments-container"></div><div id="comment-tools-23784" class="comment-tools"></div><div class="clear"></div><div id="comment-23784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23734"></span>

<div id="answer-container-23734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23734-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can produce a memory dump as shown <a href="http://support.microsoft.com/kb/931673">here</a> and post it somewhere, I can have a look at it in the debugger and try to see what the Wireshark process is up to. Please zip up the dump before processing it.</p><p>Warning! The memory dump may contain information about your system that could be considered sensitive. It will contain the full process memory image and will expose things such as the machine name, any domain it belongs to, the account the process is running under and possibly other things. There shouldn't be any passwords, but if you've added SSL private keys to Wireshark then they may be in the image.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '13, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23734" class="comments-container"><span id="23737"></span><div id="comment-23737" class="comment"><div id="post-23737-score" class="comment-score"></div><div class="comment-text"><p>I followed your link for the dump and see that it applies to Vista and Win 7. Is the process the same for XP SP3, I don't have the PC involved booted right now to test it.</p></div><div id="comment-23737-info" class="comment-info"><span class="comment-age">(13 Aug '13, 01:59)</span> charlieagiii</div></div><span id="23738"></span><div id="comment-23738" class="comment"><div id="post-23738-score" class="comment-score"></div><div class="comment-text"><p>For XP SP3 you'll need a different method. <a href="http://technet.microsoft.com/en-gb/sysinternals/dd996900.aspx">procdump</a> has worked for me, ensure you only have a single running wireshark process that's in the broken state and run procdump as <code>procdump -ma Wireshark.exe</code></p></div><div id="comment-23738-info" class="comment-info"><span class="comment-age">(13 Aug '13, 02:05)</span> grahamb ♦</div></div><span id="23765"></span><div id="comment-23765" class="comment"><div id="post-23765-score" class="comment-score"></div><div class="comment-text"><p>Will try and run procdump this evening. New info: When the Wireshark process starts ProcessExplorer also shows dumpcap.exe starting, running for about a second and shutting down. Also, I'm not finding a process for WinPCap. Can you tell me the name of the process and or service for WinPCap?</p></div><div id="comment-23765-info" class="comment-info"><span class="comment-age">(13 Aug '13, 23:26)</span> charlieagiii</div></div><span id="23767"></span><div id="comment-23767" class="comment"><div id="post-23767-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I don't see that but I do have a fast machine so maybe miss it :-) How are you starting Wireshark? Does tshark run OK for you? What about dumpcap? Use <code>dumpcap -D</code> to see what devices it can find on your machine.</p><p>WinPCap is essentially a few userspace DLL's that are linked to the user application (dumpcap) and a kernel driver (npf.sys). See the WinPCap <a href="http://www.winpcap.org/docs/docs_412/html/group__internals.html">docs</a> for more info.</p></div><div id="comment-23767-info" class="comment-info"><span class="comment-age">(14 Aug '13, 02:10)</span> grahamb ♦</div></div></div><div id="comment-tools-23734" class="comment-tools"></div><div class="clear"></div><div id="comment-23734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23771"></span>

<div id="answer-container-23771" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23771-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'd be very interested in that too because aside from wireshark I've had this issue with a few other applications</p></blockquote><p>I still think that it may be related to UAC. Can you please run Wireshark as Administrator (NOT recommended for dayily operation) and/or try to disable UAC.</p><p>If the GUI is still not showing up, please check any <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering security software</a> on your system (Firewall, AV, IDS, Endpoint Security, etc.). Please disable those tools (for a test) and restart Wireshark (after you have killed the hanging process). Does it work then?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23771" class="comments-container"><span id="23783"></span><div id="comment-23783" class="comment"><div id="post-23783-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, I found the answer (please see below?) but thought I should mention that as far as I know there is no UAC in Win XP SP 3.</p></div><div id="comment-23783-info" class="comment-info"><span class="comment-age">(14 Aug '13, 14:02)</span> charlieagiii</div></div></div><div id="comment-tools-23771" class="comment-tools"></div><div class="clear"></div><div id="comment-23771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

