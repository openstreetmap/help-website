+++
type = "question"
title = "How to decrypt the ppp protocol data content?"
description = '''One of our applications needs to connect to VPN connection and run it. When I captured traffic, I saw transaction of this program under PPP protocol, but content of transmission is compressed or encrypted. How I can see content of it? This is a screenshot of it...'''
date = "2015-02-01T01:35:00Z"
lastmod = "2015-02-01T09:46:00Z"
weight = 39533
keywords = [ "ppp", "encryption", "vpn" ]
aliases = [ "/questions/39533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt the ppp protocol data content?](/questions/39533/how-to-decrypt-the-ppp-protocol-data-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39533-score" class="post-score" title="current number of votes">0</div><span id="post-39533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of our applications needs to connect to VPN connection and run it. When I captured traffic, I saw transaction of this program under PPP protocol, but content of transmission is compressed or encrypted. How I can see content of it? This is a screenshot of it...<img src="http://cld.persiangig.com/preview/ReTQ4UbGH1/wireshar-captured.jpg" alt="Wireshark captured of ppp transaction" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ppp" rel="tag" title="see questions tagged &#39;ppp&#39;">ppp</span> <span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '15, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/fdc2e704d4f1496444a471e3dadcba7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beizavi2020&#39;s gravatar image" /><p><span>beizavi2020</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beizavi2020 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Feb '15, 09:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-39533" class="comments-container"></div><div id="comment-tools-39533" class="comment-tools"></div><div class="clear"></div><div id="comment-39533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39535"></span>

<div id="answer-container-39535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39535-score" class="post-score" title="current number of votes">0</div><span id="post-39535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dissection of PPP compressed data is <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ppp.c;h=5a108a021c64933a723f5d22c61c12364e7d37d1;hb=HEAD#l4285">not yet implemented</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '15, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-39535" class="comments-container"></div><div id="comment-tools-39535" class="comment-tools"></div><div class="clear"></div><div id="comment-39535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

