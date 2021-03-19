+++
type = "question"
title = "Why is Eclipse not recommended for Wireshark development in Linux?"
description = '''I&#x27;m used to use Eclipse for my debugging work. In the current time I need to debug a Wireshark dissector in Linux. Googling Eclipse and Wireshark gives me the impression that it is not recommended to use Eclipse for Wirshark development work in general. Here is an example. I&#x27;d like to know why is it...'''
date = "2014-07-15T12:07:00Z"
lastmod = "2014-07-15T13:00:00Z"
weight = 34676
keywords = [ "wireshark", "eclipse", "debugger", "linux" ]
aliases = [ "/questions/34676" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why is Eclipse not recommended for Wireshark development in Linux?](/questions/34676/why-is-eclipse-not-recommended-for-wireshark-development-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm used to use Eclipse for my debugging work. In the current time I need to debug a Wireshark dissector in Linux. Googling Eclipse and Wireshark gives me the impression that it is not recommended to use Eclipse for Wirshark development work in general. Here is an <a href="https://www.wireshark.org/lists/wireshark-dev/201001/msg00322.html">example</a>. I'd like to know why is it not recommended? What makes Eclipse not useful for debugging Wireshark? and If I have to learn a new debugger to debug Wireshark which one is easier to use and faster to learn DDD or GDB?</p><p>Thanks in advance for sharing your experiences!</p></div><div id="question-tags" class="tags-container tags">wireshark eclipse debugger linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '14, 12:58</p></div></div><div id="comments-container-34676" class="comments-container"><span id="34681"></span><div id="comment-34681" class="comment"><div id="post-34681-score" class="comment-score">1</div><div class="comment-text"><p>I've never heard of "GDP"; did you mean "GDB"? If you're used to debugging with an IDE, using ddd may be easier for you than jumping straight in to using gdb directly, although you should know that ddd is just a graphical front end to gdb. Learning at least the basics of interacting with gdb directly would be useful for you in the future in any case.</p></div><div id="comment-34681-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:48)</span> multipleinte...</div></div><span id="34682"></span><div id="comment-34682" class="comment"><div id="post-34682-score" class="comment-score">1</div><div class="comment-text"><p>&lt;why isn't eclipse recommended? Probably because none of the core developers use it and if some one is using it no one bothered to write an instructor how to use it. Personally I develop on windows and use the msvc debugger or g_warning() or printf()</p></div><div id="comment-34682-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:53)</span> Anders ♦</div></div><span id="34688"></span><div id="comment-34688" class="comment"><div id="post-34688-score" class="comment-score"></div><div class="comment-text"><p>I've corrected it thank you @multipleinte... Thanks @Andres for sharing your personal experience.</p></div><div id="comment-34688-info" class="comment-info"><span class="comment-age">(15 Jul '14, 13:06)</span> flora</div></div></div><div id="comment-tools-34676" class="comment-tools"></div><div class="clear"></div><div id="comment-34676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34687"></span>

<div id="answer-container-34687" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34687-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wouldn't regard Eclipse as "not recommended" more as just not used by those core developers working on Linux, where most seem to be happy with a text editor and command line compilation and debugging with GDB.</p><p>Even on Windows, I think most devs just use a text editor and command line compiles, then fire up either WinDbg or the Visual Studio debugger when needed.</p><p>You might look into using CMake to build Wireshark, as CMake can generate Eclipse CDT project files (amongst many other build formats) to build (and I presume debug) using Eclipse. When I get the CMake build for Wireshark working properly on Windows, then I would expect some more devs to use it to generate Visual Studio solutions and then work in VS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '14, 13:34</p></div></div><div id="comments-container-34687" class="comments-container"></div><div id="comment-tools-34687" class="comment-tools"></div><div class="clear"></div><div id="comment-34687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

