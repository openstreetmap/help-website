+++
type = "question"
title = "Using custom icons in your private mapnik rendered tile server"
description = '''Hello, I have been trying to find a solution to this for a long time. I have created my own tile server using http://switch2osm.org/serving-tiles/manually-building-a-tile-server/. Everything runs successfully and i am able to see my changes on the map as and when i make them using JOSM. What i reall...'''
date = "2014-06-16T14:07:00Z"
lastmod = "2014-07-02T18:13:00Z"
weight = 34002
keywords = [ "rendering", "icon", "osm", "mapnik", "custom" ]
aliases = [ "/questions/34002" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using custom icons in your private mapnik rendered tile server](/questions/34002/using-custom-icons-in-your-private-mapnik-rendered-tile-server)

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
<span id="post-34002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34002-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have been trying to find a solution to this for a long time. I have created my own tile server using <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/.">http://switch2osm.org/serving-tiles/manually-building-a-tile-server/.</a> Everything runs successfully and i am able to see my changes on the map as and when i make them using JOSM.</p>
<p>What i really want to know is can i add custom icons to my tiles for a node with key eg. Speed Limit = 40kmph ? I have seen that it is possible to create new nodes (for eg. Trees and Restaurants) which appear on the map instantly after the generation of new tiles.</p>
<p>After reading some documentation i also figured out that mapnik has a stylesheet in which these images are included. When i try to manipulate this image sources i still cannot see my changes on the map.</p>
<p>Is there someone who has done this before or has additional experience to solve this issue?</p>
<p>What i dont want to to is use OpenLayers or leaflet and add custom markers on my map. I want these images embedded in my tiles.</p>
<p>Thanks in advance for any help that you could provide.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '14, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34002" class="comments-container">
<span id="34554"></span>
<div id="comment-34554" class="comment">
<div id="post-34554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any help guys?</p>
</div>
<div id="comment-34554-info" class="comment-info">
<span class="comment-age">(02 Jul '14, 16:32)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
</div>
<div id="comment-tools-34002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34002-form-container" class="comment-form-container">
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

<span id="34557"></span>

<div id="answer-container-34557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34557-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're using the openstreetmap-carto style, I'd expect that you'd have the individual PNGs in that directory. In my case, for example, I've got files such as this one: "<code>~/openstreetmap-carto/symbols/scrub.png</code>" (my exported stylesheet is <code>~/openstreetmap-carto/mapnik.xml</code>).</p>
<p>If you just want to replace symbols in the standard stylesheet I'd imagine that you should just be able to replace the (in this case .png) files; if you want to do something more complicated you might want to use something like TileMill.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '14, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ab5d6583f3873e11af0417ff24b54b74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse2&#39;s gravatar image" />
<p><span>SomeoneElse2</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '14, 16:49</strong> </span></p>
</div>
</div>
<div id="comments-container-34557" class="comments-container">
<span id="34566"></span>
<div id="comment-34566" class="comment">
<div id="post-34566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... see also:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Map_Icons">http://wiki.openstreetmap.org/wiki/Map_Icons</a></p>
</div>
<div id="comment-34566-info" class="comment-info">
<span class="comment-age">(02 Jul '14, 18:13)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-34557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34557-form-container" class="comment-form-container">
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

