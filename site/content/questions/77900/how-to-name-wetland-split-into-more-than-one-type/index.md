+++
type = "question"
title = "How to name wetland split into more than one type?"
description = '''I&#x27;m mapping nature in national parks in Sweden. Wetlands in Sweden often have names. Most consists just of bog, but some consists of both bog and marsh, which means that they must be split into more than one polygon. In cases where two or more separate areas have the same name I just make a multipol...'''
date = "2020-12-11T11:27:00Z"
lastmod = "2021-02-11T00:21:00Z"
weight = 77900
keywords = [ "naming", "multipolygon" ]
aliases = [ "/questions/77900" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to name wetland split into more than one type?](/questions/77900/how-to-name-wetland-split-into-more-than-one-type)

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
<span id="post-77900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77900-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm mapping nature in national parks in Sweden. Wetlands in Sweden often have names. Most consists just of bog, but some consists of both bog and marsh, which means that they must be split into more than one polygon. In cases where two or more separate areas have the same name I just make a multipolygon with several outers and assign the name to the multipolygon relation, which seems to be the defacto method as group and cluster tags aren't really used. However that only works if all areas are of the same type as the tags need to be on the multipolygon relation, not on the outer ways.</p>
<p>In this case the areas are indeed all wetlands, but of different sub-types bog and marsh. I don't know of any way to name this as a single entity. Any suggestions? The only one I can think of is to have multiple (multi)polygons and just name all the same and hope renderers that see that the polygons are joined and named the same understand that it's the same entity and thus renders a single name rather than one in each sub-polygon.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-naming" rel="tag" title="see questions tagged &#39;naming&#39;">naming</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '20, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d04f4c51fab1e216224e5a7ae978b311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="torger&#39;s gravatar image" />
<p><span>torger</span><br />
<span class="score" title="220 reputation points">220</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="torger has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '20, 11:28</strong> </span></p>
</div>
</div>
<div id="comments-container-77900" class="comments-container">
&#10;</div>
<div id="comment-tools-77900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77900-form-container" class="comment-form-container">
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

<span id="77920"></span>

<div id="answer-container-77920" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77920-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We have the same situation in Uganda. We have large wetlands with a single name consisting of different wetland types like bogs, marshes, swamps, mud plains and reedbeds, even tidal flats. These wetlands are many times encroached so might contain other land uses like farmland and residential areas. We solve this by creating a multipolygon relation, surrounding the complete wetland area and give it a single name. We apply the key boundary, eventually protected area with classification, and natural = wetland. The boundary doesn't get a specific wetland tag. All the different wetland type areas, within the boundary are made part of the relation with role inner. Each defined as natural=wetland and each with wetland=(specific type). Now, as you define the inner areas, you can't share the outer boundary multipolygon with the inner areas. Leave a small gap. Bordering outer areas which are not wetland or water bodies can overlap and share their outer ways with the wetland inner areas. DUe to the small gap this renders fine and doesn't give any warnings in JOSM since none of them are overlapping. It also makes it easy to select any wetlands and update their protection classification. The only problem you get and which we didn't resolve is with wetland bordering large lakes, like in our case Lake Victoria. We do let the wetland outer boundary extend into the lake, so we can contain any tidal flats within the boundary. However you get an overlap between the wetland boundary and the lake, which gives you a warning of overlapping water areas in JOSM. We chosen to keep it this way since the tidal flats are important and the lake level rises continuously, so we need to adjust the high water level line. You could however split it in separate relations to avoid this single warning, we have chosen not to do so. You can see some examples, which we still work on between Entebbe and Kampala. This solution renders fine in most applications and Carto.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '20, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/18e8644e97eab34dbf9a4144f5fe3ab4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bert%20Araali&#39;s gravatar image" />
<p><span>Bert Araali</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bert Araali has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-77920" class="comments-container">
<span id="78793"></span>
<div id="comment-78793" class="comment">
<div id="post-78793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We solved the issue with the outer boundary extending in water bodies like a lake. You avoid any warnings by sharing a node between the lake shore (a closed way or multipolygon) and the boundary. So you can easily extend it into the lake. We map the parts of the wetland in the lake the same way as other parts of the wetland, and include them as inner parts in the wetland relation. They will render with the lake as water body overlayed. We no longer use tidal flats, since the flooded wetland parts are seasonal features or due to rise or decrease in the lake water levels over the years. The part of the boundary in the lake is also part of a second relation of type hazard and defined as a flood zone. The intention is to stop updating the lake shores whenever new satellite imagery comes available. The actual lake shore is somehow the median of the two. These long time high and low water lines don't change that often. You only need to update them when you see the lake has crossed it. I am preparing a wiki page to describe the whole principle, since it can also be used for lake shores where there are no wetlands. I will forward a link here as soon as it is ready. Greetings.</p>
</div>
<div id="comment-78793-info" class="comment-info">
<span class="comment-age">(11 Feb '21, 00:21)</span> <span class="comment-user userinfo">Bert Araali</span>
</div>
</div>
</div>
<div id="comment-tools-77920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77920-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77901"></span>

<div id="answer-container-77901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot handle this situation with a single multipolygon. You must create as many multipolygons as are needed to define the various wetland types, sharing ways when necessary. That means that some ways might be part of one or more other multipolygons. The rendering engine on the OSM webpage can handle such data structures. Other applications or software products may not be able to do that but we don't concern ourselves with issues of rendering.</p>
<p>If they are all part of a single named wetland, then the name would go on the top-level multipolygon, the one that contains the other areas, the individual multipolygons of bog, marsh, or what have you.</p>
<p>Hope this helps</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '20, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-77901" class="comments-container">
<span id="77903"></span>
<div id="comment-77903" class="comment">
<div id="post-77903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, is this considered "legal"? I am familiar with multipolygons, have lots of them already (impossible to map complex nature without them), but the arrangement you suggest I haven't used as I thought it was considered a bad polygon.</p>
<p>If I just add a name tag on the outer way surrounding all sub-polygons, I get warning from JOSM (it wants a type tag as well). If I instead make a new multipolygon based on the outer way and name that, JOSM tells me that it needs a type as well.</p>
<p>And if I do assign a type (generic wetland without subtype) I get a warning that I have overlapping natural features ("water area inside water area", JOSM doesn't differ between water and wetland in error message). If I make this on a multipolygon or directly on the surrounding outer way doesn't matter.</p>
<p>I tried upload a test (both with and without containing multipolygon) to see what OSM-Carto makes of it. It sort of seems like it works, but if you look closer the wetland pattern of the outer polygon is drawn on top of the inner polygons. It seems to me that this is not the way to do it. Which is unfortunate, as it would be quite elegant if it worked. Comments/suggestions?</p>
</div>
<div id="comment-77903-info" class="comment-info">
<span class="comment-age">(11 Dec '20, 14:21)</span> <span class="comment-user userinfo">torger</span>
</div>
</div>
<span id="77907"></span>
<div id="comment-77907" class="comment">
<div id="post-77907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's no problem in having multiple polygons with landuse overlapping in OSM. As Alaska Dave says (&amp; I believe they have extensive experience of this approach) such overlaps can be processed to achieve a wide range of desired results in consuming software. Do not worry too much about how OSM-Carto does it because OSM-Carto is optimised for rapid rendering of recently changed data. For many uses of landuse it is necessary to do some preprocessing (e.g., removing overlaps, merging adjacent similarly tagged landuse, punching holes in landuse (for instance road corridors etc. etc).</p>
</div>
<div id="comment-77907-info" class="comment-info">
<span class="comment-age">(12 Dec '20, 20:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77901-form-container" class="comment-form-container">
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

