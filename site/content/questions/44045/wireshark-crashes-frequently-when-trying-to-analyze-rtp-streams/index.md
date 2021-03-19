+++
type = "question"
title = "Wireshark crashes frequently when trying to analyze rtp streams!"
description = '''Hi guys, my wireshark crashes frequently(about 75% of times) when I try to analyze RTP streams from the show all streams window.I am building wireshark using code from git,branch is master-1.12.I am attaching the screenshot with the crash log and my git status.I am compiling my Wireshark using ./con...'''
date = "2015-07-10T03:34:00Z"
lastmod = "2015-07-10T03:34:00Z"
weight = 44045
keywords = [ "wireshark_crashed", "analyze", "crash", "rtp" ]
aliases = [ "/questions/44045" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes frequently when trying to analyze rtp streams!](/questions/44045/wireshark-crashes-frequently-when-trying-to-analyze-rtp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>my wireshark crashes frequently(about 75% of times) when I try to analyze RTP streams from the show all streams window.I am building wireshark using code from git,branch is master-1.12.I am attaching the screenshot with the crash log and my git status.I am compiling my Wireshark using</p><p><code>./configure --prefix=/path/to/wireshark-install/</code> . option.Here is the screenshot!</p><p><a href="https://drive.google.com/file/d/0B6c6B1cns2szakliM25KOFpTM2M/view?usp=sharing">https://drive.google.com/file/d/0B6c6B1cns2szaXZJOVZ1SF9uRlE/view?usp=sharing</a></p><p>and here is the gdb trace.</p><p><a href="https://drive.google.com/file/d/0B6c6B1cns2szakliM25KOFpTM2M/view?usp=sharing">https://drive.google.com/file/d/0B6c6B1cns2szckR4bXhobDBYR2c/view?usp=sharing</a></p><p>Can someone help me with this!</p><p>EDIT: I have compiled wireshark with</p><pre><code>./configure --prefix=/path/to/wireshark-install/ --with-gtk2 --without-gtk3 --with-qt

./configure --prefix=/path/to/wireshark-install/ --without-gtk2 --with-gtk3 --with-qt

./configure --prefix=/path/to/wireshark-install/ --with-gtk3 --without-qt</code></pre><p>and I can reproduce the problem in all three versions.</p><p>-koundi</p></div><div id="question-tags" class="tags-container tags">wireshark_crashed analyze crash rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '15, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '15, 04:56</p></div></div><div id="comments-container-44045" class="comments-container"><span id="44049"></span><div id="comment-44049" class="comment"><div id="post-44049-score" class="comment-score"></div><div class="comment-text"><p>I suppose your OS distribution of Wireshark is quite old, hence your own compilation. Unfortunately it's going to be quite difficult to debug this without a capture that causes the issue to occur for you. Are you able to provide one?</p></div><div id="comment-44049-info" class="comment-info"><span class="comment-age">(10 Jul '15, 05:11)</span> grahamb ♦</div></div><span id="44050"></span><div id="comment-44050" class="comment"><div id="post-44050-score" class="comment-score"></div><div class="comment-text"><p>This is probably a duplicate of <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10016">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10016</a></p></div><div id="comment-44050-info" class="comment-info"><span class="comment-age">(10 Jul '15, 05:41)</span> Pascal Quantin</div></div><span id="44067"></span><div id="comment-44067" class="comment"><div id="post-44067-score" class="comment-score"></div><div class="comment-text"><p>Ah! So it is a known bug.This link <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10714">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10714</a> has a similar gdb trace.So has someone pinpointed the problem yet?</p></div><div id="comment-44067-info" class="comment-info"><span class="comment-age">(10 Jul '15, 15:33)</span> koundi</div></div></div><div id="comment-tools-44045" class="comment-tools"></div><div class="clear"></div><div id="comment-44045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

