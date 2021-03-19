+++
type = "question"
title = "wireshark pinfo-&gt;private data field"
description = '''What is the substitute of private_data field in packet_info structure? I checked the old and the new code and figured out that the private_data field is removed. The replacement from the code which i can make out is removing the private_data, but what if we have no option of removing it? I am here t...'''
date = "2017-01-12T01:06:00Z"
lastmod = "2017-01-12T02:07:00Z"
weight = 58688
keywords = [ "private_data", "dissector", "packet_info", "plugins" ]
aliases = [ "/questions/58688" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark pinfo-&gt;private data field](/questions/58688/wireshark-pinfo-private-data-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58688-score" class="post-score" title="current number of votes">0</div><span id="post-58688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the substitute of private_data field in packet_info structure? I checked the old and the new code and figured out that the private_data field is removed. The replacement from the code which i can make out is removing the private_data, but what if we have no option of removing it?</p><p>I am here trying to convert my plugins from old Wireshark version 1.2.10 to latest version.</p><p>Please help me with this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-private_data" rel="tag" title="see questions tagged &#39;private_data&#39;">private_data</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet_info" rel="tag" title="see questions tagged &#39;packet_info&#39;">packet_info</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '17, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/54b13e716c5802540b3b28701372e876?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chirag&#39;s gravatar image" /><p><span>chirag</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chirag has no accepted answers">0%</span></p></div></div><div id="comments-container-58688" class="comments-container"></div><div id="comment-tools-58688" class="comment-tools"></div><div class="clear"></div><div id="comment-58688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58690"></span>

<div id="answer-container-58690" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58690-score" class="post-score" title="current number of votes">2</div><span id="post-58690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chirag has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What kind of data were you storing in pinfo-&gt;private_data field ? Without knowing, here is already a few suggestions.</p><p>If it's data for a sub dissector, use the the data parameter that is now the 4th parameter of the dissector_t structure.</p><p>If it is data used internally in the dissector, you can eventually use the p_add_proto_data() / p_get_proto_data() function</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '17, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58690" class="comments-container"><span id="58691"></span><div id="comment-58691" class="comment"><div id="post-58691-score" class="comment-score"></div><div class="comment-text"><p>Hi pascal, thanks for the answer. yes I used the extra param void *data in place of private_data. In the old code it was used to share the data between the dissector. After understanding the code I was able to replace it. Anyways thanks for the quick answer.</p></div><div id="comment-58691-info" class="comment-info"><span class="comment-age">(12 Jan '17, 01:59)</span> <span class="comment-user userinfo">chirag</span></div></div><span id="58693"></span><div id="comment-58693" class="comment"><div id="post-58693-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-58693-info" class="comment-info"><span class="comment-age">(12 Jan '17, 02:07)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-58690" class="comment-tools"></div><div class="clear"></div><div id="comment-58690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

