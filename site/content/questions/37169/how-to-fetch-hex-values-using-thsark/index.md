+++
type = "question"
title = "How to fetch hex values using thsark"
description = '''Would like to fetch the hex values using tshark. Please suggest the options to do so.'''
date = "2014-10-19T22:34:00Z"
lastmod = "2014-10-20T04:52:00Z"
weight = 37169
keywords = [ "hex", "tshark" ]
aliases = [ "/questions/37169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to fetch hex values using thsark](/questions/37169/how-to-fetch-hex-values-using-thsark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37169-score" class="post-score" title="current number of votes">0</div><span id="post-37169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would like to fetch the hex values using tshark. Please suggest the options to do so.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '14, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/fbfa082235ab499c4eb41ae3d8f6fe36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udaya&#39;s gravatar image" /><p><span>udaya</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udaya has one accepted answer">100%</span></p></div></div><div id="comments-container-37169" class="comments-container"><span id="37173"></span><div id="comment-37173" class="comment"><div id="post-37173-score" class="comment-score"></div><div class="comment-text"><p>Hex values of what? The hex dump of the packet?</p></div><div id="comment-37173-info" class="comment-info"><span class="comment-age">(20 Oct '14, 01:23)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37179"></span><div id="comment-37179" class="comment"><div id="post-37179-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Yes</p></div><div id="comment-37179-info" class="comment-info"><span class="comment-age">(20 Oct '14, 03:23)</span> <span class="comment-user userinfo">udaya</span></div></div></div><div id="comment-tools-37169" class="comment-tools"></div><div class="clear"></div><div id="comment-37169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37187"></span>

<div id="answer-container-37187" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37187-score" class="post-score" title="current number of votes">0</div><span id="post-37187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="udaya has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hey Jeff,</p><p>Sorry for the confusion and thanks for the immediate response. I got it. I was exactly searching for this :)</p><p>tshark -r sim_venom_sanity_DEVICE1_PORT1_1_capture.pcap -Vx -R frame.number==2 | sed -n 's/^[0-9a-f]<em>\s((\s[0-9a-f][0-9a-f]){1,16}).</em>$/\1/p'</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/fbfa082235ab499c4eb41ae3d8f6fe36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udaya&#39;s gravatar image" /><p><span>udaya</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udaya has one accepted answer">100%</span></p></div></div><div id="comments-container-37187" class="comments-container"></div><div id="comment-tools-37187" class="comment-tools"></div><div class="clear"></div><div id="comment-37187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37180"></span>

<div id="answer-container-37180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37180-score" class="post-score" title="current number of votes">1</div><span id="post-37180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -x</code> will display a complete hex dump of the packet. Is that what you're looking for?</p><p>Note: I converted your Answer to a comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '14, 05:23</strong> </span></p></div></div><div id="comments-container-37180" class="comments-container"><span id="37181"></span><div id="comment-37181" class="comment"><div id="post-37181-score" class="comment-score"></div><div class="comment-text"><p>No I need only the following values, sorry I could not paste a snap for you e.g. ff ff ff ff ff ff 00 02 3b 10 0f d8 81 00 c0 64<br />
08 00 45 c0 01 34 00 00 00 00 10 11 a0 f8 07 01</p></div><div id="comment-37181-info" class="comment-info"><span class="comment-age">(20 Oct '14, 03:31)</span> <span class="comment-user userinfo">udaya</span></div></div><span id="37184"></span><div id="comment-37184" class="comment"><div id="post-37184-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm not sure what you mean. Do you want to only print the hex dump when it matches that particular pattern?</p><p>Or do you want to only print the hex dump of a certain field? Or of a certain protocol?</p></div><div id="comment-37184-info" class="comment-info"><span class="comment-age">(20 Oct '14, 03:43)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-37180" class="comment-tools"></div><div class="clear"></div><div id="comment-37180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

