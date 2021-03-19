+++
type = "question"
title = "May I capture and see RS232 traffic with Wireshark?"
description = '''Hi everybody there. May I capture and analize traffic sent and received on an RS-232 interface (COM1 or COM2) of a PC, i.e. the traffic for a Console port of a Router, or a dialog with and old PLC, etc? Of course, RAW data would be OK! In the list of interfaces &amp;amp; protocols, I can&#x27;t find &quot;RS-232&quot;...'''
date = "2014-09-12T04:29:00Z"
lastmod = "2014-09-12T05:03:00Z"
weight = 36258
keywords = [ "com1", "serial", "rs232", "asynchronous" ]
aliases = [ "/questions/36258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [May I capture and see RS232 traffic with Wireshark?](/questions/36258/may-i-capture-and-see-rs232-traffic-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36258-score" class="post-score" title="current number of votes">0</div><span id="post-36258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody there.</p><p>May I capture and analize traffic sent and received on an RS-232 interface (COM1 or COM2) of a PC, i.e. the traffic for a Console port of a Router, or a dialog with and old PLC, etc?</p><p>Of course, RAW data would be OK!</p><p>In the list of interfaces &amp; protocols, I can't find "RS-232" at all...</p><p>Tnx in adv to you all!</p><p>Marco P. from Milan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-com1" rel="tag" title="see questions tagged &#39;com1&#39;">com1</span> <span class="post-tag tag-link-serial" rel="tag" title="see questions tagged &#39;serial&#39;">serial</span> <span class="post-tag tag-link-rs232" rel="tag" title="see questions tagged &#39;rs232&#39;">rs232</span> <span class="post-tag tag-link-asynchronous" rel="tag" title="see questions tagged &#39;asynchronous&#39;">asynchronous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '14, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/559892be4bf3040b787ae281d55c00bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pagamar&#39;s gravatar image" /><p><span>pagamar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pagamar has no accepted answers">0%</span></p></div></div><div id="comments-container-36258" class="comments-container"></div><div id="comment-tools-36258" class="comment-tools"></div><div class="clear"></div><div id="comment-36258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36263"></span>

<div id="answer-container-36263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36263-score" class="post-score" title="current number of votes">0</div><span id="post-36263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently this can't be done directly from Wireshark.</p><p>See this question for other solutions: <a href="https://ask.wireshark.org/questions/23243/how-do-you-capture-serial-com-communications">https://ask.wireshark.org/questions/23243/how-do-you-capture-serial-com-communications</a></p><p>There is also some development work being undertaken to allow external capturing facilities to be integrated into Wireshark. Look for extcap, and see <a href="http://sharkfest.wireshark.org/sharkfest.13/presentations/NAP-11_Expanding-Wireshark-Beyond-Ethernet-and-Network-Interfaces_Kershaw-Ryan.pdf">here</a> and <a href="http://www.youtube.com/watch?v=Nn84T506SwU">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '14, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36263" class="comments-container"></div><div id="comment-tools-36263" class="comment-tools"></div><div class="clear"></div><div id="comment-36263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

