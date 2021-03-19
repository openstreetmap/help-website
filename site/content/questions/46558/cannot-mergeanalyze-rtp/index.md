+++
type = "question"
title = "cannot merge/analyze rtp"
description = '''Hi, whenever I try to merge 2 traces i get the below error:  &quot;The file &quot;.&quot; could not be created because an invalid filename was specified.&quot; whenever i try to analyze rtp, i get: Can&#x27;t create temporary file for RTP analysis: Invalid argument. I&#x27;ve tried this with 2 different versions of wireshark Ver...'''
date = "2015-10-15T03:16:00Z"
lastmod = "2015-10-16T08:00:00Z"
weight = 46558
keywords = [ "merge", "analyze", "rtp" ]
aliases = [ "/questions/46558" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [cannot merge/analyze rtp](/questions/46558/cannot-mergeanalyze-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46558-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>whenever I try to merge 2 traces i get the below error: "The file "." could not be created because an invalid filename was specified."</p><p>whenever i try to analyze rtp, i get: Can't create temporary file for RTP analysis: Invalid argument.</p><p>I've tried this with 2 different versions of wireshark Version 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12) and 1.12.8</p><p>Please help</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">merge analyze rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '15, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/84ac08b0388d7bfc82d7e2e535232e70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bobert&#39;s gravatar image" /><p>Bobert<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bobert has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Oct '15, 03:16</p></div></div><div id="comments-container-46558" class="comments-container"><span id="46562"></span><div id="comment-46562" class="comment"><div id="post-46562-score" class="comment-score"></div><div class="comment-text"><p>please post the <strong>exact</strong> command you used to merge the files.</p></div><div id="comment-46562-info" class="comment-info"><span class="comment-age">(15 Oct '15, 05:37)</span> Kurt Knochner ♦</div></div><span id="46568"></span><div id="comment-46568" class="comment"><div id="post-46568-score" class="comment-score"></div><div class="comment-text"><p>not a command. using the wireshark GUI</p></div><div id="comment-46568-info" class="comment-info"><span class="comment-age">(15 Oct '15, 08:23)</span> Bobert</div></div><span id="46569"></span><div id="comment-46569" class="comment"><div id="post-46569-score" class="comment-score"></div><div class="comment-text"><p>Ok, please tell us exactly how you're performing the merge operation in the GUI.</p></div><div id="comment-46569-info" class="comment-info"><span class="comment-age">(15 Oct '15, 08:39)</span> Jim Aragon</div></div><span id="46594"></span><div id="comment-46594" class="comment"><div id="post-46594-score" class="comment-score"></div><div class="comment-text"><p>i click on File-&gt;Merge , select the file, and click open. by default, it uses "merge packets chronologically" . i am not doing anything complicated, and i am doing it exactly how i used to do it on my old computer.</p></div><div id="comment-46594-info" class="comment-info"><span class="comment-age">(15 Oct '15, 23:51)</span> Bobert</div></div><span id="46603"></span><div id="comment-46603" class="comment"><div id="post-46603-score" class="comment-score"></div><div class="comment-text"><p>Are your files located on a network share? If so, what is it? NAS, Windows Fileserver, Linux Samba, NFS?</p><p>BTW: What is your OS and OS version?</p></div><div id="comment-46603-info" class="comment-info"><span class="comment-age">(16 Oct '15, 03:14)</span> Kurt Knochner ♦</div></div><span id="46622"></span><div id="comment-46622" class="comment not_top_scorer"><div id="post-46622-score" class="comment-score"></div><div class="comment-text"><p>Works fine for me using Wireshark 1.12.8 on Windows 7. Another way to do this is, instead of loading the first file into Wireshark and then merging in the second file, close all files so that there are no packets in Wireshark, open a file explorer window, select the two files that you want to merge, and then drag them both into Wireshark at the same time.</p></div><div id="comment-46622-info" class="comment-info"><span class="comment-age">(16 Oct '15, 06:40)</span> Jim Aragon</div></div></div><div id="comment-tools-46558" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-46558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46624"></span>

<div id="answer-container-46624" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46624-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The location for temporary files cannot be properly found, see <a href="https://developer.gnome.org/glib/stable/glib-Miscellaneous-Utility-Functions.html#g-get-tmp-dir">this entry</a> in the glib documentation. You may want to have a look at these environment variables.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46624" class="comments-container"><span id="46706"></span><div id="comment-46706" class="comment"><div id="post-46706-score" class="comment-score">1</div><div class="comment-text"><p>thank you. I reset the TEMP variable and that fixed the issue.</p></div><div id="comment-46706-info" class="comment-info"><span class="comment-age">(19 Oct '15, 12:03)</span> Bobert</div></div><span id="46712"></span><div id="comment-46712" class="comment"><div id="post-46712-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-46712-info" class="comment-info"><span class="comment-age">(19 Oct '15, 13:25)</span> Jaap ♦</div></div><span id="46730"></span><div id="comment-46730" class="comment"><div id="post-46730-score" class="comment-score"></div><div class="comment-text"><p>I accepted the answer, as it's apparently the correct one (and not easy to spot).</p></div><div id="comment-46730-info" class="comment-info"><span class="comment-age">(19 Oct '15, 16:23)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46624" class="comment-tools"></div><div class="clear"></div><div id="comment-46624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

