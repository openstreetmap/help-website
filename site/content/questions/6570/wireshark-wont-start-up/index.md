+++
type = "question"
title = "Wireshark won&#x27;t start up"
description = '''Aloha from Hawaii, I&#x27;m running a 1.67 GHz PPC G4 powerbook with Mac OS 10.4.11. I installed Wireshark 1.3.5 by:  Moving the application to the Application folder. Placing the ChmodBPF directory into the StartupItems directory  Copying the Wireshark Command lines to a directory I created on the deskt...'''
date = "2011-09-26T17:30:00Z"
lastmod = "2011-10-07T07:11:00Z"
weight = 6570
keywords = [ "startup", "osx", "mac", "crash" ]
aliases = [ "/questions/6570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark won't start up](/questions/6570/wireshark-wont-start-up)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Aloha from Hawaii,</p><p>I'm running a 1.67 GHz PPC G4 powerbook with Mac OS 10.4.11. I installed Wireshark 1.3.5 by:</p><ol><li>Moving the application to the Application folder.</li><li>Placing the ChmodBPF directory into the StartupItems directory</li><li>Copying the Wireshark Command lines to a directory I created on the desktop for them.</li></ol><p>I restarted the machine and had the OS fix the permissions on the ChmodBPF, and restarted again. After the reboot, I started Wireshark. It opened my X11. A message told me that it may take a while to see the Wireshark window as a font cache was built. I waited over 10 minutes, and nothing happened. Now when I start Wireshark, the icon for the program appears in the dock for about 3 seconds and then disappears. My X11 starts at the same time and stays open. Any Ideas on what is going on?</p><p>-Ken</p></div><div id="question-tags" class="tags-container tags">startup osx mac crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '11, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/aff7c1b52b00d144c5f2d9d1ba533562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenb&#39;s gravatar image" /><p>kenb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '11, 21:52</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6570" class="comments-container"><span id="6581"></span><div id="comment-6581" class="comment"><div id="post-6581-score" class="comment-score"></div><div class="comment-text"><p>Why go for a development snapshot release? It's over a year old, unsupported. The stable releases 1.4.x and 1.6.x can be found at the download page.</p></div><div id="comment-6581-info" class="comment-info"><span class="comment-age">(26 Sep '11, 23:44)</span> Jaap ♦</div></div><span id="6583"></span><div id="comment-6583" class="comment"><div id="post-6583-score" class="comment-score"></div><div class="comment-text"><p>However, none of the builds from wireshark.org work on OS X 10.4.x; we have 32-bit x86 and PowerPC builds that run on 10.5 and later, and a 64-bit x86 build (x86-64) that runs on 10.6 and later. If you want a build that works on 10.4, you'll have to check out, for example, MacPorts or Fink - see the "Third-Party Packages" section of <a href="http://www.wireshark.org/download.html">the download page</a>.</p></div><div id="comment-6583-info" class="comment-info"><span class="comment-age">(27 Sep '11, 02:03)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6570" class="comment-tools"></div><div class="clear"></div><div id="comment-6570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6788"></span>

<div id="answer-container-6788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6788-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another user had the same <a href="http://ask.wireshark.org/questions/6780/os-x-lion-install-failure">symptom</a> (except in Lion) and resolved it by changing the ownership of <code>~/.wireshark</code> so that the font cache can be written there. The permissions problem was indicated in his syslog, which you can also examine yourself via <code>Console.app</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '11, 07:14</p></div></div><div id="comments-container-6788" class="comments-container"></div><div id="comment-tools-6788" class="comment-tools"></div><div class="clear"></div><div id="comment-6788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

