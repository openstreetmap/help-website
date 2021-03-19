+++
type = "question"
title = "Decode packet data in EBCDIC..."
description = '''We support IBM System z mainframe and IBM System i (AS/400) systems in our environment. Both these platforms utilize EBCDIC character sets instead of ASCII. I would like to make a feature request to have an option to display the packet data in EBCDIC in addition to the ASCII data that is currently d...'''
date = "2014-08-13T10:46:00Z"
lastmod = "2014-08-13T14:49:00Z"
weight = 35464
keywords = [ "data", "ebcdic", "packet" ]
aliases = [ "/questions/35464" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode packet data in EBCDIC...](/questions/35464/decode-packet-data-in-ebcdic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35464-score" class="post-score" title="current number of votes">0</div><span id="post-35464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We support IBM System z mainframe and IBM System i (AS/400) systems in our environment. Both these platforms utilize EBCDIC character sets instead of ASCII. I would like to make a feature request to have an option to display the packet data in EBCDIC in addition to the ASCII data that is currently displayed in the "Packet Bytes" window. This would enhance the use of Wireshark when troubleshooting application data flows that contain EBCDIC data.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-ebcdic" rel="tag" title="see questions tagged &#39;ebcdic&#39;">ebcdic</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '14, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/81fc7f9c31c615b319e09bc7e4812d4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KenR&#39;s gravatar image" /><p><span>KenR</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KenR has no accepted answers">0%</span></p></div></div><div id="comments-container-35464" class="comments-container"></div><div id="comment-tools-35464" class="comment-tools"></div><div class="clear"></div><div id="comment-35464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35470"></span>

<div id="answer-container-35470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35470-score" class="post-score" title="current number of votes">0</div><span id="post-35470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those platforms use EBCDIC for some protocols (unless they're running Linux :-)); they're unlikely to use EBCDIC in, for example, HTTP.</p><p>For some protocols, Wireshark automatically uses EBCDIC rather than ASCII in the Packet Bytes pane, but there's currently no way to explicitly select that from the user interface.</p><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5298">bug 5298</a>; if you want to further comment on this, sign up for an account on the Wireshark Bugzilla and add comments to that bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35470" class="comments-container"></div><div id="comment-tools-35470" class="comment-tools"></div><div class="clear"></div><div id="comment-35470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

