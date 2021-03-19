+++
type = "question"
title = "Start time for a packet capture"
description = '''I have a device that resets every night at 8:05. I would like to setup wireshark to start capturing at 8:03 every night and capture for 3 minutes. I have found where to stop the capture but am looking for where to set the option to start capturing at a certain real time? Thanks for your help'''
date = "2011-02-22T14:26:00Z"
lastmod = "2012-10-14T09:40:00Z"
weight = 2507
keywords = [ "real", "capture", "start", "time" ]
aliases = [ "/questions/2507" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Start time for a packet capture](/questions/2507/start-time-for-a-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device that resets every night at 8:05. I would like to setup wireshark to start capturing at 8:03 every night and capture for 3 minutes. I have found where to stop the capture but am looking for where to set the option to start capturing at a certain real time? Thanks for your help</p></div><div id="question-tags" class="tags-container tags">real capture start time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/387a7c7dfdea745e1423c76dceed1b4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theiman&#39;s gravatar image" /><p>theiman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theiman has no accepted answers">0%</span></p></div></div><div id="comments-container-2507" class="comments-container"><span id="14996"></span><div id="comment-14996" class="comment"><div id="post-14996-score" class="comment-score"></div><div class="comment-text"><p>i also want to how to contral the start time of cature packets!</p></div><div id="comment-14996-info" class="comment-info"><span class="comment-age">(13 Oct '12, 22:00)</span> boyxiaolong</div></div></div><div id="comment-tools-2507" class="comment-tools"></div><div class="clear"></div><div id="comment-2507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2511"></span>

<div id="answer-container-2511" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2511-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to schedule it with task scheduler or cron.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2511" class="comments-container"></div><div id="comment-tools-2511" class="comment-tools"></div><div class="clear"></div><div id="comment-2511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15000"></span>

<div id="answer-container-15000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>and then invoke a little script that starts wireshark for you, like so:</p><pre><code>ECHO Starting up tshark with capture options

path=C:\Program Files\Wireshark
mkdir D:\NoBackup\WIRESHARK\
set subor=D:\NoBackup\WIRESHARK\%COMPUTERNAME%_%DATE:/=%_%TIME:~0,2%-%TIME:~3,2%-%TIME:~6,2%.pcap
C:\Progra~1\Wireshark\tshark.exe -i 1 -a filesize:250000 -w &quot;%subor%&quot;</code></pre><p>see if that works for you..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '12, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-15000" class="comments-container"></div><div id="comment-tools-15000" class="comment-tools"></div><div class="clear"></div><div id="comment-15000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

