+++
type = "question"
title = "How do I change language of a map?"
description = '''I have tried to change the language of my map from hebrew to english. can someone help? &amp;lt;html&amp;gt;  &amp;lt;head&amp;gt;  &amp;lt;title&amp;gt;OpenLayers Demo&amp;lt;/title&amp;gt;  &amp;lt;style type=&quot;text/css&quot;&amp;gt;  html, body, #basicMap {  width: 100%;  height: 100%;  margin: 0;  }  &amp;lt;/style&amp;gt;  &amp;lt;script src=&quot;http://w...'''
date = "2010-12-15T23:05:00Z"
lastmod = "2022-03-06T19:35:00Z"
weight = 1828
keywords = [ "lang", "openlayers", "language" ]
aliases = [ "/questions/1828" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I change language of a map?](/questions/1828/how-do-i-change-language-of-a-map)

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
<span id="post-1828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1828-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have tried to change the language of my map from hebrew to english. can someone help?</p>
<pre><code>&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;OpenLayers Demo&lt;/title&gt;
    &lt;style type=&quot;text/css&quot;&gt;
      html, body, #basicMap {
          width: 100%;
          height: 100%;
          margin: 0;
      }
    &lt;/style&gt;
    &lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
    &lt;script&gt;
      function init() {
        OpenLayers.Lang.setCode(&quot;en&quot;);
        map = new OpenLayers.Map(&quot;basicMap&quot;,{ controls: [] });
&#10;        map.addControl(new OpenLayers.Control.PanZoomBar());
        map.addControl(new OpenLayers.Control.LayerSwitcher());
&#10;        var wms = new OpenLayers.Layer.OSM();
&#10;        map.addLayer(wms);
        map.setCenter(new OpenLayers.LonLat(34.78049,32.08012).transform(
            new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
            new OpenLayers.Projection(&quot;EPSG:900913&quot;) // to Spherical Mercator Projection
          ), 15);
&#10;      }
    &lt;/script&gt;
  &lt;/head&gt;
  &lt;body onload=&quot;init();&quot;&gt;
    &lt;div id=&quot;basicMap&quot;&gt;&lt;/div&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lang" rel="tag" title="see questions tagged &#39;lang&#39;">lang</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '10, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/311ca4a43b36cbaf9b22e4055972e905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="loren2978&#39;s gravatar image" />
<p><span>loren2978</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="loren2978 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '10, 15:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1828" class="comments-container">
&#10;</div>
<div id="comment-tools-1828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1828-form-container" class="comment-form-container">
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

<span id="1843"></span>

<div id="answer-container-1843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1843-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you mean that you want the names on the map to appear in a different language then the answer is that you can't if you're using our tiles (which the OpenLayers OSM layer does) as we only render one set of tiles and the names are part of the tile images.</p>
<p>So you would need to render your own tiles, or find somebody that has rendered some in the language you want and is prepared to let you use them, and then configure OpenLayers to display them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '10, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-1843" class="comments-container">
&#10;</div>
<div id="comment-tools-1843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1843-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83717"></span>

<div id="answer-container-83717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83717-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-83717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see that the question of what language to display labels in a map has been asked before ;-)</p>
<p>I understand that OSM wants to be useful and usable to the natives of a country and so OSM displays labels in that country's language. Unfortunately, the consequence is that OSM maps are at best of limited use to non-native users. I, for instance, would need to know to read Thai in order to use a Thai map and that's not going to happen. For me, OSM is only useful to if a country's labels are in Latin script.</p>
<p>Apparently, OSM uses tiles and the language used in a tile is fixed. That has been the answer given over the years to why OSM cannot display tiles in other than the native language. OK, but why can't there be multiple tiles with the one chosen based on language preference?</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '22, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/68b1b66aaa9a65b53aeef6107da3c6fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vgivanovic&#39;s gravatar image" />
<p><span>vgivanovic</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vgivanovic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83717" class="comments-container">
<span id="83718"></span>
<div id="comment-83718" class="comment">
<div id="post-83718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21485/vgivanovic"></a><a href="https://help.openstreetmap.org/users/21485/vgivanovic">@vgivanovic</a>: I wrote about that just a few days ago, see answer here: <a href="/questions/83654/french-cities-names-on-maps/83659">https://help.openstreetmap.org/questions/83654/french-cities-names-on-maps/83659</a></p>
<p>If you need latin-script world-maps, have a look at <a href="https://wiki.openstreetmap.org/wiki/osMap">https://wiki.openstreetmap.org/wiki/osMap</a> where you'll find ten different versions (Danish, Dutch, Czech, English, French, German, Italian, Polish, Portuguese and Spanish).</p>
</div>
<div id="comment-83718-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 19:35)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-83717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83717-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2068"></span>

<div id="answer-container-2068" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2068-score" class="post-score" title="current number of votes">
-5
</div>
<span id="post-2068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There used to be maps in many languages on <a href="http://cassini.toolserver.org/tile-browse/">http://cassini.toolserver.org/tile-browse/</a> - Does anybody know what has happened to them?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2068" class="comments-container">
<span id="2073"></span>
<div id="comment-2073" class="comment">
<div id="post-2073-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This isn't answer to the original question, it's a new question.</p>
</div>
<div id="comment-2073-info" class="comment-info">
<span class="comment-age">(07 Jan '11, 14:56)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
<span id="2129"></span>
<div id="comment-2129" class="comment">
<div id="post-2129-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They have moved to <a href="http://toolserver.org/~osm/locale/">http://toolserver.org/~osm/locale/</a></p>
<p>I am not sure though what their (wikimedia's) tile usage policy is with respect to using in external projects, and if their english tiles ( <a href="http://toolserver.org/~osm/locale/en.html">http://toolserver.org/~osm/locale/en.html</a> ) could be used in the case of this question</p>
</div>
<div id="comment-2129-info" class="comment-info">
<span class="comment-age">(09 Jan '11, 12:56)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-2068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2068-form-container" class="comment-form-container">
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

