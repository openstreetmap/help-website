+++
type = "question"
title = "capturing from multiple remote hosts at the same time"
description = '''Hi,  I currently can capture remotley using the following syntax.   &quot;C:&#92;Program Files (x86)&#92;PuTTY&#92;plink.exe&quot; -ssh -pw xxxxxx root@192.168.0.10 &quot;tcpdump -ni eth0 -s 0 -w- not port 22 &quot; | &quot;C:&#92;Program Files&#92;Wireshark&#92;Wireshark.exe&quot; -k -i -  However now I would like to capture from 2 remote hosts at the...'''
date = "2014-08-29T07:23:00Z"
lastmod = "2014-08-29T10:43:00Z"
weight = 35870
keywords = [ "remote", "wireshark" ]
aliases = [ "/questions/35870" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing from multiple remote hosts at the same time](/questions/35870/capturing-from-multiple-remote-hosts-at-the-same-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I currently can capture remotley using the following syntax.</p><pre><code> &quot;C:\Program Files (x86)\PuTTY\plink.exe&quot; -ssh -pw xxxxxx [email protected] &quot;tcpdump -ni eth0 -s 0 -w- not port 22 &quot; | &quot;C:\Program Files\Wireshark\Wireshark.exe&quot; -k -i -</code></pre><p>However now I would like to capture from 2 remote hosts at the same time and same window. I was wondering if it's possible , if yes, how should i proceed.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">remote wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '14, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/a1835c7e20b37d17236ebf47320a8ca9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testertester&#39;s gravatar image" /><p>testertester<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testertester has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '14, 07:25</p></div></div><div id="comments-container-35870" class="comments-container"></div><div id="comment-tools-35870" class="comment-tools"></div><div class="clear"></div><div id="comment-35870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35880"></span>

<div id="answer-container-35880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't be able to do 2 remote hosts using the method you're currently using (tcpdump to a pipe). However, I <em>think</em> it would work if you use the <a href="http://wiki.wireshark.org/CaptureSetup/WinPcapRemote">rpcapd</a> approach:</p><ol><li>install rpcapd on the 2 remote hosts</li><li>Add those 2 remote interfaces to Wireshark (Capture-&gt;Options then click on Manage Interfaces then go to the Remote Interfaces tab)</li><li>In the main Capture Options dialog select the 2 remote interfaces and start your capture</li></ol><p>Note: I've never used the remote capture facility and thus I don't have a clue if this will really work. It's completely possible Wireshark doesn't support capturing from 2 remote interfaces at the same time but at a high level (read: not knowing the details) I don't see why it wouldn't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '14, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-35880" class="comments-container"></div><div id="comment-tools-35880" class="comment-tools"></div><div class="clear"></div><div id="comment-35880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

