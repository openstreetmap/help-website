+++
type = "question"
title = "How to add delta time I/O graph in wireshark source code ?"
description = '''Hi all. How to add delta time I/O graph in wireshark source code ? and How to add delta time dissector in wireshark source code? please give information. '''
date = "2013-11-01T07:55:00Z"
lastmod = "2013-11-03T16:01:00Z"
weight = 26620
keywords = [ "04176" ]
aliases = [ "/questions/26620" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add delta time I/O graph in wireshark source code ?](/questions/26620/how-to-add-delta-time-io-graph-in-wireshark-source-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26620-score" class="post-score" title="current number of votes">0</div><span id="post-26620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. How to add delta time I/O graph in wireshark source code ? and How to add delta time dissector in wireshark source code? please give information.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-04176" rel="tag" title="see questions tagged &#39;04176&#39;">04176</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '13, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/a2a13e0f03cb135cb3a4054668d3e4fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Emily&#39;s gravatar image" /><p><span>Emily</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Emily has no accepted answers">0%</span></p></div></div><div id="comments-container-26620" class="comments-container"></div><div id="comment-tools-26620" class="comment-tools"></div><div class="clear"></div><div id="comment-26620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26632"></span>

<div id="answer-container-26632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26632-score" class="post-score" title="current number of votes">0</div><span id="post-26632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is already delta time in many places in wireshark. What kind of delta time do you want to need?</p><p>If you want to track request/response delta times for your specific protocol, you need to track the timestamps in conversation data and then add a field &lt;proto&gt;.time to your dissector. Then you can automatically use that within IO graphs.</p><p>You could have a look at the dns dissector to see how it is implemented there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-26632" class="comments-container"><span id="26647"></span><div id="comment-26647" class="comment"><div id="post-26647-score" class="comment-score"></div><div class="comment-text"><p>If you look for the code for the field "frame.time_delta_displayed", have a look at <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-frame.c?revision=52897&amp;view=markup">http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-frame.c?revision=52897&amp;view=markup</a></p></div><div id="comment-26647-info" class="comment-info"><span class="comment-age">(03 Nov '13, 16:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-26632" class="comment-tools"></div><div class="clear"></div><div id="comment-26632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

