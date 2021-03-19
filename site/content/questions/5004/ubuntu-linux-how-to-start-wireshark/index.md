+++
type = "question"
title = "Ubuntu Linux: How to start Wireshark"
description = '''I am newable in both linux and wireshark. In the start page of wireshark, I can&#x27;t see any interface can be found. However, I try to add a new interface, but the error command &quot;The capture session could not be initiated (You don&#x27;t have permission to capture on that device). Please check to make sure ...'''
date = "2011-07-12T19:00:00Z"
lastmod = "2011-07-19T05:20:00Z"
weight = 5004
keywords = [ "ubuntu" ]
aliases = [ "/questions/5004" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Ubuntu Linux: How to start Wireshark](/questions/5004/ubuntu-linux-how-to-start-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5004-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am newable in both linux and wireshark. In the start page of wireshark, I can't see any interface can be found. However, I try to add a new interface, but the error command "The capture session could not be initiated (You don't have permission to capture on that device).</p><p>Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified." is generated. Can anyone tell me how to solve this kind of problem ? What is the cause of this problem ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '11, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/fe8a3bc4475d6efae2425d685552bfcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wade&#39;s gravatar image" /><p>wade<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wade has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '11, 19:28</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-5004" class="comments-container"></div><div id="comment-tools-5004" class="comment-tools"></div><div class="clear"></div><div id="comment-5004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5005"></span>

<div id="answer-container-5005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5005-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should read the Wireshark <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges</a> wiki page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '11, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5005" class="comments-container"></div><div id="comment-tools-5005" class="comment-tools"></div><div class="clear"></div><div id="comment-5005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5118"></span>

<div id="answer-container-5118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it's a wired network then your default interface is probably eth0. Select Capture on the menu bar and all possible interfaces should be displayed, including ip address assigned and packets which are traversing those interfaces. If no interfaces are showing up, then try launcing wireshark with elevated priveleges to see if your interfaces appear. sudo wireshark.</p><p>Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-5118" class="comments-container"></div><div id="comment-tools-5118" class="comment-tools"></div><div class="clear"></div><div id="comment-5118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

