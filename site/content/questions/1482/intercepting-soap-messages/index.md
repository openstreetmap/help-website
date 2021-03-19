+++
type = "question"
title = "Intercepting SOAP messages"
description = '''Hi I need help intercepting my SOAP web service messages. I am able to see them with IEInspector, but no with wireshark. My application server is glassfish running locally on port 8080, so I changed the filter to: tcp port 8080 But it doesn&#x27;t look like any message is intercepted by wireshark when I ...'''
date = "2010-12-26T01:22:00Z"
lastmod = "2010-12-26T03:59:00Z"
weight = 1482
keywords = [ "glassfish", "8080", "soap" ]
aliases = [ "/questions/1482" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Intercepting SOAP messages](/questions/1482/intercepting-soap-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1482-score" class="post-score" title="current number of votes">0</div><span id="post-1482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I need help intercepting my SOAP web service messages. I am able to see them with IEInspector, but no with wireshark.</p><p>My application server is glassfish running locally on port 8080, so I changed the filter to: <strong>tcp port 8080</strong> But it doesn't look like any message is intercepted by wireshark when I execute a web service method (the call is successful).</p><p>This is driving me nuts ;) Any ideas?</p><p>Thanks in advance Sigal</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glassfish" rel="tag" title="see questions tagged &#39;glassfish&#39;">glassfish</span> <span class="post-tag tag-link-8080" rel="tag" title="see questions tagged &#39;8080&#39;">8080</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '10, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/7c09f33471070b25abe925f64c58e3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sigals&#39;s gravatar image" /><p><span>Sigals</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sigals has no accepted answers">0%</span></p></div></div><div id="comments-container-1482" class="comments-container"></div><div id="comment-tools-1482" class="comment-tools"></div><div class="clear"></div><div id="comment-1482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1483"></span>

<div id="answer-container-1483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1483-score" class="post-score" title="current number of votes">0</div><span id="post-1483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the webservice called by a client on the same system? If so, have a look at the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback page on the wireshark wiki</a>.</p><p>If not, do you see traffic on port 8080 that is not dissected? Or don't you see any traffic at all?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Dec '10, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1483" class="comments-container"><span id="1484"></span><div id="comment-1484" class="comment"><div id="post-1484-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help. My server and client are both local, so I tried the workaround in the link you provided.</p><p>I now receive SOAP XML messages in wireshark but not the ones I send?! Some other web service (the URL is of Microsoft)</p></div><div id="comment-1484-info" class="comment-info"><span class="comment-age">(26 Dec '10, 03:28)</span> <span class="comment-user userinfo">Sigals</span></div></div><span id="1485"></span><div id="comment-1485" class="comment"><div id="post-1485-score" class="comment-score"></div><div class="comment-text"><p>Well, I don't have much experience with capturing local traffic on Windows, but I know it is not without problems (as the page also kind of portrays). Is it possible for you to run the client and server on different systems?</p><p>Otherwise someone else might have another tip :-)</p><p>PS I changed your answer to a comment, as that will keep things together. This is a Q&amp;A site which works a bit differently than a forum...</p></div><div id="comment-1485-info" class="comment-info"><span class="comment-age">(26 Dec '10, 03:59)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1483" class="comment-tools"></div><div class="clear"></div><div id="comment-1483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

