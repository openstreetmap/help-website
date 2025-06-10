+++
type = "question"
title = "&quot;rule&quot; about discouraging remapping?"
description = '''In some cases the OSM Wiki offers more than one way to map a specific on the ground situation, without giving a clear preference to one specific mapping solution. An example for this would be that most POIs can be mapped as either polygons or points. I believe there exists an (perhaps only informal)...'''
date = "2019-05-29T11:59:00Z"
lastmod = "2019-05-29T19:20:00Z"
weight = 69363
keywords = [ "rules", "mapping" ]
aliases = [ "/questions/69363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["rule" about discouraging remapping?](/questions/69363/rule-about-discouraging-remapping)

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
<span id="post-69363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69363-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In some cases the OSM Wiki offers more than one way to map a specific on the ground situation, without giving a clear preference to one specific mapping solution. <em>An example for this would be that most POIs can be mapped as either polygons or points.</em></p>
<p>I believe there exists an (perhaps only informal) rule that says that in such cases the solution chosen by the mapper who first mapped such a feature shouldn't be changed, except when one adds significant further details and information. I think this is a logical way to prevent edit wars over minor details caused by differing personal preferences. <em>For example, a mapper shouldn't change a shop mapped as a polygon back to a single point, just because they prefer the method of mapping shops as nodes. But in a slightly different situation, where a mapper provide new information about the extent of a parking area, they would be allowed to move the information from a amenity=parking node to the newly mapped way/relation.</em></p>
<p>Unfortunately, I don't seem to be able to find any place where this rule is written or expressed. I searched the OSM wiki, forum and mailing lists, but the only places where this is mentioned are either very vague or situation-dependent. Of course the mechanical edit guidelines and the "disputes" page somehow touch this topic as well, but only partially explain how to handle this in practice.</p>
<p>Two questions:</p>
<ul>
<li>Is this representation actually the current consensus of the OSM community: “The first mapper has the right to choose whatever mapping method they prefer and it shouldn't be changed except if significant further information is added in the mapping process.”</li>
<li>Are there any places where this was already discussed in the past and/or documented?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '19, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '19, 14:16</strong> </span></p>
</div>
</div>
<div id="comments-container-69363" class="comments-container">
<span id="69371"></span>
<div id="comment-69371" class="comment">
<div id="post-69371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is not an answer to your question, but: I have often remapped restaurants/shops as nodes in cases where the original mapper added the amenity/shop tags directly to building footprints. My impression is that it's incorrect to add these tags directly to a building unless it's a single-purpose building. So if a building has residences or other shops (even vacant), using a node is better.</p>
<p>Another situation would be if the building itself has a name that is different from the POI name. There's no good way to tag that without using a separate element for the POI.</p>
<p>A shop can be mapped as a polygon without any building tag at all, so I'm not sure if "shop mapped as a polygon" in your question implies a building. But if that's the case: I would consider remapping from building to node a mistake if the building is single-purpose, because information (the fact that it's a single-purpose building) has been lost. Likewise, I would consider remapping from building to node to be an improvement if the building is not single-purpose.</p>
</div>
<div id="comment-69371-info" class="comment-info">
<span class="comment-age">(29 May '19, 19:20)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-69363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69363-form-container" class="comment-form-container">
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

<span id="69366"></span>

<div id="answer-container-69366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69366-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't frame it so strictly. Adding information is <em>generally</em> welcome, especially if combined with local knowledge; the last person to touch a restaurant POI can usually be expected to be the last person to have seen the POI on the ground and therefore their knowledge is most current. However, to cite a recent example, the renderer-driven "adding of information" to a <code>natural=bay</code> by converting it into a multipolygon that contains all the coastline is highly contentious because it doesn't really add anything of value (least of all local knowledge) and makes everything more complicated.</p>
<p>The most frequent situation in which what you say is brought up is in the context of switching between "neigbouring areas which are divided by a linear feature glued together" and "neighbouring areas separated by a linear feature" (German: "Flächen verkleben"). For example, the rejected (but for other reasons) proposal <a href="https://wiki.openstreetmap.org/wiki/DE:Proposed_features/Empfehlung_zur_Verwendung_von_Multipolygonen">https://wiki.openstreetmap.org/wiki/DE:Proposed_features/Empfehlung_zur_Verwendung_von_Multipolygonen</a> has the sentence: "Bitte unterlasse es, vorhandene Daten, die nicht dieser Empfehlung entsprechen, ohne konkreten Anlass diesen Empfehlungen anzupassen. Das gebietet der Respekt vor der Arbeit anderer Mapper. Verfeinerst, aktualisierst oder korrigierst du allerdings Daten, kannst du sie den Empfehlungen gemäß umbauen. Änderungen nur des Änderns Willen sind unerwünscht." - in English: "Out of respect for other mappers, please refrain from modifying existing data to match these recommendations unless you have a concrete cause. If you improve, update, or fix data then you can re-structure it. Editing for editing's sake is unwanted."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '19, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69366" class="comments-container">
<span id="69367"></span>
<div id="comment-69367" class="comment">
<div id="post-69367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik. Yes, the case of the "glued areas" example was one that I found as well. I'm wondering if this concept could be generalized to other cases?</p>
<p>Some example of cases where this can come into play are cuttings/embankements (embankement=… vs. <code>man_made=embankement</code>), sidewalks (<code>sidewalk=*</code> vs. <code>footway=sidewalk</code>), addresses (<code>addr:street</code> vs. associatedStreet relations), cycleways (<code>highway=path + bicycle=dedicated</code> vs. <code>highway=cycleway</code>), phone numbers (<code>phone=*</code> vs. <code>contact:phone=*</code>), and perhaps many more.</p>
<p>Do I understand you correctly, that in these cases the mapper(s) who contribute(s) the most recent local knowledge should have the right to use their preferred mapping model, but should at the same time refrain from changing the data merely for the sake of personal preference?</p>
</div>
<div id="comment-69367-info" class="comment-info">
<span class="comment-age">(29 May '19, 14:08)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="69368"></span>
<div id="comment-69368" class="comment">
<div id="post-69368-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think a good rule of thumb would be "don't change the way something is mapped if the only reason you're changing it is your personal preference".</p>
</div>
<div id="comment-69368-info" class="comment-info">
<span class="comment-age">(29 May '19, 17:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-69366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69366-form-container" class="comment-form-container">
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

