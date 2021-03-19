+++
type = "question"
title = "Filter expression"
description = '''I am studying the frame timing for a real time control system. For example, frames should go out every 1msec. I could filter the frames that are off-sync by 100usec early to 100usec late using this type expression: ((frame.time + 0.0001) MOD 0.001) &amp;lt; 0.0002 Or with integer math (((frame.time * 10...'''
date = "2011-03-16T20:45:00Z"
lastmod = "2011-03-17T00:44:00Z"
weight = 2882
keywords = [ "filter", "expressions" ]
aliases = [ "/questions/2882" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter expression](/questions/2882/filter-expression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2882-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am studying the frame timing for a real time control system. For example, frames should go out every 1msec. I could filter the frames that are off-sync by 100usec early to 100usec late using this type expression: ((frame.time + 0.0001) MOD 0.001) &lt; 0.0002 Or with integer math (((frame.time * 1000000) + 100) MOD 1000) &lt; 200 Is there a way to enter this type math expression in the filter editors?</p></div><div id="question-tags" class="tags-container tags">filter expressions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '11, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/4b71880d2f277e08870ff0f076f89ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rich%20S&#39;s gravatar image" /><p>Rich S<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rich S has no accepted answers">0%</span></p></div></div><div id="comments-container-2882" class="comments-container"></div><div id="comment-tools-2882" class="comment-tools"></div><div class="clear"></div><div id="comment-2882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2889"></span>

<div id="answer-container-2889" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2889-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Doing math in a display filter is not possible. The closest you can get to what you want is to look at the frame.time_delta. You can then look at the interpacket time with:</p><pre><code>frame.time_delta&lt;0.0002</code></pre><p>However, with a little scripting you can achieve what you want with tshark:</p><pre><code>tshark -r file.cap -T fields -e frame.number -e frame.time_relative -e ... |\
   awk &#39;{if(((($2 * 1000000) + 100) % 1000) &lt; 200) {print}}&#39;</code></pre><p>Which produces the following output (random capture file in my collection):</p><pre><code>1   0.000000000
6   0.249992000
7   0.250094000
14  0.374920000
15  0.375024000
29  0.462919000
33  0.500003000
43  0.750010000
48  0.760090000
50  0.760957000</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2889" class="comments-container"></div><div id="comment-tools-2889" class="comment-tools"></div><div class="clear"></div><div id="comment-2889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

