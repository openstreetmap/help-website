+++
type = "question"
title = "Matches operator doesn&#x27;t work with some hex digits"
description = '''I don&#x27;t know why the matches operator doesn&#x27;t find some hex digits. If I do something like: http matches &quot;&#92;xff&quot; I get no packets. This doesn&#x27;t happen with hex digit which start by a number.  The funny is that If I use contains: http contains &quot;&#92;xff&quot; I get the packet I&#x27;m looking for. The problem is th...'''
date = "2011-11-23T07:53:00Z"
lastmod = "2011-11-23T17:56:00Z"
weight = 7582
keywords = [ "matches", "operator", "contains" ]
aliases = [ "/questions/7582" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Matches operator doesn't work with some hex digits](/questions/7582/matches-operator-doesnt-work-with-some-hex-digits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7582-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I don't know why the matches operator doesn't find some hex digits. If I do something like: <code>http matches "\xff"</code></p><p>I get no packets. This doesn't happen with hex digit which start by a number.</p><p>The funny is that If I use contains: <code>http contains "\xff"</code></p><p>I get the packet I'm looking for.</p><p>The problem is that I need to use matches operator to set some regex in perl like: <code>"http matches "\xff..(\xef|\xff)+"</code></p><p>I'm using Wireshark 1.6.4 Any ideas? Thank you so much</p></div><div id="question-tags" class="tags-container tags">matches operator contains</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '11, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/57c8ddb7ed6ba271696a4631abf6dd9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BorjaMerino&#39;s gravatar image" /><p>BorjaMerino<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BorjaMerino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '11, 12:12</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7582" class="comments-container"></div><div id="comment-tools-7582" class="comment-tools"></div><div class="clear"></div><div id="comment-7582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7590"></span>

<div id="answer-container-7590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7590-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is actually a bug (just <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6613">filed</a>), and unfortunately, I'm not aware of a workaround.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '11, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7590" class="comments-container"></div><div id="comment-tools-7590" class="comment-tools"></div><div class="clear"></div><div id="comment-7590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

