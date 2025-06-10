+++
type = "question"
title = "Find coordinates of bounding box"
description = '''Hello. I started using OSM, great services and all, but I&#x27;m struggling on one point. I have an JS object that contains a list of places, with coordinates etc. I have my actual location with the geolocation API. I want to do a research within 300m and see if some of those places are into the radius. ...'''
date = "2013-01-21T11:12:00Z"
lastmod = "2013-01-22T12:53:00Z"
weight = 19227
keywords = [ "radius", "coordinates" ]
aliases = [ "/questions/19227" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find coordinates of bounding box](/questions/19227/find-coordinates-of-bounding-box)

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
<span id="post-19227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19227-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I started using OSM, great services and all, but I'm struggling on one point. I have an JS object that contains a list of places, with coordinates etc. I have my actual location with the geolocation API. I want to do a research within 300m and see if some of those places are into the radius. So I have found how to call the "radius", with the <a href="http://wiki.openstreetmap.org/wiki/OSM_Protocol_Version_0.6#Retrieving%5Fmap%5Fdata%5Fby%5Fbounding%5Fbox%3A%5FGET%5F.2Fapi.2F0.6.2Fmap">bounding box</a>, but I can't find how to simply get the 4 needed coordinates from my position (assuming I'm at the center of the circle/rectangle, of course). If anyone can help me, it'd be greatly appreciated.</p>
<p>EDIT: So, I've found a piece of code that convert two sets of lat/long in meters, so I compare all my values. Not the most efficient thing ever, but for my need, it was alright. I let my code here, in case anybody needs it someday.<br />
<a href="https://gist.github.com/4554882">Gist</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '13, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/73ee78eb58e0f4767f2c327ad3bfe0a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kilik2049&#39;s gravatar image" />
<p><span>kilik2049</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kilik2049 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '13, 12:55</strong> </span></p>
</div>
</div>
<div id="comments-container-19227" class="comments-container">
&#10;</div>
<div id="comment-tools-19227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19227-form-container" class="comment-form-container">
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

<span id="19250"></span>

<div id="answer-container-19250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19250-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="http://help.openstreetmap.org/upfiles/osm_grab.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '13, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-19250" class="comments-container">
<span id="19251"></span>
<div id="comment-19251" class="comment">
<div id="post-19251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so position map on the area you want and click on export. then you can see the lat lons of top, left right and bottom</p>
</div>
<div id="comment-19251-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 22:46)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="19261"></span>
<div id="comment-19261" class="comment">
<div id="post-19261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, but I was talking about doing it automatically in my code. Thanks anyway.</p>
</div>
<div id="comment-19261-info" class="comment-info">
<span class="comment-age">(22 Jan '13, 12:53)</span> <span class="comment-user userinfo">kilik2049</span>
</div>
</div>
</div>
<div id="comment-tools-19250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19250-form-container" class="comment-form-container">
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

