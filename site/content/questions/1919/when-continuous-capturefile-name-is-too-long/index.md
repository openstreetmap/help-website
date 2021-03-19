+++
type = "question"
title = "when continuous capture,file name is too long"
description = '''I use wireshark in the continuous capture mode, and use multiple files, file name is capture.pcap, the first file name is capture__0000120101226121523.pcap, and then I click &#x27;restart&#x27; button, the new file name is capture000012010122612152300001201012261525.pcap , But I need capture00001__20101226121...'''
date = "2011-01-25T04:20:00Z"
lastmod = "2011-03-21T22:31:00Z"
weight = 1919
keywords = [ "name", "file" ]
aliases = [ "/questions/1919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [when continuous capture,file name is too long](/questions/1919/when-continuous-capturefile-name-is-too-long)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1919-score" class="post-score" title="current number of votes">0</div><span id="post-1919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use wireshark in the continuous capture mode, and use multiple files, file name is <strong>capture.pcap</strong>, the first file name is <strong>capture__00001<strong><em>20101226121523.pcap<strong>, and then I click 'restart' button, the new file name is</strong> capture</em></strong>00001<strong><em>20101226121523</em></strong>00001<strong><em>201012261525.pcap <strong>, But I need</strong> capture</em></strong>00001__20101226121525.pcap</strong>, this is my error or wireshark' BUG or wireshark does not support this operation?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/b8b39dd5a7fa336493da43602f89b228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jackydi&#39;s gravatar image" /><p><span>jackydi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jackydi has no accepted answers">0%</span></p></div></div><div id="comments-container-1919" class="comments-container"><span id="1930"></span><div id="comment-1930" class="comment"><div id="post-1930-score" class="comment-score"></div><div class="comment-text"><p>I just checked this out and I have the same behavior. When restarting a capture to disk capture the file names get messed up. This is something you should enter as a bug.</p></div><div id="comment-1930-info" class="comment-info"><span class="comment-age">(25 Jan '11, 09:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-1919" class="comment-tools"></div><div class="clear"></div><div id="comment-1919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3005"></span>

<div id="answer-container-3005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3005-score" class="post-score" title="current number of votes">0</div><span id="post-3005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known bug, initially reported by Stig Bjørlykke back in 2008. Refer to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2274">bug 2274</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3005" class="comments-container"></div><div id="comment-tools-3005" class="comment-tools"></div><div class="clear"></div><div id="comment-3005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

