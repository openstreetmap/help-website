+++
type = "question"
title = "802.11 PPI headers so bad on OS X"
description = '''On OS X, why are Wireshark 802.11 PPI headers so bad compared to Radiotap? PPI is known to be more detailed on Windows, specifically for 802.11n, but there&#x27;s practically no info for PPI on OS X. Does this difference between the two OS come from? The network card driver, libpcap or something else?'''
date = "2015-09-17T12:21:00Z"
lastmod = "2015-09-17T13:47:00Z"
weight = 45927
keywords = [ "radiotap", "ppi", "802.11", "radioheader" ]
aliases = [ "/questions/45927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 PPI headers so bad on OS X](/questions/45927/80211-ppi-headers-so-bad-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45927-score" class="post-score" title="current number of votes">0</div><span id="post-45927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On OS X, why are Wireshark 802.11 PPI headers so bad compared to Radiotap?</p><p>PPI is known to be more detailed on Windows, specifically for 802.11n, but there's practically no info for PPI on OS X.</p><p>Does this difference between the two OS come from? The network card driver, libpcap or something else?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span> <span class="post-tag tag-link-ppi" rel="tag" title="see questions tagged &#39;ppi&#39;">ppi</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-radioheader" rel="tag" title="see questions tagged &#39;radioheader&#39;">radioheader</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-45927" class="comments-container"></div><div id="comment-tools-45927" class="comment-tools"></div><div class="clear"></div><div id="comment-45927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45933"></span>

<div id="answer-container-45933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45933-score" class="post-score" title="current number of votes">1</div><span id="post-45933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>PPI is known to be more detailed on Windows, specifically for 802.11n,</p></blockquote><p>If PPI is more detailed on Windows, that's either a deficiency in the AirPcap firmware or driver or it's a problem with the radiotap specification not specifying headers with enough information. In either case, it needs to be fixed.</p><blockquote><p>Does this difference between the two OS come from the network card driver</p></blockquote><p>Yes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45933" class="comments-container"></div><div id="comment-tools-45933" class="comment-tools"></div><div class="clear"></div><div id="comment-45933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

