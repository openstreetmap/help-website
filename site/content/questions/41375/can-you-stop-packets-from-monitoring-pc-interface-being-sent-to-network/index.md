+++
type = "question"
title = "Can you stop packets from monitoring pc interface being sent to network?"
description = '''Is there a setting in Wireshark that stops the interface on the monitoring pc from sending packets back to the network? When I am capturing data I see messages from my interface and the corresponding replies that are not relevant to the capture data. time2innov8'''
date = "2015-04-11T03:01:00Z"
lastmod = "2015-04-11T03:11:00Z"
weight = 41375
keywords = [ "disable" ]
aliases = [ "/questions/41375" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can you stop packets from monitoring pc interface being sent to network?](/questions/41375/can-you-stop-packets-from-monitoring-pc-interface-being-sent-to-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41375-score" class="post-score" title="current number of votes">0</div><span id="post-41375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a setting in Wireshark that stops the interface on the monitoring pc from sending packets back to the network? When I am capturing data I see messages from my interface and the corresponding replies that are not relevant to the capture data.</p><p>time2innov8</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '15, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/aca92b1346da932886779daed561c95f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="time2innov8&#39;s gravatar image" /><p><span>time2innov8</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="time2innov8 has no accepted answers">0%</span></p></div></div><div id="comments-container-41375" class="comments-container"></div><div id="comment-tools-41375" class="comment-tools"></div><div class="clear"></div><div id="comment-41375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41376"></span>

<div id="answer-container-41376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41376-score" class="post-score" title="current number of votes">2</div><span id="post-41376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on the OS, but on Windows, remove all check marks from the protocol bindings on the network capture card settings. That way neither IPv4, IPv6 or any of the other items should be enabled, and the card stays quiet.</p><p>On Linux, just make sure that the capture card has no IP address, which should help forcing it to stay quiet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41376" class="comments-container"></div><div id="comment-tools-41376" class="comment-tools"></div><div class="clear"></div><div id="comment-41376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

