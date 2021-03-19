+++
type = "question"
title = "How do I force packet coloring rules?"
description = '''I&#x27;m working on the FAST protocol dissector for wireshark, and I want to make it so that packets containing errors are colored red for the users. I know how to do it by modifying my coloring rules filter, but is there a way to force this change on any user using my plugin (so that they don&#x27;t have to ...'''
date = "2011-04-05T11:34:00Z"
lastmod = "2011-04-06T15:39:00Z"
weight = 3351
keywords = [ "coloring", "fast", "developer" ]
aliases = [ "/questions/3351" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I force packet coloring rules?](/questions/3351/how-do-i-force-packet-coloring-rules)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3351-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on the FAST protocol dissector for wireshark, and I want to make it so that packets containing errors are colored red for the users. I know how to do it by modifying my coloring rules filter, but is there a way to force this change on any user using my plugin (so that they don't have to manually alter the coloring rules)?</p></div><div id="question-tags" class="tags-container tags">coloring fast developer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '11, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/09314f8bf5cabd0a478d9b4d23c8c9f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="messybricks&#39;s gravatar image" /><p>messybricks<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="messybricks has no accepted answers">0%</span></p></div></div><div id="comments-container-3351" class="comments-container"></div><div id="comment-tools-3351" class="comment-tools"></div><div class="clear"></div><div id="comment-3351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3363"></span>

<div id="answer-container-3363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3363-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Add expert items to the errors. That makes them show up in the expert dialog and color coded in the packet list / details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3363" class="comments-container"></div><div id="comment-tools-3363" class="comment-tools"></div><div class="clear"></div><div id="comment-3363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3382"></span>

<div id="answer-container-3382" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm trying to implement this, and I'm making a simple function call like this:</p><pre><code>  expert_add_info_format(pinfo, 
                    NULL,
                    PI_PROTOCOL,
                    PI_ERROR,
                    &quot;ERROR 123&quot;);</code></pre><p>However, the behavior is not what I would expect. The packet color does not change, and in the Expert Info column, all I see is: ?8388608?</p><p>Also, when I go to Analyze-&gt;Expert Info, wireshark dies, and I get this error in the terminal:</p><pre><code>**
ERROR:expert_dlg.c:142:expert_dlg_packet: code should not be reached
Aborted</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '11, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/09314f8bf5cabd0a478d9b4d23c8c9f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="messybricks&#39;s gravatar image" /><p>messybricks<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="messybricks has no accepted answers">0%</span></p></div></div><div id="comments-container-3382" class="comments-container"></div><div id="comment-tools-3382" class="comment-tools"></div><div class="clear"></div><div id="comment-3382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

