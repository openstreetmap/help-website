+++
type = "question"
title = "How to use country specific map like https://openstreetmap.in"
description = '''Hi I know there are some discussions in which people have raised concern on conflicting country boundaries in https://www.openstreetmap.org.  To resolve it I want to use country specific map like https://www.openstreetmap.in I am using following code snippet to initialize map for my application. Can...'''
date = "2018-09-28T08:17:00Z"
lastmod = "2018-09-28T10:44:00Z"
weight = 66074
keywords = [ "boundaries", "maps", "india" ]
aliases = [ "/questions/66074" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to use country specific map like https://openstreetmap.in](/questions/66074/how-to-use-country-specific-map-like-httpsopenstreetmapin)

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
<span id="post-66074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I know there are some discussions in which people have raised concern on conflicting country boundaries in <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a>.</p>
<p>To resolve it I want to use country specific map like <a href="https://www.openstreetmap.in">https://www.openstreetmap.in</a></p>
<p>I am using following code snippet to initialize map for my application. Can anybody please tell me how to use <a href="https://www.openstreetmap.in">https://www.openstreetmap.in</a> some sample code. <strong>Is there any parameter which can load country specific map.</strong></p>
<pre><code>var map = new ol.Map({
        target: &#39;map&#39;,
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([37.41, 8.82]),
          zoom: 4
        })
      });</code></pre>
<p>I do not want to edit or maintain my own map database server instead use country specific map.</p>
<p>Atul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-india" rel="tag" title="see questions tagged &#39;india&#39;">india</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '18, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/5e50c9edcf83e1ca9686e10db544679d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atul%20S&#39;s gravatar image" />
<p><span>Atul S</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atul S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66074" class="comments-container">
&#10;</div>
<div id="comment-tools-66074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66074-form-container" class="comment-form-container">
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

<span id="66079"></span>

<div id="answer-container-66079" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66079-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Atul S has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to give OpenLayers the URL for the openstreetmap.in tiles you want to use, as described in the documentation.</p>
<p>You currently have a line of code which reads:</p>
<pre><code>source: new ol.source.OSM()</code></pre>
<p>which loads tiles from the standard openstreetmap.org server. Since you want to use openstreetmap.in's tiles instead, you'll need to include the URL for the tiles you want. This is usually of the format:</p>
<pre><code>source: new ol.source.OSM({url: &quot;//{a-c}.address.of.the.tile.server/{z}/{x}/{y}.png&quot;})</code></pre>
<p>You can usually find out what this is by right-clicking a map tile on openstreetmap.in, selecting 'Open Image in New Tab', and looking at the URL. Make sure you have the permission of the people who operate the tileserver first.</p>
<p>In this case, the openstreetmap.in people have generously given permission for "personal projects", and you can find the URL to use documented here: <a href="https://github.com/osm-in/openstreetmap.in#using-this-map">https://github.com/osm-in/openstreetmap.in#using-this-map</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '18, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66079" class="comments-container">
&#10;</div>
<div id="comment-tools-66079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66078"></span>

<div id="answer-container-66078" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66078-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM itself doesn't have a concept of country-specific data: there's one single database, with everything merged together in the same namespace In the case of contested borders, usually all sets of borders are included, but only one set can be the default one. What country-specific map renderings do is they change their rendering rules or their data-importing step to make sure that the "correct" set of borders is chosen.</p>
<p>You haven't said which set of disputed borders you were interested in. Maybe you're lucky and somebody else has done the job of creating tiles for that worldview, in which case you can probably (check the TOU) use their tiles on your website. See the <a href="https://openlayers.org/">openlayer</a> docs to change the tiles displayed. You might want to look at <a href="https://leafletjs.com/">leaftet</a> instead wich is a bit easyer to use.</p>
<p>If nobody created the right tiles for you, you'll have to host them yourself. It's not that hard to do nowadays but out of scope for this answer, so I'll let you search for tutorials. As for choosing a specific set of boundaries, how this is done for openstreetmap.in is explained by <a href="https://www.openstreetmap.org/user/PlaneMad/diary/38176">this diary entry</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '18, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-66078" class="comments-container">
&#10;</div>
<div id="comment-tools-66078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66078-form-container" class="comment-form-container">
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

