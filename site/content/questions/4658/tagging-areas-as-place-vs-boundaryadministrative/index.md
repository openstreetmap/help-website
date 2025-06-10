+++
type = "question"
title = "Tagging areas as place=* vs boundary=administrative"
description = '''Summary  When all is said and done, I don&#x27;t believe there is an agreed upon method of combining (or prioritizing) the place=* and boundary=administrative tagging schemas for populated places (e.g., counties and cities). If there is, please feel free to point me to the relevant writeup - or try answe...'''
date = "2011-04-20T00:22:00Z"
lastmod = "2011-04-22T20:25:00Z"
weight = 4658
keywords = [ "administrative", "places", "tagging" ]
aliases = [ "/questions/4658" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging areas as place=\* vs boundary=administrative](/questions/4658/tagging-areas-as-place-vs-boundaryadministrative)

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
<span id="post-4658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4658-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Summary</strong><br />
</p>
<p>When all is said and done, I don't believe there is an agreed upon method of combining (or prioritizing) the place=* and boundary=administrative tagging schemas for populated places (e.g., counties and cities). If there is, please feel free to point me to the relevant writeup - or try answering my questions below.</p>
<p><strong>In detail</strong></p>
<p>I have been reading and rereading pages on Place key and Boundary relation, and I feel we have talked about it here <a href="http://help.openstreetmap.org/questions/4068/when-does-it-make-sense-to-use-place-on-an-area">a lot</a> but I am still confused. Looking up the actual tagging on the ground just adds to my confusion because various user communities do it differently.</p>
<p>How are we supposed to tag an area where the border 1)is the same for the settlement and the administrative area and 2)is shared by two neighboring entities? It seems to me that if I don't want to end up with redundant ways, the only way to tag is using the boundary schema, where each segment segment belongs to a minimum of one and a maximum of two boundary relations.</p>
<p>And if that is the case, shouldn't the boundary/multipolygon schema be preferred over the place=* schema for <strong>all</strong> cases when the admin border and settlement boundary coincide?</p>
<p>And if that's true, then how far away are we from saying that the place=* schema should be applied to nodes only and boundary schema should be applied to polygons? The <a href="http://wiki.openstreetmap.org/wiki/Key:place#As_areas">As areas</a> portion of the Place key wiki page seems to come close to recommending just that, but it can be interpreted as saying we should be applying place=* tags to settlement boundaries that do not coincide with admin areas.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-places" rel="tag" title="see questions tagged &#39;places&#39;">places</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '11, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-4658" class="comments-container">
&#10;</div>
<div id="comment-tools-4658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4658-form-container" class="comment-form-container">
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

<span id="4736"></span>

<div id="answer-container-4736" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4736-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am going to state what transpired in our little conversation as an answer for posterity. The answer also includes bits and pieces of advice I received elsewhere, so feel free to comment if you consider some of it incorrect.</p>
<ol>
<li>There are no tagging differences among polygons with different topology: both closed way polygons and multipolygons can we tagged with either place=*, or boundary=administrative, or both. The difference is in what these polygons represent, not how they are drawn.</li>
<li>Both place=* and boundary=administrative schemas are in use, neither is outdated or deprecated, or superior to the other. They neither supplant nor conflict with each other. In some countries and states they are complementary, in others they can be seen as redundant. That is okay.</li>
<li>If a polygon defines the boundary of a settlement, it gets a place=* tag and related tags. If a polygon represents an administrative boundary, it gets a boundary=administrative + admin_level=* tags. If the administrative boundary coincides with the settlement, then it gets both sets of tags. However, some purists recommend even in this case tagging the closed way polygon as place=* while at the same time creating a boundary relation where this same way is added as the sole outer member, and tagging the relation as boundary=administrative + admin_level, etc. I personally consider this excessive, especially given that Nominatim knows about the logical difference between place and admin boundary and will create two objects while indexing а polygon with both sets of tags.</li>
<li>If an administrative boundary is shared by two or more entities, it should be broken up into segments, each of which should be added to two or more boundary relations. The way segments in this case should only be tagged boundary=administrative + admin_level=* with no name. If the admin boundary is the same as settlement boundary AND all boundaries are shared (this was my initial question) then each place gets represented as a multipolyogn (or boundary relation, which is synonymous), which gets tagged with BOTH place and admin tags, as described in 3. The aforementioned purists would have us create TWO multipolygons for each entity in this case: one tagged as place=*, the other as administrative. Each way segment would then belong to a FOUR relation. That is just too much.</li>
<li>All relations must have a type tag. (Closed way polygons don't.) A boundary relation can be tagged either type=boundary or type=multipolygon. I feel a little uneasy about the fact that <a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">wiki</a> leaves plenty of ambiguity (or is it ambivalence?) on this point. This is especially unfortunate because the leading mappers, in contrast, have a very strong personal opinion in favor of one or the other. Fortunately, software (as wiki prescribes) supports both.</li>
</ol>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '11, 17:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '11, 20:22</strong> </span></p>
</div>
</div>
<div id="comments-container-4736" class="comments-container">
<span id="4741"></span>
<div id="comment-4741" class="comment">
<div id="post-4741-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>2) In some countries, an area enclosed by an administrative area boundary can contain more than one settlement. That's why the two tagging concepts exist and are complementary.</p>
<p>3/4) I don't know why the purists would require duplicate relations with identical sets of members. It certainly isn't necessary as far as OSM itself is concerned.</p>
<p>5) I once tried to slightly modify the wiki to favour multipolygon relations for boundaries, while not at all deprecating type=boundary flat out. Those strong opinions you mentioned caused others to quickly revert my edit.</p>
</div>
<div id="comment-4741-info" class="comment-info">
<span class="comment-age">(22 Apr '11, 20:17)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="4742"></span>
<div id="comment-4742" class="comment">
<div id="post-4742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>2)Absolutely. But my quest has always been to determine which tags should be used in a country where they are the same. 3/4)I can take the mention of the purists out if that could confuse anyone and sounds outlandish.</p>
</div>
<div id="comment-4742-info" class="comment-info">
<span class="comment-age">(22 Apr '11, 20:25)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4736-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4668"></span>

<div id="answer-container-4668" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4668-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO there is a clear distinction between the two, which might overlap in certain cases. Place has nothing to do with administrative boundaries, it is dealing with the topography of settlements. On the other hand, administrative boundaries are only about legal (administrative) limits, they don't deal with the actual built up space.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-4668" class="comments-container">
<span id="4683"></span>
<div id="comment-4683" class="comment">
<div id="post-4683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forgive me for marking your answer down: it is to indicate that I don't consider my question answered. Nothing personal, I know you want to help.</p>
<p>I keep hearing this opinion, so it's not just yours (or else you keep answering my questions on this topic), but it just happens to be that where I live there is no distinction between a settlement and legal limits. The topography is defined by the administrative boundaries. Where one city ends, the next begins, with houses on each side of the street delineating the two "settlements", and residents often confused which city their are in.</p>
</div>
<div id="comment-4683-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 22:49)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4684"></span>
<div id="comment-4684" class="comment not_top_scorer">
<div id="post-4684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This may be unusual and hard for the rest of the world to picture, but this is how we live. About 20 million people, give or take.</p>
</div>
<div id="comment-4684-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 22:53)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4686"></span>
<div id="comment-4686" class="comment">
<div id="post-4686-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>no, there is no problem with this, in your case both do coincide. But you should be aware that this is not the same everywhere, that's why there are two tags for it.</p>
</div>
<div id="comment-4686-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 22:56)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="4687"></span>
<div id="comment-4687" class="comment not_top_scorer">
<div id="post-4687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Agreed, so that means that the answer to the third (and possibly second) part of my question may be "no". Now I just need to figure out the first part. I actually got an interesting suggestion from someone elsewhere: map out the cities as multipolygons and tag the multipolygons as both administrative and place=city. I am happy to go that route if that's an accepted convention. So far everything I have read says to only tag closed ways as places and multipolygons as administrative.</p>
</div>
<div id="comment-4687-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 23:10)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4714"></span>
<div id="comment-4714" class="comment">
<div id="post-4714-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Closed ways and multipolygons, conceptually, are the same. They are as related as a square and a rectangle are. A closed way is an area with no bells and whistles possible, and a multipolygon is also an area, but with the possibility of holes (and multiple outer rings, if you ask some).</p>
</div>
<div id="comment-4714-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 21:15)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="4715"></span>
<div id="comment-4715" class="comment not_top_scorer">
<div id="post-4715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So - to finish your thought - it is perfectly correct to tag a multipolygon with place=*, and it is also correct to tag the same multipolygon with place=* and boundary=administrative + admin_level=* if the administrative boundary coincides with the settlement? Both schemas are in use, they are parallel and non-exclusive? Am I finally getting it? And maybe it is even okay to tag a closed way with boundary=administrative? Or is that taking it too far? If you're saying that closed ways and multipolygons are the same, then there should be no restrictions on tagging either way.</p>
</div>
<div id="comment-4715-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 21:50)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4726"></span>
<div id="comment-4726" class="comment">
<div id="post-4726-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@Lennard</span>: a closed way might describe an area, but also not. Multipolygons do in all cases describe areas. A closed way might just as well be a linear object. This depends only on the associated tags and on interpretation (even more if there is no tag area=yes/no).</p>
</div>
<div id="comment-4726-info" class="comment-info">
<span class="comment-age">(22 Apr '11, 10:14)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="4730"></span>
<div id="comment-4730" class="comment">
<div id="post-4730-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@ponzu</span>: Yes to all your questions except the "taking it too far" one.</p>
<p><span></span><span>@dieterdreist</span>: Thank you for pointing out that some closed ways do not describe areas. I should've mentioned that there are exceptions and as you say: the tags make the difference. I was only thinking about the most common closed ways (landuse, administrative regions, etc) and the example at hand. For these examples (place tagging and administrative areas), a closed way would describe an area.</p>
</div>
<div id="comment-4730-info" class="comment-info">
<span class="comment-age">(22 Apr '11, 10:30)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
</div>
<div id="comment-tools-4668" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-4668-form-container" class="comment-form-container">
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

