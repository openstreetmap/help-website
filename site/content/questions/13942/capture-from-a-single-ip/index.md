+++
type = "question"
title = "Capture from a single IP"
description = '''Hi, I&#x27;m new on the Wireshark and, even I have read some manuals, the capture filter doesn&#x27;t seems to work for me. I only want to capture packets to/from a single IP. So, I open Capture -&amp;gt; Capture Filters.. and create a new rule:  name: MyRule string: host 192.168.1.100 But it doesn&#x27;t work, I see ...'''
date = "2012-08-28T11:12:00Z"
lastmod = "2012-08-28T11:15:00Z"
weight = 13942
keywords = [ "capture-filter" ]
aliases = [ "/questions/13942" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture from a single IP](/questions/13942/capture-from-a-single-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13942-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new on the Wireshark and, even I have read some manuals, the capture filter doesn't seems to work for me. I only want to capture packets to/from a single IP. So, I open Capture -&gt; Capture Filters.. and create a new rule:</p><p><strong>name:</strong> <em>MyRule</em></p><p><strong>string:</strong> <em>host 192.168.1.100</em></p><p>But it doesn't work, I see (and Wireshark captures) packets from every host on the LAN. I've tryed to clear all the other rules and have only my rule, but it still capturing everything.</p><p>I assume that I'm doing something wrong, but I don't know what it is and I need some help.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/13eca5c6b45cdcc3e591e28bdc05dd15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A_Perez&#39;s gravatar image" /><p>A_Perez<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A_Perez has no accepted answers">0%</span></p></div></div><div id="comments-container-13942" class="comments-container"></div><div id="comment-tools-13942" class="comment-tools"></div><div class="clear"></div><div id="comment-13942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13944"></span>

<div id="answer-container-13944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13944-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So, I open Capture -&gt; Capture Filters.. and create a new rule:</p></blockquote><p>By doing that, you only <strong>defined</strong> a capture filter, but you have to <strong>apply</strong> it during capturing!</p><p>Wireshark 1.6.x:</p><blockquote><p><code>Capture -&gt; Options -&gt; Capture Filter:</code><br />
</p></blockquote><p>Wireshark 1.8.x:</p><blockquote><p><code>Capture -&gt; Options</code><br />
</p></blockquote><p>Then double-click on the desired interface and select the filter</p><blockquote><p><code>Capture filter:</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '12, 11:18</p></div></div><div id="comments-container-13944" class="comments-container"><span id="13945"></span><div id="comment-13945" class="comment"><div id="post-13945-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt.</p><p>That was the problem, I needed to apply...</p><p>Thanks you very much.</p></div><div id="comment-13945-info" class="comment-info"><span class="comment-age">(28 Aug '12, 12:06)</span> A_Perez</div></div></div><div id="comment-tools-13944" class="comment-tools"></div><div class="clear"></div><div id="comment-13944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

