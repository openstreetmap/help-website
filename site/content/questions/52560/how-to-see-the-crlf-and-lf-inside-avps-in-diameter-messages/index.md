+++
type = "question"
title = "How to see the CRLF and LF inside AVPs in diameter messages"
description = '''Hi  Can you please tell how CRLF (Carrage return line feed) and Line feed charecter on Diameter messages(&#92;r&#92;n) In SIP i have an option of RAWpcaps Regards Vijay'''
date = "2016-05-14T02:46:00Z"
lastmod = "2016-05-18T18:32:00Z"
weight = 52560
keywords = [ "and", "lf", "in", "crlf", "diameter" ]
aliases = [ "/questions/52560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to see the CRLF and LF inside AVPs in diameter messages](/questions/52560/how-to-see-the-crlf-and-lf-inside-avps-in-diameter-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52560-score" class="post-score" title="current number of votes">0</div><span id="post-52560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Can you please tell how CRLF (Carrage return line feed) and Line feed charecter on Diameter messages(\r\n) In SIP i have an option of RAWpcaps Regards Vijay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-lf" rel="tag" title="see questions tagged &#39;lf&#39;">lf</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span> <span class="post-tag tag-link-crlf" rel="tag" title="see questions tagged &#39;crlf&#39;">crlf</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '16, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/f1c4ad8a11798f63ad06d58ac22b5630?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grvijay&#39;s gravatar image" /><p><span>grvijay</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grvijay has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '16, 00:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-52560" class="comments-container"><span id="52566"></span><div id="comment-52566" class="comment"><div id="post-52566-score" class="comment-score"></div><div class="comment-text"><p>What makes you believe that there are any CR and/or LF characters in the binary-encoded Diameter protocol?</p><p>SIP is text-based so these characters are there by nature of it, and the choice whether to show or hide them in packet dissection is useful to show them when you concentrate on proper formatting of the messages or hide them when you concentrate on its proper contents, as their rendering as \r\n adds visual noise to the message text. But in Diameter, there is no CR/LF to be displayed, so what do you actually want to happen?</p></div><div id="comment-52566-info" class="comment-info"><span class="comment-age">(14 May '16, 09:57)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52560" class="comment-tools"></div><div class="clear"></div><div id="comment-52560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52567"></span>

<div id="answer-container-52567" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52567-score" class="post-score" title="current number of votes">0</div><span id="post-52567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In SIP i can see them in indivsual lines like m=audio 49152 RTP/AVP 97 98 99 100 101 102 \r\n</p><p>In diameter TS 24.229 the SDP parameters are in Codec-data in AAR messages.I was not seeing in this fashion as i had not expanded the Media component description. It was my mistake that i did not expand (without expanding the SDP in SIP ia was able to see it). My purpose is solved thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '16, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/f1c4ad8a11798f63ad06d58ac22b5630?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grvijay&#39;s gravatar image" /><p><span>grvijay</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grvijay has one accepted answer">100%</span></p></div></div><div id="comments-container-52567" class="comments-container"><span id="52751"></span><div id="comment-52751" class="comment"><div id="post-52751-score" class="comment-score"></div><div class="comment-text"><p>(I converted your comment to an answer and accepted it so this question doesn't show up in the list of unanswered questions--see the FAQ.)</p></div><div id="comment-52751-info" class="comment-info"><span class="comment-age">(18 May '16, 18:32)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-52567" class="comment-tools"></div><div class="clear"></div><div id="comment-52567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

