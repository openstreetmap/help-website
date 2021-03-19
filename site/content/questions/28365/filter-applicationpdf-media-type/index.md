+++
type = "question"
title = "filter application/pdf media type"
description = '''I&#x27;m trying to build a filter that will show me HTTP packets that have the Media Type as application/pdf. So far, &quot;media contains application&quot; is not bringing them up; however it will bring up other packets in the capture such as javascript, octect-stream, and x-msdownload. Simply using &quot;media&quot; will ...'''
date = "2013-12-24T05:44:00Z"
lastmod = "2013-12-28T10:59:00Z"
weight = 28365
keywords = [ "filters" ]
aliases = [ "/questions/28365" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [filter application/pdf media type](/questions/28365/filter-applicationpdf-media-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28365-score" class="post-score" title="current number of votes">0</div><span id="post-28365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build a filter that will show me HTTP packets that have the Media Type as application/pdf. So far, "media contains application" is not bringing them up; however it will bring up other packets in the capture such as javascript, octect-stream, and x-msdownload. Simply using "media" will gain me these packets, but I'd like to be more precise. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/47a9b6c14475abd5e3427af4f10047ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob_D&#39;s gravatar image" /><p><span>Rob_D</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob_D has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Dec '13, 05:44</strong> </span></p></div></div><div id="comments-container-28365" class="comments-container"></div><div id="comment-tools-28365" class="comment-tools"></div><div class="clear"></div><div id="comment-28365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28382"></span>

<div id="answer-container-28382" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28382-score" class="post-score" title="current number of votes">2</div><span id="post-28382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try one of these:</p><blockquote><p>http.content_type == "application/pdf"<br />
</p></blockquote><p>or</p><blockquote><p>http.content_type contains "pdf"<br />
</p></blockquote><p>or</p><blockquote><p>frame contains "application/pdf"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '13, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28382" class="comments-container"><span id="28463"></span><div id="comment-28463" class="comment"><div id="post-28463-score" class="comment-score"></div><div class="comment-text"><p>The first 2 worked exactly as I needed! Thanks Kurt!</p></div><div id="comment-28463-info" class="comment-info"><span class="comment-age">(28 Dec '13, 10:59)</span> <span class="comment-user userinfo">Rob_D</span></div></div></div><div id="comment-tools-28382" class="comment-tools"></div><div class="clear"></div><div id="comment-28382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28376"></span>

<div id="answer-container-28376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28376-score" class="post-score" title="current number of votes">0</div><span id="post-28376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Rob one method I have seen work is to do a follow stream at the start of the packet. Its important to know the beginning and end packets. Do a save as and select your filetype i.e. "pdf". So first filter the correct ip &amp; time. Do a follow stream then save as. This might help.<img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2013-12-24_at_11.53.58_PM.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/e5d5ba5d8ba47e0415a52577bf7bcc4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rayyai%20beach&#39;s gravatar image" /><p><span>rayyai beach</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rayyai beach has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-28376" class="comments-container"></div><div id="comment-tools-28376" class="comment-tools"></div><div class="clear"></div><div id="comment-28376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

