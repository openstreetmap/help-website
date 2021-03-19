+++
type = "question"
title = "howto count total IP size of a capture"
description = '''Hello, I would like to get a total IP size of captured packets. I am asking IP size, not total size of the packets (with ethernet header included for example). Thank you, G. Husson'''
date = "2011-12-09T07:04:00Z"
lastmod = "2011-12-09T07:47:00Z"
weight = 7870
keywords = [ "count", "ip", "total", "size" ]
aliases = [ "/questions/7870" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [howto count total IP size of a capture](/questions/7870/howto-count-total-ip-size-of-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to get a total IP size of captured packets. I am asking IP size, not total size of the packets (with ethernet header included for example).</p><p>Thank you, G. Husson</p></div><div id="question-tags" class="tags-container tags">count ip total size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '11, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/6130baf2862e1c67fdef32883d241885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thalos_ghusson&#39;s gravatar image" /><p>thalos_ghusson<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thalos_ghusson has no accepted answers">0%</span></p></div></div><div id="comments-container-7870" class="comments-container"></div><div id="comment-tools-7870" class="comment-tools"></div><div class="clear"></div><div id="comment-7870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7875"></span>

<div id="answer-container-7875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7875-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> Statistics</p><pre><code>$ tshark -r Clmt_04.pcap -qz &quot;io,stat,300,SUM(ip.len)ip.len&quot;
===================================================================
IO Statistics
Interval: 300.000 secs
Column #0: SUM(ip.len)ip.len
                |   Column #0
Time            |            SUM
000.000-300.000            877439
===================================================================</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div></div><div id="comments-container-7875" class="comments-container"><span id="7907"></span><div id="comment-7907" class="comment"><div id="post-7907-score" class="comment-score">1</div><div class="comment-text"><p>Hello,</p><p>Thank you for this, it perfectly feeds my needs ! Personnaly, I will put "0"s, as in man it says that it will not limit the analysis.</p><p>tshark.exe" -r "test.pcap" -qz "io,stat,0,SUM(ip.len)ip.len"</p><p>G. Husson</p></div><div id="comment-7907-info" class="comment-info"><span class="comment-age">(12 Dec '11, 00:11)</span> thalos_ghusson</div></div><span id="7908"></span><div id="comment-7908" class="comment"><div id="post-7908-score" class="comment-score"></div><div class="comment-text"><p>You are welcome:)<br />
Just another example:<br />
</p><pre><code>$ tshark -r Clmt_04.pcap -qz &quot;io,stat,0,SUM(frame.len)frame.len&quot; -z &quot;io,stat,0,SUM(ip.len)ip.len&quot;
======
IO Statistics
Column #0: SUM(ip.len)ip.len
                |   Column #0
Time            |            SUM
000.000-                   877439
======
======
IO Statistics
Column #0: SUM(frame.len)frame.len
                |   Column #0
Time            |            SUM
000.000-                   901742
======</code></pre></div><div id="comment-7908-info" class="comment-info"><span class="comment-age">(12 Dec '11, 01:26)</span> joke</div></div></div><div id="comment-tools-7875" class="comment-tools"></div><div class="clear"></div><div id="comment-7875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7872"></span>

<div id="answer-container-7872" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7872-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would start with tshark filtering the needed information:</p><pre><code>tshark -r &quot;Test-Run.cap&quot; -R &quot;ip.len&gt;0&quot; -Tfields -e ip.len</code></pre><p>then do whatever to sum those results up and your good. Excel, Calc, perl scripting ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '11, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '11, 07:21</p></div></div><div id="comments-container-7872" class="comments-container"><span id="7873"></span><div id="comment-7873" class="comment"><div id="post-7873-score" class="comment-score"></div><div class="comment-text"><p>I tryed that : C:Documents and SettingsXXXBureau&gt;"C:Program FilesWiresharktshark.exe" tshark -r "test.pcap" -R "ip.len&gt;0" -Tfields -e ip.len NOTE: you should run 'diskperf -y' to enable the disk statistics tshark: Read filters were specified both with "-R" and with additional command-line arguments Wireshark does not run.</p><p>My version : Version 1.6.1 (SVN Rev 38096 from /trunk-1.6) on windows XP SP3</p><p>Thank you, G. HUsson</p></div><div id="comment-7873-info" class="comment-info"><span class="comment-age">(09 Dec '11, 07:30)</span> thalos_ghusson</div></div><span id="7874"></span><div id="comment-7874" class="comment"><div id="post-7874-score" class="comment-score"></div><div class="comment-text"><p>Sorry, my mistake, I let a "tshark" on the command line. Now it is working. It is a good start point, thank you !</p><p>C:Documents and SettingsthalosBureau&gt;"C:Program FilesWiresharktshark.exe" -r "test.pcap" -R "ip.len&gt;0" -Tfields -e ip.len NOTE: you should run 'diskperf -y' to enable the disk statistics 76 40 76 76 76 76 164 40</p></div><div id="comment-7874-info" class="comment-info"><span class="comment-age">(09 Dec '11, 07:40)</span> thalos_ghusson</div></div></div><div id="comment-tools-7872" class="comment-tools"></div><div class="clear"></div><div id="comment-7872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

