+++
type = "question"
title = "Why is the attribution information not updated?"
description = '''When using Openlayers.Layer.Osm and Openlayers.Control.Attribution, the attribution information shows Data CC-By-SA by OpenStreetMap  But OpenStreetMap has changed to ODBL license.  UPDATED I am using data from OSM and tiles from mapnik, how do i attribute both at once?'''
date = "2013-03-14T05:05:00Z"
lastmod = "2013-07-15T08:55:00Z"
weight = 20705
keywords = [ "attribution", "odbl", "openlayers" ]
aliases = [ "/questions/20705" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is the attribution information not updated?](/questions/20705/why-is-the-attribution-information-not-updated)

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
<span id="post-20705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20705-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using Openlayers.Layer.Osm and Openlayers.Control.Attribution, the attribution information shows</p>
<pre><code>Data CC-By-SA by OpenStreetMap</code></pre>
<p>But OpenStreetMap has changed to ODBL license.</p>
<p><strong>UPDATED</strong> I am using data from OSM and tiles from mapnik, how do i attribute both at once?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attribution" rel="tag" title="see questions tagged &#39;attribution&#39;">attribution</span> <span class="post-tag tag-link-odbl" rel="tag" title="see questions tagged &#39;odbl&#39;">odbl</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '13, 05:05</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '13, 09:31</strong> </span></p>
</div>
</div>
<div id="comments-container-20705" class="comments-container">
&#10;</div>
<div id="comment-tools-20705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20705-form-container" class="comment-form-container">
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

<span id="20706"></span>

<div id="answer-container-20706" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20706-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's correct. The latest stable release (2.12) still has an outdated layer attribution. Yet this has already been <a href="https://github.com/openlayers/openlayers/commit/499055e24717d4458879383bd8bafd5884d5cbc0#lib/OpenLayers/Layer/OSM.js">fixed in the repository</a> about 6 months ago. You can apply this change in your version manually or use the <a href="https://github.com/openlayers/openlayers">development version from GitHub</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '13, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20706" class="comments-container">
<span id="20708"></span>
<div id="comment-20708" class="comment">
<div id="post-20708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To answer your edit, there is an example attribution image shown at <a href="http://www.openstreetmap.org/copyright">http://www.openstreetmap.org/copyright</a></p>
</div>
<div id="comment-20708-info" class="comment-info">
<span class="comment-age">(14 Mar '13, 11:44)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="20712"></span>
<div id="comment-20712" class="comment">
<div id="post-20712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which matches the updated OpenLayers attribution :)</p>
</div>
<div id="comment-20712-info" class="comment-info">
<span class="comment-age">(14 Mar '13, 15:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20790"></span>
<div id="comment-20790" class="comment">
<div id="post-20790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Github version says, resource identified as js but transferred with mime type as html. what is work around this?</p>
</div>
<div id="comment-20790-info" class="comment-info">
<span class="comment-age">(18 Mar '13, 09:30)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="20791"></span>
<div id="comment-20791" class="comment">
<div id="post-20791-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What exactly are you trying to download? You can get the <a href="http://raw.github.com/openlayers/openlayers/master/lib/OpenLayers/Layer/OSM.js">single file</a> containing the layer attribution text or the whole <a href="http://github.com/openlayers/openlayers/archive/master.zip">OpenLayers project as a zip</a>. But remember that his is not a stable release.</p>
</div>
<div id="comment-20791-info" class="comment-info">
<span class="comment-age">(18 Mar '13, 10:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20861"></span>
<div id="comment-20861" class="comment">
<div id="post-20861-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i was trying to add the script file directly (using html script tag), no more needed now, i changed the attribution info in app.</p>
</div>
<div id="comment-20861-info" class="comment-info">
<span class="comment-age">(21 Mar '13, 04:09)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="24246"></span>
<div id="comment-24246" class="comment not_top_scorer">
<div id="post-24246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>map.addLayer(new OpenLayers.Layer.OSM("OSM",null,{attribution: "© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors (ODbL)"}));</p>
</div>
<div id="comment-24246-info" class="comment-info">
<span class="comment-age">(15 Jul '13, 08:55)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
</div>
<div id="comment-tools-20706" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-20706-form-container" class="comment-form-container">
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

