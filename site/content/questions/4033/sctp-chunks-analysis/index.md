+++
type = "question"
title = "SCTP chunks analysis"
description = '''Hi, I have a problem with analyzing SCTP traffic with many chunks in one SCTP packet - for example in one SCTP packet I have chunks with BSSAP RANAP GSM MAP and ISUP. When I select display filter BSSAP I see all SCTP packets which contains BSSAP packets - but to see for example call flow on BSSAP tr...'''
date = "2011-05-11T06:20:00Z"
lastmod = "2011-05-11T09:37:00Z"
weight = 4033
keywords = [ "sctp", "bssap" ]
aliases = [ "/questions/4033" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SCTP chunks analysis](/questions/4033/sctp-chunks-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4033-score" class="post-score" title="current number of votes">0</div><span id="post-4033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a problem with analyzing SCTP traffic with many chunks in one SCTP packet - for example in one SCTP packet I have chunks with BSSAP RANAP GSM MAP and ISUP. When I select display filter BSSAP I see all SCTP packets which contains BSSAP packets - but to see for example call flow on BSSAP transaction it is impossible because each SCTP packets contains more chunks with BSSAP data.</p><p>Is there any possibility to enable functionality that allows me to clone SCTP packets with only one chunk to see every chunk in new line - now I have few chunks in SCTP packet in one row.</p><p>Best Regards Tom (<span class="__cf_email__" data-cfemail="1f6b70727e6c65317a756c7270716b5f6b7a737a7470726a7176747e7c757e316f73">[email protected]</span>)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-bssap" rel="tag" title="see questions tagged &#39;bssap&#39;">bssap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '11, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/0e6ff404c13ad3036fef82bea619239c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alluryn&#39;s gravatar image" /><p><span>alluryn</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alluryn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '11, 08:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4033" class="comments-container"></div><div id="comment-tools-4033" class="comment-tools"></div><div class="clear"></div><div id="comment-4033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4041"></span>

<div id="answer-container-4041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4041-score" class="post-score" title="current number of votes">0</div><span id="post-4041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, no.</p><p>One solution was discussed <a href="http://www.wireshark.org/lists/wireshark-dev/200606/msg00147.html">many years ago</a>, but it has not been worked on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-4041" class="comments-container"></div><div id="comment-tools-4041" class="comment-tools"></div><div class="clear"></div><div id="comment-4041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

