+++
type = "question"
title = "Adding a Window or Text Popup to Wireshark"
description = '''I would like to add protocol information such as is available in the wiki directly into the Wireshark interface, either via a mouse over text box popup or in a view window. Is there a mechanism to do this? Thanks, Tom'''
date = "2015-01-06T21:05:00Z"
lastmod = "2015-01-07T01:07:00Z"
weight = 38917
keywords = [ "box", "text", "over", "popup", "mouse" ]
aliases = [ "/questions/38917" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding a Window or Text Popup to Wireshark](/questions/38917/adding-a-window-or-text-popup-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38917-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to add protocol information such as is available in the wiki directly into the Wireshark interface, either via a mouse over text box popup or in a view window. Is there a mechanism to do this?</p><p>Thanks, Tom</p></div><div id="question-tags" class="tags-container tags">box text over popup mouse</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '15, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/3cb1526cbdd50d5f59fa202dbd8ff377?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fwammy&#39;s gravatar image" /><p>Fwammy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fwammy has no accepted answers">0%</span></p></div></div><div id="comments-container-38917" class="comments-container"></div><div id="comment-tools-38917" class="comment-tools"></div><div class="clear"></div><div id="comment-38917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38919"></span>

<div id="answer-container-38919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38919-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Something like that was done in ..ui/gtk/proto_help.c but the code was never ported to the newer GTK API but it can perhaps be used as an inspiration. Note that we are moving over to Qt so any GUI code should primary be written for Qt. Porting the old code to new GTK API may have some merrit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-38919" class="comments-container"></div><div id="comment-tools-38919" class="comment-tools"></div><div class="clear"></div><div id="comment-38919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

