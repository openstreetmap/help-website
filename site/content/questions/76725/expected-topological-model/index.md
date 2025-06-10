+++
type = "question"
title = "Expected Topological Model"
description = '''I am currently mapping a large university (amenity=university). JOSM detects errors (overlapped area) when wooded areas (natural=wood) overlap the university polygon. Only wood/university overlaps are shown as errors, there is no error over the segments of the wooded area that is outside the univers...'''
date = "2020-09-20T16:44:00Z"
lastmod = "2020-09-29T20:24:00Z"
weight = 76725
keywords = [ "josm", "errors", "topology", "areas" ]
aliases = [ "/questions/76725" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Expected Topological Model](/questions/76725/expected-topological-model)

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
<span id="post-76725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76725-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently mapping a large university (amenity=university). JOSM detects errors (overlapped area) when wooded areas (natural=wood) overlap the university polygon. Only wood/university overlaps are shown as errors, there is no error over the segments of the wooded area that is outside the university. To avoid these errors, I see three possibilities.</p>
<ul>
<li>To exclude these elements from the polygon, even if they are actually owned by the university.</li>
<li>To split these elements at polygon’s boundary, using relations (multipolygons)</li>
<li>To do nothing.</li>
</ul>
<p>Which one is expected according to OSM best practices? Thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-topology" rel="tag" title="see questions tagged &#39;topology&#39;">topology</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '20, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '20, 19:55</strong> </span></p>
</div>
</div>
<div id="comments-container-76725" class="comments-container">
<span id="76732"></span>
<div id="comment-76732" class="comment">
<div id="post-76732-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is it possible to link to the area so that people can have a look at exactly what the error is?</p>
<p>It sounds like a false positive, and if that's the case I'd definitely report it on JOSM's trac. For info, I've always found the JOSM devs to be extremely helpful and responsive to things raised with them in this way.</p>
</div>
<div id="comment-76732-info" class="comment-info">
<span class="comment-age">(20 Sep '20, 20:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76746"></span>
<div id="comment-76746" class="comment">
<div id="post-76746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to be clear, is the validator reporting these as errors or warnings? I don't think I've seen overlapping areas reported as errors in the past. If they are now, it could be a bug.</p>
</div>
<div id="comment-76746-info" class="comment-info">
<span class="comment-age">(21 Sep '20, 17:44)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="76893"></span>
<div id="comment-76893" class="comment">
<div id="post-76893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Validator reports the errors as "Other-Overlapping Areas". So it may just be a "Have a look" message.</p>
</div>
<div id="comment-76893-info" class="comment-info">
<span class="comment-age">(29 Sep '20, 20:24)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-76725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76725-form-container" class="comment-form-container">
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

<span id="76744"></span>

<div id="answer-container-76744" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-76744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My basic answer is 3) "do nothing", such cases are quite commmon in OSM and therefore need to be considered by data consumers.</p>
<p>Longer answer below.</p>
<p>There is no need in OSM mapping for a single polygon reflecting landuse/landcover in any given area. The reasons for this are many:</p>
<ul>
<li>Woods, lakes, meadows, residential areas all exist in university, school and hospital campuses. These are either not, or unlikely to be, errors. I would regard the JOSM validation rules to be incorrect in these situations.</li>
<li>Individual polygons will be created by different mappers at different times with different levels of knowledge of OSM, time available to add data, expectations of how the data will be used, quality of imagery at the time the polygon was mapped (which may be vastly different now).</li>
<li>Small polygons with a different class within a larger polygon are very common and entirely reasonable way of mapping the data. The main OSM map produced using CartoCSS makes a number of assumptions based on area and tag to decide which ones should be rendered on top of others. These algorithms work very well. (One exception is in the area you mention, where a small wood overlaps a larger feature, see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2641">https://github.com/gravitystorm/openstreetmap-carto/issues/2641</a> for discussion).</li>
</ul>
<p>If you want a tesselated layer consisting of a contiguous set of polygons you need to post-process OSM data. You may need something like the CartoCSS algorithm, although in practice I have found a simple hierarchy of tags can work well (slide 16 <a href="https://www.slideshare.net/SK53/38-jerry-cloughurbanatlassk53">here</a>). My approach (slide 24 in previous link) involved progressive spatial unions and clipping according to the hierarchy I used. The main complication was dealing with invalid geometries at all stages of the process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '20, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76744" class="comments-container">
&#10;</div>
<div id="comment-tools-76744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76744-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76726"></span>

<div id="answer-container-76726" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76726-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure why amenity would conflict with woodlands and bodies of water, so I assume the issue is nested landuse tagging. Which is one reason that I avoid using landuse for things like wooded areas and bodies of water. I prefer using natural tags. Actually, I prefer landcover tagging (are those trees there "naturally" or because of some human reason? Don't know, don't care, but they are there thus landcover rather than natural). But that is poorly supported so I generally dual tag for natural and landcover.</p>
<p>If something is really a land use, like maybe a reservoir, in the middle of another land use, then make the larger one a multi-polygon if it isn't already. Then make the smaller contained land use an inner polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '20, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-76726" class="comments-container">
<span id="76730"></span>
<div id="comment-76730" class="comment">
<div id="post-76730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wooded areas are labelled as natural=wood, water as natural=water. Only sections of wooded areas that overlap the amenity=university are identified as errors.</p>
</div>
<div id="comment-76730-info" class="comment-info">
<span class="comment-age">(20 Sep '20, 19:26)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
<span id="76735"></span>
<div id="comment-76735" class="comment">
<div id="post-76735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure you haven't accidentally added a wood tag to the university?</p>
</div>
<div id="comment-76735-info" class="comment-info">
<span class="comment-age">(20 Sep '20, 23:55)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-76726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76726-form-container" class="comment-form-container">
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

