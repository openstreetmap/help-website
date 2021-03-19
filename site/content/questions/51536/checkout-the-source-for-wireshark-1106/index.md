+++
type = "question"
title = "checkout the source for wireshark 1.10.6"
description = '''Checked out wireshark 1.12.9 and made a build on ubuntu 14.04. I saw there is an executable &quot;reordercap&quot;. This reordercap can&#x27;t run with the default wireshark (1.10.6) that comes with Ubuntu 14.04 installation: this &quot;reordercap&quot; requires libwiretap.so.4 and libwsutil.so.4 but the wireshark 1.10.6 in...'''
date = "2016-04-09T12:46:00Z"
lastmod = "2016-04-09T13:25:00Z"
weight = 51536
keywords = [ "wireshark" ]
aliases = [ "/questions/51536" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [checkout the source for wireshark 1.10.6](/questions/51536/checkout-the-source-for-wireshark-1106)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51536-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Checked out wireshark 1.12.9 and made a build on ubuntu 14.04. I saw there is an executable "reordercap". This reordercap can't run with the default wireshark (1.10.6) that comes with Ubuntu 14.04 installation: this "reordercap" requires libwiretap.so.4 and libwsutil.so.4 but the wireshark 1.10.6 installation comes with libwiretap.so.3 and libwsutil.so.3.</p><p>I would like to checkout the source for wireshark 1.10.6 and build a reordercap that works with the standard wireshark installation, but don't know where the source for 1.10.6 is. Any ideas?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '16, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-51536" class="comments-container"><span id="51538"></span><div id="comment-51538" class="comment"><div id="post-51538-score" class="comment-score"></div><div class="comment-text"><p>Can't you just uninstall the distribution 1.10.6 and install the 1.12.9 you've built?</p></div><div id="comment-51538-info" class="comment-info"><span class="comment-age">(09 Apr '16, 14:53)</span> grahamb ♦</div></div></div><div id="comment-tools-51536" class="comment-tools"></div><div class="clear"></div><div id="comment-51536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51537"></span>

<div id="answer-container-51537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51537-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can find it <a href="https://www.wireshark.org/download/src/all-versions/wireshark-1.10.6.tar.bz2">here</a>. <a href="http://www.linuxfromscratch.org/blfs/view/7.5/basicnet/wireshark.html">Linux from Scratch</a> is another good source for Linux builds with instructions, but there are for 1.10.5 (they do have the 1.10.5 to 1.10.6 patch, though).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '16, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div></div><div id="comments-container-51537" class="comments-container"><span id="51539"></span><div id="comment-51539" class="comment"><div id="post-51539-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much @coloncm.</p></div><div id="comment-51539-info" class="comment-info"><span class="comment-age">(09 Apr '16, 16:17)</span> pktUser1001</div></div></div><div id="comment-tools-51537" class="comment-tools"></div><div class="clear"></div><div id="comment-51537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

