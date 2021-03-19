+++
type = "question"
title = "Display filter with white spaces"
description = '''Hi, I am trying to launch the Wireshark through command line as:  wireshark -r mycapture.pcap -R &quot;frame.time eq Nov 2, 2010 18:49:42.000710000&quot;  Its giving an error:  2&quot; was unexpected in this context.  The filter expression &quot;frame.time == Nov 2, 2010 18:49:42.000710000&quot; isn&#x27;t a valid display filter...'''
date = "2011-06-16T06:02:00Z"
lastmod = "2011-06-16T06:31:00Z"
weight = 4591
keywords = [ "display-filter" ]
aliases = [ "/questions/4591" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display filter with white spaces](/questions/4591/display-filter-with-white-spaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to launch the Wireshark through command line as:</p><blockquote><p>wireshark -r mycapture.pcap -R "frame.time eq Nov 2, 2010 18:49:42.000710000"</p></blockquote><p>Its giving an error:</p><blockquote><p>2" was unexpected in this context.</p></blockquote><p>The filter expression "frame.time == Nov 2, 2010 18:49:42.000710000" isn't a valid display filter.</p><p>It seems like the white space is causing the problem. Any suggestions how to do this?</p><p>Thanks, Puneet</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '11, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/f7eb6de4bbc2a45548b787cd3b1fda72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PuneetNay&#39;s gravatar image" /><p>PuneetNay<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PuneetNay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '11, 11:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4591" class="comments-container"></div><div id="comment-tools-4591" class="comment-tools"></div><div class="clear"></div><div id="comment-4591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4592"></span>

<div id="answer-container-4592" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4592-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:</p><pre><code>wireshark -r mycapture.pcap -R &quot;frame.time eq \&quot;Nov 2, 2010 18:49:42.000710000\&quot;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '11, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4592" class="comments-container"><span id="4609"></span><div id="comment-4609" class="comment"><div id="post-4609-score" class="comment-score"></div><div class="comment-text"><p>It works! Thanks a ton!</p></div><div id="comment-4609-info" class="comment-info"><span class="comment-age">(16 Jun '11, 19:37)</span> PuneetNay</div></div></div><div id="comment-tools-4592" class="comment-tools"></div><div class="clear"></div><div id="comment-4592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

