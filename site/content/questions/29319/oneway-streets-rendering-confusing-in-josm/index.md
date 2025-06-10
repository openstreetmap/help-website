+++
type = "question"
title = "Oneway streets rendering confusing in JOSM"
description = '''I have a lot of trouble distinguishing the direction of a oneway highway in JOSM. Usually, I select the segment and note the direction in which the big arrowhead is pointing. When the segment is not selected there are small arrows inside the rendered way that do not necessarily point in that same di...'''
date = "2013-12-24T05:52:00Z"
lastmod = "2022-12-01T08:28:00Z"
weight = 29319
keywords = [ "josm", "direction", "rendering", "arrow", "oneway" ]
aliases = [ "/questions/29319" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Oneway streets rendering confusing in JOSM](/questions/29319/oneway-streets-rendering-confusing-in-josm)

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
<span id="post-29319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a lot of trouble distinguishing the direction of a oneway highway in JOSM. Usually, I select the segment and note the direction in which the big arrowhead is pointing. When the segment is not selected there are small arrows inside the rendered way that do not necessarily point in that same direction. The rendering for tertiary highways is worse than that for primaries or trunks-- deciphering the direction those tiny "arrowheads" are pointing (if indeed they are pointing) is practically impossible. Very confusing.</p>
<p>Adding to that confusion is the fact that I'm mapping in a country where you drive on the opposite side from the U.S. and the situation can be very error prone.</p>
<p>Help me understand the best way to visualize the direction of a oneway segment.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-arrow" rel="tag" title="see questions tagged &#39;arrow&#39;">arrow</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '13, 05:52</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-29319" class="comments-container">
<span id="29320"></span>
<div id="comment-29320" class="comment">
<div id="post-29320-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you please post a screenshot? Maybe this problem is caused by your resolution etc. as personally I don't have problems to identify oneway roads in the default style :(</p>
</div>
<div id="comment-29320-info" class="comment-info">
<span class="comment-age">(24 Dec '13, 07:35)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-29319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29319-form-container" class="comment-form-container">
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

<span id="29323"></span>

<div id="answer-container-29323" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29323-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to Hendrikklaas's answer, some settings you can play with in edit -&gt; preferences -&gt; display (first icon) -&gt; OSM data :</p>
<ul>
<li>Draw direction arrows (of the osm way itself, regardless of oneway setting)</li>
<li>Only at the head of a way (I find this clearer)</li>
<li>Draw oneway arrows (you definitely want this one)</li>
<li>Smooth map graphics (try both; turn it off if you load a lot of data and/or have a slow computer)</li>
</ul>
<p>If those easy changes aren't enough, you might be able to tweak the oneway arrow style explicitly :</p>
<ul>
<li>Create a mystle.mapcss file somewhere</li>
<li>Put <strong>:way[oneway=yes]::arrows { z-index: 15; color: #555555; width: 4; dashes: 10,50; }</strong></li>
<li>Play with the values to get something you like (I haven't managed to change the arrow itself, it is probably hardcoded)</li>
<li>Go to preferences -&gt; map setting -&gt; map paint styles, and add your own style file (by clicking the "+" on the right).</li>
<li>Close the preferences and activate the style in the map paint styles dialog (alt+shift+m).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '13, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29323" class="comments-container">
<span id="29331"></span>
<div id="comment-29331" class="comment">
<div id="post-29331-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That is exactly what I was looking for. Adding the arrow at the head of the way works wonderfully.</p>
<p>I'll try the paint style too, but right now I have some multi-lane intersections to check for correctness.</p>
<p>Thanks</p>
</div>
<div id="comment-29331-info" class="comment-info">
<span class="comment-age">(24 Dec '13, 16:30)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="29332"></span>
<div id="comment-29332" class="comment">
<div id="post-29332-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Vincent</span> - I've been playing around with the mapcss file and would like to understand the various parameters. Can you point me to a tutorial or language reference? My Google searches haven't found anything worthwhile ....</p>
</div>
<div id="comment-29332-info" class="comment-info">
<span class="comment-age">(25 Dec '13, 03:53)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="29349"></span>
<div id="comment-29349" class="comment">
<div id="post-29349-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@AlaskaDave</span> See <a href="http://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">the reference page</a> or <a href="http://josm.openstreetmap.de/wiki/Help/Styles/MapCSSTutorial">this tutorial</a> or just the <a href="http://josm.openstreetmap.de/wiki/Styles">styles page</a> which links to them. The documentation isn'guaranteed to match the latest implementation.</p>
</div>
<div id="comment-29349-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 00:07)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="29350"></span>
<div id="comment-29350" class="comment">
<div id="post-29350-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Vincent - I've tried many things but none seem to work exactly as advertised. Plus, the custom styles that do work "get remembered" after I update the mapcss file.</p>
<p>I tried to come up with a style that would better illustrate the oneway direction but have given that up and settled for merely displaying the direction arrow at the head of the ways, as you suggested in bullet 2 above.</p>
</div>
<div id="comment-29350-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 02:16)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-29323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29322"></span>

<div id="answer-container-29322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alaskadave, visualizing a way is part of the rendering, you won’t be able to change that. The direction of a way is managed with the tags in the advanced menus. Look here, <a href="http://wiki.openstreetmap.org/wiki/Key:oneway.">http://wiki.openstreetmap.org/wiki/Key:oneway.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '13, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-29322" class="comments-container">
<span id="29324"></span>
<div id="comment-29324" class="comment">
<div id="post-29324-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"you won’t be able to change that" &lt;- yes you will, you can create your own MapCSS style (as Vincent has correctly explained)</p>
</div>
<div id="comment-29324-info" class="comment-info">
<span class="comment-age">(24 Dec '13, 11:10)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="29327"></span>
<div id="comment-29327" class="comment">
<div id="post-29327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Off course a local map, dont tag for the renderer isnt a frase, is it ?</p>
</div>
<div id="comment-29327-info" class="comment-info">
<span class="comment-age">(24 Dec '13, 12:25)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="29328"></span>
<div id="comment-29328" class="comment">
<div id="post-29328-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The question is about an editor and likewise Richard/Vincent meant changing the editor's stylesheet.</p>
</div>
<div id="comment-29328-info" class="comment-info">
<span class="comment-age">(24 Dec '13, 12:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="86285"></span>
<div id="comment-86285" class="comment">
<div id="post-86285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An oldy while I was looking for a render problem solution in Rapino, Via Fiume <a href="https://www.openstreetmap.org/changeset/129553561#map=18/42.21186/14.18746">https://www.openstreetmap.org/changeset/129553561#map=18/42.21186/14.18746</a></p>
<p>Followed all of the above while using JOSM 18583, always latest stable. Changed a oneway direction using the R key. The red arrow while selected changed direction, the pop-up window proposed to change direction value to oneway=-1 value (yes). Before the change and the way not selected, the way shows grey with little black triangles pointing east. After the change the little black triangles still point east, when the oneway that is on the other side of the block points west with oneway=yes, correctly.</p>
<p>Then, I got a QA alert next day to say the -1 value is deprecated and should use the reverse function to set the direction. Checking in ID Editor indeed the -1 value is on the oneway and then using the reverse in ID twice, the value changed is back to yes, it is in fact in ID always yes. The arrows on the way in ID properly change direction with each reverse operation.</p>
<p>So, does JOSM have 1) a render problem for the little black triangles. 2) an issue with using deprecated value for oneway, either yes or -1</p>
</div>
<div id="comment-86285-info" class="comment-info">
<span class="comment-age">(01 Dec '22, 08:28)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-29322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29322-form-container" class="comment-form-container">
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

