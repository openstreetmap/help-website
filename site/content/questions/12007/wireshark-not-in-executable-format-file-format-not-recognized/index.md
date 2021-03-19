+++
type = "question"
title = "wireshark not in executable format: File format not recognized"
description = '''I followed standard procedure , autogen.sh , configure then make .. And somehow executable was not produced instead a shell script was made up , that&#x27;s why getting this error below in gdb :- I want to make executable , in order to debug via gdb .. what i am missing? [root@localhost wireshark-1.7.1]#...'''
date = "2012-06-18T02:45:00Z"
lastmod = "2012-06-18T03:43:00Z"
weight = 12007
keywords = [ "wireshark" ]
aliases = [ "/questions/12007" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark not in executable format: File format not recognized](/questions/12007/wireshark-not-in-executable-format-file-format-not-recognized)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12007-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I followed standard procedure , autogen.sh , configure then make .. And somehow executable was not produced instead a shell script was made up , that's why getting this error below in gdb :-</p><p>I want to make executable , in order to debug via gdb .. what i am missing?</p><p>[[email protected] wireshark-1.7.1]# gdb ./wireshark GNU gdb Fedora (6.8-1.fc9)</p><p>Copyright (C) 2008 Free Software Foundation, Inc.</p><p>License GPLv3+: GNU GPL version 3 or later <a href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a></p><p>This is free software: you are free to change and redistribute it.</p><p>There is NO WARRANTY, to the extent permitted by law. Type "show copying" and "show warranty" for details.</p><p>This GDB was configured as "i386-redhat-linux-gnu"...</p><blockquote><blockquote><p>"/root/wireshark/wireshark-1.7.1/wireshark": not in executable format: File format not recognized (gdb) run</p></blockquote></blockquote></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '12, 02:47</p></div></div><div id="comments-container-12007" class="comments-container"><span id="12008"></span><div id="comment-12008" class="comment"><div id="post-12008-score" class="comment-score"></div><div class="comment-text"><p>What is the output of these commands?</p><blockquote><p><code>file /root/wireshark/wireshark-1.7.1/wireshark</code><br />
<code>ldd /root/wireshark/wireshark-1.7.1/wireshark</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-12008-info" class="comment-info"><span class="comment-age">(18 Jun '12, 03:01)</span> Kurt Knochner ♦</div></div><span id="12009"></span><div id="comment-12009" class="comment"><div id="post-12009-score" class="comment-score"></div><div class="comment-text"><p>/root/wireshark/wireshark-1.7.1/wireshark: Bourne shell script text executable</p><p>and</p><p>[[email protected] wireshark-1.7.1]# ldd /root/wireshark/wireshark-1.7.1/wireshark not a dynamic executable</p><p>thanks.</p></div><div id="comment-12009-info" class="comment-info"><span class="comment-age">(18 Jun '12, 03:04)</span> yogeshg</div></div><span id="12010"></span><div id="comment-12010" class="comment"><div id="post-12010-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Bourne shell script text executable</p></blockquote><p>O.K. you see, why you can't debug that? ;-)</p><p>It's just a wrapper script for the wireshark binary, which is in <code>.libs/lt-wireshark</code>. Run the script like this and you will see the path on your system:</p><blockquote><p><code>sh -x /root/wireshark/wireshark-1.7.1/wireshark</code><br />
</p></blockquote><p>So, run gdb:</p><blockquote><p><code>gdb /root/wireshark/wireshark-1.7.1/wireshark/.libs/lt-wireshark</code><br />
</p></blockquote><p>or add gdb to the wrapper script.</p><p><strong>UPDATE:</strong> or even better: see answer below</p></div><div id="comment-12010-info" class="comment-info"><span class="comment-age">(18 Jun '12, 03:34)</span> Kurt Knochner ♦</div></div><span id="12013"></span><div id="comment-12013" class="comment"><div id="post-12013-score" class="comment-score"></div><div class="comment-text"><p>I ain't enough comfortable with shell scripting, moreover i was interested in seeing what and which functions get called. Thanks anyways</p></div><div id="comment-12013-info" class="comment-info"><span class="comment-age">(18 Jun '12, 03:55)</span> yogeshg</div></div></div><div id="comment-tools-12007" class="comment-tools"></div><div class="clear"></div><div id="comment-12007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12011"></span>

<div id="answer-container-12011" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12011-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Run wireshark through libtool, like this:</p><blockquote><p><code>libtool --mode=execute gdb /root/wireshark/wireshark-1.7.1/wireshark</code><br />
</p></blockquote><p>see here: <a href="http://wiki.wireshark.org/Development/Tips">http://wiki.wireshark.org/Development/Tips</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12011" class="comments-container"><span id="12012"></span><div id="comment-12012" class="comment"><div id="post-12012-score" class="comment-score"></div><div class="comment-text"><p>You are saviour!</p></div><div id="comment-12012-info" class="comment-info"><span class="comment-age">(18 Jun '12, 03:50)</span> yogeshg</div></div></div><div id="comment-tools-12011" class="comment-tools"></div><div class="clear"></div><div id="comment-12011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

