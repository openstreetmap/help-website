+++
type = "question"
title = "PPP captured but MPPC decompres?"
description = '''I want to go deep to GRE/PPP packets. The PPP Compressed data by MPPC (Microsoft Point-to-Point Compression) which is one of three compress methods under CiscoIOS. The problem is Wireshark just stop at decoding the PPP packets not go any further to decompress the payload of them. Any one who know so...'''
date = "2012-06-04T17:52:00Z"
lastmod = "2012-06-04T18:02:00Z"
weight = 11648
keywords = [ "mppc", "decompress" ]
aliases = [ "/questions/11648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PPP captured but MPPC decompres?](/questions/11648/ppp-captured-but-mppc-decompres)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11648-score" class="post-score" title="current number of votes">0</div><span id="post-11648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to go deep to GRE/PPP packets. The PPP Compressed data by MPPC (Microsoft Point-to-Point Compression) which is one of three compress methods under CiscoIOS. The problem is Wireshark just stop at decoding the PPP packets not go any further to decompress the payload of them. Any one who know some kind of plug-in for Wireshark to do such thing??? Pls, help.</p><p>I know that MPPC based on Lempel-Ziv algorithm. I have some C-code to compress and decompress as well. I don't know how to integrate them into Wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mppc" rel="tag" title="see questions tagged &#39;mppc&#39;">mppc</span> <span class="post-tag tag-link-decompress" rel="tag" title="see questions tagged &#39;decompress&#39;">decompress</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '12, 17:52</strong></p><img src="https://secure.gravatar.com/avatar/d7afdb6ac0124cfc73dba46f772bd78f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tdhung&#39;s gravatar image" /><p><span>tdhung</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tdhung has no accepted answers">0%</span></p></div></div><div id="comments-container-11648" class="comments-container"></div><div id="comment-tools-11648" class="comment-tools"></div><div class="clear"></div><div id="comment-11648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11649"></span>

<div id="answer-container-11649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11649-score" class="post-score" title="current number of votes">0</div><span id="post-11649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would suggest that you file an enhancement <a href="https://bugs.wireshark.org/bugzilla/">bug report</a> for this. Feel free to include your C-code that performs the compression/decompression, but be sure to include a GPLv2 or compatible license with it if you want to share it with the project. I haven't looked too deeply into Wireshark's support for the various compression/decompression routines; perhaps there are already routines available, but it certainly wouldn't hurt if you share what you've got.</p><p>Also, please attach a sample capture file to the bug report so that the compression/decompression can be effectively tested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '12, 18:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11649" class="comments-container"></div><div id="comment-tools-11649" class="comment-tools"></div><div class="clear"></div><div id="comment-11649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

