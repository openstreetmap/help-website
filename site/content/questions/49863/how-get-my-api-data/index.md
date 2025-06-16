+++
type = "question"
title = "how get my api data?"
description = '''Hi, why I can´t get any data from this api: http://api06.dev.openstreetmap.org/api/0.6/map?bbox=7.1,47.5,7.8,48.1'''
date = "2016-05-27T14:14:00Z"
lastmod = "2016-05-27T14:57:00Z"
weight = 49863
keywords = [ "development", "api", "error" ]
aliases = [ "/questions/49863" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how get my api data?](/questions/49863/how-get-my-api-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, why I can´t get any data from this api: <a href="http://api06.dev.openstreetmap.org/api/0.6/map?bbox=7.1,47.5,7.8,48.1">http://api06.dev.openstreetmap.org/api/0.6/map?bbox=7.1,47.5,7.8,48.1</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '16, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/122eea6c5b91fa9a90ad61ff6057049f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OuedraogoMichel&#39;s gravatar image" />
<p><span>OuedraogoMichel</span><br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OuedraogoMichel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '16, 20:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49863" class="comments-container">
&#10;</div>
<div id="comment-tools-49863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49863-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49864"></span>

<div id="answer-container-49864" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49864-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OuedraogoMichel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The message you get back from that is "The maximum bbox size is 0.25, and your request was too large. Either request a smaller area, or use planet.osm".</p>
<p>Which part of that response do you need help with - what the units of "maximum bbox size" are, why there's a limit on size at all, or what planet.osm is?</p>
<p>Actually, there's not a whole amount of data there at all. You're using the dev api, and looking at <a href="http://api06.dev.openstreetmap.org/#map=11/47.6138/7.6441&amp;layers=D">http://api06.dev.openstreetmap.org/#map=11/47.6138/7.6441&amp;layers=D</a> you can see there are only a couple of ways potentially within that bbox at all (even if the dev API didn't have a maximum bbox size the same as the live API).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '16, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '16, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-49864" class="comments-container">
<span id="49865"></span>
<div id="comment-49865" class="comment">
<div id="post-49865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how can I get an planet api? I Need to get a flexible api where I can can give a minlat, maxlat, minlng and maxlng.</p>
<p>Thanks</p>
</div>
<div id="comment-49865-info" class="comment-info">
<span class="comment-age">(27 May '16, 14:31)</span> <span class="comment-user userinfo">OuedraogoMichel</span>
</div>
</div>
<span id="49867"></span>
<div id="comment-49867" class="comment">
<div id="post-49867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need in my Project to produce some data from OSM where I can give the Parameter of the latitude and longitude. Further I have to get the properties of the street like Bridge tunnel etc...</p>
<p>Thanks</p>
</div>
<div id="comment-49867-info" class="comment-info">
<span class="comment-age">(27 May '16, 14:51)</span> <span class="comment-user userinfo">OuedraogoMichel</span>
</div>
</div>
<span id="49868"></span>
<div id="comment-49868" class="comment">
<div id="post-49868-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> .</p>
</div>
<div id="comment-49868-info" class="comment-info">
<span class="comment-age">(27 May '16, 14:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49864-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

