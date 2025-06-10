+++
type = "question"
title = "Improving Watercourse Data"
description = '''The watercourse data in Southern Alberta, Canada (as well as some other parts of the country) is really inaccurate. Hundreds of km&#x27;s of watercourses are not showing in OSM. This data is available in Geogratis - a data set produced by the federal Government of Canada and is free to use (as in not cop...'''
date = "2017-12-14T09:04:00Z"
lastmod = "2017-12-17T15:13:00Z"
weight = 61176
keywords = [ "shapefile", "import", "waterway" ]
aliases = [ "/questions/61176" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Improving Watercourse Data](/questions/61176/improving-watercourse-data)

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
<span id="post-61176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61176-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The watercourse data in Southern Alberta, Canada (as well as some other parts of the country) is really inaccurate. Hundreds of km's of watercourses are not showing in OSM. This data is available in Geogratis - a data set produced by the federal Government of Canada and is free to use (as in not copyrighted). (I know this is important, but my question is more about the technical side of things - let's not start a copyright debate - I am sure the existing set came from them too, but it's old and inaccurate).</p>
<p>I would like to use the dataset to improve OSM. How do I do it? I can download the data in a vector format (shapefile) - one tile at a time... then what do I do? How do I import the whole shapefile (covers about 36km x 27km area) into OSM? Uploading each stream in GPX and Re-tracing it is way too laborious and will produce errors (= not an option). Is there a way to do this in JOSM? How? Is there a procedure that's written out for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '17, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/2c140ca87216d03dd53a5cf101914c72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbcnp&#39;s gravatar image" />
<p><span>pbcnp</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbcnp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61176" class="comments-container">
&#10;</div>
<div id="comment-tools-61176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61176-form-container" class="comment-form-container">
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

<span id="61177"></span>

<div id="answer-container-61177" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61177-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pbcnp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Canada data in OSM suffers from a great many badly done imports. Often, data was already bad and outdated at the time it was imported. It is therefore very important that you first check that the data you wish to import is indeed an improvement.</p>
<p>With waterways data especially, there's a number of potential pitfalls about their classification; you don't want to end up with ditches that are dry most of the time prominently shown on zoom 10.</p>
<p>When importing data, you will be expected to "conflate" it with existing data, i.e. make sure you don't create duplicate copies of things; you cannot simply delete everything that's there and replace it because that <em>might</em> kill someone's diligent tracing from aerial imagery of a river and replace it with a lower quality version from your import. Also, the data you are importing might "interact" with other data that is there (and might have been imported from a different source). Imagine a forest area that ends at the riverbank; you wouldn't want your new river data to meander in and out out of the existing forest, or maybe even cross into an existing building or so. Also, you will be expected to check if the edges of your shapefiles actually match up, something that has been an issue with previous imports in Canada. There is much more to a successful import than converting a shape file and uploading it. It will be laborious, and if this is "not an option" for you, then you cannot import the data.</p>
<p>What you can do is try and distribute the labour onto many shoulders - you could help prepare the data for import, and then seek people who help with the conflation. Ideally, these people would be locals to the area being imported and could bring local knowledge to the table as well.</p>
<p>It would be best if you asked your question again on the <a href="http://lists.openstreetmap.org/listinfo/improrts">imports mailing list</a> where you're likely to find people who have done similar work before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '17, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-61177" class="comments-container">
<span id="61188"></span>
<div id="comment-61188" class="comment">
<div id="post-61188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer! To be clear, I know it will be laborious, but re-tracing each stream would take the work to a whole new level (= two orders of magnitude more time? That's the part I am not excited about). I like the idea of only adding to the OSM data currently there - I don't want to undo anybody's work. I am fine with just doing the local area I know, and only adding tails of creeks that are currently not in OSM. Then I could also re-align them with aerial imagery where possible. Thanks for the suggestions.</p>
</div>
<div id="comment-61188-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 17:20)</span> <span class="comment-user userinfo">pbcnp</span>
</div>
</div>
<span id="61234"></span>
<div id="comment-61234" class="comment">
<div id="post-61234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>pbcnp, don’t forget that IMHO OSM &amp; GPS trails or tracks are congruent, building streams inside a forest without an observation is hardly reliable. Start or stick to the local area and take a hike. And don’t forget to add the local or known names as well. I once walked along Carrot Creek from Lake Minnewanka but looking at it here, <a href="https://www.openstreetmap.org/#map=17/51.16642/-115.39166">https://www.openstreetmap.org/#map=17/51.16642/-115.39166</a> its a bit of a strange mess. (import without survey?) But named, yes. So be carefull.</p>
</div>
<div id="comment-61234-info" class="comment-info">
<span class="comment-age">(17 Dec '17, 15:13)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-61177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61177-form-container" class="comment-form-container">
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

