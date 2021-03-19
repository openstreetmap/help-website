+++
type = "question"
title = "Tshark to produce conversation list and payload length for conversation"
description = '''Hi Experts,  Is there any way to use tshark to produce the conversation list and the payload length for the conversations?  When I click on Statistics-&amp;gt; Conversations, I can&#x27;t find the payload length (minus headers). I can find payload length by specifying a field in tshark.  My question is can I...'''
date = "2016-09-19T20:59:00Z"
lastmod = "2016-09-19T20:59:00Z"
weight = 55673
keywords = [ "conversation", "statistics" ]
aliases = [ "/questions/55673" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark to produce conversation list and payload length for conversation](/questions/55673/tshark-to-produce-conversation-list-and-payload-length-for-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55673-score" class="post-score" title="current number of votes">0</div><span id="post-55673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>Is there any way to use tshark to produce the conversation list and the payload length for the conversations?</p><p>When I click on Statistics-&gt; Conversations, I can't find the payload length (minus headers). I can find payload length by specifying a field in tshark.</p><p>My question is can I combine tshark to do something like this below:</p><p>tshark -r test.pcap -T fields -e tcp.len -q -z conv, tcp</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '16, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/dce851b25638fdbabdfc55a27f8dbb6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rsharkz&#39;s gravatar image" /><p><span>Rsharkz</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rsharkz has no accepted answers">0%</span></p></div></div><div id="comments-container-55673" class="comments-container"></div><div id="comment-tools-55673" class="comment-tools"></div><div class="clear"></div><div id="comment-55673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

