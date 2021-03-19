+++
type = "question"
title = "ip.id fields to capture traffic."
description = '''I have two traces one on the server and one of the client; there is no fragmentation involved.In this case is it a good idea to filter using ip.id field capture lost packets.'''
date = "2015-05-12T14:40:00Z"
lastmod = "2015-05-12T20:38:00Z"
weight = 42345
keywords = [ "ip.id" ]
aliases = [ "/questions/42345" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ip.id fields to capture traffic.](/questions/42345/ipid-fields-to-capture-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42345-score" class="post-score" title="current number of votes">0</div><span id="post-42345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two traces one on the server and one of the client; there is no fragmentation involved.In this case is it a good idea to filter using ip.id field capture lost packets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip.id" rel="tag" title="see questions tagged &#39;ip.id&#39;">ip.id</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/9a1a0de12bb57758046b74161b3d746b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravneet&#39;s gravatar image" /><p><span>Ravneet</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravneet has no accepted answers">0%</span></p></div></div><div id="comments-container-42345" class="comments-container"><span id="42346"></span><div id="comment-42346" class="comment"><div id="post-42346-score" class="comment-score"></div><div class="comment-text"><p>Is there a router or firewall involved in this connection?</p></div><div id="comment-42346-info" class="comment-info"><span class="comment-age">(12 May '15, 15:04)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="42348"></span><div id="comment-42348" class="comment"><div id="post-42348-score" class="comment-score"></div><div class="comment-text"><p>yes there is a firewall involved; actually its an ipsec tunnel between the two.</p></div><div id="comment-42348-info" class="comment-info"><span class="comment-age">(12 May '15, 15:35)</span> <span class="comment-user userinfo">Ravneet</span></div></div><span id="42351"></span><div id="comment-42351" class="comment"><div id="post-42351-score" class="comment-score"></div><div class="comment-text"><p>If the original IP header is preserved and not modified (especially the IP ID) then most likely, it could be used to synchronize the traces.</p><p>If not, you can disable the "use relative sequence numbers" in the TCP protocol to temporarily find the related TCP streams, and then go from there.</p></div><div id="comment-42351-info" class="comment-info"><span class="comment-age">(12 May '15, 20:38)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-42345" class="comment-tools"></div><div class="clear"></div><div id="comment-42345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

