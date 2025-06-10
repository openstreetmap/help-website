+++
type = "question"
title = "Find the area of a map (Xkm x Ykm) from the left &amp; right longitude and latitude"
description = '''How can the area of a map from OpenStreetMap be determined in the form of Xkm x Ykm, given the following information: Left Longitude = 103.554879 Right Longitude = 103.740497 Top Latitude = 1.585770 Bottom Latitude = 1.490873 Any ideas? Thanks a lot!'''
date = "2015-10-13T10:47:00Z"
lastmod = "2015-10-13T16:43:00Z"
weight = 45861
keywords = [ "latitude", "distance", "longitude", "area" ]
aliases = [ "/questions/45861" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find the area of a map (Xkm x Ykm) from the left & right longitude and latitude](/questions/45861/find-the-area-of-a-map-xkm-x-ykm-from-the-left-right-longitude-and-latitude)

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
<span id="post-45861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45861-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can the area of a map from OpenStreetMap be determined in the form of Xkm x Ykm, given the following information:</p>
<p>Left Longitude = 103.554879 Right Longitude = 103.740497 Top Latitude = 1.585770 Bottom Latitude = 1.490873</p>
<p>Any ideas? Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '15, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f0f1d9ff64290b70b4a0d9359c781c8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amatek&#39;s gravatar image" />
<p><span>amatek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amatek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45861" class="comments-container">
<span id="45868"></span>
<div id="comment-45868" class="comment">
<div id="post-45868-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/166302/find-the-area-of-a-map-xkm-x-ykm-from-the-left-right-longitude-and-latitude">https://gis.stackexchange.com/questions/166302/find-the-area-of-a-map-xkm-x-ykm-from-the-left-right-longitude-and-latitude</a></p>
</div>
<div id="comment-45868-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 12:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45861-form-container" class="comment-form-container">
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

<span id="45869"></span>

<div id="answer-container-45869" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45869-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an OpenStreetMap specific question and should better have been asked at a general GIS or geography Q&amp;A site. (Edit: I see it was cross posted. Not generally a recommended practice as it wastes helpers' time.)</p>
<p>You can use PostGIS for this. PostgreSQL with the PostGIS extension is a database system but often handy to do quick geometry or geography calculations like this:</p>
<pre><code># select st_area(
     st_setsrid(
        st_makebox2d(
            st_makepoint(103.55487,1.490873),st_makepoint(103.740497, 1.585770)
        ),
     4326)::geography);
&#10;    st_area      
------------------
  216753707.811525
(1 row)</code></pre>
<p>The area is returned in square metres.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '15, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '15, 13:26</strong> </span></p>
</div>
</div>
<div id="comments-container-45869" class="comments-container">
<span id="45871"></span>
<div id="comment-45871" class="comment">
<div id="post-45871-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot. Since the image has a resolution of 17408x9216, the area should then be around 141723578m x 75030130m ?</p>
</div>
<div id="comment-45871-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 13:49)</span> <span class="comment-user userinfo">amatek</span>
</div>
</div>
<span id="45872"></span>
<div id="comment-45872" class="comment">
<div id="post-45872-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, 141723578 * 75030130 is 10633538481405140 and not 216753707. Your aspect ratio seems to be about 1.88:1, so you're looking at an area of perhaps 20186 * 10737, assuming the earth is flat.</p>
</div>
<div id="comment-45872-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 16:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45869" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45869-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45864"></span>

<div id="answer-container-45864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45864-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This isn't a simple question, as the answer won't be a square as the Earth isn't flat, so the bottom edge will be a different length to the top edge. Additionally because of the spherical bulge the surface will be greater than the 'flat' area. I think <a href="http://mathforum.org/library/drmath/view/63767.html">this might answer your question</a> if you're willing to approximate the Earth to a sphere.</p>
<p>Edit: Of course this won't be in the format Xkm x Ykm but give the area in square km, if you specify a value for R, the radius of your spherical Earth, in km, for which 6,371km is an approximation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '15, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '15, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-45864" class="comments-container">
<span id="45865"></span>
<div id="comment-45865" class="comment">
<div id="post-45865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response. Actually, I downloaded a map enclosed by those coordinates to be used in a large-scale simulation. Since the image is in XxY format (resolution of 17,408 x 9,216 to be precise), I would like to get an approximate value for my simulation area.</p>
</div>
<div id="comment-45865-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 11:50)</span> <span class="comment-user userinfo">amatek</span>
</div>
</div>
</div>
<div id="comment-tools-45864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45864-form-container" class="comment-form-container">
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

