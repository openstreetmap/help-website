+++
type = "question"
title = "Question on Filtering HTTP"
description = '''I want to filter only http, but when I did that it shows me both ssdp and http. However, if write http and tcp.dstport != 1900 on the display filter command it shows me only http which is what I want. So I dont quite understand why if I type only http on the filter command it doesnt show only http?'''
date = "2015-01-07T02:38:00Z"
lastmod = "2015-01-07T05:26:00Z"
weight = 38923
keywords = [ "display-filter" ]
aliases = [ "/questions/38923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Question on Filtering HTTP](/questions/38923/question-on-filtering-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38923-score" class="post-score" title="current number of votes">0</div><span id="post-38923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to filter only http, but when I did that it shows me both ssdp and http. However, if write http and tcp.dstport != 1900 on the display filter command it shows me only http which is what I want. So I dont quite understand why if I type only http on the filter command it doesnt show only http?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '15, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/c7f979e79f947239e06d110e51fd8b03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Specialone&#39;s gravatar image" /><p><span>Specialone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Specialone has no accepted answers">0%</span></p></div></div><div id="comments-container-38923" class="comments-container"></div><div id="comment-tools-38923" class="comment-tools"></div><div class="clear"></div><div id="comment-38923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38924"></span>

<div id="answer-container-38924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38924-score" class="post-score" title="current number of votes">3</div><span id="post-38924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>http</strong> is a display filter that will show all frames that Wireshark recognized (dissected) as HTTP, which <strong>includes SSDP</strong> (<a href="http://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol">as that's using a 'dialect' of HTTP</a>).</p><p>If you don't want to see SSDP, you can use the filter you have mentioned, or remove port 1900 from the HTTP preferences.</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP Ports</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38924" class="comments-container"><span id="38926"></span><div id="comment-38926" class="comment"><div id="post-38926-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Kurt for your answer. Appreciate it very much:D</p></div><div id="comment-38926-info" class="comment-info"><span class="comment-age">(07 Jan '15, 05:26)</span> <span class="comment-user userinfo">Specialone</span></div></div></div><div id="comment-tools-38924" class="comment-tools"></div><div class="clear"></div><div id="comment-38924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

