+++
type = "question"
title = "compile dissector for Wireshark 1.10"
description = '''Hello, I was devising application-specific dissector and was doing fine with Wireshark 1.8. After update to 1.10 it fails to compile with following compiler output: /usr/include/wireshark/wiretap/wtap.h:32:30: fatal error: ws_symbol_export.h: No such file or directory #include &quot;ws_symbol_export.h&quot; I...'''
date = "2013-06-26T06:10:00Z"
lastmod = "2013-06-26T12:14:00Z"
weight = 22355
keywords = [ "compile", "plugin", "dissector", "1.10.0", "linux" ]
aliases = [ "/questions/22355" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [compile dissector for Wireshark 1.10](/questions/22355/compile-dissector-for-wireshark-110)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22355-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I was devising application-specific dissector and was doing fine with Wireshark 1.8. After update to 1.10 it fails to compile with following compiler output:</p><p>/usr/include/wireshark/wiretap/wtap.h:32:30: fatal error: ws_symbol_export.h: No such file or directory</p><p>#include "ws_symbol_export.h"</p><p>I'm not sure whether it could be headers installation issue. I use standard Extra repository of Arch Linux to install Wireshark, so it shouldn't be.</p></div><div id="question-tags" class="tags-container tags">compile plugin dissector 1.10.0 linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p>Andrey<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22355" class="comments-container"></div><div id="comment-tools-22355" class="comment-tools"></div><div class="clear"></div><div id="comment-22355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22371"></span>

<div id="answer-container-22371" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22371-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you've installed a "wireshark development" package that came with the OS and the OS hasn't included all the necessary header files. I'd suggest you raise a bug with them if this is the case.</p><p>The normal suggested method of doing (C language) Wireshark development is to build from a Wireshark source tarball or, better yet, SVN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-22371" class="comments-container"><span id="22510"></span><div id="comment-22510" class="comment"><div id="post-22510-score" class="comment-score"></div><div class="comment-text"><p>Not sure whether they heard me or just fixed it themselves. But after another update it's seems fine. I have another issue though. Anyway, thank you.</p></div><div id="comment-22510-info" class="comment-info"><span class="comment-age">(01 Jul '13, 06:58)</span> Andrey</div></div></div><div id="comment-tools-22371" class="comment-tools"></div><div class="clear"></div><div id="comment-22371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22357"></span>

<div id="answer-container-22357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22357-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That header was added In Feb 2013. Looks like your source tree should be updated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22357" class="comments-container"><span id="22358"></span><div id="comment-22358" class="comment"><div id="post-22358-score" class="comment-score"></div><div class="comment-text"><p>Wireshark source tree or my plug-in source tree?</p></div><div id="comment-22358-info" class="comment-info"><span class="comment-age">(26 Jun '13, 06:38)</span> Andrey</div></div><span id="22359"></span><div id="comment-22359" class="comment"><div id="post-22359-score" class="comment-score"></div><div class="comment-text"><p>Wireshark sources. It's in the top level directory, e.g. <a href="http://anonsvn.wireshark.org/viewvc/trunk/ws_symbol_export.h?revision=48170&amp;view=markup">trunk</a> or trunk-1.10</p></div><div id="comment-22359-info" class="comment-info"><span class="comment-age">(26 Jun '13, 06:43)</span> grahamb ♦</div></div></div><div id="comment-tools-22357" class="comment-tools"></div><div class="clear"></div><div id="comment-22357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

