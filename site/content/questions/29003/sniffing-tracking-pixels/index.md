+++
type = "question"
title = "Sniffing tracking pixels?"
description = '''Problem: I&#x27;m trying to check if a tracking pixel is firing on a page. We installed third party tracking mechanism (Mediaplex) and I need to make sure it&#x27;s working properly. This mechanism is just a bit of code that looks something like this: &amp;lt;iframe src=&quot;https://secure.img-cdn.mediaplex.com/0/123...'''
date = "2014-01-17T13:29:00Z"
lastmod = "2014-01-21T04:44:00Z"
weight = 29003
keywords = [ "tracking", "pixel" ]
aliases = [ "/questions/29003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing tracking pixels?](/questions/29003/sniffing-tracking-pixels)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29003-score" class="post-score" title="current number of votes">0</div><span id="post-29003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Problem: I'm trying to check if a tracking pixel is firing on a page. We installed third party tracking mechanism (Mediaplex) and I need to make sure it's working properly. This mechanism is just a bit of code that looks something like this:</p>&lt;iframe src="https://secure.img-cdn.mediaplex.com/0/1236/universal.html?page_name=sitepage &amp;amp;Value=PASS_VALUE &amp;amp;Value1=PASS_VALUE &amp;amp;mpuid=additionainfo#" height="1" width="1" frameborder="0"&gt;&lt;/iframe&gt;<p>This bit of code sits inside a body tag.</p><p>Question: Can Wireshark help me see if the Mediaplex tag is sending data out? If yes, how please? I'm a total noon when it come to this. :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tracking" rel="tag" title="see questions tagged &#39;tracking&#39;">tracking</span> <span class="post-tag tag-link-pixel" rel="tag" title="see questions tagged &#39;pixel&#39;">pixel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/ffe8b9568674731e7cade577a9487495?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Whatatrip&#39;s gravatar image" /><p><span>Whatatrip</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Whatatrip has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jan '14, 14:19</strong> </span></p></div></div><div id="comments-container-29003" class="comments-container"></div><div id="comment-tools-29003" class="comment-tools"></div><div class="clear"></div><div id="comment-29003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29053"></span>

<div id="answer-container-29053" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29053-score" class="post-score" title="current number of votes">0</div><span id="post-29053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can Wireshark help me see if the Mediaplex tag is sending data out?</p></blockquote><p>yes. Just start Wireshark and let it capture all traffic of your client (see the docs how to do that).</p><p>Then start a browser and load the page that has the mediaplex code included. If the browser loads the link in the iframe, you will see a SSL/HTTPS connection from your client to secure.img-cdn.mediaplex.com.</p><p>HOWEVER: the connection is encrypted, so you will neither see the URL (you mentioned above) nor any other data in that connection.</p><p>There are ways to decrypt the connection, if you browser exports the session keys. However, that's rather complicated for a 'noon' (as you said).</p><p>So, in your case I would recommend to check if the mediaplex code works, with one of the following methods</p><ul><li>ask the vendor (mediaplex) if it works and/or check your mediaplex logs</li><li>use <a href="http://fiddler2.com">Fiddler2</a> to intercept SSL traffic of your client. Then you will be able to see the requests and contents of the mediaplex connections.</li><li>use some browser developer tools (Firebug or similar) to monitor requests of your client</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '14, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '14, 04:45</strong> </span></p></div></div><div id="comments-container-29053" class="comments-container"></div><div id="comment-tools-29053" class="comment-tools"></div><div class="clear"></div><div id="comment-29053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

