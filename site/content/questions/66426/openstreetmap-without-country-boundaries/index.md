+++
type = "question"
title = "OpenStreetmap without country boundaries"
description = '''Hi, I am using OSM with open layers, following is the code snippet. It loads the default world map. How can I load the OSM which does not have any country/city labels and country boundaries? I believe there should be some option to do that. var map = new ol.Map({  target: &#x27;map&#x27;,  layers: [  new ol.l...'''
date = "2018-10-23T12:25:00Z"
lastmod = "2018-10-23T12:34:00Z"
weight = 66426
keywords = [ "openstreetmap", "maps", "map", "boundaries", "country" ]
aliases = [ "/questions/66426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetmap without country boundaries](/questions/66426/openstreetmap-without-country-boundaries)

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
<span id="post-66426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66426-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using OSM with open layers, following is the code snippet. It loads the default world map.</p>
<p>How can I load the OSM which does not have any country/city labels and country boundaries? I believe there should be some option to do that.</p>
<pre><code>var map = new ol.Map({
    target: &#39;map&#39;,
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([72.41, 18.82]),
      zoom: 6
    })
  });</code></pre>
<p>Any help is much appreciated.</p>
<p>Atul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '18, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/5e50c9edcf83e1ca9686e10db544679d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atul%20S&#39;s gravatar image" />
<p><span>Atul S</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atul S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66426" class="comments-container">
&#10;</div>
<div id="comment-tools-66426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66426-form-container" class="comment-form-container">
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

<span id="66427"></span>

<div id="answer-container-66427" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66427-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to find a set of map tiles that doesn't have borders or create one yourself, or use a vector tile map source with a corresponding style.</p>
<p>The long version: what you are currently doing is loading server side generated small (normally 256x256 pixel size) map images. These are pre-generate in one style and for that reason cannot be changed on the fly. To get around this you can either use a set of tiles without borders (you would have to google if you can find if something like that is available) or use vector tiles with a corresponding rendering style that doesn't show borders. Vector tiles contain preprocessed OSM data that then is rendered (that is turned in to a bitmap) locally on the clients computer. This allows the styling to be client specific and more flexible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '18, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '18, 12:34</strong> </span></p>
</div>
</div>
<div id="comments-container-66427" class="comments-container">
<span id="66428"></span>
<div id="comment-66428" class="comment">
<div id="post-66428-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>An example map style that doesn't show country boundaries at medium and high zooms is <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load">this one</a>. If you'd prefer to use a different map style you can, but you'll to edit it so that administrative boundaries aren't shown. If you'd like to do this with OSM's standard style then you can use their <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/DOCKER.md">docker container</a> created for map design.</p>
</div>
<div id="comment-66428-info" class="comment-info">
<span class="comment-age">(23 Oct '18, 12:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66427-form-container" class="comment-form-container">
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

