+++
type = "question"
title = "How wireshark recognize Quic protocol rather than normal udp packet"
description = '''as the title,i don&#x27;t see any flags to show whether it is a Quic or other'''
date = "2015-06-14T23:21:00Z"
lastmod = "2016-10-06T08:00:00Z"
weight = 43163
keywords = [ "quic" ]
aliases = [ "/questions/43163" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How wireshark recognize Quic protocol rather than normal udp packet](/questions/43163/how-wireshark-recognize-quic-protocol-rather-than-normal-udp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43163-score" class="post-score" title="current number of votes">0</div><span id="post-43163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>as the title,i don't see any flags to show whether it is a Quic or other</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-quic" rel="tag" title="see questions tagged &#39;quic&#39;">quic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '15, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/bac8cbee0f3a1748b25438dff604892a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidNorth&#39;s gravatar image" /><p><span>DavidNorth</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidNorth has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '15, 02:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43163" class="comments-container"><span id="43166"></span><div id="comment-43166" class="comment"><div id="post-43166-score" class="comment-score"></div><div class="comment-text"><p>Do you have an example capture with the issue you can share, e.g. via <a href="http://cloudshark.org">Cloudshark</a>, Google Drive, Dropbox, etc.</p></div><div id="comment-43166-info" class="comment-info"><span class="comment-age">(15 Jun '15, 02:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43163" class="comment-tools"></div><div class="clear"></div><div id="comment-43163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43167"></span>

<div id="answer-container-43167" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43167-score" class="post-score" title="current number of votes">2</div><span id="post-43167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DavidNorth has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark recognizes UDP traffic to or from port 80 or 443 as being QUIC traffic. QUIC runs over UDP, so QUIC packets <em>are</em> normal UDP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '15, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43167" class="comments-container"><span id="43198"></span><div id="comment-43198" class="comment"><div id="post-43198-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot .</p></div><div id="comment-43198-info" class="comment-info"><span class="comment-age">(16 Jun '15, 00:15)</span> <span class="comment-user userinfo">DavidNorth</span></div></div><span id="56161"></span><div id="comment-56161" class="comment"><div id="post-56161-score" class="comment-score"></div><div class="comment-text"><p>Do wireshark decide by looking at the port numbers only? or will it validate L7 data too?</p></div><div id="comment-56161-info" class="comment-info"><span class="comment-age">(05 Oct '16, 06:33)</span> <span class="comment-user userinfo">Brijesh Valera</span></div></div><span id="56194"></span><div id="comment-56194" class="comment"><div id="post-56194-score" class="comment-score"></div><div class="comment-text"><p>Looking port number and for some dissector, there is a heuristic (but no for QUIC)</p></div><div id="comment-56194-info" class="comment-info"><span class="comment-age">(06 Oct '16, 08:00)</span> <span class="comment-user userinfo">Alexis La Go...</span></div></div></div><div id="comment-tools-43167" class="comment-tools"></div><div class="clear"></div><div id="comment-43167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

