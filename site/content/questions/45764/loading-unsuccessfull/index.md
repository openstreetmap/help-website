+++
type = "question"
title = "Loading unsuccessfull"
description = '''Hi, When I am starting up wireshark, the loading screen comes up, it loads to 100% and, if I am unlucky, nothing happens. If it is not able to load, and I close the program, and try to reinstall it, then I am not able to because of the pcap programs that is running in the background. When I am tryin...'''
date = "2015-09-10T11:46:00Z"
lastmod = "2015-09-10T12:33:00Z"
weight = 45764
keywords = [ "load", "startup" ]
aliases = [ "/questions/45764" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Loading unsuccessfull](/questions/45764/loading-unsuccessfull)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I am starting up wireshark, the loading screen comes up, it loads to 100% and, if I am unlucky, nothing happens. If it is not able to load, and I close the program, and try to reinstall it, then I am not able to because of the pcap programs that is running in the background. When I am trying to force kill them/it, the task manager ignore my calls. So I need to turn off and on my computer to uninstall the software so that I can reinstall it. Sometimes it works, and other times it doesn't work. In other words, it is very troublesome for me to startup wireshark.</p><p>Note that I installed the software (windows 32-bit) from wireshark.org and I have not been having this problem with any other programs that I have used earlier. My computer has 8Gb ram and I have tried to close every program before opening wireshark without increasing my probability of a successfull startup.</p><p>Do you know what is actually happening, and what I can do to make this program work?</p></div><div id="question-tags" class="tags-container tags">load startup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '15, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/9296b5b4da6368186f9a37713f0f1f7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcNogard&#39;s gravatar image" /><p>mcNogard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcNogard has no accepted answers">0%</span></p></div></div><div id="comments-container-45764" class="comments-container"></div><div id="comment-tools-45764" class="comment-tools"></div><div class="clear"></div><div id="comment-45764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45765"></span>

<div id="answer-container-45765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From other similar occasional reports, it appears that when Wireshark queries WinPCap for the adaptor information at start-up, the calls into WinPCap hang.</p><p>I can only suggest trying to remove WinPCap using Add\Remove Programs (make sure you've killed all instances of dumpcap.exe first), reboot and then reinstall WinPcap using the install from <a href="http://www.winpcap.org/install/default.htm">WinPCap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '15, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45765" class="comments-container"><span id="45770"></span><div id="comment-45770" class="comment"><div id="post-45770-score" class="comment-score"></div><div class="comment-text"><p>At least I am able to open it now, I'll come back and give a message if the problem returns.</p></div><div id="comment-45770-info" class="comment-info"><span class="comment-age">(10 Sep '15, 13:32)</span> mcNogard</div></div><span id="46354"></span><div id="comment-46354" class="comment"><div id="post-46354-score" class="comment-score"></div><div class="comment-text"><p>I'm not using wireshark so often, so that is the reason why I came back so late. The problem returned, just wanted you to know.</p></div><div id="comment-46354-info" class="comment-info"><span class="comment-age">(04 Oct '15, 05:47)</span> mcNogard</div></div></div><div id="comment-tools-45765" class="comment-tools"></div><div class="clear"></div><div id="comment-45765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

