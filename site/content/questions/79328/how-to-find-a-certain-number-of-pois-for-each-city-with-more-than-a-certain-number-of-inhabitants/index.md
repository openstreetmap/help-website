+++
type = "question"
title = "How to find a certain number of POIs for each city with more than a certain number of inhabitants?"
description = '''I&#x27;m trying to understand how to extract data from overpass-turbo, but it&#x27;s quite difficult for a newbie with my goal. I&#x27;m trying to find a quick way to: 1) isolate only cities with +100,000 inhabitants in Europe and North America 2) for each of them obtain 9 different parks (or any other POI, I mean...'''
date = "2021-03-19T16:09:00Z"
lastmod = "2021-03-21T21:14:00Z"
weight = 79328
keywords = [ "openstreetmap", "overpass", "poi", "overpass-turbo", "city" ]
aliases = [ "/questions/79328" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find a certain number of POIs for each city with more than a certain number of inhabitants?](/questions/79328/how-to-find-a-certain-number-of-pois-for-each-city-with-more-than-a-certain-number-of-inhabitants)

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
<span id="post-79328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to understand how to extract data from overpass-turbo, but it's quite difficult for a newbie with my goal. I'm trying to find a quick way to: 1) isolate only cities with +100,000 inhabitants in Europe and North America 2) for each of them obtain 9 different parks (or any other POI, I mean it could even be 9 different squares)</p>
<p>For the moment the closest thing I've found is <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Pub_tour_in_Dublin">this example</a> for a pub tour in Dublin. I don't ask you to write the code for me, I just need to know if it's feasible or not, so that I don't waste my time with an impossible task. Then of course if you can help me directly with queries it's even better!</p>
<p>Edit: it would be enough to have the possibility of extracting the 9 parks in every city of a given list, I mean even if it's not possible to select the cities from overpass, is it possible to give it a list of (as an example) 1000 cities?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '21, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/dbb5bfc797c4467e0feb771e5c0beb0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sfngll&#39;s gravatar image" />
<p><span>sfngll</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sfngll has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '21, 16:50</strong> </span></p>
</div>
</div>
<div id="comments-container-79328" class="comments-container">
<span id="79344"></span>
<div id="comment-79344" class="comment">
<div id="post-79344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's an Overpass query which provides a start (based on an example on the wiki): <a href="https://overpass-turbo.eu/s/15eN.">https://overpass-turbo.eu/s/15eN.</a> There are numerous things which need tweaking with it (1 km from centre is not large enough, it doesn't limit the number of elements returned, it only works on place=city not all places over 100k, etc., etc.)</p>
</div>
<div id="comment-79344-info" class="comment-info">
<span class="comment-age">(20 Mar '21, 20:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="79348"></span>
<div id="comment-79348" class="comment">
<div id="post-79348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this is helping a lot. Do you know if it's possible to set a limit to the no. of parks? Like "look for 10 parks around this point", without the full list of all parks in that area but just 10 random ones</p>
</div>
<div id="comment-79348-info" class="comment-info">
<span class="comment-age">(21 Mar '21, 16:20)</span> <span class="comment-user userinfo">sfngll</span>
</div>
</div>
<span id="79349"></span>
<div id="comment-79349" class="comment">
<div id="post-79349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nope, or I would have done it!</p>
</div>
<div id="comment-79349-info" class="comment-info">
<span class="comment-age">(21 Mar '21, 21:14)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79328-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

