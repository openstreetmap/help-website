+++
type = "question"
title = "How to filter smpp by message type"
description = '''I see https://www.wireshark.org/docs/dfref/s/smpp.html but I still cannot understand how to filter only submit_sm only. Can any one clarify this for me pls?'''
date = "2014-09-29T13:18:00Z"
lastmod = "2014-10-20T05:20:00Z"
weight = 36704
keywords = [ "smpp" ]
aliases = [ "/questions/36704" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter smpp by message type](/questions/36704/how-to-filter-smpp-by-message-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36704-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see <a href="https://www.wireshark.org/docs/dfref/s/smpp.html">https://www.wireshark.org/docs/dfref/s/smpp.html</a> but I still cannot understand how to filter only submit_sm only. Can any one clarify this for me pls?</p></div><div id="question-tags" class="tags-container tags">smpp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '14, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/edcbd91a6646415652791302627a3370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ky4k0b&#39;s gravatar image" /><p>ky4k0b<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ky4k0b has no accepted answers">0%</span></p></div></div><div id="comments-container-36704" class="comments-container"></div><div id="comment-tools-36704" class="comment-tools"></div><div class="clear"></div><div id="comment-36704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37193"></span>

<div id="answer-container-37193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37193-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have trouble figuring out what filter to use, select a packet with the thing you want to filter on and:</p><ol><li>Look in the lower-left corner of Wireshark: it will tell you the filter name of the object you're looking at</li><li>(or) right-click on the object you're interested in and click "prepare as filter"</li></ol><p>Using the SMPP capture on the SampleCaptures page we can find that you can use these filters to find submit_sm's:</p><ul><li><code>smpp.command_id == 0x00000004</code></li><li><code>smpp.command_id == "Submit_sm"</code></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37193" class="comments-container"></div><div id="comment-tools-37193" class="comment-tools"></div><div class="clear"></div><div id="comment-37193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

