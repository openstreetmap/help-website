+++
type = "question"
title = "filter: opposite of &quot;contains&quot;?"
description = '''OK, I know when I want to filter out HTTPs which have wanted text in them i type: http.referer contains &quot;text&quot; but what is the command to display all HTTPs except the ones which have certain text in them (which is now unwanted)?'''
date = "2013-12-15T13:48:00Z"
lastmod = "2013-12-16T06:42:00Z"
weight = 28133
keywords = [ "filter", "contains", "http" ]
aliases = [ "/questions/28133" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [filter: opposite of "contains"?](/questions/28133/filter-opposite-of-contains)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28133-score" class="post-score" title="current number of votes">0</div><span id="post-28133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, I know when I want to filter out HTTPs which have wanted text in them i type:</p><p>http.referer contains "text"</p><p>but what is the command to display all HTTPs except the ones which have certain text in them (which is now unwanted)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-contains" rel="tag" title="see questions tagged &#39;contains&#39;">contains</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '13, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/412b10652e55b9c4d3cc5243b7b58d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myrddin&#39;s gravatar image" /><p><span>myrddin</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myrddin has no accepted answers">0%</span></p></div></div><div id="comments-container-28133" class="comments-container"></div><div id="comment-tools-28133" class="comment-tools"></div><div class="clear"></div><div id="comment-28133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28134"></span>

<div id="answer-container-28134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28134-score" class="post-score" title="current number of votes">2</div><span id="post-28134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try</p><pre><code>http and not (http.referer contains &quot;text&quot;)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '13, 15:13</strong> </span></p></div></div><div id="comments-container-28134" class="comments-container"><span id="28136"></span><div id="comment-28136" class="comment"><div id="post-28136-score" class="comment-score"></div><div class="comment-text"><p>Hi, it works but it shows all protocols except HTTPs which contain that text. I want to see all HTTP protocols which don't have that text in the referer field. I know this is is probably stupid question, but I skimmed quickly through help and didn't find it and I don;t have time to read it in detail...</p></div><div id="comment-28136-info" class="comment-info"><span class="comment-age">(15 Dec '13, 14:46)</span> <span class="comment-user userinfo">myrddin</span></div></div><span id="28137"></span><div id="comment-28137" class="comment"><div id="post-28137-score" class="comment-score"></div><div class="comment-text"><p>OK, I've updated my answer to give a filter that only matches HTTP packets where the Referer: field doesn't contain the specified text.</p></div><div id="comment-28137-info" class="comment-info"><span class="comment-age">(15 Dec '13, 15:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="28139"></span><div id="comment-28139" class="comment"><div id="post-28139-score" class="comment-score"></div><div class="comment-text"><p>Works great, thanks!</p></div><div id="comment-28139-info" class="comment-info"><span class="comment-age">(15 Dec '13, 15:29)</span> <span class="comment-user userinfo">myrddin</span></div></div><span id="28141"></span><div id="comment-28141" class="comment"><div id="post-28141-score" class="comment-score"></div><div class="comment-text"><p>I think <code>http.referer and not (http.referer contains "text")</code> would work even better, as not every http packet will contain an <code>http.referer</code> field.</p></div><div id="comment-28141-info" class="comment-info"><span class="comment-age">(15 Dec '13, 17:41)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="28142"></span><div id="comment-28142" class="comment"><div id="post-28142-score" class="comment-score"></div><div class="comment-text"><p>Depends on whether he wants "all HTTP messages except for those that have a Referer: field containing the text in question" or "all HTTP messages including a Referer: field that doesn't contain the text in question". The first would be</p><pre><code>http and not (http.referer contains &quot;text&quot;)</code></pre><p>and the second would be</p><pre><code>http.referer and not (http.referer contains &quot;text&quot;)</code></pre></div><div id="comment-28142-info" class="comment-info"><span class="comment-age">(15 Dec '13, 17:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-28134" class="comment-tools"></div><div class="clear"></div><div id="comment-28134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28158"></span>

<div id="answer-container-28158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28158-score" class="post-score" title="current number of votes">2</div><span id="post-28158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another idea: use a filter with a regular expression, that contains the field <code>http.referer</code> only once. The filter is shorter, but maybe slower than others and harder to understand, so take this just as an example of what can be done :-)</p><blockquote><p>http.referer matches "^((?!text).)*$"</p></blockquote><p>Will match all frames with a field <code>http.referer</code> that does <strong>not contain</strong> the string <code>text</code><br />
</p><p>Anyway, the regular expression answers your question in the title:</p><blockquote><p>filter: <strong>opposite</strong> of "contains"?</p></blockquote><p>The opposite (as I understand it) is the regular expression shown above: <code>xxx matches "^((?!text).)*$"</code>, where <strong>xxx</strong> is the field in question and <strong>text</strong> is the search string.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '13, 11:27</strong> </span></p></div></div><div id="comments-container-28158" class="comments-container"></div><div id="comment-tools-28158" class="comment-tools"></div><div class="clear"></div><div id="comment-28158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

