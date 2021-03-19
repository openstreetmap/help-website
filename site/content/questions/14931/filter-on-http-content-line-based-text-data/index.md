+++
type = "question"
title = "Filter on HTTP Content (Line-based text data)"
description = '''Hi, I have about a months worth of Wireshark captures that I&#x27;d like to now view only http content that contains the word &quot;EXITAU&quot;. That data appears in the &quot;Line-based text data&quot;. I don&#x27;t know how to create a display filter on that. Can it even be done? Thanks, Dana'''
date = "2012-10-11T08:32:00Z"
lastmod = "2016-05-06T15:31:00Z"
weight = 14931
keywords = [ "filter", "content", "http" ]
aliases = [ "/questions/14931" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter on HTTP Content (Line-based text data)](/questions/14931/filter-on-http-content-line-based-text-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14931-score" class="post-score" title="current number of votes">0</div><span id="post-14931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have about a months worth of Wireshark captures that I'd like to now view only http content that contains the word "EXITAU". That data appears in the "Line-based text data".</p><p>I don't know how to create a display filter on that. Can it even be done?</p><p>Thanks,</p><p>Dana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-content" rel="tag" title="see questions tagged &#39;content&#39;">content</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/10a8fff9df1cf196eead74c7160b7e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dana&#39;s gravatar image" /><p><span>Dana</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dana has no accepted answers">0%</span></p></div></div><div id="comments-container-14931" class="comments-container"></div><div id="comment-tools-14931" class="comment-tools"></div><div class="clear"></div><div id="comment-14931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14933"></span>

<div id="answer-container-14933" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14933-score" class="post-score" title="current number of votes">1</div><span id="post-14933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dana has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this filter: <code>data-text-lines contains "EXITAU"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14933" class="comments-container"><span id="14934"></span><div id="comment-14934" class="comment"><div id="post-14934-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. I'm new to Wireshark and I searched all over the internet, but never found "data-text-lines". I'll search on that now to get more documentation on it and other such filterable names.</p><p>Dana</p></div><div id="comment-14934-info" class="comment-info"><span class="comment-age">(11 Oct '12, 09:20)</span> <span class="comment-user userinfo">Dana</span></div></div><span id="14935"></span><div id="comment-14935" class="comment"><div id="post-14935-score" class="comment-score">1</div><div class="comment-text"><p>There's a simple trick to find that kind of thing: select the part/field that contains what you want to filter on, and you'll see the filter name for it on the left of the status bar. And you can also right click on the part/field and select "prepare as filter -&gt; selected" which will put the filter right into the filter box for you to change and execute.</p><p>Also, you can click on "Expression..." right next to the filter input field, which will open the filter "phone book" of Wireshark, containing all possible filters.</p></div><div id="comment-14935-info" class="comment-info"><span class="comment-age">(11 Oct '12, 09:25)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="14937"></span><div id="comment-14937" class="comment"><div id="post-14937-score" class="comment-score"></div><div class="comment-text"><p>Excellent. Thanks again, Jasper. I'm a software developer who was given the network to look after. I have no training and likely will never be able to get training. It's all interesting, but confusing at times.</p><p>Wireshark has really opened up at least the guts of the network to me.</p><p>Thanks again.</p><p>Dana</p></div><div id="comment-14937-info" class="comment-info"><span class="comment-age">(11 Oct '12, 09:57)</span> <span class="comment-user userinfo">Dana</span></div></div><span id="52291"></span><div id="comment-52291" class="comment"><div id="post-52291-score" class="comment-score"></div><div class="comment-text"><p>the option of "Apply as filter".. thats the best thing to know. Thanks for the question &amp; answers...</p></div><div id="comment-52291-info" class="comment-info"><span class="comment-age">(06 May '16, 15:31)</span> <span class="comment-user userinfo">khader</span></div></div></div><div id="comment-tools-14933" class="comment-tools"></div><div class="clear"></div><div id="comment-14933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

