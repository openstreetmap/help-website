+++
type = "question"
title = "TLS1.2  record length gt 16K  valid?"
description = '''I&#x27;m facing an issue where a ftp transfer hangs sometimes when TLS records are exceeding the 2^14 limit defined in RFC5246 is exceeded. The client=receiver (RHEL64) is reporting a windo_wsize of 0 and not reading the data anymore. So I&#x27;m wondering if this &quot;oversized&quot; TLS record is truly oversized and...'''
date = "2016-11-26T01:12:00Z"
lastmod = "2016-11-26T05:42:00Z"
weight = 57641
keywords = [ "tls", "record", "oversize", "oversized", "size" ]
aliases = [ "/questions/57641" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TLS1.2 record length gt 16K valid?](/questions/57641/tls12-record-length-gt-16k-valid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57641-score" class="post-score" title="current number of votes">1</div><span id="post-57641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm facing an issue where a ftp transfer hangs <em>sometimes</em> when TLS records are exceeding the 2^14 limit defined in RFC5246 is exceeded.<br />
The client=receiver (RHEL64) is reporting a windo_wsize of 0 and not reading the data anymore.<br />
So I'm wondering if this "oversized" TLS record is truly oversized and therefore invalid.<br />
It's not causing trouble all the time and the RFC is somehow confusing (to me )<br />
The trace was taken at th sender with LS enabled. <img src="https://osqa-ask.wireshark.org/upfiles/TLS_oversized.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-record" rel="tag" title="see questions tagged &#39;record&#39;">record</span> <span class="post-tag tag-link-oversize" rel="tag" title="see questions tagged &#39;oversize&#39;">oversize</span> <span class="post-tag tag-link-oversized" rel="tag" title="see questions tagged &#39;oversized&#39;">oversized</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '16, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-57641" class="comments-container"></div><div id="comment-tools-57641" class="comment-tools"></div><div class="clear"></div><div id="comment-57641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57642"></span>

<div id="answer-container-57642" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57642-score" class="post-score" title="current number of votes">1</div><span id="post-57642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The FTP server (or its TLS library) is faulty. <a href="https://tools.ietf.org/html/rfc5246#page-20">RFC 5246 (TLS 1.2), page 20</a> explicitly forbids larger sizes ("MUST"):</p><blockquote><p>The length (in bytes) of the following TLSPlaintext.fragment. The length MUST NOT exceed 2^14.</p></blockquote><p>The client rightfully fails the TLS session with an Alert message since larger values are illegal by the spec.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span> </br></br></p></div></div><div id="comments-container-57642" class="comments-container"><span id="57643"></span><div id="comment-57643" class="comment"><div id="post-57643-score" class="comment-score"></div><div class="comment-text"><p>As this seems to be out in the wild, should we add an Expert Info for this?</p></div><div id="comment-57643-info" class="comment-info"><span class="comment-age">(26 Nov '16, 04:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57644"></span><div id="comment-57644" class="comment"><div id="post-57644-score" class="comment-score">1</div><div class="comment-text"><p>Proposed patch that adds expert info for this: <a href="https://code.wireshark.org/review/18959">https://code.wireshark.org/review/18959</a></p></div><div id="comment-57644-info" class="comment-info"><span class="comment-age">(26 Nov '16, 05:42)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-57642" class="comment-tools"></div><div class="clear"></div><div id="comment-57642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

