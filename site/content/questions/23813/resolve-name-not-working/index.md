+++
type = "question"
title = "resolve name not working"
description = '''When I right-click on a packet or IP address and choose resolve name nothing happens. The only way I can get DNS resolution in my trace is by going to view &amp;gt; name resolution &amp;gt; enable for network layer. When I do that I get name resolution for the entice trace, not just a selected packet/IP. I&#x27;...'''
date = "2013-08-15T16:59:00Z"
lastmod = "2013-08-16T11:42:00Z"
weight = 23813
keywords = [ "name-resolving", "dns" ]
aliases = [ "/questions/23813" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [resolve name not working](/questions/23813/resolve-name-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23813-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I right-click on a packet or IP address and choose resolve name nothing happens. The only way I can get DNS resolution in my trace is by going to view &gt; name resolution &gt; enable for network layer.</p><p>When I do that I get name resolution for the entice trace, not just a selected packet/IP.</p><p>I'm running Windows version 1.10.1</p></div><div id="question-tags" class="tags-container tags">name-resolving dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '13, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/9501a0a9cba9c6ae399345ab0baf8b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsuida&#39;s gravatar image" /><p>dsuida<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsuida has no accepted answers">0%</span></p></div></div><div id="comments-container-23813" class="comments-container"></div><div id="comment-tools-23813" class="comment-tools"></div><div class="clear"></div><div id="comment-23813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23821"></span>

<div id="answer-container-23821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23821-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where are you right-clicking? The IP addresses displayed in the Packet List will not change. Expand the Internet Protocol header in the Packet Details pane to the resolved names.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '13, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-23821" class="comments-container"><span id="23829"></span><div id="comment-23829" class="comment"><div id="post-23829-score" class="comment-score"></div><div class="comment-text"><p>See <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayPopUpSection.html#ChWorkPacketDetailsPanePopUpMenuSection">section 6.2.3</a> of the User Guide. (Search for "Resolve Name")</p></div><div id="comment-23829-info" class="comment-info"><span class="comment-age">(16 Aug '13, 11:44)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-23821" class="comment-tools"></div><div class="clear"></div><div id="comment-23821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23828"></span>

<div id="answer-container-23828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23828-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a bug to me. I suggest <a href="https://bugs.wireshark.org/bugzilla/">filing a bug report</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '13, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23828" class="comments-container"></div><div id="comment-tools-23828" class="comment-tools"></div><div class="clear"></div><div id="comment-23828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

