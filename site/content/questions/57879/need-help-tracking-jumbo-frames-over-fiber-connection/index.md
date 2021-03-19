+++
type = "question"
title = "Need help tracking Jumbo Frames over fiber connection"
description = '''I am attempting to use Wire Shark to track a Jumbo Frame issue that I am seeing on my network. I do not have Jumbo Frames enabled on any device on my network but I am continuously getting Jumbo Frames (which show up as errors on one of my switch stacks) and I have no idea where they are coming from....'''
date = "2016-12-05T13:41:00Z"
lastmod = "2016-12-12T08:38:00Z"
weight = 57879
keywords = [ "jumbo", "packets" ]
aliases = [ "/questions/57879" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help tracking Jumbo Frames over fiber connection](/questions/57879/need-help-tracking-jumbo-frames-over-fiber-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57879-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to use Wire Shark to track a Jumbo Frame issue that I am seeing on my network. I do not have Jumbo Frames enabled on any device on my network but I am continuously getting Jumbo Frames (which show up as errors on one of my switch stacks) and I have no idea where they are coming from. I have connected the PC that I have Wire Shark on to the receiving switch stack but the switch is dropping the jumbo packets as errors so I do not see them. I have connected the PC to the switch stack that the packets would be the sending switch stack and I still have no idea where these packets are coming from.</p><p>Any advice? Specific configuration on Wire Shark that would help capture it?<br />
</p></div><div id="question-tags" class="tags-container tags">jumbo packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '16, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/76db7f36a9abb3dc7cd6f03dc62518e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cerobinson&#39;s gravatar image" /><p>cerobinson<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cerobinson has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-57879" class="comments-container"></div><div id="comment-tools-57879" class="comment-tools"></div><div class="clear"></div><div id="comment-57879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58022"></span>

<div id="answer-container-58022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to get serious with the network devices detailed statistics, which I assume you already are, too see where the jumbo frame counters add up. Otherwise a network tap to insert into the network link and a beefy capture platform to get the traffic on that fiber link and see what it tells you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58022" class="comments-container"></div><div id="comment-tools-58022" class="comment-tools"></div><div class="clear"></div><div id="comment-58022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

