+++
type = "question"
title = "How to enable RTP dissector preferences in Wireshark v2.0.1"
description = '''Under Preferences &amp;gt; Protocols I don&#x27;t see an option to enable setting the dissector preference &#x27;Try to decode RTP outside conversations&#x27;. I am using Wireshark 2.0.1. What am i missing.'''
date = "2016-01-12T14:26:00Z"
lastmod = "2016-12-07T04:41:00Z"
weight = 49150
keywords = [ "rtp" ]
aliases = [ "/questions/49150" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to enable RTP dissector preferences in Wireshark v2.0.1](/questions/49150/how-to-enable-rtp-dissector-preferences-in-wireshark-v201)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49150-score" class="post-score" title="current number of votes">1</div><span id="post-49150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under Preferences &gt; Protocols I don't see an option to enable setting the dissector preference 'Try to decode RTP outside conversations'. I am using Wireshark 2.0.1. What am i missing.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/b76add3dbdc4eced097a7d2310afd09c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meggig&#39;s gravatar image" /><p><span>meggig</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meggig has no accepted answers">0%</span></p></div></div><div id="comments-container-49150" class="comments-container"><span id="49151"></span><div id="comment-49151" class="comment"><div id="post-49151-score" class="comment-score"></div><div class="comment-text"><p>this issue has been raised before</p></div><div id="comment-49151-info" class="comment-info"><span class="comment-age">(12 Jan '16, 14:54)</span> <span class="comment-user userinfo">meggig</span></div></div><span id="49154"></span><div id="comment-49154" class="comment"><div id="post-49154-score" class="comment-score"></div><div class="comment-text"><p>Could this be a duplicate: <a href="https://ask.wireshark.org/questions/48159/decode-rtp-outside-of-conversations-ws-20">https://ask.wireshark.org/questions/48159/decode-rtp-outside-of-conversations-ws-20</a></p></div><div id="comment-49154-info" class="comment-info"><span class="comment-age">(12 Jan '16, 15:15)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-49150" class="comment-tools"></div><div class="clear"></div><div id="comment-49150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49153"></span>

<div id="answer-container-49153" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49153-score" class="post-score" title="current number of votes">2</div><span id="post-49153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This option was replaced in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=21e5a950ade6a20260b63b5f5c055c52ac07b599">v1.99.8rc0-454-g21e5a95</a> by new <code>rtp_udp</code> and <code>rtp_stun</code> protocols. You can enable these at <em>Analyze</em> -&gt; <em>Enabled Protocols</em>. Then search for <code>rtp</code> and check these options.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot_5DejVpO.png" alt="screenshot of Wireshark - Enabled Protocols" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></img></div></div><div id="comments-container-49153" class="comments-container"><span id="49388"></span><div id="comment-49388" class="comment"><div id="post-49388-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-49388-info" class="comment-info"><span class="comment-age">(19 Jan '16, 11:26)</span> <span class="comment-user userinfo">meggig</span></div></div><span id="57928"></span><div id="comment-57928" class="comment"><div id="post-57928-score" class="comment-score"></div><div class="comment-text"><p>Lekensteyn: can you tell me how to enable "rtp_udp" in tshark? Something like "-o rtp_udp.enable:True"?</p></div><div id="comment-57928-info" class="comment-info"><span class="comment-age">(07 Dec '16, 03:31)</span> <span class="comment-user userinfo">oposum</span></div></div><span id="57930"></span><div id="comment-57930" class="comment"><div id="post-57930-score" class="comment-score">1</div><div class="comment-text"><p><span>@oposum</span> Try <code>tshark --enable-heuristic rtp_udp</code> (see <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>man tshark</code></a>).</p></div><div id="comment-57930-info" class="comment-info"><span class="comment-age">(07 Dec '16, 04:41)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-49153" class="comment-tools"></div><div class="clear"></div><div id="comment-49153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

