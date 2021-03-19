+++
type = "question"
title = "Any way to use frame.time_delta_displayed in a filter?"
description = '''I&#x27;m working with a capture file in which a particular conversation suffers from a periodic interruption. I&#x27;d like to be able to use that delay in a display filter, but it just doesn&#x27;t seem to work when I&#x27;m dealing with one conversation among many. I&#x27;ve tried: tcp.stream eq 12 &amp;amp;&amp;amp; frame.time_d...'''
date = "2012-05-07T13:36:00Z"
lastmod = "2012-05-07T14:53:00Z"
weight = 10747
keywords = [ "delay", "packet-display", "display-filter" ]
aliases = [ "/questions/10747" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Any way to use frame.time\_delta\_displayed in a filter?](/questions/10747/any-way-to-use-frametime_delta_displayed-in-a-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10747-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working with a capture file in which a particular conversation suffers from a periodic interruption. I'd like to be able to use that delay in a display filter, but it just doesn't seem to work when I'm dealing with one conversation among many. I've tried:</p><p>tcp.stream eq 12 &amp;&amp; frame.time_delta_displayed &gt; 5.0</p><p>and</p><p>tcp.stream eq 12 &amp;&amp; frame.time_delta_displayed == 6.671905000 (from Copy -&gt; as Filter in Details)</p><p>but both yield empty results. Now, I can save that conversation to a separate file and then use:</p><p>frame.time_delta &gt; 5.0</p><p>so my immediate need has been met. Is there any other filter that would select such packets WITHOUT the need to isolate the conversation in a separate file?</p></div><div id="question-tags" class="tags-container tags">delay packet-display display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-10747" class="comments-container"></div><div id="comment-tools-10747" class="comment-tools"></div><div class="clear"></div><div id="comment-10747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10750"></span>

<div id="answer-container-10750" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10750-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can enable TCP conversation timestamps (go to the TCP protocol preferences) and then use:</p><pre><code>&quot;tcp.time_delta &gt; 5.0&quot;</code></pre><p>(no need to select one particular TCP stream, unless you are interested in one particular stream of course).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '12, 14:54</p></div></div><div id="comments-container-10750" class="comments-container"><span id="10781"></span><div id="comment-10781" class="comment"><div id="post-10781-score" class="comment-score"></div><div class="comment-text"><p>Perfect - many thanks!</p></div><div id="comment-10781-info" class="comment-info"><span class="comment-age">(08 May '12, 07:16)</span> wesmorgan1</div></div></div><div id="comment-tools-10750" class="comment-tools"></div><div class="clear"></div><div id="comment-10750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

