+++
type = "question"
title = "editcap behavior confirmation"
description = '''Hi all, Got a packet capture with 10 packets and the time interval between 1st and last packet is 2.315 seconds. Time stamps of 10 packets respectively {51.770989000;51.771761000;51.771783000;51.771880000;51.774776000;51.774966000; 51.774985000;51.775097000;54.085199000;54.085748000} Now, I gave the...'''
date = "2013-03-15T11:19:00Z"
lastmod = "2013-03-15T16:13:00Z"
weight = 19542
keywords = [ "editcap" ]
aliases = [ "/questions/19542" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [editcap behavior confirmation](/questions/19542/editcap-behavior-confirmation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19542-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Got a packet capture with 10 packets and the time interval between 1st and last packet is 2.315 seconds.</p><p>Time stamps of 10 packets respectively {51.770989000;51.771761000;51.771783000;51.771880000;51.774776000;51.774966000; 51.774985000;51.775097000;54.085199000;54.085748000}</p><p>Now, I gave the following editcap command which creates trace files with 1 second worth of capture.</p><p>editcap -i 1 padding.pcap 1_padding.pcapng</p><p>This command created 3 trace files and the second trace file is having 0 packets.</p><p>I am seeing a behavior that the engine is going through a pattern of checking packets at 0th second,1st second,2nd sec etc...If the engine is not finding any packets at nth second it is creating empty trace against it.</p><p>Any specific reason for creating an empty trace file against not creating at all?</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '13, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '13, 11:27</p></div></div><div id="comments-container-19542" class="comments-container"></div><div id="comment-tools-19542" class="comment-tools"></div><div class="clear"></div><div id="comment-19542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19549"></span>

<div id="answer-container-19549" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19549-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's "works as designed". Editcap will create a new tracefile as soon as the first interval is finished. And closes it when the next interval is finished. It does not delete the file is zero packets were written, neither does it wait to open a new file until the first packet in the interval is seen.</p><p>I kinda like the fact that it explicitly shows you that that particular interval did not contain any packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19549" class="comments-container"></div><div id="comment-tools-19549" class="comment-tools"></div><div class="clear"></div><div id="comment-19549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

