+++
type = "question"
title = "Indoor mapping: Mapping a shop in a mall that extends over more than one level"
description = '''I have noticed a situation on the map where somebody mapped all (or many) individual stores in a shopping mall, as areas representing the rooms. This shopping mall has some shops that extend over more than one level, connected inside the store with stairs or escalators. Currently, each level is mapp...'''
date = "2021-10-29T13:19:00Z"
lastmod = "2021-11-11T03:18:00Z"
weight = 82409
keywords = [ "indoor", "levels" ]
aliases = [ "/questions/82409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Indoor mapping: Mapping a shop in a mall that extends over more than one level](/questions/82409/indoor-mapping-mapping-a-shop-in-a-mall-that-extends-over-more-than-one-level)

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
<span id="post-82409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82409-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have noticed a situation on the map where somebody mapped all (or many) individual stores in a shopping mall, as areas representing the rooms.</p>
<p>This shopping mall has some shops that extend over more than one level, connected inside the store with stairs or escalators.</p>
<p>Currently, each level is mapped as a separate way (room) and the tags are on both. That is obviously wrong, violates the "one feature, one OSM element" rule, and causes maps to render those shops twice.</p>
<p>What is the right way to map such a situation? Could I put the rooms into a multipolygon relation with "outer" role on both rooms, then put the shop tags on that multipolygon relation?</p>
<p>Just so that people know what situation I am talking about: I am talking about the "Interspar" and "Müller" shops here, in the mall labelled "Wien Mitte - The Mall": <a href="https://www.openstreetmap.org/#map=19/48.20717/16.38546">https://www.openstreetmap.org/#map=19/48.20717/16.38546</a></p>
<p>Thanks in advance for any advice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-levels" rel="tag" title="see questions tagged &#39;levels&#39;">levels</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '21, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d8e8b3b2421046bb07e0f28e51a4cc6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goaned&#39;s gravatar image" />
<p><span>goaned</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goaned has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82409" class="comments-container">
&#10;</div>
<div id="comment-tools-82409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82409-form-container" class="comment-form-container">
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

<span id="82411"></span>

<div id="answer-container-82411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82411-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My initial thought was simply to add a single indoor room with all levels tagged, eg for Interspar, level=0;1. But it's not that simple of course, because the level=0 and level=1 portions of Interspar have different footprints, with other shops ("New Yorker" and "Tom &amp; White") occupying the non-overlapping areas.</p>
<p>As far as I know, there's no generally accepted tagging standard for mapping multi-level shops like this Interspar that will both 1) accurately specify the footprint of each level, and 2) only tag a single element with shop=supermarket.</p>
<p>Offhand a multipolygon feels wrong to me, and JOSM agrees -- you'll get an "Intersection between multipolygon ways" error. I think the situation would need its own sort of relation, akin to a 3D building relation. (Most 3D buildings don't use relations, but they're needed when upper floors of a building jut out larger than the footprint, especially if they overhang another building.)</p>
<p>Note that there's a dedicated subforum for indoor mapping on the OSM forum site, and a similar question has been sitting unanswered for three years: <a href="https://forum.openstreetmap.org/viewtopic.php?id=63721">https://forum.openstreetmap.org/viewtopic.php?id=63721</a></p>
<p>I think the right way forward is to bring this up on the tagging mailing list, and eventually write a proposal. This is difficult and often thankless work with no guarantee of a happy ending, so instead many mappers seem to have settled on this method of bending the "one feature, one OSM element" rule in these cases, in order to have something that looks nice on indoor renderers like OpenLevelUp: <a href="https://openlevelup.net/?l=0#18/48.20683/16.38484">https://openlevelup.net/?l=0#18/48.20683/16.38484</a></p>
<p>Personally I just use shop nodes for these sorts of situations, rather than trying to map the exact floorplan with areas. Doesn't look as nice on OpenLevelUp, but simpler and less incorrect.</p>
<p>(Btw, the Müller shop you mentioned is actually mapped as two different shop types: a chemist on level 1 and a department store on level 2. I have no idea if that's legit.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '21, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '21, 15:58</strong> </span></p>
</div>
</div>
<div id="comments-container-82411" class="comments-container">
<span id="82412"></span>
<div id="comment-82412" class="comment">
<div id="post-82412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. Unfortunate that there's no standard way of doing this. I will simply keep it as is for now unless anyone else answers with a great idea how to keep the indoor mapping but prevent it from being rendered twice.</p>
<p>I also noticed that the Müller shop is tagged in two different ways. It is certainly debatable how Müller stores should be tagged. This is a store that sells cosmetics, hygiene products, but also office supplies, board games, some simple electronics. There is no consistency among their other locations around Vienna either.</p>
</div>
<div id="comment-82412-info" class="comment-info">
<span class="comment-age">(29 Oct '21, 17:12)</span> <span class="comment-user userinfo">goaned</span>
</div>
</div>
<span id="82541"></span>
<div id="comment-82541" class="comment">
<div id="post-82541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also of interest is this issue at the OpenLevelUp dev site: <a href="https://framagit.org/OpenLevelUp/OpenLevelUp/-/issues/79">https://framagit.org/OpenLevelUp/OpenLevelUp/-/issues/79</a></p>
<p>It describes a mullti-level mall shop mapped as a site relation, with the shop tags on the relation and the room ways on each level as the relation members. (And it doesn't render; thus the open issue.) A lot of people hate site relations, though.</p>
<p>IMO the most important goal of any solution would be to maintain compatibility with existing data consumers, who generally expect a shop to be either a single node, a single closed way, or a multipolygon. So I'd suggest something like a "feature_rooms" relation, which would include the traditionally mapped node/way/multipolygon feature in a "feature" role and the component rooms in "room" roles. Software that cared could associate the feature with the rooms and comprehend the indoor details, and meanwhile all existing software would work as before.</p>
<p>But chicken-and-egg-wise, it doesn't feel like there's much point in contemplating a tagging solution if there's no interest from indoor mapping data consumers. And it appears that OpenLevelUp hasn't been updated in over a year.</p>
</div>
<div id="comment-82541-info" class="comment-info">
<span class="comment-age">(11 Nov '21, 03:18)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-82411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82411-form-container" class="comment-form-container">
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

