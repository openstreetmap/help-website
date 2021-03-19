+++
type = "question"
title = "Remote capture via ssh and pipe"
description = '''Hello Everyone, i have a new configuration where i try to capture my linux machines and display the traffic with wireshark on windows. On windows i&#x27;m using cygwin to receive the data from my linux machines via ssh $ mkfifo /tmp/capture_1 $ ssh root@192.168.2.1 &quot;tcpdump -s0 -U -n -w - -i eth0 &#x27;not po...'''
date = "2013-08-07T06:54:00Z"
lastmod = "2013-08-08T07:12:00Z"
weight = 23609
keywords = [ "pipe", "windows", "remote", "ssh" ]
aliases = [ "/questions/23609" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Remote capture via ssh and pipe](/questions/23609/remote-capture-via-ssh-and-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everyone,</p><p>i have a new configuration where i try to capture my linux machines and display the traffic with wireshark on windows. On windows i'm using cygwin to receive the data from my linux machines via ssh</p><pre><code>$ mkfifo /tmp/capture_1
$ ssh [email protected] &quot;tcpdump -s0 -U -n -w - -i eth0 &#39;not port 22&#39;&quot; &gt; /tmp/capture_1</code></pre><p>So far everything is working quite well. My problem occurs when i try to capture the pipe. When i try to capture in the same manner on ubuntu everything works well.</p></div><div id="question-tags" class="tags-container tags">pipe windows remote ssh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/75aa771136473e5be6bb3d6bca9c3f9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALKA&#39;s gravatar image" /><p>ALKA<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALKA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 07 Aug '13, 08:42</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23609" class="comments-container"><span id="23613"></span><div id="comment-23613" class="comment"><div id="post-23613-score" class="comment-score"></div><div class="comment-text"><p>I presume you're using a regular windows version of Wireshark, not some unknown Cygwin version. If so, are Cygwin pipes compatible with Windows programs?</p></div><div id="comment-23613-info" class="comment-info"><span class="comment-age">(07 Aug '13, 08:43)</span> grahamb ♦</div></div></div><div id="comment-tools-23609" class="comment-tools"></div><div class="clear"></div><div id="comment-23609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23648"></span>

<div id="answer-container-23648" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23648-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please use <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">plink</a> on windows and pipe the binary output of tcpdump directly to Wireshark, instead of trying to create named pipes with Cygwin (as it looks like in your example).</p><blockquote><p>plink.exe -ssh -pw abc123 [email protected] "tcpdump -ni eth0 -s 0 -w - not port 22" | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23648" class="comments-container"><span id="23704"></span><div id="comment-23704" class="comment"><div id="post-23704-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p><p>The named pipes in cygwin were the problem. plink works fine</p></div><div id="comment-23704-info" class="comment-info"><span class="comment-age">(12 Aug '13, 02:08)</span> ALKA</div></div></div><div id="comment-tools-23648" class="comment-tools"></div><div class="clear"></div><div id="comment-23648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

