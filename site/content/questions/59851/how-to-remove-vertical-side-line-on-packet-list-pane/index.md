+++
type = "question"
title = "how to remove vertical side line on packet list pane?"
description = ''' i could not find anything in preferences about it, what purpose does it serve? thanks'''
date = "2017-03-04T13:09:00Z"
lastmod = "2017-03-04T13:34:00Z"
weight = 59851
keywords = [ "packetlist", "line", "sideline", "side", "gutter" ]
aliases = [ "/questions/59851" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to remove vertical side line on packet list pane?](/questions/59851/how-to-remove-vertical-side-line-on-packet-list-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59851-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_1.png" alt="alt text" /></p><p>i could not find anything in preferences about it,</p><p>what purpose does it serve?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">packetlist line sideline side gutter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '17, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/3510a895f51727a474bbafc643b65d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A_Bones&#39;s gravatar image" /><p>A_Bones<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A_Bones has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59851" class="comments-container"></div><div id="comment-tools-59851" class="comment-tools"></div><div class="clear"></div><div id="comment-59851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59852"></span>

<div id="answer-container-59852" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59852-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It shows <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChUsePacketListPaneSection.html">related packets</a>. A solid line means that each packet is in the same conversation as the selected packet. You can disable it by going to <em>Preferences → Advanced</em> and searching for "related".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '17, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-59852" class="comments-container"><span id="59854"></span><div id="comment-59854" class="comment"><div id="post-59854-score" class="comment-score"></div><div class="comment-text"><p>Great! Thank you Mr Gerald! This is amazing because i am new to this and was just watching this common talk session between you and Hansang Bae on youtube, wireshark looks so powerful :)</p></div><div id="comment-59854-info" class="comment-info"><span class="comment-age">(04 Mar '17, 13:37)</span> A_Bones</div></div></div><div id="comment-tools-59852" class="comment-tools"></div><div class="clear"></div><div id="comment-59852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59853"></span>

<div id="answer-container-59853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59853-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This vertical line is for a new feature (well, new with Wireshark 2.0 at least) called <em>"Related Packets"</em>.</p><p>For a more in depth explanation, please refer to the <a href="https://youtu.be/rLfYuO6pdVA?t=19m56s">"Introduction to Wireshark 2.0"</a> w/Gerald Combs and Laura Chappell YouTube Video.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '17, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59853" class="comments-container"><span id="59855"></span><div id="comment-59855" class="comment"><div id="post-59855-score" class="comment-score"></div><div class="comment-text"><p>nice, thank you, i was just looking for tutorial videos and that channel seems full of them</p></div><div id="comment-59855-info" class="comment-info"><span class="comment-age">(04 Mar '17, 13:41)</span> A_Bones</div></div></div><div id="comment-tools-59853" class="comment-tools"></div><div class="clear"></div><div id="comment-59853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

