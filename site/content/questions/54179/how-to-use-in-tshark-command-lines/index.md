+++
type = "question"
title = "How to use &quot;;&quot; in tshark command lines?"
description = '''How to deal with the command : tshark -Y &quot;diameter.Session-Id == &quot;pbugw_8.robi.com.bd;2699435848;4206;80502&quot; &quot; The trouble is in &quot;tshark: &quot;;&quot; was unexpected in this context.&quot;'''
date = "2016-07-20T05:09:00Z"
lastmod = "2016-07-20T05:19:00Z"
weight = 54179
keywords = [ "tshark", "semicolon" ]
aliases = [ "/questions/54179" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to use ";" in tshark command lines?](/questions/54179/how-to-use-in-tshark-command-lines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54179-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to deal with the command :</p><p><code>tshark -Y "diameter.Session-Id == "pbugw_8.robi.com.bd;2699435848;4206;80502" "</code></p><p>The trouble is in "tshark: ";" was unexpected in this context."</p></div><div id="question-tags" class="tags-container tags">tshark semicolon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '16, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/853d7093103a60a3b0083b42b705b99e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neil_hao&#39;s gravatar image" /><p>neil_hao<br />
<span class="score" title="26 reputation points">26</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neil_hao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 08:02</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-54179" class="comments-container"></div><div id="comment-tools-54179" class="comment-tools"></div><div class="clear"></div><div id="comment-54179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54181"></span>

<div id="answer-container-54181" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54181-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apply backslashes to escape command line interpretation of special characters, <code>"</code> and <code>;</code></p><p><code>tshark -Y "diameter.Session-Id == \"pbugw_8.robi.com.bd\;2699435848\;4206;80502\" "</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '16, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54181" class="comments-container"><span id="54183"></span><div id="comment-54183" class="comment"><div id="post-54183-score" class="comment-score"></div><div class="comment-text"><p>thanks jaap, it's work well;</p></div><div id="comment-54183-info" class="comment-info"><span class="comment-age">(20 Jul '16, 05:33)</span> neil_hao</div></div></div><div id="comment-tools-54181" class="comment-tools"></div><div class="clear"></div><div id="comment-54181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

