+++
type = "question"
title = "Displaying UTF-8 in wireshark packet info tree"
description = '''Making a plugin for a protocol that sometimes contains UTF-8 and would like to display the Unicode characters in the packet info. Is it possible?'''
date = "2010-10-25T11:02:00Z"
lastmod = "2010-10-25T19:07:00Z"
weight = 625
keywords = [ "unicode" ]
aliases = [ "/questions/625" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Displaying UTF-8 in wireshark packet info tree](/questions/625/displaying-utf-8-in-wireshark-packet-info-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-625-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Making a plugin for a protocol that sometimes contains UTF-8 and would like to display the Unicode characters in the packet info.</p><p>Is it possible?</p></div><div id="question-tags" class="tags-container tags">unicode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/4d2675634ece1c72f6c5d6b7dedc5426?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DRJTower&#39;s gravatar image" /><p>DRJTower<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DRJTower has no accepted answers">0%</span></p></div></div><div id="comments-container-625" class="comments-container"></div><div id="comment-tools-625" class="comment-tools"></div><div class="clear"></div><div id="comment-625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="643"></span>

<div id="answer-container-643" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-643-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Currently, no; fields of type FT_STRING, FT_STRINGZ, etc. are only displayed as if they were ASCII, with all octets with the 8th bit set displayed as escape sequences. At some point we should add the ability to specify a character encoding for strings, just as, for example, a byte order can be specified for integral values.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-643" class="comments-container"></div><div id="comment-tools-643" class="comment-tools"></div><div class="clear"></div><div id="comment-643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

