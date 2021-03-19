+++
type = "question"
title = "Dissecting data from two ports"
description = '''By following the guide for how to write a dissecting plugin for Wireshark I managed to get a working dll that dissects the data I put in, but only one port. All guides I have found has a pre defined source port. But my data comes through two different ports and the data blocks are slightly different...'''
date = "2015-09-08T10:54:00Z"
lastmod = "2015-09-08T12:04:00Z"
weight = 45709
keywords = [ "plugin" ]
aliases = [ "/questions/45709" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissecting data from two ports](/questions/45709/dissecting-data-from-two-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>By following the guide for how to write a dissecting plugin for Wireshark I managed to get a working dll that dissects the data I put in, but only one port. All guides I have found has a pre defined source port.</p><p>But my data comes through two different ports and the data blocks are slightly different depending on which port it comes from. This means that I need to construct different trees with subtrees depending on from which port the data comes from. It would be nice if I could check which port the data comes from before I dissect. Is there a way to do this? A more elegant solution than one dll for each port I wanna check. It would also make it easier if the ports would change in the future or if I want put another data block through a different port in the future.</p><p>A code like: - Check source port - case port 1 ... - case port 2 ...</p><p>Is this possible? Or any other idea how I could solve it?</p></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '15, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/31c0c24dddb3d431d4122fffd672c58a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anchang&#39;s gravatar image" /><p>Anchang<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anchang has no accepted answers">0%</span></p></div></div><div id="comments-container-45709" class="comments-container"></div><div id="comment-tools-45709" class="comment-tools"></div><div class="clear"></div><div id="comment-45709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45710"></span>

<div id="answer-container-45710" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45710-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can get the port number from <code>pinfo-&gt;match_uint</code>. That will contain the port which was used to decide to call your dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '15, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-45710" class="comments-container"><span id="45714"></span><div id="comment-45714" class="comment"><div id="post-45714-score" class="comment-score"></div><div class="comment-text"><p>Ok, so it was that simple. Thank you very much for the fast answer!</p></div><div id="comment-45714-info" class="comment-info"><span class="comment-age">(08 Sep '15, 12:34)</span> Anchang</div></div><span id="45716"></span><div id="comment-45716" class="comment"><div id="post-45716-score" class="comment-score"></div><div class="comment-text"><p>Your welcome. If this answered your question, please be sure to Accept the answer by clicking the little checkbox (that way the question will show up as having an answer--and won't show in the list of unanswered questions).</p></div><div id="comment-45716-info" class="comment-info"><span class="comment-age">(08 Sep '15, 12:48)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-45710" class="comment-tools"></div><div class="clear"></div><div id="comment-45710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

