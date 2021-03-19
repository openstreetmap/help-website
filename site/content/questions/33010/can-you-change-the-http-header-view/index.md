+++
type = "question"
title = "Can you change the http header view"
description = '''Hi, When viewing HTTP Headers I notice its in tree format and copy pasting is somewhat trivial. Its no big deal at all, but I was just wondering is there a way to view the response headers in &quot;raw&quot; text? Like I could highlight and copy paste. I actually dont even want to copy paste I just want it to...'''
date = "2014-05-22T16:19:00Z"
lastmod = "2014-05-23T06:04:00Z"
weight = 33010
keywords = [ "header", "http", "view" ]
aliases = [ "/questions/33010" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can you change the http header view](/questions/33010/can-you-change-the-http-header-view)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33010-score" class="post-score" title="current number of votes">0</div><span id="post-33010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, When viewing HTTP Headers I notice its in tree format and copy pasting is somewhat trivial.</p><p>Its no big deal at all, but I was just wondering is there a way to view the response headers in "raw" text?</p><p>Like I could highlight and copy paste. I actually dont even want to copy paste I just want it to be in text mode the way a browser sees it, like no extra data at the end after the last \r\n. Even maybe instead of \r\n just a newline and instead of putting the x-www-form-urlencoded data way way at the bottom on a new tree node just have it appear the way it does in the raw header body?</p><p>Im not sure if Ive been clear with my question :S let me know and i will try to make it more clear if not.</p><p>THANKS!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-view" rel="tag" title="see questions tagged &#39;view&#39;">view</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '14, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/b9b99e7ed7766e068c878146a095d56b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leathan&#39;s gravatar image" /><p><span>leathan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leathan has no accepted answers">0%</span></p></div></div><div id="comments-container-33010" class="comments-container"></div><div id="comment-tools-33010" class="comment-tools"></div><div class="clear"></div><div id="comment-33010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33014"></span>

<div id="answer-container-33014" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33014-score" class="post-score" title="current number of votes">0</div><span id="post-33014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="leathan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use TCP "Follow Stream" and the resulting dialog gives you the raw text which you can copy and paste elsewhere. Note the dialog contains all the contents of that particular stream, not just the headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33014" class="comments-container"><span id="33021"></span><div id="comment-33021" class="comment"><div id="post-33021-score" class="comment-score"></div><div class="comment-text"><p>It would make your comment even more perfect if you could explain how to keep this type of view up for the entire conversation between my server. When I enter this view it shows me the entire stream UP TILL THAT POINT. and will not refresh or continue the stream with my server. Not a big problem I just use tcp.stream eq # || http and open up a new "view stream" window. I notice that this is because its actually a new stream, but maybe you can add how to leave this view up for the entire session between a specific server? What I mean by this is have the window you showed me continually update its content in real time! Either way you have been more than helpful. this was exactly what I wanted.</p></div><div id="comment-33021-info" class="comment-info"><span class="comment-age">(23 May '14, 05:32)</span> <span class="comment-user userinfo">leathan</span></div></div><span id="33022"></span><div id="comment-33022" class="comment"><div id="post-33022-score" class="comment-score">1</div><div class="comment-text"><p>Unfortunately, the "entire conversation" for http streams is usually carried over several TCP streams, and the "Follow TCP Stream" functionality only works for a single stream at a time, and, as you mention, only works for the stream contents in the capture at that point.</p><p>Your other option is to use tshark at the command prompt to display only http headers. There may be existing questions on that.</p></div><div id="comment-33022-info" class="comment-info"><span class="comment-age">(23 May '14, 06:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33014" class="comment-tools"></div><div class="clear"></div><div id="comment-33014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

