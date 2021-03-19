+++
type = "question"
title = "Upgrading dissector plugin to 2.0.x from 1.12.x"
description = '''Hello, I would like to update my plugin that currently works with 1.12.x to work with 2.0.x. I have built wireshark 2.0.2 from source successfully and noticed that the file structure of each of the plugin directories is different (now in a VS project rather than using the previous structure, which I...'''
date = "2016-03-30T12:44:00Z"
lastmod = "2016-04-04T06:30:00Z"
weight = 51300
keywords = [ "2.0.x", "upgrade", "plugin" ]
aliases = [ "/questions/51300" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Upgrading dissector plugin to 2.0.x from 1.12.x](/questions/51300/upgrading-dissector-plugin-to-20x-from-112x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51300-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to update my plugin that currently works with 1.12.x to work with 2.0.x. I have built wireshark 2.0.2 from source successfully and noticed that the file structure of each of the plugin directories is different (now in a VS project rather than using the previous structure, which I used along with these instructions <a href="http://www.sewio.net/open-sniffer/develop/how-to-compile-your-wireshark-dissector/">http://www.sewio.net/open-sniffer/develop/how-to-compile-your-wireshark-dissector/</a> to build the last one. I can't seem to find any instructions on how to work with the new file structure (I can't simply use the old one because libwireshark.dll is now in a different place). Please let me know how to go about this. Thank you!</p></div><div id="question-tags" class="tags-container tags">2.0.x upgrade plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p>j-demars<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div></div><div id="comments-container-51300" class="comments-container"></div><div id="comment-tools-51300" class="comment-tools"></div><div class="clear"></div><div id="comment-51300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51303"></span>

<div id="answer-container-51303" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51303-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The canonical reference for this is the Wireshark Developers Guide, in particular for you <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">Section 9.2</a> that describes the changes required to add your own dissector as a plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '16, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51303" class="comments-container"><span id="51304"></span><div id="comment-51304" class="comment"><div id="post-51304-score" class="comment-score"></div><div class="comment-text"><p>I've looked over this link but it literally says nothing about how to actually build the plugin, as in produce the .dll. I have the packet-xxx.c and packet-xxx.h already done from the old plugin, I just need to know how to integrate it into the new build structure with 2.0.2. Something like the link I mentioned above.</p></div><div id="comment-51304-info" class="comment-info"><span class="comment-age">(30 Mar '16, 14:47)</span> j-demars</div></div><span id="51306"></span><div id="comment-51306" class="comment"><div id="post-51306-score" class="comment-score"></div><div class="comment-text"><p>I'll assume that you have followed the instructions on which files to add and modify, then it's simply a case of re-running the CMake generation step and then building exactly as you did to build the original unmodified source, i.e. <code>msbuild ...</code>. Note the CMake generation step is only required when modifying the CMakeLists.txt or CMakeListsCustom.txt files.</p><p>Someone else did note that the instruction <em>Compile the dissector to a DLL or shared library</em> wasn't clear enough, but nobody has offered up a suggestion for what should replace it.</p></div><div id="comment-51306-info" class="comment-info"><span class="comment-age">(30 Mar '16, 15:19)</span> grahamb ♦</div></div><span id="51307"></span><div id="comment-51307" class="comment"><div id="post-51307-score" class="comment-score">1</div><div class="comment-text"><p>I figured it out. With the other plugin, I wasn't always rebuilding all of wireshark to build the plugin, only the way it is done above in the link. I fixed it to build the whole thing and now it's working.</p><p>Thank you!!</p></div><div id="comment-51307-info" class="comment-info"><span class="comment-age">(30 Mar '16, 16:19)</span> j-demars</div></div></div><div id="comment-tools-51303" class="comment-tools"></div><div class="clear"></div><div id="comment-51303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51392"></span>

<div id="answer-container-51392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51392-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>maybe you will use wireshark 2.0* headers and rebuild your plugin</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/1f422a72eab029cae4d8742650674201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cicciovo&#39;s gravatar image" /><p>cicciovo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cicciovo has no accepted answers">0%</span></p></div></div><div id="comments-container-51392" class="comments-container"></div><div id="comment-tools-51392" class="comment-tools"></div><div class="clear"></div><div id="comment-51392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

