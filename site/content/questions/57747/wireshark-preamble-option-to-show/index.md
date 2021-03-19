+++
type = "question"
title = "Wireshark preamble option to show?"
description = '''Hello, I&#x27;m using wireshark to look at the data i&#x27;m capturing i&#x27;m using a hilscher netANALYZER to capture some data on the wires. With this netAnalyzer there is a transparent mode (captures the preamble aswell) is it possible to make wireshark show the preamble if it is captured or does wireshark not...'''
date = "2016-12-01T01:14:00Z"
lastmod = "2016-12-01T13:52:00Z"
weight = 57747
keywords = [ "wiresharkpreamble" ]
aliases = [ "/questions/57747" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark preamble option to show?](/questions/57747/wireshark-preamble-option-to-show)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57747-score" class="post-score" title="current number of votes">0</div><span id="post-57747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using wireshark to look at the data i'm capturing i'm using a hilscher netANALYZER to capture some data on the wires. With this netAnalyzer there is a transparent mode (captures the preamble aswell) is it possible to make wireshark show the preamble if it is captured or does wireshark not support the preamble at all? I googled a bit myself and it does not seem possible or am I wrong?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wiresharkpreamble" rel="tag" title="see questions tagged &#39;wiresharkpreamble&#39;">wiresharkpreamble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '16, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/fbe95a60cae1c2cdf4e2d421f259999e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DemoLux&#39;s gravatar image" /><p><span>DemoLux</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DemoLux has no accepted answers">0%</span></p></div></div><div id="comments-container-57747" class="comments-container"></div><div id="comment-tools-57747" class="comment-tools"></div><div class="clear"></div><div id="comment-57747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57754"></span>

<div id="answer-container-57754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57754-score" class="post-score" title="current number of votes">0</div><span id="post-57754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it does. If you go into the menu View|Internals|Supported Protocols you get a window with them all. Scroll (way) down to netANALYZER, where you can see it's supported, and which fields it dissects. This dissection is based on the netANALYZER producing capture files with the correct <a href="http://www.tcpdump.org/linktypes/LINKTYPE_NETANALYZER.html">link layer type</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57754" class="comments-container"></div><div id="comment-tools-57754" class="comment-tools"></div><div class="clear"></div><div id="comment-57754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57770"></span>

<div id="answer-container-57770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57770-score" class="post-score" title="current number of votes">0</div><span id="post-57770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried reading a transparent-mode capture with Wireshark?</p><p>If not, don't assume it doesn't work, just try it. Wireshark <em>does</em>, as Jaap noted, support the link-layer header type format for transparent netANALYZER captures.</p><p>If you <em>have</em> tried it, and it <em>doesn't</em> work, file a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, and attach the capture if possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '16, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57770" class="comments-container"></div><div id="comment-tools-57770" class="comment-tools"></div><div class="clear"></div><div id="comment-57770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

