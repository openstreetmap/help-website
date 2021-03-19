+++
type = "question"
title = "A question about capturing from a named pipe"
description = '''Hello! I, with an intern, wrote a small utility to capture named pipe traffic from another process on the system. It works like this: I have a process that connects to a process server using some named pipe name. I run an application that forces the target application to load a DLL and hijack the Re...'''
date = "2015-08-24T12:06:00Z"
lastmod = "2015-08-24T12:55:00Z"
weight = 45323
keywords = [ "pipe", "reassembly", "named", "winpcap" ]
aliases = [ "/questions/45323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [A question about capturing from a named pipe](/questions/45323/a-question-about-capturing-from-a-named-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I, with an intern, wrote a small utility to capture named pipe traffic from another process on the system. It works like this: I have a process that connects to a process server using some named pipe name. I run an application that forces the target application to load a DLL and hijack the ReadFile, WriteFile, and GetQueuedCompletionStatus Win32API methods. It then has the process create a named pipe server which sends over Pcap-formatted traffic. I connect to this with Wireshark, which causes the aforementioned methods to start serving captured named pipe traffic, encapsulated in TCP/IP headers so that I can track (potentially) multiple named pipe streams from the same process, independently.</p><p>Now, this code is in early alpha, but it is currently working and sending over data. It may crash the target application on unload, as I still need to ensure that all callers are out of the hijacked methods before unloading. Does it make any sense to have this kind of functionality built into WinPcap or Wireshark directly?</p></div><div id="question-tags" class="tags-container tags">pipe reassembly named winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '15, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/7fd3bb983202ed777b50c2bb65b7d857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Mueller&#39;s gravatar image" /><p>Scott Mueller<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Mueller has no accepted answers">0%</span></p></div></div><div id="comments-container-45323" class="comments-container"></div><div id="comment-tools-45323" class="comment-tools"></div><div class="clear"></div><div id="comment-45323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45326"></span>

<div id="answer-container-45326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45326-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds a lot like the functionality provided by extcap, which is in the development (1.99.x) builds of Wireshark.</p><p>Unfortunately extcap isn't very well documented as yet, there is an html page for the interface provided with the dev builds, which doesn't show up online, and also the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=extcap.c;h=339021971bed79f0e793657617d8a5bed51d909d;hb=HEAD">code</a> and an example <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/extcap_example.py;h=dcd7ebbd41efcd77f568fc711ba58c34630b19d6;hb=HEAD">extcap interface</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '15, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45326" class="comments-container"><span id="45328"></span><div id="comment-45328" class="comment"><div id="post-45328-score" class="comment-score"></div><div class="comment-text"><p>I see. Would I need to write an interface for extcap to be able to consume this data that I serve out on a named pipe?</p></div><div id="comment-45328-info" class="comment-info"><span class="comment-age">(24 Aug '15, 14:19)</span> Scott Mueller</div></div></div><div id="comment-tools-45326" class="comment-tools"></div><div class="clear"></div><div id="comment-45326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

