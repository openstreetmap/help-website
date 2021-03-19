+++
type = "question"
title = "BitTorrent capture"
description = '''does anybody know how wireshark identify p2p traffic? Port number? or payload checking?'''
date = "2011-04-11T12:27:00Z"
lastmod = "2011-04-12T12:25:00Z"
weight = 3449
keywords = [ "capture.bittorrent" ]
aliases = [ "/questions/3449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [BitTorrent capture](/questions/3449/bittorrent-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3449-score" class="post-score" title="current number of votes">0</div><span id="post-3449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>does anybody know how wireshark identify p2p traffic? Port number? or payload checking?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture.bittorrent" rel="tag" title="see questions tagged &#39;capture.bittorrent&#39;">capture.bittorrent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/d63022e61f1359d3e54de6b4a853e67d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LeviVic&#39;s gravatar image" /><p><span>LeviVic</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LeviVic has no accepted answers">0%</span></p></div></div><div id="comments-container-3449" class="comments-container"></div><div id="comment-tools-3449" class="comment-tools"></div><div class="clear"></div><div id="comment-3449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3467"></span>

<div id="answer-container-3467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3467-score" class="post-score" title="current number of votes">2</div><span id="post-3467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The bittorrent dissector registers itself as a heuristic dissector to tcp. The heuristic works by first ensuring that the TCP payload is at least 20 bytes in length, that the first byte is equal to the value of 19 (0x13), and that the 19 bytes following that value are equal to the string, <em>"BitTorrent protocol"</em>. If all of that is true, then the payload is assumed to be bittorrent traffic; otherwise, it's assumed not to be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '11, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3467" class="comments-container"><span id="3468"></span><div id="comment-3468" class="comment"><div id="post-3468-score" class="comment-score"></div><div class="comment-text"><p>Thanks, you are quite right. How about other p2p protocols, dose wireshark has the ability detecting them?</p></div><div id="comment-3468-info" class="comment-info"><span class="comment-age">(12 Apr '11, 12:21)</span> <span class="comment-user userinfo">LeviVic</span></div></div><span id="3469"></span><div id="comment-3469" class="comment"><div id="post-3469-score" class="comment-score"></div><div class="comment-text"><p>Each p2p protocol would have to be checked individually.</p></div><div id="comment-3469-info" class="comment-info"><span class="comment-age">(12 Apr '11, 12:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-3467" class="comment-tools"></div><div class="clear"></div><div id="comment-3467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

