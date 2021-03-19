+++
type = "question"
title = "Accessing the column data"
description = '''How do I access a column&#x27;s data for a packet from my dissector code?'''
date = "2011-06-28T09:31:00Z"
lastmod = "2011-06-28T11:06:00Z"
weight = 4786
keywords = [ "column", "dissector" ]
aliases = [ "/questions/4786" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Accessing the column data](/questions/4786/accessing-the-column-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I access a column's data for a packet from my dissector code?</p></div><div id="question-tags" class="tags-container tags">column dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '11, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/25b19db92f6c5c1102813db491e41432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tut087&#39;s gravatar image" /><p>tut087<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tut087 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '11, 18:13</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4786" class="comments-container"><span id="4790"></span><div id="comment-4790" class="comment"><div id="post-4790-score" class="comment-score"></div><div class="comment-text"><p>Well, the Protocol and Info column reflect what you've put there, so you access them by remembering what you put there.</p><p>Many of the other columns are generated from data in the packet_info structure; what particular column or columns do you want?</p></div><div id="comment-4790-info" class="comment-info"><span class="comment-age">(28 Jun '11, 10:58)</span> Guy Harris ♦♦</div></div><span id="4793"></span><div id="comment-4793" class="comment"><div id="post-4793-score" class="comment-score"></div><div class="comment-text"><p>I just want the packet number... guess that is there in frame_data. How do I access frame_data?</p></div><div id="comment-4793-info" class="comment-info"><span class="comment-age">(28 Jun '11, 11:02)</span> tut087</div></div></div><div id="comment-tools-4786" class="comment-tools"></div><div class="clear"></div><div id="comment-4786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4795"></span>

<div id="answer-container-4795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4795-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>PINFO_FD_NUM(pinfo)</code></pre><p>or, in older versions of Wireshark that might not have that macro,</p><pre><code>pinfo-&gt;fd-&gt;num</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '11, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4795" class="comments-container"><span id="4796"></span><div id="comment-4796" class="comment"><div id="post-4796-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot.... :)</p></div><div id="comment-4796-info" class="comment-info"><span class="comment-age">(28 Jun '11, 11:13)</span> tut087</div></div></div><div id="comment-tools-4795" class="comment-tools"></div><div class="clear"></div><div id="comment-4795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

