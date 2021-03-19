+++
type = "question"
title = "Updates for Y.1731 - 2015 specification"
description = '''The Y.1731 specification was updated and added some new messages to the current set. The new messages are: 1SL One-way Synthetic Loss measurement BNM Bandwidth Notification Message GNM Generic Notification Message The new specification is at: http://www.itu.int/rec/T-REC-Y.1731/en Does anyone do the...'''
date = "2016-12-08T13:38:00Z"
lastmod = "2016-12-08T13:49:00Z"
weight = 57968
keywords = [ "y.1731", "802.1q", "802.1ag" ]
aliases = [ "/questions/57968" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Updates for Y.1731 - 2015 specification](/questions/57968/updates-for-y1731-2015-specification)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57968-score" class="post-score" title="current number of votes">0</div><span id="post-57968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Y.1731 specification was updated and added some new messages to the current set. The new messages are:</p><p>1SL One-way Synthetic Loss measurement BNM Bandwidth Notification Message GNM Generic Notification Message</p><p>The new specification is at: <a href="http://www.itu.int/rec/T-REC-Y.1731/en">http://www.itu.int/rec/T-REC-Y.1731/en</a></p><p>Does anyone do thee kind of updates (i.e. maintain the y.1731 decode)? Or is this something I need to add myself?</p><p>The FAQs talked about adding new protocols but since this protocol already exist, I was not sure the proper way to proceed to get these new messages added.</p><p>Thanks, Bill Matern NComm, Inc. www.ncomm.com</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-y.1731" rel="tag" title="see questions tagged &#39;y.1731&#39;">y.1731</span> <span class="post-tag tag-link-802.1q" rel="tag" title="see questions tagged &#39;802.1q&#39;">802.1q</span> <span class="post-tag tag-link-802.1ag" rel="tag" title="see questions tagged &#39;802.1ag&#39;">802.1ag</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '16, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/a3cc9e9e61206881cd5a76a179e7340d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Matern&#39;s gravatar image" /><p><span>Bill Matern</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Matern has no accepted answers">0%</span></p></div></div><div id="comments-container-57968" class="comments-container"></div><div id="comment-tools-57968" class="comment-tools"></div><div class="clear"></div><div id="comment-57968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57969"></span>

<div id="answer-container-57969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57969-score" class="post-score" title="current number of votes">0</div><span id="post-57969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Bill,</p><p>as seen in the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=history;f=epan/dissectors/packet-cfm.c;h=52d1019597de69990bbd2c182b23cc155cd3e9f0;hb=refs/heads/master">Wireshark source repository</a>, this dissector has not been updated since a long time and does not have any official maintainer.</p><p>So feel free to either enhance it <a href="https://wiki.wireshark.org/CreatingPatches">by yourself and push the change to our Gerrit review site</a>, or submit <a href="https://bugs.wireshark.org/">an enhancement bug to our bug tracker</a> with a capture containing an example of the new packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '16, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '16, 08:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-57969" class="comments-container"></div><div id="comment-tools-57969" class="comment-tools"></div><div class="clear"></div><div id="comment-57969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

