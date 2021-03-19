+++
type = "question"
title = "Get message sent using the &quot;SUBMIT&quot; button"
description = '''I am trying to automate the process of getting the nine digit zip code from the US Postal service web site (http://zip4.usps.com/zip4/welcome.jsp) To do so I need the message sent when I click on the Submit button at that site. Is this a facility provided by WireShark? Thanks, Jim'''
date = "2010-11-29T08:07:00Z"
lastmod = "2010-11-29T13:02:00Z"
weight = 1153
keywords = [ "post", "messages", "get" ]
aliases = [ "/questions/1153" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get message sent using the "SUBMIT" button](/questions/1153/get-message-sent-using-the-submit-button)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1153-score" class="post-score" title="current number of votes">0</div><span id="post-1153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to automate the process of getting the nine digit zip code from the US Postal service web site (http://zip4.usps.com/zip4/welcome.jsp)</p><p>To do so I need the message sent when I click on the Submit button at that site. Is this a facility provided by WireShark?</p><p>Thanks,</p><p>Jim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-messages" rel="tag" title="see questions tagged &#39;messages&#39;">messages</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '10, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/6940ea5753562f708f012f9ec22729bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim&#39;s gravatar image" /><p><span>Jim</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim has no accepted answers">0%</span></p></div></div><div id="comments-container-1153" class="comments-container"></div><div id="comment-tools-1153" class="comment-tools"></div><div class="clear"></div><div id="comment-1153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1154"></span>

<div id="answer-container-1154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1154-score" class="post-score" title="current number of votes">0</div><span id="post-1154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark cannot script the retrieval process for you. That is something you might do using <strong>wget</strong> or some other tool that fetches web pages. Wireshark can help you to get the wget request right though: capture a manual search that works, and then work with the wget parameters until your automated request matches the manual one when you capture it. This should then give you the results as you need them.</p><p>You might look into something like <strong>"wget http://zip4.usps.com/zip4/zcl_0_results.jsp --post-data [your query parameters]"</strong>, because the web page expects the form to be submitted by POST operation. Good luck :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '10, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1154" class="comments-container"><span id="1157"></span><div id="comment-1157" class="comment"><div id="post-1157-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. I'm not sure I make myself clear--my bad.</p><p>I have no trouble fetching web pages for which I have the url. My problem is feeding the USPS the info that is sent via the SUBMIT button on their site. I need to know what it is that I should POST to the USPS site: url "http://zip4.usps.com/zip4/zcl_0_results.jsp" so that that site will return the 9 digit zip code--actually the himl source code from which I can parse out the zip code.</p><p>Is that a little clearer?</p><p>Jim</p></div><div id="comment-1157-info" class="comment-info"><span class="comment-age">(29 Nov '10, 09:31)</span> <span class="comment-user userinfo">Jim</span></div></div><span id="1160"></span><div id="comment-1160" class="comment"><div id="post-1160-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is. This is what you can use Wireshark for, which is what I meant by capturing manual search: start Wireshark, capture on the network card that you are going to use to fetch the web page manually, and after you run the manual process, stop the capture. Then you need to find the POST request that you made to the page, for example by filtering for <strong>http.request.method=="POST"</strong>. You should then be able to find the packet containing your POST request. Take a look at the decode of that packet: in the last section you can unfold the details of your request, including all name/value pairs.</p></div><div id="comment-1160-info" class="comment-info"><span class="comment-age">(29 Nov '10, 13:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-1154" class="comment-tools"></div><div class="clear"></div><div id="comment-1154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

