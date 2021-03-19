+++
type = "question"
title = "|Newbie| - I just want to set a Filter to google.com!"
description = '''Hi there. I been reading for half an hour now - how to apply a simple filter. and non seems to work.. I want to know which computers in my organization - accessing google.com from there computers.'''
date = "2015-02-12T01:33:00Z"
lastmod = "2015-02-12T01:48:00Z"
weight = 39825
keywords = [ "google.com" ]
aliases = [ "/questions/39825" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [|Newbie| - I just want to set a Filter to google.com!](/questions/39825/newbie-i-just-want-to-set-a-filter-to-googlecom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there. I been reading for half an hour now - how to apply a simple filter. and non seems to work..</p><p>I want to know which computers in my organization - accessing google.com from there computers.</p></div><div id="question-tags" class="tags-container tags">google.com</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '15, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/7b393ff1fc36e62a1012a5d6ae9bb40a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smounche&#39;s gravatar image" /><p>smounche<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smounche has no accepted answers">0%</span></p></div></div><div id="comments-container-39825" class="comments-container"></div><div id="comment-tools-39825" class="comment-tools"></div><div class="clear"></div><div id="comment-39825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39826"></span>

<div id="answer-container-39826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39826-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since the traffic to google is most likely encrypted you won't find HTTP GET requests. But you could filter on DNS packets, e.g. for something like</p><pre><code>dns.qry.name contains &quot;google&quot;.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '15, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '15, 08:42</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39826" class="comments-container"><span id="39835"></span><div id="comment-39835" class="comment"><div id="post-39835-score" class="comment-score"></div><div class="comment-text"><p>Note: this is a display filter and not a capture filter. This means you must first perform the packet capture and then apply the filter.</p></div><div id="comment-39835-info" class="comment-info"><span class="comment-age">(12 Feb '15, 08:56)</span> Amato_C</div></div></div><div id="comment-tools-39826" class="comment-tools"></div><div class="clear"></div><div id="comment-39826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

