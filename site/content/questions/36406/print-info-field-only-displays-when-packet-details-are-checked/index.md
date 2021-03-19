+++
type = "question"
title = "Print info field only displays when Packet Details are checked"
description = '''In WireShark, if you use the Print, Output to file, and only select Packet summary line, the Info field is blank. If you also include Packet Details, All collapsed, the Info field is displayed but then you have to edit the text file to delete the details. Is there a way to print just the Packet summ...'''
date = "2014-09-17T07:17:00Z"
lastmod = "2014-10-22T02:21:00Z"
weight = 36406
keywords = [ "print", "info" ]
aliases = [ "/questions/36406" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Print info field only displays when Packet Details are checked](/questions/36406/print-info-field-only-displays-when-packet-details-are-checked)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In WireShark, if you use the Print, Output to file, and only select Packet summary line, the Info field is blank.</p><p>If you also include Packet Details, All collapsed, the Info field is displayed but then you have to edit the text file to delete the details.</p><p>Is there a way to print just the Packet summary line with the Info field to a text file?</p></div><div id="question-tags" class="tags-container tags">print info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '14, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/d14fb6508e58cc1e19da06473c20b172?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jds&#39;s gravatar image" /><p>jds<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jds has no accepted answers">0%</span></p></div></div><div id="comments-container-36406" class="comments-container"></div><div id="comment-tools-36406" class="comment-tools"></div><div class="clear"></div><div id="comment-36406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37265"></span>

<div id="answer-container-37265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37265-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It works fine for me: when I print only the Packet Summaries I get just the summaries including the Info line. For example:</p><pre><code>No.     Time            Source                Destination           Protocol Length User-Name  Info
  1 11:10:53.878966 10.226.202.118        10.226.202.53         TCP      62                1770→9000 [SYN] Seq=3871210362 Win=32767 Len=0 MSS=1260 SACK_PERM=1
  2 11:10:53.879393 10.226.202.53         10.226.202.118        TCP      60                9000→1770 [SYN, ACK] Seq=2819423808 Ack=3871210363 Win=61440 Len=0 MSS=1460
  3 11:10:53.879422 10.226.202.118        10.226.202.53         TCP      54                1770→9000 [ACK] Seq=3871210363 Ack=2819423809 Win=34020 Len=0</code></pre><p>You may want to try upgrading to the latest release (1.12.1).</p><p>Another possibility is that the protocol dissector in question is doing something which causes it to not fill in the Info column in this situation. If that's the case even in the latest release, please <a href="https://bugs.wireshark.org">file a bug report</a> including a sample capture and the exact steps to repeat the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37265" class="comments-container"></div><div id="comment-tools-37265" class="comment-tools"></div><div class="clear"></div><div id="comment-37265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

