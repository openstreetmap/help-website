+++
type = "question"
title = "Tagging US National Forests"
description = '''So I&#x27;ve just moved to the US to Northern Colorado which has the Roosevelt National Forest. It seems that all US National Forests are tagged with landuse=forest. This seems crazy to me for three reasons:  Because this tag is incorrect. landuse=forest implies that the area inside is being active fores...'''
date = "2015-08-14T00:27:00Z"
lastmod = "2015-08-14T15:08:00Z"
weight = 44763
keywords = [ "protected_area", "forest", "usa" ]
aliases = [ "/questions/44763" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging US National Forests](/questions/44763/tagging-us-national-forests)

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
<span id="post-44763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44763-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I've just moved to the US to Northern Colorado which has the Roosevelt National Forest. It seems that all US National Forests are tagged with landuse=forest. This seems crazy to me for three reasons:</p>
<ol>
<li>Because this tag is incorrect. landuse=forest implies that the area inside is being active forested for timber.</li>
<li>Because a lot of the land inside a US National Forest is not actually wood-land, and rather scrub or grassland.</li>
<li>Because it renders badly. I've been doing a lot of work drawing in the land-cover around the <a href="http://www.openstreetmap.org/#map=13/40.6106/-105.2547">Roosevelt National Forest and Rocky Mountain National Park</a>, and it would not be possible to do this work if the whole area were covered with a massive blob of green inside the boundary.</li>
</ol>
<p>From reading the wiki it seems that boundary=protected_area,protect_class=6 is much more appropriate. The only issue is that the boundary is not rendered.</p>
<p>Does anyone know the story is here? I would expect boundary=protected_area to render similarly to leasure=national_park.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-protected_area" rel="tag" title="see questions tagged &#39;protected_area&#39;">protected_area</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-usa" rel="tag" title="see questions tagged &#39;usa&#39;">usa</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '15, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9b82a338cfe9772c5d5eb48646e1e060?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joelholdsworth&#39;s gravatar image" />
<p><span>joelholdsworth</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joelholdsworth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>18 Aug '15, 15:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span></p>
</div>
</div>
<div id="comments-container-44763" class="comments-container">
<span id="44764"></span>
<div id="comment-44764" class="comment">
<div id="post-44764-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have noticed this in other parts of the U.S. as well. The Adirondack Forest Preserve in NY state is tagged that way, even the parts that are classified as wilderness areas where no logging or development of any kind is allowed. I think those tags came along with imports that while helpful often contain bad tags, illogical tags or superfluous points. Like the Tiger street data they're a mixed bag for sure.</p>
</div>
<div id="comment-44764-info" class="comment-info">
<span class="comment-age">(14 Aug '15, 01:08)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="44765"></span>
<div id="comment-44765" class="comment">
<div id="post-44765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On one of the tagging mail lists it was recently suggested that landcover=trees be used to show areas covered by woods/forest. I believe that landuse=forest simply says that it is being managed as a forest area and in the US that includes ranching, mining, recreation, logging, watershed, etc. So landuse and landcover would be orthogonal tagging, one for the management aspects the other for what is actually growing (or not growning) there.</p>
<p>I don't think any renderers honor landcover=trees but I like the concept.</p>
</div>
<div id="comment-44765-info" class="comment-info">
<span class="comment-age">(14 Aug '15, 01:31)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="44771"></span>
<div id="comment-44771" class="comment">
<div id="post-44771-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Completely agree. I did an image showing actual tree cover in a National Forest a couple of years back. Logical extension would be to map the admin HQ in DC as landuse=forest.</p>
</div>
<div id="comment-44771-info" class="comment-info">
<span class="comment-age">(14 Aug '15, 15:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="44772"></span>
<div id="comment-44772" class="comment">
<div id="post-44772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forgot link to image of Prescott National Forest <a href="https://www.flickr.com/photos/sk53_osm/9921095216">https://www.flickr.com/photos/sk53_osm/9921095216</a></p>
</div>
<div id="comment-44772-info" class="comment-info">
<span class="comment-age">(14 Aug '15, 15:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44763-form-container" class="comment-form-container">
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

<span id="44770"></span>

<div id="answer-container-44770" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44770-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-44770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the National Forest boundary, boundary=protected_area is preferred over leisure=national_park--see <a href="http://wiki.openstreetmap.org/wiki/US_Forest_Service_Data#National_Forest_Boundaries">http://wiki.openstreetmap.org/wiki/US_Forest_Service_Data#National_Forest_Boundaries</a>. If you read the text there, it suggests adding landuse=forest if it's pretty much all forest, but logically it should probably be separated--see below. Also note <a href="https://lists.openstreetmap.org/pipermail/talk-us/2015-June/014925.html">this discussion</a> on talk-us in June 2015.</p>
<p>What is actually on the ground (forest, scrub, grassland, etc) is different and should be tagged as such. You can see a discussion of the multiple issues with forest tagging here: <a href="http://wiki.openstreetmap.org/wiki/Forest">http://wiki.openstreetmap.org/wiki/Forest</a>. However, I'd still use it, as it is not going away anytime soon, and maybe add the <a href="http://wiki.openstreetmap.org/wiki/Landcover">landcover</a> tag if you want to support that schema.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '15, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44770" class="comments-container">
&#10;</div>
<div id="comment-tools-44770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44770-form-container" class="comment-form-container">
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

