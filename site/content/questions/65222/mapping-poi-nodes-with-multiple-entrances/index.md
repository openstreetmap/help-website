+++
type = "question"
title = "Mapping POI nodes with multiple entrances"
description = '''How should we map POI nodes with multiple entrances?  For instance, a restaurant occupies the ground floor of a multi-level building that spans an entire city block. It has a main entrance that corresponds to its official address, and another entrance on a parallel street. If this restaurant were a ...'''
date = "2018-08-08T21:01:00Z"
lastmod = "2018-10-30T15:48:00Z"
weight = 65222
keywords = [ "entrance", "indoor", "wheelchair", "tagging", "poi" ]
aliases = [ "/questions/65222" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping POI nodes with multiple entrances](/questions/65222/mapping-poi-nodes-with-multiple-entrances)

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
<span id="post-65222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65222-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should we map POI nodes with multiple entrances?</p>
<p>For instance, a restaurant occupies the ground floor of a multi-level building that spans an entire city block. It has a main entrance that corresponds to its official address, and another entrance on a parallel street.</p>
<p>If this restaurant were a mapped as way, I'd simply add two entrance nodes to the way's perimeter, <code>entrance=main</code> and <code>entrance=yes</code>. But because there are other tenants in the building -- maybe just flats, or maybe other amenities -- the restaurant is mapped as a node. There's no obvious way to associate entrance nodes with the restaurant node.</p>
<p>Note that:</p>
<ul>
<li>Entrances might be on the same street, or on different streets.</li>
<li>Secondary entrance is often constructed and signed for wheelchair access.</li>
<li>Secondary entrance may be signed with its own differing address, or with the main address, or may have no address.</li>
<li>In some buildings, both main and secondary entrances can correspond to multiple POIs.</li>
<li>When a building contains multiple POIs, a secondary entrance may be signed for a single POI but in fact allow access to all of them.</li>
</ul>
<p>My instinct says there should be a way to join the POI node and the entrance nodes into a relation, but I wouldn't know what to use for type or roles.</p>
<p>Another thought was simply drawing footways connecting the POI to the entrance nodes, but I'm a little uncomfortable mapping a footway that does not, in fact, correspond to anything in real life. Is there an appropriate tag for a way that isn't meant to directly correspond to something geographically? <code>symbolic=yes</code> or <code>isomorphic=yes</code> or <code>visible=routing_only</code>, something like that?</p>
<p>Using the <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">indoor tagging scheme</a> also comes to mind, but ideally I'd want a solution that would allow indoor-tagging-agnostic routing engines to be able to direct users to the best entrance (especially for wheelchair users) without having to deduce, for instance, that an entrance on level 0 corresponds to a POI on level 0 when connected by a corridor on level 0.</p>
<p>Thanks, J</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-wheelchair" rel="tag" title="see questions tagged &#39;wheelchair&#39;">wheelchair</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '18, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '18, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-65222" class="comments-container">
&#10;</div>
<div id="comment-tools-65222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65222-form-container" class="comment-form-container">
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

<span id="65223"></span>

<div id="answer-container-65223" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65223-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-65223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jmapb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From your description, I see no reason not to map this restaurant as an area instead of a node. That the building has other tenants is a good reason to avoid putting the restaurant's tag onto the <em>building area</em>, but it does not stop you from creating an area for the restaurant itself – this second area can even share nodes with the building area. By <strong>mapping the POI as an area</strong>, adding multiple entrances becomes very easy.</p>
<p>Although this particular situation may be solved using an area, though, you are ultimately correct that there are more complex cases where that doesn't work any more – such as an entrance that provides access to multiple amenities. <strong>Using relations</strong> is probably the best solution for those cases. There is no firmly established relation type yet, but there have been some proposals over the years. For example, I believe the <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Associated_Entrance">associated_entrance</a> relation would cover this use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '18, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-65223" class="comments-container">
<span id="65224"></span>
<div id="comment-65224" class="comment">
<div id="post-65224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. A distinct but overlapping area specifically for the POI is a mapping method I've never encountered, but it sounds useful for the simple cases, of which there are many. Also useful for POIs that span the ground floor of multiple buildings. And it would be compatible with the indoor tagging schema.</p>
<p>Offhand, one thing that gives me pause is the difficulty of estimating the footprint of a restaurant etc if it's <em>not</em> occupying the entire floor. How best to tag the fact that this may be a rough estimate? I'd hate to clutter the map with notes.</p>
<p>The associated_entrance relation, though, looks very much like what I had in mind originally. But do any routing engines respect this?</p>
</div>
<div id="comment-65224-info" class="comment-info">
<span class="comment-age">(08 Aug '18, 23:27)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="65225"></span>
<div id="comment-65225" class="comment">
<div id="post-65225-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a>: it's very unlikely that routers support an abandonned proposal with only 44 occurrences (according to taginfo).</p>
</div>
<div id="comment-65225-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 04:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="65237"></span>
<div id="comment-65237" class="comment">
<div id="post-65237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a>: Estimated polygons can still be useful. And for indoor and underground features, them being estimates would be my default assumption unless the changeset has a source indicating otherwise. But yeah, if you want to explicitly indicate that you've been using an estimate, <a href="https://wiki.openstreetmap.org/wiki/Key:note">note</a> or <a href="https://wiki.openstreetmap.org/wiki/Key:fixme">fixme</a> tags would do the job.</p>
<p>And routing engines are of course highly unlikely to already support relations for entrances. But one of the best ways to encourage developers to add support for any new tag is to use it a lot!</p>
</div>
<div id="comment-65237-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 15:15)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="65488"></span>
<div id="comment-65488" class="comment">
<div id="post-65488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks... I've been trying out some polygon areas for shops and restaurants. Here's a restaurant similar to the situation described in the original question, with a main entry on the corner and a wheelchair entry in the back: <a href="https://www.openstreetmap.org/way/617474313">https://www.openstreetmap.org/way/617474313</a></p>
<p>I've also found this is a great way to map large USA drug stores like Duane Reade and Rite Aid which function as grocery/convenience stores 24/7 and contain a pharmacy with daytime-only hours:</p>
<p><a href="https://www.openstreetmap.org/way/617474312">https://www.openstreetmap.org/way/617474312</a> <a href="https://www.openstreetmap.org/way/616812439">https://www.openstreetmap.org/way/616812439</a></p>
<p>I've taken special care to make the the <code>entrance</code> nodes are connected to the POI way only, not to the building polygon, so they won't be mistaken for general entrances to the building. I've even separated them from the building footprint by a couple inches, which might be overkill.</p>
<p>I've also tried out the <code>associated_entrance</code> relation, and though it makes sense to me, JOSM flags it, so I doubt these will survive for too long.</p>
</div>
<div id="comment-65488-info" class="comment-info">
<span class="comment-age">(21 Aug '18, 16:20)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="65489"></span>
<div id="comment-65489" class="comment">
<div id="post-65489-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's all a bit moot at the moment because the available routing doesn't even route to an entrance in the simple case (ie, directions to building that has one and only one entrance node), much less an <code>associated_entrance</code>. But hopefully these things will get more sophisticated with time.</p>
</div>
<div id="comment-65489-info" class="comment-info">
<span class="comment-age">(21 Aug '18, 16:21)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="66568"></span>
<div id="comment-66568" class="comment not_top_scorer">
<div id="post-66568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Something I've just noticed re: mapping POIs as areas versus as nodes -- A POI mapped as a node inside a building will inherit that building's address (if it has one) in Nominatim, a but a POI mapped as a closed way will <strong>not</strong>. Even if the way is entirely inside the building, Nominatim will simply associate it with the nearest road, not the building address. So when mapping POIs as areas, be sure to tag them explicitly with <code>addr:*</code> tags if possible.</p>
</div>
<div id="comment-66568-info" class="comment-info">
<span class="comment-age">(30 Oct '18, 15:48)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-65223" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65223-form-container" class="comment-form-container">
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

