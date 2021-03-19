+++
type = "question"
title = "independently build a wireshark plugin. (outside the wireshark source code)"
description = '''Hi, currently, I complete a wireshark plugin which works well in wireshark build environment (wireshark/plugin). However, I am thinking about can I build the plugin outside the wireshark which means I can compile my plugin without the wireshark source code and generate the .o and .la file?? Because ...'''
date = "2011-08-02T15:08:00Z"
lastmod = "2011-08-03T17:33:00Z"
weight = 5408
keywords = [ "plugin" ]
aliases = [ "/questions/5408" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [independently build a wireshark plugin. (outside the wireshark source code)](/questions/5408/independently-build-a-wireshark-plugin-outside-the-wireshark-source-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, currently, I complete a wireshark plugin which works well in wireshark build environment (wireshark/plugin). However, I am thinking about can I build the plugin outside the wireshark which means I can compile my plugin without the wireshark source code and generate the .o and .la file?? Because I want to compile my plugin to binary library file (.o .la) in a machine which may not have wireshark source code but only rpm or sth like that.</p><p>Thanks<br />
</p></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/649a6c1ba91eff5982e125e86dbc760c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xuan&#39;s gravatar image" /><p>xuan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xuan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5408" class="comments-container"></div><div id="comment-tools-5408" class="comment-tools"></div><div class="clear"></div><div id="comment-5408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5437"></span>

<div id="answer-container-5437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5437-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not set up to do such a thing. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1199">Bug 1199</a> provides a (probably long obsolete) patch to support it, but it has never checked in--and in my opinion probably never will be.</p><p>If you want to develop without the source, your best bet would be to transition to a Lua- or Python-based dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5437" class="comments-container"></div><div id="comment-tools-5437" class="comment-tools"></div><div class="clear"></div><div id="comment-5437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5462"></span>

<div id="answer-container-5462" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5462-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>there is a patch for Bug 1199 but it is to generate plugin c code. And the comment mentioned independent build. They never touch it again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/649a6c1ba91eff5982e125e86dbc760c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xuan&#39;s gravatar image" /><p>xuan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xuan has no accepted answers">0%</span></p></div></div><div id="comments-container-5462" class="comments-container"></div><div id="comment-tools-5462" class="comment-tools"></div><div class="clear"></div><div id="comment-5462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

