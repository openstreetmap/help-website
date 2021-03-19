+++
type = "question"
title = "How to  get all of the http sessions related to one web page?"
description = '''how to get all of the http session related to one web page? Dear , When I load one web-page, it generates many http sessions (like get/response..), and it&#x27;s difficult to get all of the http packets related to one web page. Do you have some ideas?'''
date = "2012-07-18T05:32:00Z"
lastmod = "2012-09-28T01:36:00Z"
weight = 12824
keywords = [ "session", "http", "web-page" ]
aliases = [ "/questions/12824" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all of the http sessions related to one web page?](/questions/12824/how-to-get-all-of-the-http-sessions-related-to-one-web-page)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12824-score" class="post-score" title="current number of votes">0</div><span id="post-12824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to get all of the http session related to one web page? Dear , When I load one web-page, it generates many http sessions (like get/response..), and it's difficult to get all of the http packets related to one web page. Do you have some ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-web-page" rel="tag" title="see questions tagged &#39;web-page&#39;">web-page</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p><span>chinasan</span><br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '12, 05:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-12824" class="comments-container"></div><div id="comment-tools-12824" class="comment-tools"></div><div class="clear"></div><div id="comment-12824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12827"></span>

<div id="answer-container-12827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12827-score" class="post-score" title="current number of votes">1</div><span id="post-12827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how to get all of the htttp session related to one web page?</p></blockquote><p>Unfortunately that's not easy as HTTP is a stateless protocol and there is no way to relate several HTTP requests with one "web page" (what you see in the browser).</p><p>Take a look at <a href="http://www.nbc.com">http://www.nbc.com</a> There is a lot of content from other pages (adclick, twitter, etc.) linked into that page. Your browser first loads the main page (<a href="http://www.nbc.com">www.nbc.com</a>) and then follows all links in the HTML document. So, for the browser it is easy to get it all together.</p><p>Wireshark however captures only single (unrelated) requests and responses. So, it's hard to figure out if a request belongs to one page or another (if it's the same server)</p><p>Imagine you load two different pages on the same webserver in parallel (two browser windows). The browsers knwo what they requested and what to show. Wireshark sees only requests and responses from the same IP addresses and cannot distinguish if they came from one browser window or the other. So it's nearly impossible to get all "sessions related to one page".</p><p>So, what can you do:</p><ul><li>Filter on the IP address of the target server (ip.addr eq x.x.x.x). This will at least give you all requests and responses from one server. However, these could be from different pages ("sessions") on the server (see two browser sample above)</li><li>Try to find a SESSIONID in the first request (a Cookie, JSESSIONID, PHPSESSIONID) and try to filter on that</li><li>Write your own TAP that does a more thorough HTTP inspection. Then you can parse the HTML code and figure out all links in the page. Then, if you see a request to one of those links within a short period of time it's kind of likely that these requests belong to the same "session", although there is no guarantee.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '12, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jul '12, 07:05</strong> </span></p></div></div><div id="comments-container-12827" class="comments-container"><span id="14586"></span><div id="comment-14586" class="comment"><div id="post-14586-score" class="comment-score"></div><div class="comment-text"><p>I see that you awarded one (your only) karma point to Kurt, that's a great gesture. However, the best way to award someone for providing you with a useful answer is to click on the thumps-up. That will give the person 15 karma points. On top of that you can "accept" the answer that answered your question best by clicking on the "Checkmark" under the thumps-up/down. This will add another 25 karma points to the person that gave the answer.</p></div><div id="comment-14586-info" class="comment-info"><span class="comment-age">(28 Sep '12, 01:36)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-12827" class="comment-tools"></div><div class="clear"></div><div id="comment-12827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

