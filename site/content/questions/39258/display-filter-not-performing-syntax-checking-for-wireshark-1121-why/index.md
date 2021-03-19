+++
type = "question"
title = "Display Filter not performing syntax checking for Wireshark 1.12.1 - Why?"
description = '''I have Wireshare 1.12.1 installed on my Linux Mint 17 box. All is well except that on the main screen in the space for typing in a disply filter, no syntax checking is being performed. The field does not turn red when an incorrect filter is typed, and it doesn&#x27;t turn green when a correct one is. Any...'''
date = "2015-01-18T19:46:00Z"
lastmod = "2015-01-19T12:46:00Z"
weight = 39258
keywords = [ "check", "syntax" ]
aliases = [ "/questions/39258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display Filter not performing syntax checking for Wireshark 1.12.1 - Why?](/questions/39258/display-filter-not-performing-syntax-checking-for-wireshark-1121-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39258-score" class="post-score" title="current number of votes">0</div><span id="post-39258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshare 1.12.1 installed on my Linux Mint 17 box. All is well except that on the main screen in the space for typing in a disply filter, no syntax checking is being performed. The field does not turn red when an incorrect filter is typed, and it doesn't turn green when a correct one is.</p><p>Anyone see this happen before with Linux?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span> <span class="post-tag tag-link-syntax" rel="tag" title="see questions tagged &#39;syntax&#39;">syntax</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '15, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/e9b28f3a68d2709d5233cdcc740b2209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iThrive&#39;s gravatar image" /><p><span>iThrive</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iThrive has no accepted answers">0%</span></p></div></div><div id="comments-container-39258" class="comments-container"></div><div id="comment-tools-39258" class="comment-tools"></div><div class="clear"></div><div id="comment-39258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39262"></span>

<div id="answer-container-39262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39262-score" class="post-score" title="current number of votes">2</div><span id="post-39262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think that may have been a bug,is Wireshark built with GTK3? If you can update to the latest 1.12. version I think it's fixed there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-39262" class="comments-container"><span id="39270"></span><div id="comment-39270" class="comment"><div id="post-39270-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, and yes, it was built with with GTK+ 3.10.8. I did however download it from a PPA source as a pre-built package for Linux Mint (.deb based distro). I suspected it was a bug. I take it I will have to build from source then in order to upgrade to 1.12.3 as I don't think the latest version is available a pre-built package for Linux (or at least not Linux Mint).</p></div><div id="comment-39270-info" class="comment-info"><span class="comment-age">(19 Jan '15, 03:44)</span> <span class="comment-user userinfo">iThrive</span></div></div><span id="39294"></span><div id="comment-39294" class="comment"><div id="post-39294-score" class="comment-score"></div><div class="comment-text"><p>Since 1.12.1 is the latest available package for a deb based distro (such as Linux Mint), I had to download the 1.12.3 source. I have built it using GTK3+ fine but nothing changed. It still does not fix the syntax checking issue. I have also tried building with Qt but have run into nothing but issues there (as I'm not very familiar with building from source) so I can't confirm if this is a GTK issue or not.</p><p>Any ideas?</p></div><div id="comment-39294-info" class="comment-info"><span class="comment-age">(19 Jan '15, 12:26)</span> <span class="comment-user userinfo">iThrive</span></div></div><span id="39297"></span><div id="comment-39297" class="comment"><div id="post-39297-score" class="comment-score"></div><div class="comment-text"><p>It is working fine here with GTK+ 3.12.2 when running on Ubuntu 14.10. The bug Anders was referring to (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8598)">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8598)</a> is already merged in 1.12.X releases.</p></div><div id="comment-39297-info" class="comment-info"><span class="comment-age">(19 Jan '15, 12:46)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-39262" class="comment-tools"></div><div class="clear"></div><div id="comment-39262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

