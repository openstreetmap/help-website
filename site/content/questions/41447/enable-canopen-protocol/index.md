+++
type = "question"
title = "Enable CANopen Protocol"
description = '''Tried to log some CanOpen traffic using wireshark, but the traffic is only shown as standard &quot;CAN&quot; traffic.  The same happens when loading the example pcap file from the wiki (https://wiki.wireshark.org/CANopen)  Tried Wireshark 1.12.3 and 1.8.2 (Stock Debian stable) Can&#x27;t force using &quot;Analyze -&amp;gt;...'''
date = "2015-04-15T04:26:00Z"
lastmod = "2015-04-15T04:44:00Z"
weight = 41447
keywords = [ "canopen", "canbus" ]
aliases = [ "/questions/41447" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Enable CANopen Protocol](/questions/41447/enable-canopen-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41447-score" class="post-score" title="current number of votes">0</div><span id="post-41447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tried to log some CanOpen traffic using wireshark, but the traffic is only shown as standard "CAN" traffic. The same happens when loading the example pcap file from the wiki (<a href="https://wiki.wireshark.org/CANopen)">https://wiki.wireshark.org/CANopen)</a></p><ul><li>Tried Wireshark 1.12.3 and 1.8.2 (Stock Debian stable)</li><li>Can't force using "Analyze -&gt; Decode as", this option is greyed out</li></ul><p>Anyone an Idea how to tell wireshark to dissect the data as CANopen on top of CAN instead as "just" CAN?</p><p>Thanks for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-canopen" rel="tag" title="see questions tagged &#39;canopen&#39;">canopen</span> <span class="post-tag tag-link-canbus" rel="tag" title="see questions tagged &#39;canbus&#39;">canbus</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/5cf88ac5f042f908eb3711fd8049f4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin%20Wagner&#39;s gravatar image" /><p><span>Martin Wagner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin Wagner has no accepted answers">0%</span></p></div></div><div id="comments-container-41447" class="comments-container"></div><div id="comment-tools-41447" class="comment-tools"></div><div class="clear"></div><div id="comment-41447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41450"></span>

<div id="answer-container-41450" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41450-score" class="post-score" title="current number of votes">1</div><span id="post-41450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Martin Wagner has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to the protocol preferences for CAN and set the "Next level protocol" to "CANopen protocol".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41450" class="comments-container"></div><div id="comment-tools-41450" class="comment-tools"></div><div class="clear"></div><div id="comment-41450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

