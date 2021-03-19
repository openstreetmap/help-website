+++
type = "question"
title = "wireshark has stopped working"
description = '''Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) I am trying to run a packet capture using the above version. I have windows 10 on the laptop. The capture is being done on a Cisco 6880. I have the port on the switch setup to monitor all VLAN traffic on the switch. It will run fine for a little whil...'''
date = "2016-03-11T07:48:00Z"
lastmod = "2016-03-11T10:08:00Z"
weight = 50824
keywords = [ "error", "wireshark" ]
aliases = [ "/questions/50824" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark has stopped working](/questions/50824/wireshark-has-stopped-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50824-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0)</p><p>I am trying to run a packet capture using the above version. I have windows 10 on the laptop. The capture is being done on a Cisco 6880. I have the port on the switch setup to monitor all VLAN traffic on the switch. It will run fine for a little while and then an error occurs and the application terminates. All the message says is"wireshark has stopped working, a problem caused the program to sop working correctly. Windows will close the program"</p></div><div id="question-tags" class="tags-container tags">error wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '16, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/3533b8dac920a5234d874db0b6f99fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shannon%20Eakins&#39;s gravatar image" /><p>Shannon Eakins<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shannon Eakins has no accepted answers">0%</span></p></div></div><div id="comments-container-50824" class="comments-container"><span id="50826"></span><div id="comment-50826" class="comment"><div id="post-50826-score" class="comment-score"></div><div class="comment-text"><p>Are you running in "Compatibility Mode" ?</p></div><div id="comment-50826-info" class="comment-info"><span class="comment-age">(11 Mar '16, 08:40)</span> msmorten</div></div></div><div id="comment-tools-50824" class="comment-tools"></div><div class="clear"></div><div id="comment-50824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="50825"></span>

<div id="answer-container-50825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50825-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like a bug which might be related to specific contents of a particular captured packet. It could be useful to run dumpcap instead of Wireshark for, say, triple the time it normally takes Wireshark to crash, and then try to open the capture file saved by dumpcap with Wireshark. If in this case Wireshark crashes too, it is worth filing a bug and attaching that capture.</p><p>BTW, the error message you can see is a Windows message, not a Wireshark one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50825" class="comments-container"></div><div id="comment-tools-50825" class="comment-tools"></div><div class="clear"></div><div id="comment-50825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50827"></span>

<div id="answer-container-50827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What's the expected traffic rate? Are you running the 32 bit or 64 bit version of Wireshark?</p><p>Given that you're trying to "monitor all VLAN traffic on the switch" I'd suspect that you're simply running out of memory, which is more likely if you're using the 32 bit version.</p><p>As @sindy says, try using dumpcap to make the capture as that doesn't retain state or dissect as much traffic so is less likely to run out of memory or hit any possible bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50827" class="comments-container"><span id="50830"></span><div id="comment-50830" class="comment"><div id="post-50830-score" class="comment-score"></div><div class="comment-text"><p>Well, OK, maybe my understanding of "a little while" is different from author's :) These words were the reason why I've suppressed the very first idea of memory exhaustion and suggested a bug instead.</p></div><div id="comment-50830-info" class="comment-info"><span class="comment-age">(11 Mar '16, 10:19)</span> sindy</div></div></div><div id="comment-tools-50827" class="comment-tools"></div><div class="clear"></div><div id="comment-50827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50828"></span>

<div id="answer-container-50828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50828-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried compatibility mode ? WireShark may not be yet compatible with Windows 10 yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-50828" class="comments-container"><span id="50829"></span><div id="comment-50829" class="comment"><div id="post-50829-score" class="comment-score"></div><div class="comment-text"><p>Wireshark runs perfectly well on Windows 10. If you have direct evidence of an issue please raise an entry at the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p></div><div id="comment-50829-info" class="comment-info"><span class="comment-age">(11 Mar '16, 10:12)</span> grahamb ♦</div></div><span id="50831"></span><div id="comment-50831" class="comment"><div id="post-50831-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/questions/40972/wireshark-and-windows-10-build-10041-no-capture-interfaces">https://ask.wireshark.org/questions/40972/wireshark-and-windows-10-build-10041-no-capture-interfaces</a></p><p>This says otherwise. I know the issues are a bit different but there are some known issues. So to say it "runs perfectly well..." is a slight over statement.</p></div><div id="comment-50831-info" class="comment-info"><span class="comment-age">(11 Mar '16, 11:52)</span> msmorten</div></div><span id="50832"></span><div id="comment-50832" class="comment"><div id="post-50832-score" class="comment-score"></div><div class="comment-text"><p>Look at the date and Win 10 build in that question. That wasn't an RTM release of Win 10, and at that time Win 10 preview builds had issues with NDIS5 drivers and thus affected WinPCap not Wireshark, although WinPCap not working did prevent Wireshark from making captures.</p><p>Again, if you have a specific bug for Wireshark on Win 10, please raise it, don't just make general wild assertions.</p></div><div id="comment-50832-info" class="comment-info"><span class="comment-age">(11 Mar '16, 11:57)</span> grahamb ♦</div></div><span id="50833"></span><div id="comment-50833" class="comment"><div id="post-50833-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/questions/48178/wireshark-fails-to-start-on-windows-10">https://ask.wireshark.org/questions/48178/wireshark-fails-to-start-on-windows-10</a></p><p>The above build or seemingly a number of builds have issues with WinPCap and Wireshark which seem to conflict with one another in Windows 10. I am only saying that this setup seems to fit the bill.</p><p>That doesn't seem very wild to me, but if you say so. I'll just wait for you to repeat one of these previous answers.</p><p>Again, I'd try compatibility mode or run a VM of a previous version of Windows and see if it happens then. I have a similar switch and pulling much more traffic on a network with very heavy traffic, and havent had an issue with Wireshark. But I'm running Windows 7 with WinPCap, and 2 linux servers. So, I think the issue has to do with running the program in a Windows 10 environment w/ WinPCaP. This has been reported many times in various setups.</p><p>But thats just my wild, but educated guess.</p><p>Good luck.</p></div><div id="comment-50833-info" class="comment-info"><span class="comment-age">(11 Mar '16, 12:10)</span> msmorten</div></div><span id="50834"></span><div id="comment-50834" class="comment"><div id="post-50834-score" class="comment-score"></div><div class="comment-text"><p>That issue of a hang in a call in WinPcap has been around for quite a while, I've investigated a few myself that have previously been reported and it's happened on other OS's before Win 10 arrived. Unfortunately without debug symbols for WinPcap it's next to impossible to debug from a crash dump. If I could make it happen on a dev machine with a debugger I might have a chance.</p><p>That issue seems to be something peculiar in the environments where it fails that can't be replicated elsewhere. Very few people appear to suffer with that issue, but regardless that's a failure to start, not a crash during capture.</p></div><div id="comment-50834-info" class="comment-info"><span class="comment-age">(11 Mar '16, 12:33)</span> grahamb ♦</div></div></div><div id="comment-tools-50828" class="comment-tools"></div><div class="clear"></div><div id="comment-50828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

