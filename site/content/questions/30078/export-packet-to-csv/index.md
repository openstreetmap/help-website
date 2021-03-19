+++
type = "question"
title = "Export packet to csv"
description = '''Hi, When I try to export packet as csv Wireshark crashes. I haven&#x27;t found information in bug list or I missed it. Is there a bug or it only happend to me ? My revision is 54437.'''
date = "2014-02-21T03:22:00Z"
lastmod = "2016-10-25T07:06:00Z"
weight = 30078
keywords = [ "csv", "export", "packet" ]
aliases = [ "/questions/30078" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export packet to csv](/questions/30078/export-packet-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30078-score" class="post-score" title="current number of votes">0</div><span id="post-30078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I try to export packet as csv Wireshark crashes.</p><p>I haven't found information in bug list or I missed it. Is there a bug or it only happend to me ? My revision is 54437.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '14, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-30078" class="comments-container"><span id="30106"></span><div id="comment-30106" class="comment"><div id="post-30106-score" class="comment-score"></div><div class="comment-text"><p>Can you post the capture file containing the packet(s) that you're trying to export to CSV? If you post it at <a href="http://cloudshark.org/">cloudshark</a>, please provide the URL. Otherwise, you could open a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a> and attach the capture file to the bug report.</p></div><div id="comment-30106-info" class="comment-info"><span class="comment-age">(23 Feb '14, 09:52)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-30078" class="comment-tools"></div><div class="clear"></div><div id="comment-30078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30116"></span>

<div id="answer-container-30116" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30116-score" class="post-score" title="current number of votes">3</div><span id="post-30116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Afrim has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This was fixed in revision 54722. Please upgrade your development build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '14, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-30116" class="comments-container"><span id="30232"></span><div id="comment-30232" class="comment"><div id="post-30232-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I upgraded my build it works fine now.</p></div><div id="comment-30232-info" class="comment-info"><span class="comment-age">(27 Feb '14, 06:26)</span> <span class="comment-user userinfo">Afrim</span></div></div><span id="56645"></span><div id="comment-56645" class="comment"><div id="post-56645-score" class="comment-score"></div><div class="comment-text"><p>Can you tell me the version number of 54722? I can not find which version..</p></div><div id="comment-56645-info" class="comment-info"><span class="comment-age">(25 Oct '16, 05:45)</span> <span class="comment-user userinfo">saniye</span></div></div><span id="56646"></span><div id="comment-56646" class="comment"><div id="post-56646-score" class="comment-score"></div><div class="comment-text"><p>The change is in 1.12 or later. It might also have been backported to 1.10.x but that's harder to check.</p></div><div id="comment-56646-info" class="comment-info"><span class="comment-age">(25 Oct '16, 07:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-30116" class="comment-tools"></div><div class="clear"></div><div id="comment-30116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

