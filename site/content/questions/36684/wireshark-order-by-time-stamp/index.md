+++
type = "question"
title = "Wireshark - order by Time Stamp"
description = '''Hi to all,  I am using whireshark wireshark 1.8.10 on centos 6.3 .  I have a pcap trace that packet are not in chronological order. I want to reorder packet chronologically. Mergecap work only with ordered trace. How can I do that? Thanks in advanced,  Diana'''
date = "2014-09-29T02:30:00Z"
lastmod = "2014-09-29T04:21:00Z"
weight = 36684
keywords = [ "timestamp" ]
aliases = [ "/questions/36684" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - order by Time Stamp](/questions/36684/wireshark-order-by-time-stamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36684-score" class="post-score" title="current number of votes">0</div><span id="post-36684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to all,</p><p>I am using whireshark wireshark 1.8.10 on centos 6.3 . I have a pcap trace that packet are not in chronological order. I want to reorder packet chronologically. Mergecap work only with ordered trace. How can I do that?</p><p>Thanks in advanced, Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '14, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-36684" class="comments-container"></div><div id="comment-tools-36684" class="comment-tools"></div><div class="clear"></div><div id="comment-36684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36685"></span>

<div id="answer-container-36685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36685-score" class="post-score" title="current number of votes">0</div><span id="post-36685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean that the absolute time stamps of the frames are not in chronological order you can use "reordercap" to do that. Reordercap should be available in the same directory as Wireshark and mergecap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '14, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36685" class="comments-container"><span id="36687"></span><div id="comment-36687" class="comment"><div id="post-36687-score" class="comment-score"></div><div class="comment-text"><p>I am using version 1.8.7 (windows) and there is no reordercap; can you advice?</p></div><div id="comment-36687-info" class="comment-info"><span class="comment-age">(29 Sep '14, 03:28)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="36688"></span><div id="comment-36688" class="comment"><div id="post-36688-score" class="comment-score"></div><div class="comment-text"><p>My advice would be to upgrade to 1.12.1</p></div><div id="comment-36688-info" class="comment-info"><span class="comment-age">(29 Sep '14, 03:30)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36689"></span><div id="comment-36689" class="comment"><div id="post-36689-score" class="comment-score"></div><div class="comment-text"><p>OK, I will try. Thank you!</p></div><div id="comment-36689-info" class="comment-info"><span class="comment-age">(29 Sep '14, 03:32)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="36690"></span><div id="comment-36690" class="comment"><div id="post-36690-score" class="comment-score"></div><div class="comment-text"><p>If we are using Wireshark on Linux, to which version should we upgrade? We just did the update and the latest version we are using is 1.8.10. Maybe it is available only in developer version? can you advice?</p></div><div id="comment-36690-info" class="comment-info"><span class="comment-age">(29 Sep '14, 03:48)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="36691"></span><div id="comment-36691" class="comment"><div id="post-36691-score" class="comment-score"></div><div class="comment-text"><p>In general it is always a good idea to upgrade to the latest stable version, which is 1.12.1 right now. Depending on your Linux distribution the package management may not have that version yet, so you can either live with the one provided by your distribution, or you try to compile/install the latest stable build manually.</p></div><div id="comment-36691-info" class="comment-info"><span class="comment-age">(29 Sep '14, 03:57)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36692"></span><div id="comment-36692" class="comment not_top_scorer"><div id="post-36692-score" class="comment-score"></div><div class="comment-text"><p>OK, Thank you very much!</p></div><div id="comment-36692-info" class="comment-info"><span class="comment-age">(29 Sep '14, 04:21)</span> <span class="comment-user userinfo">Dianalab9</span></div></div></div><div id="comment-tools-36685" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-36685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

