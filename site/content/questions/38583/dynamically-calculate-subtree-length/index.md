+++
type = "question"
title = "Dynamically calculate subtree length"
description = '''Hi all I have a requirement like,  - Calculate the subtree length dynamically. Would like to how this can be achieved. I am using Wireshark 1.10.8 version. One more question: Can i create a subtree with length given as &quot;0&quot; and then can i update the same tree with the actual length after parsing the ...'''
date = "2014-12-15T12:07:00Z"
lastmod = "2014-12-16T06:21:00Z"
weight = 38583
keywords = [ "subtree" ]
aliases = [ "/questions/38583" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dynamically calculate subtree length](/questions/38583/dynamically-calculate-subtree-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38583-score" class="post-score" title="current number of votes">0</div><span id="post-38583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I have a requirement like, - Calculate the subtree length dynamically. Would like to how this can be achieved. I am using Wireshark 1.10.8 version.</p><p>One more question: Can i create a subtree with length given as "0" and then can i update the same tree with the actual length after parsing the data and displaying on Wireshark GUI ?</p><p>Thanks in advance.</p><p>Regards Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subtree" rel="tag" title="see questions tagged &#39;subtree&#39;">subtree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '14, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-38583" class="comments-container"></div><div id="comment-tools-38583" class="comment-tools"></div><div class="clear"></div><div id="comment-38583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38585"></span>

<div id="answer-container-38585" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38585-score" class="post-score" title="current number of votes">3</div><span id="post-38585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kiran Kumar G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can have a look at proto_item_set_len() function so as to set afterwards the size of a given item. Not sure that you can create a subtree with a length of 0 (it might trigger an assertion) so create it with a size of 1 ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38585" class="comments-container"><span id="38586"></span><div id="comment-38586" class="comment"><div id="post-38586-score" class="comment-score"></div><div class="comment-text"><p>Thanks Pascal for the answer, it worked to set the length of the tree after the dissection is completed.</p><p>One more information i would like to know is how to highlight the bytes of the length set using proto_item_set_len() in the hex window pane.</p><p>Thank you.</p></div><div id="comment-38586-info" class="comment-info"><span class="comment-age">(15 Dec '14, 13:18)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="38587"></span><div id="comment-38587" class="comment"><div id="post-38587-score" class="comment-score">1</div><div class="comment-text"><p>Not sure to understand your question. The bytes of the subtree will be automatically highlighted when you select it.</p></div><div id="comment-38587-info" class="comment-info"><span class="comment-age">(15 Dec '14, 13:50)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38588"></span><div id="comment-38588" class="comment"><div id="post-38588-score" class="comment-score"></div><div class="comment-text"><p>I would like to re-iterate the question.</p><p>1 - I have created an item using proto_tree_add_none_format(), here i am passing length = 0, it worked. If i pass -1 or 1 it showed as malformed packet.</p><p>2 - Then, i calculated the length of the tree during the dissection.</p><p>3 - Now, used proto_item_set_len() function to set the length calculated in point 2. Length is getting reflected when i select the subtree but not highlighting the corresponding bytes in the hex window pane.</p></div><div id="comment-38588-info" class="comment-info"><span class="comment-age">(15 Dec '14, 14:04)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="38589"></span><div id="comment-38589" class="comment"><div id="post-38589-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Pascal, your solution worked fine for our requirement. Now, we are able to dynamically calculate the length of the tree and set it after the dissection. We are also able to see the highlighting of the subtree for the length bytes set.</p><p>Thank you very much for your help and suggestion :)</p></div><div id="comment-38589-info" class="comment-info"><span class="comment-age">(15 Dec '14, 14:34)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="38590"></span><div id="comment-38590" class="comment"><div id="post-38590-score" class="comment-score"></div><div class="comment-text"><p>As far as I know this is working fine (you can find an example of its usage in file-gif.c). If ou get an assertion when setting a size of 1, then it means that there is something wrong with your code. Are you at the end of the TVB?</p></div><div id="comment-38590-info" class="comment-info"><span class="comment-age">(15 Dec '14, 14:34)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38591"></span><div id="comment-38591" class="comment not_top_scorer"><div id="post-38591-score" class="comment-score"></div><div class="comment-text"><p><span>@Kiran Kumar G</span>,</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38591-info" class="comment-info"><span class="comment-age">(15 Dec '14, 14:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38598"></span><div id="comment-38598" class="comment not_top_scorer"><div id="post-38598-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb, i have accepted the solution provided by Pascal as the correct answer. Thank you.</p></div><div id="comment-38598-info" class="comment-info"><span class="comment-age">(16 Dec '14, 06:21)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div></div><div id="comment-tools-38585" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-38585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

