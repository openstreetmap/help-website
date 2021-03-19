+++
type = "question"
title = "How to find HTTP content encoding"
description = '''I know it is an old post, but I need to know if there is a way to tell from wireshark what the content encoding is? How should I know if it is gzip encoded? Is it in the TCP header somewhere?'''
date = "2013-11-07T09:23:00Z"
lastmod = "2013-11-11T07:26:00Z"
weight = 26724
keywords = [ "content", "http", "encoding" ]
aliases = [ "/questions/26724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find HTTP content encoding](/questions/26724/how-to-find-http-content-encoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26724-score" class="post-score" title="current number of votes">0</div><span id="post-26724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know it is an old post, but I need to know if there is a way to tell from wireshark what the content encoding is? How should I know if it is gzip encoded? Is it in the TCP header somewhere?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-content" rel="tag" title="see questions tagged &#39;content&#39;">content</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/8c5736436291d4a1992989487921f61c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doodlekana&#39;s gravatar image" /><p><span>doodlekana</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doodlekana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>07 Nov '13, 15:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26724" class="comments-container"><span id="26737"></span><div id="comment-26737" class="comment"><div id="post-26737-score" class="comment-score"></div><div class="comment-text"><p>I converted your comment to a question, as your question is not related to the content of the original question: <a href="http://ask.wireshark.org/questions/6598/how-to-decompress-gzipped-contents">http://ask.wireshark.org/questions/6598/how-to-decompress-gzipped-contents</a></p></div><div id="comment-26737-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26724" class="comment-tools"></div><div class="clear"></div><div id="comment-26724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26841"></span>

<div id="answer-container-26841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26841-score" class="post-score" title="current number of votes">1</div><span id="post-26841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How should I know if it is gzip encoded? Is it in the TCP header somewhere?</p></blockquote><p>No, it's not in the <strong>TCP</strong> header it's in the <strong>HTTP</strong> header. The HTTP header is called <strong><a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">Content-Encoding</a></strong>. If there is compressed content, the value of <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">Content-Encoding</a> will be <strong>gzip</strong> (or any other supported compression method).</p><p>You can use a Wireshark display filter for that:</p><blockquote><p>http.content_encoding == "gzip"</p></blockquote><p>This will show frames with compressed HTTP content.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26841" class="comments-container"></div><div id="comment-tools-26841" class="comment-tools"></div><div class="clear"></div><div id="comment-26841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

