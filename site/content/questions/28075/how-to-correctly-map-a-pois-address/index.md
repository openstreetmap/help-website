+++
type = "question"
title = "How to correctly map a POI&#x27;s address ?"
description = '''Can someone please tell me how I can properly tag this POI http://www.openstreetmap.org/browse/way/237662466 ? It&#x27;s a shop located in the Pierstraat in Reet. The building has an addr:street tag and is part of an associatedStreet relation. However Nominatim (and openlinkmap) places it in the Pierstra...'''
date = "2013-11-14T06:24:00Z"
lastmod = "2013-11-15T08:27:00Z"
weight = 28075
keywords = [ "nominatim", "address", "poi" ]
aliases = [ "/questions/28075" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to correctly map a POI's address ?](/questions/28075/how-to-correctly-map-a-pois-address)

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
<span id="post-28075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28075-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can someone please tell me how I can properly tag this POI <a href="http://www.openstreetmap.org/browse/way/237662466">http://www.openstreetmap.org/browse/way/237662466</a> ?</p>
<p>It's a shop located in the Pierstraat in Reet. The building has an addr:street tag and is part of an associatedStreet relation. However Nominatim (and openlinkmap) places it in the Pierstraat - Matenstraat. Do a look-up for "Vero Golf" on osm.org</p>
<p>I know this is a complex street that starts as Pierstraat in Reet/Rumst in the east, becomes Pierstraat (Reet side)- Reetsesteenweg (Aartselaar side), Pierstraat (both Reet &amp; Aartselaar), Pierstraat (Aartselaar side) - Matenstraat (Niel side) while traveling to the west.</p>
<p>Nevertheless the building is nearer a Pierstraat-Pierstraat part and has all those additional tags.</p>
<p>So I'm confused, it is correctly tagged and is there a problem in Nominatim, or is my way of tagging incorrect ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '13, 06:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-28075" class="comments-container">
&#10;</div>
<div id="comment-tools-28075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28075-form-container" class="comment-form-container">
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

<span id="28122"></span>

<div id="answer-container-28122" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28122-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="escada has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've mapped it correctly, Nominatim is just not very good at updating associatedStreet relations. It's a <a href="https://trac.openstreetmap.org/ticket/4619">known bug</a>.</p>
<p>Here is what happened: you've originally put the house into <a href="http://www.openstreetmap.org/browse/relation/2594673">this associatedStreet relation</a> which does contain the 'Pierstraat - Matenstraat' street. Nominatim simply uses the first street it finds in such a relation for the name an ignores all tags on the relation itself, so that is where the name comes from. Later you have moved the house to the new relation and that move was not caught by Nominatim's update process. The houses will only be updated when they are changed themselves again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-28122" class="comments-container">
&#10;</div>
<div id="comment-tools-28122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28079"></span>

<div id="answer-container-28079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28079-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://nominatim.openstreetmap.org">nominatim.openstreetmap.org</a> can help to clarify such issues. After <a href="http://nominatim.openstreetmap.org/search.php?q=Vero+Golf">searching for Vero Golf</a> and clicking on <a href="http://nominatim.openstreetmap.org/details.php?place_id=9140432282">(details)</a> you can see Nominatim's internal view for this place including the address hierarchy. According to this, <em>Pierstraat - Matenstraat</em> comes from <a href="http://www.openstreetmap.org/browse/way/22949350">this street</a>. Additionally there is no associatedStreet-relation in the hierarchy. So I guess there is an internal error because Nominatim is supposed to support associatedStreet-relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '13, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28079" class="comments-container">
<span id="28080"></span>
<div id="comment-28080" class="comment">
<div id="post-28080-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks scai for pointing me to the nominatim website. I forgot to check there.</p>
<p>Just as you, I also assumed that it supports associatedStreet-relations. I also thought that it would take the nearest road, or use the information from the building itself. None of this seems to be the case.</p>
</div>
<div id="comment-28080-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 08:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="28085"></span>
<div id="comment-28085" class="comment">
<div id="post-28085-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=9140432282">http://nominatim.openstreetmap.org/details.php?place_id=9140432282</a> suggests last updated on 13th September 2013 and it wasn't added to the associatedStreet relation until 26th September (as such I'd have expected the addr:street on the POI way itself to take priority, but what do I know). Note though that the associatedStreet relation <a href="http://www.openstreetmap.org/browse/relation/2789005">http://www.openstreetmap.org/browse/relation/2789005</a> does contain some ways with role street but the name Pierstraat - Matenstraat so perhaps that is causing the confusion.</p>
</div>
<div id="comment-28085-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 09:22)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="28091"></span>
<div id="comment-28091" class="comment">
<div id="post-28091-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, I overlooked that. So it seems like Nominatim missed the update.<br />
</p>
<p>Regarding your comment on the relation members. The relation itself contains a <em>name</em> tag which is supposed to set the name of the associated street according to the <a href="https://wiki.openstreetmap.org/wiki/Relation:associatedStreet">associatedStreet wiki page</a>. Therefore I guess the names of the actual street members should get ignored. However I don't know how Nominatim's implementation handles such issues.</p>
</div>
<div id="comment-28091-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 10:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28093"></span>
<div id="comment-28093" class="comment">
<div id="post-28093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just read <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview</a> . it has a section on Building indexing. My interpretation now is that it takes the data from one of the street members in the associatedStreet, not from the tags on the relation. Is this correct ?</p>
<p>Thanks EdLoach for pointing me to the "missing" update. I wonder what I did on the 13th. I normally put everything immediately in the associatedStreet relation. Maybe I created a second one by accident and merged the two together on the 26th ?</p>
<p>Is there a way to trigger the update in Nominatim ?</p>
</div>
<div id="comment-28093-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 11:28)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="28123"></span>
<div id="comment-28123" class="comment">
<div id="post-28123-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is no public interface to trigger updates manually. I've done it now for the area. Looks ok now.</p>
</div>
<div id="comment-28123-info" class="comment-info">
<span class="comment-age">(15 Nov '13, 08:27)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-28079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28079-form-container" class="comment-form-container">
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

