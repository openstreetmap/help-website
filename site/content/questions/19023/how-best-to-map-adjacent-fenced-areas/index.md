+++
type = "question"
title = "How best to map adjacent fenced areas?"
description = '''Say there are several adjacent properties (residential, retail, school, hospital, whatever), all of which have surrounding fences. I see several ways to map these areas, but do all of them work? And which is best?   Map each property as an enclosed area, with adjacent properties sharing nodes. Also ...'''
date = "2013-01-13T11:36:00Z"
lastmod = "2017-02-08T18:13:00Z"
weight = 19023
keywords = [ "relations", "barrier", "tagging", "area" ]
aliases = [ "/questions/19023" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How best to map adjacent fenced areas?](/questions/19023/how-best-to-map-adjacent-fenced-areas)

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
<span id="post-19023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19023-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Say there are several adjacent properties (residential, retail, school, hospital, whatever), all of which have surrounding fences. I see several ways to map these areas, but do all of them work? And which is best?</p>
<ol>
<li><p>Map each property as an enclosed area, with adjacent properties sharing nodes. Also tag each area with barrier=fence. This is simple but dependent on the renderer's ability to interpret the way both as an area (for the property) and as a closed way (for the fence). This would also result in overlapping fences, which I'm not sure would be a problem.</p></li>
<li><p>Also map properties as enclosed areas sharing nodes, but map the fence as a separate way sharing the areas' boundary nodes. This is less ambiguous, and would allow the fence to be tagged with its own properties, but would result in nodes being shared by at least three ways which may be confusing to editors.</p></li>
<li><p>Map each shared border separately, tagging it with barrier=fence, and use multipolygon relations to tag the areas using these ways as members. This seems to be the clearest and least redundant method, but also the most complicated, requiring a lot of relations.</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '13, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '13, 13:10</strong> </span></p>
</div>
</div>
<div id="comments-container-19023" class="comments-container">
<span id="54554"></span>
<div id="comment-54554" class="comment">
<div id="post-54554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please also bear in mind that unlike a lot of fences mapped in the UK it is unlikely that a fence would go through the middle of a semi-detached pair of houses.</p>
</div>
<div id="comment-54554-info" class="comment-info">
<span class="comment-age">(08 Feb '17, 18:13)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-19023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19023-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="19025"></span>

<div id="answer-container-19025" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19025-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-19025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Paul_012 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think your second option is preferable. As you say, it avoids possible confusion of a way representing both a line and an area. There's nothing wrong sharing nodes between different ways.</p>
<p>Plus you can tag other details of the barrier, eg the height or width. Also the fence may not go all of the way around the area, part of it might be a wall or a hedge or a gate etc, so they can be mapped as separate ways. Or leave a gap for a an entrance.</p>
<p>Your third option of using multipolygon relations would be equivalent to this. Though as you say, relations can be more complicated, and confusing to new users, and may get broken. In general I wouldn't use a relation unless it was a large/complicated area - ie made up of dozens of separate ways, or several hundred nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '13, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-19025" class="comments-container">
<span id="19069"></span>
<div id="comment-19069" class="comment">
<div id="post-19069-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Both 2) and 3) are semantically correct, so the choice comes down to what is easyer to create/maintain. Annoyingly, this is slightly subjective, depending on the mapper's proficiency and editor of choice. Because it is subjective, that kind of question comes up often.</p>
<p>I have a slight (subjective :p) preference for 3), unless you have a whole neighbourhood of them to map. Hopefully relations will only get easyer to handle. They need not be restricted to big/complicated areas, I'd say most relations have only a handfull of members.</p>
</div>
<div id="comment-19069-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 09:28)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19025-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19084"></span>

<div id="answer-container-19084" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19084-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would also support option 2, for two reasons.</p>
<ol>
<li>It follows the general principle of mapping what we find on the ground. A school's grounds, a residential area and a fence are three separate entities, and are best mapped as three separate ways.</li>
<li>The method can be extended to represent more complicated areas. Suppose that the school were separated from a residential area by a wall, and had a fence along the rest of its perimeter. The school's grounds are a single closed way, but the perimeter wall and fence are two separate linear ways.</li>
</ol>
<p>A node that is shared between several ways is not really a problem. In Potlatch 2, it can be separated into several separate nodes by pressing shift-J, and each node can then be moved or deleted independently of the others. Any nodes that have not been moved can be recombined by selecting them and pressing J.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '13, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-19084" class="comments-container">
<span id="19090"></span>
<div id="comment-19090" class="comment">
<div id="post-19090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>These arguments are all perfectly valid for option 3 (relation) too. You have one osm entity per real-world entity, and it can be extended to more complicated cases (it's actually better than option 2 in that respect).</p>
<p>Relations are slightly more work to create (a few more clicks, which you save by not creating the same way 3 times), but are easyer to maintain afterwards (no cumbersome glued nodes).</p>
</div>
<div id="comment-19090-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 22:28)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="19122"></span>
<div id="comment-19122" class="comment">
<div id="post-19122-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Having read some more about multipolygons (<a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon)">https://wiki.openstreetmap.org/wiki/Relation:multipolygon)</a> I would accept that method 3 is a perfectly good alternative to method 2. The choice probably depends which is easier to create, and which is easier to edit if anything changes. Does anyone know where I can find an example of method 3 in the map?</p>
</div>
<div id="comment-19122-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 18:52)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="19125"></span>
<div id="comment-19125" class="comment">
<div id="post-19125-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/?lat=51.94675&amp;lon=5.0223&amp;zoom=15&amp;layers=M">Here</a> is an example of method 3 with drains in stead of fences.</p>
<p>The parcels were imported (not by me) as polygons. So there were two lines on top of each other. Adding the drains would have added a third line, which is irritating to edit in JOSM (the editor I use mainly). So I converted the polygons to "multipolygons", deduplicated the lines and added the waterway tags where appropriate.</p>
</div>
<div id="comment-19125-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 20:30)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="19126"></span>
<div id="comment-19126" class="comment">
<div id="post-19126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>&lt;continued&gt;</p>
<p>One of the reasons I didn't continue with this, is that this method of mapping turned out to be confusing for people working with Potlatch. Potlatch does not fill the "advanced multipolygons" so these people tend to overlook all the grass.</p>
</div>
<div id="comment-19126-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 20:30)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-19084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19084-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19142"></span>

<div id="answer-container-19142" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19142-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Create seperate ways for landuse areas and fences, it's alot easier to handle, and fences will not follow the edge of a property.</p>
<p>My second argument is weak, but the first one isn't, it's not fun explaining stacked ways for newbies.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '13, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-19142" class="comments-container">
<span id="54530"></span>
<div id="comment-54530" class="comment">
<div id="post-54530-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Well, in many cases fences <em>do</em> indeed follow the edge of a property. Actually, in many cases fences are the only indicator of the property boundary, so for practical purposes, they <em>are</em> the boundary.</p>
</div>
<div id="comment-54530-info" class="comment-info">
<span class="comment-age">(07 Feb '17, 08:30)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-19142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19142-form-container" class="comment-form-container">
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

