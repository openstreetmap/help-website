+++
type = "question"
title = "Wireshark crashing"
description = '''Hey All, I am getting an issue with WireShark crashing after around 50 minutes of caputring.  I read some posts saying this was down to a memory issue but I have monitored the server and although memory consumption by wireshark reachs a few GB it nevers maxes out the available memory. I even tried h...'''
date = "2013-04-26T09:14:00Z"
lastmod = "2013-04-26T09:38:00Z"
weight = 20816
keywords = [ "crash", "wireshark" ]
aliases = [ "/questions/20816" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashing](/questions/20816/wireshark-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20816-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey All,</p><p>I am getting an issue with WireShark crashing after around 50 minutes of caputring.<br />
</p><p>I read some posts saying this was down to a memory issue but I have monitored the server and although memory consumption by wireshark reachs a few GB it nevers maxes out the available memory. I even tried having it split the captures into 10mb files and it still crashes around 50 minutes.</p><p>Anyone have any ideas what could be causing this issue?</p><p>I am monitring a HP Teamed Network, the server in question is a HP DL360 G7 and running windows 2008R2 SP1</p><pre><code>Faulting application name: wireshark.exe, version: 1.8.6.48142, time stamp: 0x513791b6
Faulting module name: libglib-2.0-0.dll, version: 2.34.1.0, time stamp: 0x508d9e80
Exception code: 0x40000015
Fault offset: 0x00000000000509c2
Faulting process id: 0x2d34
Faulting application start time: 0x01ce428f5ce63f4a
Faulting application path: C:\Program Files\Wireshark\wireshark.exe
Faulting module path: C:\Program Files\Wireshark\libglib-2.0-0.dll
Report Id: a03eb28a-ae88-11e2-860e-ac162d6f982c</code></pre></div><div id="question-tags" class="tags-container tags">crash wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '13, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/766ed47b848752675473c89eb0ee4be6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steven576&#39;s gravatar image" /><p>Steven576<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steven576 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Apr '13, 19:12</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20816" class="comments-container"><span id="20817"></span><div id="comment-20817" class="comment"><div id="post-20817-score" class="comment-score"></div><div class="comment-text"><p>I have also tried running it on a different server and still experience the same issue.</p></div><div id="comment-20817-info" class="comment-info"><span class="comment-age">(26 Apr '13, 09:19)</span> Steven576</div></div></div><div id="comment-tools-20816" class="comment-tools"></div><div class="clear"></div><div id="comment-20816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20819"></span>

<div id="answer-container-20819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20819-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are running 32 bit Wireshark, then like all 32 bit Windows programs it will be limited to the amount of memory it can use, even on a 64 bit OS. The executable is large memory aware, so on a properly configured 32 bit OS (using the /3GB boot flag) it may use up to 3GB, otherwise only 2GB. On a 64 bit OS it may use up to 4GB.</p><p>The 64 bit version of Wireshark may use up to 8TB.</p><p>As Jasper says, when large amounts of traffic are involved dumpcap should be used with multiple files (-b option). This is because Wireshark (and tshark) accumulate state information about conversations that cause them to run out of memory.</p><p>See <a href="http://support.microsoft.com/default.aspx?scid=889654">this</a> KB article for more info on process memory space.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '13, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Apr '13, 19:14</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20819" class="comments-container"></div><div id="comment-tools-20819" class="comment-tools"></div><div class="clear"></div><div id="comment-20819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20818"></span>

<div id="answer-container-20818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20818-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it looks like you encounter the Out-of-memory problem, see this Wiki page: <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a>. Keep in mind that this problem cannot simply be fought by putting more memory in the PC - Wireshark will still into trouble. The only way to get around it is by not having Wireshark build up data structures of packets.</p><p>Try capturing using the command line tool dumpcap instead, you can find it in the Wireshark directory. "dumpcap -d" will give you a list of interfaces, "dumpcap -i INTERFACENO" will capture on that interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '13, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Apr '13, 09:32</p></div></div><div id="comments-container-20818" class="comments-container"></div><div id="comment-tools-20818" class="comment-tools"></div><div class="clear"></div><div id="comment-20818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

