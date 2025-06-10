+++
type = "question"
title = "Google maps vs Open Street Map"
description = '''Can i use osm data like longitude and latitude, to draw on google maps? Are the coordinates the same?'''
date = "2016-05-26T17:39:00Z"
lastmod = "2016-05-27T06:21:00Z"
weight = 49846
keywords = [ "coordinates", "googlemaps" ]
aliases = [ "/questions/49846" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Google maps vs Open Street Map](/questions/49846/google-maps-vs-open-street-map)

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
<span id="post-49846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49846-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can i use osm data like longitude and latitude, to draw on google maps? Are the coordinates the same?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-googlemaps" rel="tag" title="see questions tagged &#39;googlemaps&#39;">googlemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '16, 17:39</strong></p>
<img src="https://secure.gravatar.com/avatar/260680ff58506528c6e2a8830a9f5d61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PopaPetru&#39;s gravatar image" />
<p><span>PopaPetru</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PopaPetru has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '16, 23:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49846" class="comments-container">
&#10;</div>
<div id="comment-tools-49846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49846-form-container" class="comment-form-container">
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

<span id="49849"></span>

<div id="answer-container-49849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49849-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-49849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, but OSM uses decimal degrees with a positive sign for North and East and negative for South and West. For example New York USA as a lat long from its url of <a href="https://www.openstreetmap.org/#map=11/40.7069/-73.9696">https://www.openstreetmap.org/#map=11/40.7069/-73.9696</a> which means it is 40.7069 degrees N and 73.9696 degrees W. for the Northing If you multiply fractional bit-- .7069 by 60 you will then have minutes = 42.414' multiply .414 by 60 and you will have the seconds =24 . So NY is 40 deg 42 sec and 24 mins North. I think OSM's DD.dddd is easier don't you? GPXes can be used by OSM and Google. Hope this helps. Note Google can use OSM info, BUT we can't use Google Data to edit OSM. EDIT I have just used those co-ords N 40.7069 W 73.9696 and they work in Google Earth.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '16, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>26 May '16, 19:34</strong> </span></p>
</div>
</div>
<div id="comments-container-49849" class="comments-container">
<span id="49852"></span>
<div id="comment-49852" class="comment">
<div id="post-49852-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thx a lot :D</p>
</div>
<div id="comment-49852-info" class="comment-info">
<span class="comment-age">(26 May '16, 20:11)</span> <span class="comment-user userinfo">PopaPetru</span>
</div>
</div>
</div>
<div id="comment-tools-49849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49849-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49856"></span>

<div id="answer-container-49856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49856-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't understand what you mean by "draw on Google maps". Are you donating OSM data to Google? That is probably not allowed by the license and/or terms of service for either OSM or Google.</p>
<p>Technically, I think the data should overlay as I believe both use the WGS84 datum and the same spherical mercator projection.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '16, 01:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-49856" class="comments-container">
<span id="49857"></span>
<div id="comment-49857" class="comment">
<div id="post-49857-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>No. I'm just creating an Xamarin app and i'd rather use google maps than osmdroid. I'm using this just for learning purposes,for my computer science license. I use osm data for server side and google maps for client side. :D</p>
</div>
<div id="comment-49857-info" class="comment-info">
<span class="comment-age">(27 May '16, 06:21)</span> <span class="comment-user userinfo">PopaPetru</span>
</div>
</div>
</div>
<div id="comment-tools-49856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49856-form-container" class="comment-form-container">
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

