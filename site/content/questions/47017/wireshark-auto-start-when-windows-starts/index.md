+++
type = "question"
title = "Wireshark auto start when WIndows starts"
description = '''I am trying to capture IP traffic to narrow down an issue. The PC gets rebooted daily so I have to start wireshark and set the capture to save a new file every hour. Is it possible to create a batch file that runs wireshark with the settings I need to capture and save a file every hour when Windows ...'''
date = "2015-10-28T08:13:00Z"
lastmod = "2015-10-28T08:33:00Z"
weight = 47017
keywords = [ "automate" ]
aliases = [ "/questions/47017" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark auto start when WIndows starts](/questions/47017/wireshark-auto-start-when-windows-starts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47017-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture IP traffic to narrow down an issue. The PC gets rebooted daily so I have to start wireshark and set the capture to save a new file every hour. Is it possible to create a batch file that runs wireshark with the settings I need to capture and save a file every hour when Windows is started?</p></div><div id="question-tags" class="tags-container tags">automate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/683d519e2080265f19c3a290f891ed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Videocom%20JM&#39;s gravatar image" /><p>Videocom JM<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Videocom JM has no accepted answers">0%</span></p></div></div><div id="comments-container-47017" class="comments-container"></div><div id="comment-tools-47017" class="comment-tools"></div><div class="clear"></div><div id="comment-47017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47019"></span>

<div id="answer-container-47019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47019-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, but you should use dumpcap, not Wireshark as Wireshark (and tshark) will eventually run out of memory when capturing.</p><p>You can see the command line options for dumpcap here, you'll need to use an option such as <code>-b files:24 -b duration:3600</code> as well as your other capturing options to make each capture file hold 1 hours worth of data and to keep the last 24 files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47019" class="comments-container"><span id="47028"></span><div id="comment-47028" class="comment"><div id="post-47028-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information. I setup a command and tested but I get an error "dumpcap: the file to which the capture would be saved &lt;"qmaster.pcap"&gt; could not be opened: No such file or directory." Below is the syntax I used, am I missing something?</p><p>dumpcap -i 2 -b files:24 -b duration:3600 -w qmaster.pcap</p><p>Thanks, Jason</p></div><div id="comment-47028-info" class="comment-info"><span class="comment-age">(28 Oct '15, 10:53)</span> Videocom JM</div></div><span id="47034"></span><div id="comment-47034" class="comment"><div id="post-47034-score" class="comment-score"></div><div class="comment-text"><p>Your syntax appears to be correct. The error is a permissions issue. Your command works for me, <em>except</em> when I try to run the command from the directory where the Wireshark executables are located (C:\Program Files\Wireshark, in my case), and then I get the same error you did.</p><p>If you're going to use the Wireshark command-line tools, put the Wireshark directory on your path so that you can run the executables from anywhere, and if you're using a Windows computer, save the output somewhere that is not under C:\Windows or C:\Program Files.</p></div><div id="comment-47034-info" class="comment-info"><span class="comment-age">(28 Oct '15, 13:22)</span> Jim Aragon</div></div></div><div id="comment-tools-47019" class="comment-tools"></div><div class="clear"></div><div id="comment-47019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

