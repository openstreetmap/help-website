+++
type = "question"
title = "Why is -t option not working in tshark script?"
description = '''I want to create .txt file contains frame.time, ip addresses, tcp ports and also the frame length. for frame time I want to save it in epoch format, but -t option didn&#x27;t work! tshark -r capture/flows/${nbase}/mainflow/${base}_$id.pcapng -T &quot;text&quot; -t &quot;e&quot; -T fields -E separator=&quot;/t&quot; -e &quot;frame.time&quot; -e...'''
date = "2016-09-04T00:41:00Z"
lastmod = "2016-09-04T01:10:00Z"
weight = 55326
keywords = [ "tshark" ]
aliases = [ "/questions/55326" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why is -t option not working in tshark script?](/questions/55326/why-is-t-option-not-working-in-tshark-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to create .txt file contains frame.time, ip addresses, tcp ports and also the frame length. for frame time I want to save it in epoch format, but -t option didn't work!</p><pre><code>tshark -r capture/flows/${nbase}/mainflow/${base}_$id.pcapng -T &quot;text&quot; -t &quot;e&quot; -T fields -E separator=&quot;/t&quot; -e &quot;frame.time&quot; -e &quot;ip.src&quot; -e &quot;tcp.srcport&quot; -e &quot;ip.dst&quot; -e &quot;tcp.dstport&quot; -e &quot;frame.len&quot; &gt; capture/flows/${nbase}/filtered/${base}_$id.txt</code></pre><p>here is output:</p><pre><code>Aug  9, 2016 16:58:57.657202000 125.108.4.179   443 10.42.0.16  46253   155
Aug  9, 2016 16:58:57.768886000 10.42.0.16  46253   125.108.4.179   443 155</code></pre><p>what's wrong with this option?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '16, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p>Zahra<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '16, 01:11</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55326" class="comments-container"></div><div id="comment-tools-55326" class="comment-tools"></div><div class="clear"></div><div id="comment-55326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55328"></span>

<div id="answer-container-55328" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55328-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The manual says that the purpose of the <code>-t</code> option is to "set the format of the packet timestamp printed <strong>in summary lines</strong>." But you use <code>-T</code> and print the <code>frame.time</code> <strong>field</strong>, so <code>-t</code> does not affect the format. So use <code>-e frame.time_epoch</code> instead of <code>-e frame.time</code> to reach your goal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '16, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55328" class="comments-container"></div><div id="comment-tools-55328" class="comment-tools"></div><div class="clear"></div><div id="comment-55328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

