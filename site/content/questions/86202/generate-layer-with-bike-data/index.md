+++
type = "question"
title = "Generate Layer with bike data"
description = '''Hello,  with a small association, we&#x27;ve got a umap with some rendering of overpass that start to not scale right (the number of overpass query, and the size of the region, number of people). The idea is to put in given style some particular piece of roads  (like cycle ways, or bad pavement, or share...'''
date = "2022-11-22T14:54:00Z"
lastmod = "2022-11-25T13:22:00Z"
weight = 86202
keywords = [ "tiles", "bicycle", "layer", "tileserver" ]
aliases = [ "/questions/86202" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Generate Layer with bike data](/questions/86202/generate-layer-with-bike-data)

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
<span id="post-86202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>with a small association, we've got a umap with some rendering of overpass that start to not scale right (the number of overpass query, and the size of the region, number of people).</p>
<p>The idea is to put in given style some particular piece of roads (like cycle ways, or bad pavement, or shared cycleway, etc...), the rest of the map could stay the same</p>
<p>So, i was thinking about generating [vector/image] tiles to replace the umap, but I'm not sure about what's the best option here.</p>
<p>I looked at mapbox / maptiler, but if i understand correctly the schema is a simplification of what OSM offers, and thus is too limiting for our need (we need the full extend of OSM tags)</p>
<p>Then i think about generating tiles with something <a href="https://github.com/Overv/openstreetmap-tile-server">https://github.com/Overv/openstreetmap-tile-server</a> but i feel it will be quite heavy to maintain for our need.</p>
<p>What's the best/easiest solution ?</p>
<p>Thanks for the help :)</p>
<p>note for scale, we will have only a few visitors a day/month, between 16000-30000 km2 max, only a roads/cycleway/path will be customized (or generate for transparent layer)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '22, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d31af35d62ec20f3a2c6a465880e9960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eMerzh&#39;s gravatar image" />
<p><span>eMerzh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eMerzh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '22, 14:56</strong> </span></p>
</div>
</div>
<div id="comments-container-86202" class="comments-container">
&#10;</div>
<div id="comment-tools-86202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86202-form-container" class="comment-form-container">
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

<span id="86214"></span>

<div id="answer-container-86214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86214-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-86214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a tendency I would have suggested using vector tiles for an overlay with the data you are interested in, generated for example with tilemaker <a href="https://github.com/systemed/tilemaker">https://github.com/systemed/tilemaker</a> and a third party base map raster or vector. If you go the vector route you would need to use <a href="https://maplibre.org/">https://maplibre.org/</a> (an open source fork of mapbox-gl) to embed the map in a webpage.</p>
<p>But there are really many ways to skin the cat in this case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '22, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '22, 13:24</strong> </span></p>
</div>
</div>
<div id="comments-container-86214" class="comments-container">
&#10;</div>
<div id="comment-tools-86214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86228"></span>

<div id="answer-container-86228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86228-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to go with the transparent raster tiles, I think the <a href="https://github.com/waymarkedtrails/waymarkedtrails-backend/">waymarkedtrails</a> backend might be useful.</p>
<p>It's meant to display routes (based on relations I suppose), but it might be tweaked to suit your need.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '22, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-86228" class="comments-container">
&#10;</div>
<div id="comment-tools-86228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86228-form-container" class="comment-form-container">
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

