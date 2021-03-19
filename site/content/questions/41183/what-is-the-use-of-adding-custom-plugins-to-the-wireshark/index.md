+++
type = "question"
title = "What is the use of adding custom plugins to the wireshark ?"
description = '''Hi all, I would like to know the use of dissector is added as a custom plugins into the wireshark. In example mac-lte protocol is supported by wiresark. But what is the use If I will install mac-lte protocol dissector as a custom plugins. How to install custom plugins into the wireshark in linux sys...'''
date = "2015-04-03T23:26:00Z"
lastmod = "2015-04-04T05:37:00Z"
weight = 41183
keywords = [ "plugin" ]
aliases = [ "/questions/41183" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the use of adding custom plugins to the wireshark ?](/questions/41183/what-is-the-use-of-adding-custom-plugins-to-the-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41183-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I would like to know the use of dissector is added as a custom plugins into the wireshark. In example mac-lte protocol is supported by wiresark. But what is the use If I will install mac-lte protocol dissector as a custom plugins.</p><p>How to install custom plugins into the wireshark in linux system.</p><p>Thanks and regards, Sathish</p></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '15, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/7ba5607f38325cbf87766b918e1d76a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sathish%20kannan&#39;s gravatar image" /><p>Sathish kannan<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sathish kannan has no accepted answers">0%</span></p></div></div><div id="comments-container-41183" class="comments-container"></div><div id="comment-tools-41183" class="comment-tools"></div><div class="clear"></div><div id="comment-41183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41184"></span>

<div id="answer-container-41184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41184-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>custom plugins can be developed in two ways</p><ol><li>using C language</li><li>using LUA script</li></ol><p>If you have developed your custom plugin in C. then you have to make dll of it and then put into "plugin" folder of wireshark directory.If you have developed using lua then just put your lua file in "plugin" folder. it will work.</p><p>By using custom plugin, you can develop your own protocol and you can dissect as per your need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '15, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Apr '15, 07:56</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41184" class="comments-container"></div><div id="comment-tools-41184" class="comment-tools"></div><div class="clear"></div><div id="comment-41184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

