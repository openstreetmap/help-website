+++
type = "question"
title = "Wireshark installation on Windows 8 Core"
description = '''I have previously asked about Wireshark installation on a Raspberry Pi 2 Model B. I was given some disheartening information about its compatibility with ARM architecture. (https://ask.wireshark.org/questions/46422/can-wireshark-be-installed-on-windows-10-iot-core) I just so happen to also have an I...'''
date = "2015-10-09T10:11:00Z"
lastmod = "2015-10-11T07:18:00Z"
weight = 46438
keywords = [ "core" ]
aliases = [ "/questions/46438" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark installation on Windows 8 Core](/questions/46438/wireshark-installation-on-windows-8-core)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46438-score" class="post-score" title="current number of votes">0</div><span id="post-46438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have previously asked about Wireshark installation on a Raspberry Pi 2 Model B. I was given some disheartening information about its compatibility with ARM architecture. (<a href="https://ask.wireshark.org/questions/46422/can-wireshark-be-installed-on-windows-10-iot-core)">https://ask.wireshark.org/questions/46422/can-wireshark-be-installed-on-windows-10-iot-core)</a></p><p>I just so happen to also have an Intel Galileo 2. This particular device runs Windows 8 IoT Core Build 9600.16384.x86fre.winblue_rtm_iotbuild.150309-0310</p><p>Again, i have successfully installed the winpcap driver using its INF file and DevCon.EXE via a Telnet session.</p><p>I have been unsuccessful from this point forward. I am attempting to install Wireshark-win32-1.12.7.exe. I run the command: Wireshark-win32-1.12.7.exe /S</p><p>I am returned directly to the c:\Drivers&gt; prompt in my telnet session. No errors, no messages or confirmations of success for failure.</p><p>Are there some switches to write a log file of Wireshark install? Is there a way to just install Tshark only only, or is entire Wireshark package required?</p><p>Has anyone been successful doing what i am trying to do, or anything anywhere similar to this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '15, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/b7af5749249abc686438721de5bf81d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="areue&#39;s gravatar image" /><p><span>areue</span><br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="areue has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Oct '15, 10:12</strong> </span></p></div></div><div id="comments-container-46438" class="comments-container"></div><div id="comment-tools-46438" class="comment-tools"></div><div class="clear"></div><div id="comment-46438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46454"></span>

<div id="answer-container-46454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46454-score" class="post-score" title="current number of votes">0</div><span id="post-46454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Again, i have successfully installed the winpcap driver using its INF file and DevCon.EXE via a Telnet session.<br />
Is there a way to just install Tshark only only, or is entire Wireshark package required?</p></blockquote><p>If you successfully managed to install WinPcap, you can try to use the Wireshark portable package.</p><blockquote><p><a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a><br />
</p></blockquote><p>Download "Windows PortableApps® (32-bit)"</p><p>Then, unpack it on any Windows machine and copy the files to your Galileo 2.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '15, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46454" class="comments-container"></div><div id="comment-tools-46454" class="comment-tools"></div><div class="clear"></div><div id="comment-46454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46457"></span>

<div id="answer-container-46457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46457-score" class="post-score" title="current number of votes">0</div><span id="post-46457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another option is to simply xcopy deploy, i.e. copy the Wireshark "program files" directory from another machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-46457" class="comments-container"></div><div id="comment-tools-46457" class="comment-tools"></div><div class="clear"></div><div id="comment-46457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

