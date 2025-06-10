+++
type = "question"
title = "Adding indoor data on josm"
description = '''I am creating my university indoor map on Android. I have picture.jpg which is my university&#x27;s map:  When I import this picture on josm , it is showing like this   How can I import this school indoormap on josm?? and add data is there any video. Because wiki language is very hard to understand to me...'''
date = "2014-03-16T08:43:00Z"
lastmod = "2020-04-28T10:37:00Z"
weight = 31585
keywords = [ "josm", "editing", "indoor" ]
aliases = [ "/questions/31585" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Adding indoor data on josm](/questions/31585/adding-indoor-data-on-josm)

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
<span id="post-31585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31585-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am creating my university indoor map on Android.</p>
<p>I have picture.jpg which is my university's map:</p>
<p><img src="/upfiles/b1dnm_2.jpg" alt="university&#39;s map" /></p>
<p><strong>When I import this picture on josm , it is showing like this</strong></p>
<p><img src="/upfiles/json_1.JPG" alt="picture on josm" /></p>
<p><strong>How can I import this school indoormap on josm??</strong> and add data is there any video. Because wiki language is very hard to understand to me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '14, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/edb3f664fcdbd97a2cd1c3037412403c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ayse%20duygu&#39;s gravatar image" />
<p><span>Ayse duygu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ayse duygu has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '14, 13:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-31585" class="comments-container">
&#10;</div>
<div id="comment-tools-31585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31585-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="31590"></span>

<div id="answer-container-31590" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31590-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ayse duygu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First you need to understand the (different!) schmemas for modelling indoor OSM data: <a href="http://wiki.openstreetmap.org/wiki/Indoor">http://wiki.openstreetmap.org/wiki/Indoor</a><br />
Then you need to figure out a good workflow for JOSM (e.g. adding your sketch in background, hiding levels to get better overflow, ...). To add your image, I recommend an aerial alignment service, so you can add the image as WMS.<br />
Last but not least you need to find a services that makes use of your modelled data. AFAIK there is currently no renderer or anything that supports this schema and has a clever output (3D or multilayer floorplan)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '14, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-31590" class="comments-container">
<span id="31618"></span>
<div id="comment-31618" class="comment">
<div id="post-31618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much your answer. I learn so much think due to you. But could you give more example about aerial alignment service.. and You said you need to find services It is like what ? So.. I am googling what I meet new word.. If you give more information , I will me pleased</p>
</div>
<div id="comment-31618-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 06:49)</span> <span class="comment-user userinfo">Ayse duygu</span>
</div>
</div>
<span id="31623"></span>
<div id="comment-31623" class="comment">
<div id="post-31623-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The Metalabs rectifier seems to be offline, but <a href="http://labs.metacarta.com/rectifier/">there are alternatives</a>. Please keep in mind, that the floorplan might be copyright protected and itself is intellectual property, so you might get problems to host it public.</p>
</div>
<div id="comment-31623-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 08:46)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="31626"></span>
<div id="comment-31626" class="comment">
<div id="post-31626-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>… if it is not explicitly public domain or something, then it is not even allowed to be used as help in drawing (if you plan to add the data to OSM)!</p>
</div>
<div id="comment-31626-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 13:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31590-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74439"></span>

<div id="answer-container-74439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74439-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-74439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I hope you will add indoor data on josm successfully, thank you for sharing your information with us.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74439" class="comments-container">
<span id="74441"></span>
<div id="comment-74441" class="comment">
<div id="post-74441-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please stop reviving old questions by adding answers containing no useful information.</p>
</div>
<div id="comment-74441-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 10:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74439-form-container" class="comment-form-container">
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

