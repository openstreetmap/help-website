+++
type = "question"
title = "Airopeek and Peekremote are missing"
description = '''I do not have the options available when I navigate to decode as&amp;gt;link or decode as&amp;gt;network. I&#x27;m using Wireshark 1.12.8. Any assistance will be greatly appreciated. Thank you.'''
date = "2015-11-17T10:23:00Z"
lastmod = "2015-11-17T17:35:00Z"
weight = 47674
keywords = [ "and", "peekremote", "airopeek" ]
aliases = [ "/questions/47674" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Airopeek and Peekremote are missing](/questions/47674/airopeek-and-peekremote-are-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47674-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I do not have the options available when I navigate to decode as&gt;link or decode as&gt;network. I'm using Wireshark 1.12.8. Any assistance will be greatly appreciated. Thank you.</p></div><div id="question-tags" class="tags-container tags">and peekremote airopeek</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/871f736acbe24c12f1fad6bf5ebadd5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgennc&#39;s gravatar image" /><p>georgennc<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgennc has no accepted answers">0%</span></p></div></div><div id="comments-container-47674" class="comments-container"><span id="47675"></span><div id="comment-47675" class="comment"><div id="post-47675-score" class="comment-score"></div><div class="comment-text"><p>I downgraded to an earlier version of Wireshark and now I can atleast see airopeek.</p></div><div id="comment-47675-info" class="comment-info"><span class="comment-age">(17 Nov '15, 10:42)</span> georgennc</div></div></div><div id="comment-tools-47674" class="comment-tools"></div><div class="clear"></div><div id="comment-47674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47695"></span>

<div id="answer-container-47695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47695-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol used by AiroPeek and OmniPeek for remote packet capture was called "AIROPEEK" in Wireshark releases through 1.6 and was renamed "PEEKREMOTE" in 1.8, so you won't see "AIROPEEK" in 1.8 or any later release, and you won't see "PEEKREMOTE" in 1.6 or any earlier release.</p><p>That protocol runs on top of a transport-layer protocol, namely UDP, not on top of any link-layer protocol or on top of any network-layer protocol so it's not available, in any Wireshark release, for "Link" or "Network" Decode As, only for "Transport".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47695" class="comments-container"></div><div id="comment-tools-47695" class="comment-tools"></div><div class="clear"></div><div id="comment-47695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

