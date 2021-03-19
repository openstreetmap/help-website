+++
type = "question"
title = "Run wireshark 2.2.2 on CentOS7"
description = '''Hi, I downloaded and installed wireshark 2.2.2 on CentOS 7, however I do not know how to open the GUI for this wireshark. I also have the default wireshark 1.10.14 installed and everytime when trying to open, it only opens the older version. How do I open UI for wireshark 2.2.2 that is already insta...'''
date = "2016-12-02T09:41:00Z"
lastmod = "2016-12-02T12:51:00Z"
weight = 57794
keywords = [ "wireshark2.2.2" ]
aliases = [ "/questions/57794" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Run wireshark 2.2.2 on CentOS7](/questions/57794/run-wireshark-222-on-centos7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57794-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I downloaded and installed wireshark 2.2.2 on CentOS 7, however I do not know how to open the GUI for this wireshark. I also have the default wireshark 1.10.14 installed and everytime when trying to open, it only opens the older version. How do I open UI for wireshark 2.2.2 that is already installed? Also, how do I verify the wireshark 2.2.2 is installed successfully?</p></div><div id="question-tags" class="tags-container tags">wireshark2.2.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '16, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/46cf76db4e0bd89f26d24da675cbd57b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shah&#39;s gravatar image" /><p>Shah<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shah has no accepted answers">0%</span></p></div></div><div id="comments-container-57794" class="comments-container"><span id="57796"></span><div id="comment-57796" class="comment"><div id="post-57796-score" class="comment-score"></div><div class="comment-text"><p>Presumably this is a version of Wireshark you built yourself as I don't think CentOS 7 has a Wireshark 2.2.1 rpm?</p></div><div id="comment-57796-info" class="comment-info"><span class="comment-age">(02 Dec '16, 10:04)</span> grahamb ♦</div></div></div><div id="comment-tools-57794" class="comment-tools"></div><div class="clear"></div><div id="comment-57794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57799"></span>

<div id="answer-container-57799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where did you install Wireshark 2.2.2 (I'm assuming you did a "make install")? I /think/ by default it goes into <code>/usr/local/bin/</code>.</p><p>Options:</p><ol><li>run <code>/usr/local/bin/wireshark</code> (assuming it installed there)</li><li>(else) do (assuming you're in <code>bash</code>): <code>type -a wireshark</code>. That should list 2 Wireshark executables. Try both.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57799" class="comments-container"><span id="57800"></span><div id="comment-57800" class="comment"><div id="post-57800-score" class="comment-score"></div><div class="comment-text"><p>I got the wireshark file from here:</p><p>www.wireshark.org/downloads/src</p><p>on typing whereis wireshark, i see the file is in path: usr/sbin/wireshark usr/share/wireshark /usr/share/man/man1/wireshark.1.gz</p><p>when i check the wireshark file - its the old version 1.10.14 I don't know where the new version is stored in.</p></div><div id="comment-57800-info" class="comment-info"><span class="comment-age">(02 Dec '16, 12:56)</span> Shah</div></div><span id="57802"></span><div id="comment-57802" class="comment"><div id="post-57802-score" class="comment-score"></div><div class="comment-text"><p>Note that wireshark.org does not ship RPMs for CentOS 7. So what you downloaded was probably a source tarball. You can't run Wireshark from there--you need to first configure and compile it. Did you do that?</p></div><div id="comment-57802-info" class="comment-info"><span class="comment-age">(02 Dec '16, 13:22)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-57799" class="comment-tools"></div><div class="clear"></div><div id="comment-57799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

