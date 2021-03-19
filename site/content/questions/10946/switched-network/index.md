+++
type = "question"
title = "Switched Network"
description = '''Is it possible to use wireshark over a switched network! I&#x27;m trying to capture data packets being sent to and from a computer other than mine! I tried setting the capture filter like so &#x27;host 10.x.x.x&#x27; (where x is a number) but after using the internet on said machine no packets are captured???'''
date = "2012-05-11T10:09:00Z"
lastmod = "2012-05-11T10:25:00Z"
weight = 10946
keywords = [ "switchednetwork", "wireshark" ]
aliases = [ "/questions/10946" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Switched Network](/questions/10946/switched-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10946-score" class="post-score" title="current number of votes">0</div><span id="post-10946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use wireshark over a switched network! I'm trying to capture data packets being sent to and from a computer other than mine! I tried setting the capture filter like so 'host 10.x.x.x' (where x is a number) but after using the internet on said machine no packets are captured???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switchednetwork" rel="tag" title="see questions tagged &#39;switchednetwork&#39;">switchednetwork</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '12, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/e55c2a06f49a85d36557af37afbc5b72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scorpio&#39;s gravatar image" /><p><span>scorpio</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scorpio has no accepted answers">0%</span></p></div></div><div id="comments-container-10946" class="comments-container"></div><div id="comment-tools-10946" class="comment-tools"></div><div class="clear"></div><div id="comment-10946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10947"></span>

<div id="answer-container-10947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10947-score" class="post-score" title="current number of votes">0</div><span id="post-10947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On a switch you will only see packets to and from your machine (and broadcasts). That's the way a switch works. To sniff in a switched environment, you need to configure a "mirror/span/monitor" port on the switch. However, this is only possible with managed switches.</p><p>Another option would be the use of a simple TAP, like Dualcomm DCGS-2005 or any other cheap switch with port mirroring capabilities (e.g. HP Procurce 1810g-8).</p><p>See also these links in the wiki</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
<code>http://wiki.wireshark.org/SwitchReference</code></p></blockquote><p>Also search this site for "switched network" for numerous solutions for this "problem".</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '12, 10:26</strong> </span></p></div></div><div id="comments-container-10947" class="comments-container"></div><div id="comment-tools-10947" class="comment-tools"></div><div class="clear"></div><div id="comment-10947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

