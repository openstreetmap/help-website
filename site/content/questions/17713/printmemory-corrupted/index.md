+++
type = "question"
title = "print&quot;Memory corrupted&quot;."
description = '''when I open a *.pcap, then it popup a cmd window, print&quot;Memory corrupted&quot;. why? and how can I fix the bug.'''
date = "2013-01-15T19:44:00Z"
lastmod = "2013-01-16T06:39:00Z"
weight = 17713
keywords = [ "corrupted", "memory" ]
aliases = [ "/questions/17713" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [print"Memory corrupted".](/questions/17713/printmemory-corrupted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when I open a *.pcap, then it popup a cmd window, print"Memory corrupted". why? and how can I fix the bug.</p></div><div id="question-tags" class="tags-container tags">corrupted memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '13, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p>smilezuzu<br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-17713" class="comments-container"><span id="17714"></span><div id="comment-17714" class="comment"><div id="post-17714-score" class="comment-score"></div><div class="comment-text"><p>Is this a unchanged Wireshark version? Which version is it? How was the .pcap created/transported to the system if ftp was used it should be transfered in binary mode as the file is binary and ftp might mangle it if transfered in ASCII. Does it happen straight away or after reading a portion of the file? How big is the file?</p></div><div id="comment-17714-info" class="comment-info"><span class="comment-age">(15 Jan '13, 23:24)</span> Anders ♦</div></div></div><div id="comment-tools-17713" class="comment-tools"></div><div class="clear"></div><div id="comment-17713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17717"></span>

<div id="answer-container-17717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17717-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually this error message indicates (canary) memory corruption. I'd suggest first trying with the latest version of Wireshark (if you're not already using it). If that doesn't help, <a href="https://bugs.wireshark.org">open a bug report</a> and attach the capture file so we can find and fix the bug.</p><p>(It might also be useful if you tried an <a href="https://www.wireshark.org/download/automated/">automated development build</a>.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17717" class="comments-container"></div><div id="comment-tools-17717" class="comment-tools"></div><div class="clear"></div><div id="comment-17717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

