+++
type = "question"
title = "Can I start a monitor and then log off/on as a new user?"
description = '''OK, so here&#x27;s my strange setup. I have an XP machine that we need to monitor the traffic on. This machine runs a special program under a special User ID. When that ID is logged on, the whole machine is locked down and it loads up the program it runs. There is no way to get to the start bar or the de...'''
date = "2011-12-05T07:18:00Z"
lastmod = "2011-12-05T07:28:00Z"
weight = 7768
keywords = [ "xp", "logoff", "monitor" ]
aliases = [ "/questions/7768" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I start a monitor and then log off/on as a new user?](/questions/7768/can-i-start-a-monitor-and-then-log-offon-as-a-new-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, so here's my strange setup.</p><p>I have an XP machine that we need to monitor the traffic on. This machine runs a special program under a special User ID. When that ID is logged on, the whole machine is locked down and it loads up the program it runs. There is no way to get to the start bar or the desktop or anything.</p><p>I can log onto this machine as the admin and have normal access to everything. I'm wondering if there's some way I can start up a capture under the admin account, then log off and on as the user that we need to monitor, let it run for a while, then log off and back on as the admin to save the file.</p><p>When the special user is logged on, I can remote into the machine and run some command line commands through the remote control software so it might work to just do it that way if that's easier. If so, does someone have a link to all the command line commands I'd need to use to start the capture and then stop it and save off the file?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">xp logoff monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '11, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/caa2ffd31240cafdaba6bbab216c96b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kelemvor&#39;s gravatar image" /><p>kelemvor<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kelemvor has no accepted answers">0%</span></p></div></div><div id="comments-container-7768" class="comments-container"></div><div id="comment-tools-7768" class="comment-tools"></div><div class="clear"></div><div id="comment-7768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7770"></span>

<div id="answer-container-7770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7770-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure if Wireshark will continue to capture if the user that started the capture logs off, because then the programs will shut down (except you're actually talking about "switching" users, not "logging off").</p><p>It should work from a remote desktop session though, you can use dumpcap.exe to do the capture for you:</p><ol><li>run <strong>dumpcap -d</strong> to get a list of all interfaces, write down the index of the interface</li><li>run <strong>dumpcap -i &lt;interface index=""&gt; -w filename.pcap</strong> to capture on the interface you want and write it to a file called filename.pcap. You can optionally go for ring buffer captures, but I don't think it's necessary. You might have to filter out your remote session afterwards, but that should be easy.</li></ol><p>By the way, dumpcap.exe can be found in the same directory as the Wireshark executable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '11, 07:28</p></div></div><div id="comments-container-7770" class="comments-container"></div><div id="comment-tools-7770" class="comment-tools"></div><div class="clear"></div><div id="comment-7770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7771"></span>

<div id="answer-container-7771" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7771-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have <a href="http://support.microsoft.com/kb/279765" title="How To Use the Fast User Switching Feature in Windows XP">Fast User Switching</a> enabled on the machine, you can do roughly as you described:</p><ol><li>start Wireshark as the administrator</li><li>switch users (not log off)</li><li>log in as the locked down user</li><li>do what you need to do</li><li>log off</li><li>log in as administrator again</li><li>stop the capture</li></ol><p>I would recommend you use a separate machine to actually perform the capture (unless this is not possible/prohibitive in your environment). You can read the <a href="http://wiki.wireshark.org/CaptureSetup" title="CaptureSetup">Capture Setup</a> wiki article for some more information as to why.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7771" class="comments-container"></div><div id="comment-tools-7771" class="comment-tools"></div><div class="clear"></div><div id="comment-7771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

