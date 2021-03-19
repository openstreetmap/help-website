+++
type = "question"
title = "Disabling discovery of interfaces on startup"
description = '''Is it possible to not discover all the possible interfaces to capture on when starting wireshark? If I have many interfaces connected it can take over a minute for wireshark to start up as it finds all the interfaces connected to the computer. Instead I would like to specify which interface(s) I wou...'''
date = "2016-08-22T15:48:00Z"
lastmod = "2016-08-23T02:50:00Z"
weight = 55056
keywords = [ "interface", "slow", "startup", "disable", "discovery" ]
aliases = [ "/questions/55056" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disabling discovery of interfaces on startup](/questions/55056/disabling-discovery-of-interfaces-on-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55056-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to not discover all the possible interfaces to capture on when starting wireshark? If I have many interfaces connected it can take over a minute for wireshark to start up as it finds all the interfaces connected to the computer. Instead I would like to specify which interface(s) I would like to monitor either in a config file or startup parameter.</p></div><div id="question-tags" class="tags-container tags">interface slow startup disable discovery</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/3dbb7786b10842688aa045287183f0f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saxguy&#39;s gravatar image" /><p>saxguy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saxguy has no accepted answers">0%</span></p></div></div><div id="comments-container-55056" class="comments-container"></div><div id="comment-tools-55056" class="comment-tools"></div><div class="clear"></div><div id="comment-55056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55066"></span>

<div id="answer-container-55066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55066-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is currently not possible. It would require changes in interface handling, User Interface, preference handling and other areas. You can file an <a href="https://bugs.wireshark.org/bugzilla/">enhancement request</a> for someone to implement this.</p><p>Depending on the platform you use, it maybe possible to run Wireshark in a network namespace / VM / Container or whatnot and use its remote capture capabilities. That would limit its exposure to all interfaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55066" class="comments-container"></div><div id="comment-tools-55066" class="comment-tools"></div><div class="clear"></div><div id="comment-55066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

