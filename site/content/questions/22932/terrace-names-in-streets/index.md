+++
type = "question"
title = "Terrace names in streets"
description = '''Does anyone know the correct way to indicate a named terrace of houses within a street, please? The case in question is a &#x27;terrace&#x27; of semi-detached houses, so although I could tediously put an address to each house, I opted to enclose them in a landuse=residential and name that, but suspect this is...'''
date = "2013-05-31T21:50:00Z"
lastmod = "2013-07-14T17:10:00Z"
weight = 22932
keywords = [ "houses", "streetnames", "terrace" ]
aliases = [ "/questions/22932" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Terrace names in streets](/questions/22932/terrace-names-in-streets)

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
<span id="post-22932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22932-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone know the correct way to indicate a named terrace of houses within a street, please? The case in question is a 'terrace' of semi-detached houses, so although I could tediously put an address to each house, I opted to enclose them in a landuse=residential and name that, but suspect this is not the preferred method.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-houses" rel="tag" title="see questions tagged &#39;houses&#39;">houses</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-terrace" rel="tag" title="see questions tagged &#39;terrace&#39;">terrace</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '13, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/b96c53807761fec6103da2fc2f003b26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonga&#39;s gravatar image" />
<p><span>Jonga</span><br />
<span class="score" title="101 reputation points">101</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22932" class="comments-container">
&#10;</div>
<div id="comment-tools-22932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22932-form-container" class="comment-form-container">
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

<span id="22935"></span>

<div id="answer-container-22935" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22935-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The technique I have come to favour is roughly as follows:</p>
<p>Create a building for the complete terrace, tag this <code>building_name=Blabla Terrace</code>.</p>
<p>Afterwards there are a number of choices:</p>
<ul>
<li>You can either split the building using the JOSM terracer plug-in and <strong>retain</strong> the original building, or do it manually in which case you will have to recreate the original building.</li>
<li>Remove the superfluous building_name tag from the individual building=house elements.</li>
<li>Add address information to the house polygons. Option 1: to remove the building tags from these just leaving polygons providing the address, and this seems to work for most purposes - thanks to Dee Earley for this idea); Option 2: use the building_part relation to identify the individual properties in the terrace.</li>
</ul>
<p>Here's an example where I have not yet terraced the terrace: <a href="https://www.openstreetmap.org/browse/way/118145309">Peel Villas</a>.</p>
<p>A much simpler way is to represent the terrace as a address interpolation way in which case you can just name the way as here: <a href="https://www.openstreetmap.org/browse/way/210630478">Robroy Terrace</a>.</p>
<p>JOSM of course will protest loudly about overlapping buildings, but much of the information (other than addresses) which one may want to associate with houses in a terrace belong to the terrace (date of construction, no of levels, roof type, building material, builder, architect, etc).</p>
<p>The whole process requires more refinement, but in some places I think accurate information is not merely a nice to have, but essential. For instance Fford Garth Isaf (Lower Garth Road) in Bangor, Gwynedd (<a href="http://osm.org/go/eudHFpOI0-)">http://osm.org/go/eudHFpOI0-)</a> has many terraces, with houses numbered in the terrace. Conventional sequential house numbering has been introduced relatively recently (also on Fford Garth Uchaf, where houses just used to have names).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22935" class="comments-container">
&#10;</div>
<div id="comment-tools-22935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22935-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22936"></span>

<div id="answer-container-22936" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22936-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A mapper near here does as you do. e.g. <a href="http://osm.org/go/0EHxd3Kgf--">http://osm.org/go/0EHxd3Kgf--</a></p>
<p>I generally either put the terrace name in the housename field and the number in the terrace in the housenumber field, or I put both in the house name field. So in SK53's example I might have</p>
<p>addr:housename = 1 Peel Villas addr:street = Gregory Boulevard</p>
<p>None of these solutions feel entirely satisfactory. In the UK you might need to worry about "<a href="http://support.qas.com/all_you_need_to_know_about_uk_address_elements_1478.htm">dependent thoroughfares</a>"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '13, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22936" class="comments-container">
<span id="22937"></span>
<div id="comment-22937" class="comment">
<div id="post-22937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually the houses in Peel Villas all have standard Gregory Boulevard addresses (surveyed but not entered into OSM).</p>
</div>
<div id="comment-22937-info" class="comment-info">
<span class="comment-age">(01 Jun '13, 00:44)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22936-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24231"></span>

<div id="answer-container-24231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24231-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my home town in the UK which I have mapping they are many terraces and other residential areas that have a different name to the road that they sited along how I have solved this problem (though not sure if htis is the right one) is to draw a "living street" along the main street or road then naming the living street by the name of the terrace. Or I have drawn a single terraced house and named it for the whole terrace.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '13, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8281697894512106f7673e11f86add?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="penrithguy&#39;s gravatar image" />
<p><span>penrithguy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="penrithguy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24231" class="comments-container">
&#10;</div>
<div id="comment-tools-24231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24231-form-container" class="comment-form-container">
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

