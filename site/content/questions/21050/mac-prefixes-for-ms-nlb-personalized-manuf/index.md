+++
type = "question"
title = "MAC prefixes for MS NLB - personalized manuf"
description = '''Hello, I just ran into an issue with wireshark suggesting a machine was talking to a Microsoft NLB when it fact it wasn&#x27;t. The reasion is the manuf file in the global configurtion folder containing following entries: 02-BF-00-00-00-00/16 MS-NLB-VirtServer 02-01-00-00-00-00/16 MS-NLB-PhysServer-01 02...'''
date = "2013-05-08T23:24:00Z"
lastmod = "2013-05-10T12:58:00Z"
weight = 21050
keywords = [ "manuf", "mac", "resolution", "prefix", "oui" ]
aliases = [ "/questions/21050" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MAC prefixes for MS NLB - personalized manuf](/questions/21050/mac-prefixes-for-ms-nlb-personalized-manuf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21050-score" class="post-score" title="current number of votes">0</div><span id="post-21050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I just ran into an issue with wireshark suggesting a machine was talking to a Microsoft NLB when it fact it wasn't. The reasion is the manuf file in the global configurtion folder containing following entries:</p><pre><code>02-BF-00-00-00-00/16 MS-NLB-VirtServer
02-01-00-00-00-00/16 MS-NLB-PhysServer-01
02-02-00-00-00-00/16 MS-NLB-PhysServer-02
...
02-1e-00-00-00-00/16 MS-NLB-PhysServer-30
02-1f-00-00-00-00/16 MS-NLB-PhysServer-31
02-20-00-00-00-00/16 MS-NLB-PhysServer-32</code></pre><p>It took me quite some time and embarassing discussions to figure that one out. So I went to <a href="http://standards.ieee.org/cgi-bin/ouisearch">IEEE OUI search</a> and couldn't find those prefixes assigned here.</p><p>Easy enough for me to comment those out now (and replace it with a new assignement matching this installations names). But then, this goes into global configuration folder and will probably be overridden when I upgrade wireshark.</p><p>Is there a way to create a personalized manuf (not ethers) to assign Names to MAC <strong>prefixes</strong> that will take precedence that I could use for this purpose?</p><p>Help -&gt; About Wireshark -&gt; Folders does not indicate that this is possible...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-manuf" rel="tag" title="see questions tagged &#39;manuf&#39;">manuf</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-prefix" rel="tag" title="see questions tagged &#39;prefix&#39;">prefix</span> <span class="post-tag tag-link-oui" rel="tag" title="see questions tagged &#39;oui&#39;">oui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-21050" class="comments-container"></div><div id="comment-tools-21050" class="comment-tools"></div><div class="clear"></div><div id="comment-21050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21057"></span>

<div id="answer-container-21057" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21057-score" class="post-score" title="current number of votes">1</div><span id="post-21057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These entries come from the "Microsoft Windows 2000 Server Operating System Network Load Balancing Technical Overview White Paper", section "Distribution of Cluster Traffic". Since these addresses are marked 'Locally administered' you will not find them in the IEEE OUI database, you are running into the situation where your locally assigned MAC addresses conflict with the ones Wireshark just happen to know otherwise. Wireshark supports no other mechanism than ethers for this on a personal preferences level.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '13, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-21057" class="comments-container"><span id="21089"></span><div id="comment-21089" class="comment"><div id="post-21089-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer</p></div><div id="comment-21089-info" class="comment-info"><span class="comment-age">(10 May '13, 12:58)</span> <span class="comment-user userinfo">mrEEde2</span></div></div></div><div id="comment-tools-21057" class="comment-tools"></div><div class="clear"></div><div id="comment-21057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

