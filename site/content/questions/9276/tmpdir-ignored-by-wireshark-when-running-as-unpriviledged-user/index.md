+++
type = "question"
title = "TMPDIR ignored by Wireshark when running as unpriviledged user"
description = '''Hi, wireshark-1.0.15-1.el5_5.3 RHEL5.6 I have set the dumpcap with below so that all users in the group &quot;testgroup&quot; can run the wireshark and capture (without sudoers) chgrp testgroup /usr/sbin/dumpcap chmod 4750 /usr/sbin/dumpcap  Meaning that when I run the dumpcap command manually  as root: [root...'''
date = "2012-02-29T03:37:00Z"
lastmod = "2012-02-29T07:45:00Z"
weight = 9276
keywords = [ "tmp", "unpriviledged", "tmpdir", "temp", "dumpcap" ]
aliases = [ "/questions/9276" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TMPDIR ignored by Wireshark when running as unpriviledged user](/questions/9276/tmpdir-ignored-by-wireshark-when-running-as-unpriviledged-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9276-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>wireshark-1.0.15-1.el5_5.3<br />
RHEL5.6</p><p>I have set the dumpcap with below so that all users in the group "testgroup" can run the wireshark and capture (without sudoers)</p><p>chgrp testgroup /usr/sbin/dumpcap<br />
chmod 4750 /usr/sbin/dumpcap</p><p><br />
Meaning that when I run the dumpcap command manually</p><p>as root:</p><p>[[email protected] etc]# env |grep TMPDIR<br />
TMPDIR=/data<br />
[[email protected] etc]# /usr/sbin/dumpcap<br />
File: /data/etherXXXXGhhoEl<br />
Packets: 25 Packets dropped: 0</p><p>as normal user:</p><p>[[email protected] ~]$ env |grep TMPDIR<br />
TMPDIR=/data<br />
[[email protected] ~]$ /usr/sbin/dumpcap<br />
File: /tmp/etherXXXXrWpaJ8<br />
Packets: 12 Pac<br />
</p><p>But still it writes the temp data to /tmp...</p><p>Everyone is able to write to /data:</p><p>[[email protected] ~]$ ls -ld /data<br />
drwxrwxrwt 4 root root 4096 Feb 19 18:28 /data<br />
[[email protected] ~]$</p><p>It seems that inside the dumpcap there is TMPDIR parameter which seems to overwrite:<br />
<br />
How to overcome this problem ?</p><p>[[email protected] ~]$ strings /usr/sbin/dumpcap |grep -i tmp<br />
TMPDIR /tmp</p><p>All help appreciated.</p></div><div id="question-tags" class="tags-container tags">tmp unpriviledged tmpdir temp dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '12, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/1ab4e0b44e17f63ecd221c76abf3acdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keke&#39;s gravatar image" /><p>keke<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keke has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 03:40</p></div></div><div id="comments-container-9276" class="comments-container"></div><div id="comment-tools-9276" class="comment-tools"></div><div class="clear"></div><div id="comment-9276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9280"></span>

<div id="answer-container-9280" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9280-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another <a href="http://ask.wireshark.org/questions/2516/tmpdir-ignored-when-setuid-for-dumpcap">question</a> asked the same thing. Admittedly it wasn't answered until just now though.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '12, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 06:59</p></div></div><div id="comments-container-9280" class="comments-container"></div><div id="comment-tools-9280" class="comment-tools"></div><div class="clear"></div><div id="comment-9280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

