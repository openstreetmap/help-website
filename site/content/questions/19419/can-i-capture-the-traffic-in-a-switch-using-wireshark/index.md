+++
type = "question"
title = "Can I capture the traffic in a switch using wireshark"
description = '''Hello  i want to use some traffic measurement software to study self similarity of a network. The measurement will be the traffic in the core switch. I know wireshark can capture the traffic in the interface only but not the whole traffic in the switch/router. Does wireshark support SNMP or not? Can...'''
date = "2013-03-12T23:37:00Z"
lastmod = "2013-05-05T08:02:00Z"
weight = 19419
keywords = [ "switch", "snmp" ]
aliases = [ "/questions/19419" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I capture the traffic in a switch using wireshark](/questions/19419/can-i-capture-the-traffic-in-a-switch-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19419-score" class="post-score" title="current number of votes">0</div><span id="post-19419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i want to use some traffic measurement software to study self similarity of a network. The measurement will be the traffic in the core switch. I know wireshark can capture the traffic in the interface only but not the whole traffic in the switch/router. Does wireshark support SNMP or not? Can i capture the traffic in the switch using wire shark. <span class="__cf_email__" data-cfemail="c1aca8afa8aca4a5a281a6aca0a8adefa2aeac">[email protected]</span></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/583b809745fa45690fa8b950c5d28714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashraf&#39;s gravatar image" /><p><span>Ashraf</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashraf has no accepted answers">0%</span></p></div></div><div id="comments-container-19419" class="comments-container"></div><div id="comment-tools-19419" class="comment-tools"></div><div class="clear"></div><div id="comment-19419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19436"></span>

<div id="answer-container-19436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19436-score" class="post-score" title="current number of votes">2</div><span id="post-19436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a network monitoring tool, it is a packet analysis tool. Wireshark can produce some statistics about the traffic in a capture, but this is not the same as all the traffic across a switch.</p><p>Wireshark can dissect snmp packets, but doesn't originate snmp requests, nor collate the results of snmp responses in a fancy graph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19436" class="comments-container"><span id="20960"></span><div id="comment-20960" class="comment"><div id="post-20960-score" class="comment-score"></div><div class="comment-text"><p>thank you for helping me</p></div><div id="comment-20960-info" class="comment-info"><span class="comment-age">(05 May '13, 08:02)</span> <span class="comment-user userinfo">Ashraf</span></div></div></div><div id="comment-tools-19436" class="comment-tools"></div><div class="clear"></div><div id="comment-19436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19441"></span>

<div id="answer-container-19441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19441-score" class="post-score" title="current number of votes">1</div><span id="post-19441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answer to this similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/18789/detecting-bottleneck-devices">http://ask.wireshark.org/questions/18789/detecting-bottleneck-devices</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19441" class="comments-container"><span id="20959"></span><div id="comment-20959" class="comment"><div id="post-20959-score" class="comment-score"></div><div class="comment-text"><p>thank you for helping me out</p></div><div id="comment-20959-info" class="comment-info"><span class="comment-age">(05 May '13, 08:01)</span> <span class="comment-user userinfo">Ashraf</span></div></div></div><div id="comment-tools-19441" class="comment-tools"></div><div class="clear"></div><div id="comment-19441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

