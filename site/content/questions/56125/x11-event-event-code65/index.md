+++
type = "question"
title = "X11 event, event code:65"
description = '''Hi I found this in Wireshark around the time of a TP Link WR702N nano router disconnect and have reported it to TP Link. But could you tell me what it means please? Its followed by error codes 108, 60 ,51 61 and 47. Thanks Tim Tim.Hodkinson@siemens.com'''
date = "2016-10-04T03:17:00Z"
lastmod = "2016-10-04T15:55:00Z"
weight = 56125
keywords = [ "x11" ]
aliases = [ "/questions/56125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [X11 event, event code:65](/questions/56125/x11-event-event-code65)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56125-score" class="post-score" title="current number of votes">0</div><span id="post-56125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I found this in Wireshark around the time of a TP Link WR702N nano router disconnect and have reported it to TP Link. But could you tell me what it means please?</p><p>Its followed by error codes 108, 60 ,51 61 and 47. Thanks Tim <span class="__cf_email__" data-cfemail="683c01054620070c0301061b0706281b010d050d061b460b0705">[email protected]</span></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '16, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/1cda802062d42734fb5fab752c5e7f53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim777&#39;s gravatar image" /><p><span>Tim777</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim777 has no accepted answers">0%</span></p></div></div><div id="comments-container-56125" class="comments-container"><span id="56127"></span><div id="comment-56127" class="comment"><div id="post-56127-score" class="comment-score"></div><div class="comment-text"><p>Although it's possible someone who knows the X11 protocol might be reading this, you'll probably be better off asking the question on an X11 support forum.</p><p>There's also the <a href="https://www.x.org/archive/X11R7.5/doc/x11proto/proto.pdf">X11 protocol spec</a> if that helps.</p></div><div id="comment-56127-info" class="comment-info"><span class="comment-age">(04 Oct '16, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56125" class="comment-tools"></div><div class="clear"></div><div id="comment-56125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56147"></span>

<div id="answer-container-56147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56147-score" class="post-score" title="current number of votes">0</div><span id="post-56147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps you're seeing TCP traffic to or from a port in the range 6000-6063 that's <em>not</em> X11 traffic but that happens to be dissected as X11 traffic because Wireshark's X11 dissector registers for TCP ports in that range (because that's a typical use of those ports).</p><p>My guess is that your router <em>doesn't</em> use X11, so, if that traffic is related to the router, it's traffic for some other protocol. We'd have to see the raw binary data to try to guess what it might be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '16, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-56147" class="comments-container"></div><div id="comment-tools-56147" class="comment-tools"></div><div class="clear"></div><div id="comment-56147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

