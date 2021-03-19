+++
type = "question"
title = "Static linking dissector with library"
description = '''Hi Is it possible to make dissector without dependence on the dynamic-link libraries (e.g. libwireshark.so.0)? Thank you'''
date = "2016-11-30T03:23:00Z"
lastmod = "2017-01-04T11:36:00Z"
weight = 57726
keywords = [ "libwireshark", "dissector", "linux" ]
aliases = [ "/questions/57726" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Static linking dissector with library](/questions/57726/static-linking-dissector-with-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57726-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Is it possible to make dissector without dependence on the dynamic-link libraries (e.g. libwireshark.so.0)?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">libwireshark dissector linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '16, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/029d7fbaf888936459f60cc4376cf3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BorisBochkarev&#39;s gravatar image" /><p>BorisBochkarev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BorisBochkarev has no accepted answers">0%</span></p></div></div><div id="comments-container-57726" class="comments-container"></div><div id="comment-tools-57726" class="comment-tools"></div><div class="clear"></div><div id="comment-57726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58512"></span>

<div id="answer-container-58512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Oof, I suppose it's possible but you'd have to work out how to do it yourself. Basically you'd be statically linking all of the dynamic libraries into your dissector. (Presumably you're talking about a plugin dissector since a built-in dissector is part of libwireshark.so.)</p><p>Of course one would have to wonder: why would you want to? You'll end up with one giant plugin which wouldn't be loadable by Wireshark or any of its tools (since those will have duplicate symbols for all of the things statically linked into your plugin). Using it in a separate program might be feasible but that program is going to have to know all about libwireshark anyway (that's how the dissector is going to be called) so it wouldn't make sense for that program to not link with libwireshark directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58512" class="comments-container"></div><div id="comment-tools-58512" class="comment-tools"></div><div class="clear"></div><div id="comment-58512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

