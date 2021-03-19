+++
type = "question"
title = "How to interpret signal strength"
description = '''Hi, I use Google for hours but I do not find a satisfying answer how to interpret the captured signal strength, given by the radiotap header. For instance Wireshark shows me a SSI Signal of -52 dBm and I want to convert it to a linear representation/unit. For me, a sensible unit would be the signal ...'''
date = "2011-12-26T15:51:00Z"
lastmod = "2011-12-27T02:45:00Z"
weight = 8136
keywords = [ "localisation", "signal", "strength" ]
aliases = [ "/questions/8136" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to interpret signal strength](/questions/8136/how-to-interpret-signal-strength)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I use Google for hours but I do not find a satisfying answer how to interpret the captured signal strength, given by the radiotap header. For instance Wireshark shows me a SSI Signal of -52 dBm and I want to convert it to a linear representation/unit. For me, a sensible unit would be the signal power at the antenna in Watt oder mW. Is it possible to convert this -52 dBm to mW?</p><p>Some background information: I implement a WLAN-based localisation and want to estimate the position of APs by combining some reference points and the measured signal strength. With the help of triangulation, this should produce a rogh map of the environment.</p><p>Sebastian</p></div><div id="question-tags" class="tags-container tags">localisation signal strength</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '11, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/02b5d0c0e3aad32f6ad0d537d114bded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EyDu&#39;s gravatar image" /><p>EyDu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EyDu has no accepted answers">0%</span></p></div></div><div id="comments-container-8136" class="comments-container"></div><div id="comment-tools-8136" class="comment-tools"></div><div class="clear"></div><div id="comment-8136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8141"></span>

<div id="answer-container-8141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8141-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If that value comes from a <a href="http://www.radiotap.org/">radiotap</a> header, then the signal-in-dBm is <a href="http://www.radiotap.org/defined-fields/Antenna%20signal">defined by the radiotap specification</a> as "a single signed 8-bit value, which indicates the RF signal power at the antenna, in decibels difference from 1mW", so, as per the formula in <a href="http://en.wikipedia.org/wiki/DBm">the Wikipedia page for dBm</a>, <em>power</em> = 10^((<em>dBm</em>-30)/10), so -52 dBm is 10^((-52-30)/10) W, or 10^-8.2 W, or .0000000063W, or .0000063mW, or 6.3nW.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '11, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8141" class="comments-container"></div><div id="comment-tools-8141" class="comment-tools"></div><div class="clear"></div><div id="comment-8141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

