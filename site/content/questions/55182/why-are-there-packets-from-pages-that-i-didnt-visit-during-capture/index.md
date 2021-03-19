+++
type = "question"
title = "why are there packets from pages that I didn&#x27;t visit during capture?"
description = '''Hi everyone, I&#x27;m very new to this whole packet analyzing thing and I would really appreciate any help you guys can offer. The other day I started capturing packets on our wifi network and When I looked at the captured packets later, everything seemed normal except for several HTTP requests from (and...'''
date = "2016-08-29T16:54:00Z"
lastmod = "2016-08-30T02:45:00Z"
weight = 55182
keywords = [ "capture", "spoofing", "http", "poisoning", "wireshark" ]
aliases = [ "/questions/55182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why are there packets from pages that I didn't visit during capture?](/questions/55182/why-are-there-packets-from-pages-that-i-didnt-visit-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm very new to this whole packet analyzing thing and I would really appreciate any help you guys can offer.</p><p>The other day I started capturing packets on our wifi network and When I looked at the captured packets later, everything seemed normal except for several HTTP requests from (and to) my computer's IP to a specific website which I didn't visit during the capture. The last time I had visited that website was more than a month before the capture. Moreover, there were several HTTP and TCP packets from different pages on that website, as if someone was browsing through it.</p><p>When I saw these packets I doubled check my browser's history(chrome) and my browser's history confirms that the last visit to anything related to this website was more than a month ago.</p><p>This seems very wired specially that I can't see any other visits to other websites from my chrome's history. Also, this is a very sensitive governmental website.</p><p>I tried to run this filter "arp.duplicate-address-frame" on the capture to see if someone was spoofing my ip or anything like that but no results came up.</p><p>Does anyone know what might be going on here?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">capture spoofing http poisoning wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/794056ff8fae9cf4bec23f98e4ac7636?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="truthWins&#39;s gravatar image" /><p>truthWins<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="truthWins has no accepted answers">0%</span></p></div></div><div id="comments-container-55182" class="comments-container"></div><div id="comment-tools-55182" class="comment-tools"></div><div class="clear"></div><div id="comment-55182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55192"></span>

<div id="answer-container-55192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Browser background processing, most likely. They like to keep their caches/history updated, so that when you revisit them (statistically likely, since you've been there before) they can show you the site/page quicker.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55192" class="comments-container"></div><div id="comment-tools-55192" class="comment-tools"></div><div class="clear"></div><div id="comment-55192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

