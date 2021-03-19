+++
type = "question"
title = "HTTP requests without cookies"
description = '''We have an apparent problem in that some requests to our IIS server do not have cookies. We actually have an ISAPI filter that is reporting the problem but we would like an independent verification: (a) how do we set up a filter in Wireshark that shows the http requests that do NOT have cookies [ign...'''
date = "2011-01-31T16:02:00Z"
lastmod = "2011-02-01T21:13:00Z"
weight = 2050
keywords = [ "cookies", "http", "cookiesize" ]
aliases = [ "/questions/2050" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP requests without cookies](/questions/2050/http-requests-without-cookies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2050-score" class="post-score" title="current number of votes">0</div><span id="post-2050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have an apparent problem in that some requests to our IIS server do not have cookies. We actually have an ISAPI filter that is reporting the problem but we would like an independent verification: (a) how do we set up a filter in Wireshark that shows the http requests that do NOT have cookies [ignoring those that do]. (b) how to we set up a filter that shows HTTP traffic with cookies that exceed a certain size</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cookies" rel="tag" title="see questions tagged &#39;cookies&#39;">cookies</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-cookiesize" rel="tag" title="see questions tagged &#39;cookiesize&#39;">cookiesize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/c09fa113c27f68e304b1e4ced7e8bf12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julian%20Dohmen&#39;s gravatar image" /><p><span>Julian Dohmen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julian Dohmen has no accepted answers">0%</span></p></div></div><div id="comments-container-2050" class="comments-container"></div><div id="comment-tools-2050" class="comment-tools"></div><div class="clear"></div><div id="comment-2050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2051"></span>

<div id="answer-container-2051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2051-score" class="post-score" title="current number of votes">1</div><span id="post-2051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(a) <code>http.request.method and not http.cookie</code></p><p>(b) not sure how to do this, there doesn't seem to be a good way to filter for this, but maybe somebody else has a good idea</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jan '11, 17:07</strong> </span></p></div></div><div id="comments-container-2051" class="comments-container"><span id="2067"></span><div id="comment-2067" class="comment"><div id="post-2067-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I am pretty new to Wireshark - I see that the filter above is a Display Filter which I am trying out [and I did use the word <em>show</em> of course] but is there a capture filter that would only allow cookie-less http requests through? Thanks</p></div><div id="comment-2067-info" class="comment-info"><span class="comment-age">(01 Feb '11, 06:28)</span> <span class="comment-user userinfo">Julian Dohmen</span></div></div><span id="2068"></span><div id="comment-2068" class="comment"><div id="post-2068-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if this is possible, maybe through some very advanced offset matching filters, but that is beyond my experience as I rarely use capture filters at all (and when I do I usually filter on nothing more than MAC or IP addresses). Maybe somebody else has a solution for you.</p></div><div id="comment-2068-info" class="comment-info"><span class="comment-age">(01 Feb '11, 06:49)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="2079"></span><div id="comment-2079" class="comment"><div id="post-2079-score" class="comment-score"></div><div class="comment-text"><p>Thanks - we can probably use your display filter as the main thing is to see items without cookies.</p></div><div id="comment-2079-info" class="comment-info"><span class="comment-age">(01 Feb '11, 11:29)</span> <span class="comment-user userinfo">Julian Dohmen</span></div></div></div><div id="comment-tools-2051" class="comment-tools"></div><div class="clear"></div><div id="comment-2051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2090"></span>

<div id="answer-container-2090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2090-score" class="post-score" title="current number of votes">0</div><span id="post-2090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture HTTP GET requests:<br />
port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</p><p>You can find this and other capture filter examples in the <a href="http://wiki.wireshark.org/CaptureFilters">Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '11, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-2090" class="comments-container"></div><div id="comment-tools-2090" class="comment-tools"></div><div class="clear"></div><div id="comment-2090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

