+++
type = "question"
title = "assert_not_reached:"
description = '''hello, i&#x27;m working on a project, that uses libwireshark.so while initializing the dissector &quot;init_dissection()&quot; it flashes an error &quot; Dissector bug, protocol Ethernet, in packet 1: tvbuff.c:902: failed assertion &quot;DISSECTOR_ASSERT_NOT_REACHED&quot;  why i am getting this error: possible solutions.?? thank...'''
date = "2012-01-23T04:02:00Z"
lastmod = "2012-01-24T06:32:00Z"
weight = 8557
keywords = [ "dissector", "assertion", "wireshark" ]
aliases = [ "/questions/8557" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [assert\_not\_reached:](/questions/8557/assert_not_reached)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8557-score" class="post-score" title="current number of votes">0</div><span id="post-8557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>i'm working on a project, that uses libwireshark.so while initializing the dissector "init_dissection()" it flashes an</p><p>error " Dissector bug, protocol Ethernet, in packet 1: tvbuff.c:902: failed assertion "DISSECTOR_ASSERT_NOT_REACHED"</p><p>why i am getting this error: possible solutions.??</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-assertion" rel="tag" title="see questions tagged &#39;assertion&#39;">assertion</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8557" class="comments-container"><span id="8561"></span><div id="comment-8561" class="comment"><div id="post-8561-score" class="comment-score">1</div><div class="comment-text"><p>What version of Wireshark are you building from ??</p><p>In any case, you are basically on your own if you are trying to use libwireshark directly. :-)</p><p>At the very least you need to be quite comfortable using a debugger to trace through the code to see why you are getting the error.</p><p>My guess: you've not done some required setup/initialization.</p></div><div id="comment-8561-info" class="comment-info"><span class="comment-age">(23 Jan '12, 06:38)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8575"></span><div id="comment-8575" class="comment"><div id="post-8575-score" class="comment-score"></div><div class="comment-text"><p>thanks!! you are right.. there was some error while initializing the data buffer :)</p></div><div id="comment-8575-info" class="comment-info"><span class="comment-age">(23 Jan '12, 21:31)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="8582"></span><div id="comment-8582" class="comment"><div id="post-8582-score" class="comment-score"></div><div class="comment-text"><p>(Answer converted to a comment in keeping with the format of ask.wireshark.org; See the FAQ).</p></div><div id="comment-8582-info" class="comment-info"><span class="comment-age">(24 Jan '12, 06:32)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-8557" class="comment-tools"></div><div class="clear"></div><div id="comment-8557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

