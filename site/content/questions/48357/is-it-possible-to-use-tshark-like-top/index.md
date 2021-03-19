+++
type = "question"
title = "Is it possible to use tshark like top ?"
description = '''Is it possible to run tshark in the same way that you would run &#x27;top&#x27; (or any curses-based refreshing status ?) Let&#x27;s say I am looking at signal strength of a local GSM tower with: tshark -Y &#x27;!icmp &amp;amp;&amp;amp; gsmtap&#x27; -i lo -t ad -T fields -e gsmtap.signal_dbm I will see a continuously scrolling outp...'''
date = "2015-12-08T10:19:00Z"
lastmod = "2015-12-08T20:29:00Z"
weight = 48357
keywords = [ "ncurses", "top", "tshark", "curses" ]
aliases = [ "/questions/48357" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to use tshark like top ?](/questions/48357/is-it-possible-to-use-tshark-like-top)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48357-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to run tshark in the same way that you would run 'top' (or any curses-based refreshing status ?)</p><p>Let's say I am looking at signal strength of a local GSM tower with:</p><p>tshark -Y '!icmp &amp;&amp; gsmtap' -i lo -t ad -T fields -e gsmtap.signal_dbm</p><p>I will see a continuously scrolling output of numbers, just scrolling up the terminal. That's what I expect.</p><p>Is it possible to instruct tshark to refresh a single line of output with that number, updating the number as it changes, but not scrolling ... basically like 'top' ?</p><p>If not, are there other tools that would provide this with tshark input ?</p></div><div id="question-tags" class="tags-container tags">ncurses top tshark curses</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '15, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/3948989c3c37b2439d799349175f2211?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wshuser&#39;s gravatar image" /><p>wshuser<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wshuser has no accepted answers">0%</span></p></div></div><div id="comments-container-48357" class="comments-container"></div><div id="comment-tools-48357" class="comment-tools"></div><div class="clear"></div><div id="comment-48357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48360"></span>

<div id="answer-container-48360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48360-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can get tshark to output a single result and exit, you could use the "watch" utility to accomplish this. "watch [-n &lt;refresh seconds&gt;] &lt;command&gt;" is the syntax. &lt;command&gt; may need quoted.</p><p>Starting point:</p><pre><code>watch -n1 &quot;tshark -Y &#39;!icmp &amp;&amp; gsmtap&#39; -i lo -t ad -T fields -e gsmtap.signal_dbm&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '15, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/71acacce7fe27a77d777260d76e4b178?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hextreme&#39;s gravatar image" /><p>Hextreme<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hextreme has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '15, 12:15</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-48360" class="comments-container"></div><div id="comment-tools-48360" class="comment-tools"></div><div class="clear"></div><div id="comment-48360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48370"></span>

<div id="answer-container-48370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48370-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wrote a perl script to do this once. Basically it just ran in a loop by calling tshark with the "-a duration:{seconds}" option on the "-T fields" output, then it would clear the screen and execute "print" statements to push a top-like display to the user plus the tshark output that had just been captured.</p><p>In my case I used the "-z io,stat" output because I wanted to print the averages of various counters within a given time period. As a very short script I didn't think to save it, but it worked nicely for the job.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '15, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-48370" class="comments-container"></div><div id="comment-tools-48370" class="comment-tools"></div><div class="clear"></div><div id="comment-48370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

