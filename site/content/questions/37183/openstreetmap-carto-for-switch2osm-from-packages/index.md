+++
type = "question"
title = "openstreetmap-carto for switch2osm &#x27;&#x27;from packages&quot;"
description = '''I have an OSM tile server that I built using switch2osm &quot;Building a tile server from packages&quot;. It works fine. Now I want to make some styling changes. I have set up openstreetmap-carto as per the instructions. When I create the xml file I get the same error as described in a previous post I took th...'''
date = "2014-10-01T12:57:00Z"
lastmod = "2014-10-02T16:03:00Z"
weight = 37183
keywords = [ "openstreetmap", "tilemill", "switch2osm", "tileserver" ]
aliases = [ "/questions/37183" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [openstreetmap-carto for switch2osm ''from packages"](/questions/37183/openstreetmap-carto-for-switch2osm-from-packages)

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
<span id="post-37183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37183-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an OSM tile server that I built using switch2osm "Building a tile server from packages". It works fine. Now I want to make some styling changes. I have set up openstreetmap-carto as per the instructions. When I create the xml file I get the same error as described in a <a href="https://help.openstreetmap.org/questions/14468/format-of-osmxml-stylesheet">previous post</a></p>
<p>I took the advice there and now get SQL errors:</p>
<pre><code>ERROR:  column &quot;pixel_width&quot; does not exist LINE 2: ...y, &quot;natural&quot;, waterway, landuse, name, way_area/(!pixel_widt...                                                              ^ Full sql was: &#39;SELECT * FROM (SELECT     way, &quot;natural&quot;, waterway, landuse, name, way_area/(!pixel_width!*!pixel_height!) AS way_pixels   FROM planet_osm_polygon   WHERE     (waterway IN (&#39;dock&#39;, &#39;riverbank&#39;, &#39;canal&#39;)       OR landuse IN (&#39;reservoir&#39;,&#39;basin&#39;)       OR &quot;natural&quot; IN (&#39;lake&#39;,&#39;water&#39;,&#39;land&#39;,&#39;glacier&#39;,&#39;mud&#39;))     AND building IS NULL     AND way_area/(!pixel_width!*!pixel_height!) &gt; 0.01   ORDER BY z_order, way_area) AS water_areas LIMIT 0&#39;  (encountered during parsing of layer &#39;water-areas&#39; in map &#39;/etc/mapnik-carto/ma</code></pre>
<p>Any help would be fantastic.</p>
<p>Harold Ship</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '14, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/86d98b7622295c7fdc8bdf8f449e4c78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haroldship&#39;s gravatar image" />
<p><span>haroldship</span><br />
<span class="score" title="90 reputation points">90</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haroldship has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37183" class="comments-container">
<span id="37184"></span>
<div id="comment-37184" class="comment">
<div id="post-37184-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A couple of notes from IRC when this was first raised:</p>
<p>The required mapnik version was increased to 2.1.0 <a href="https://github.com/gravitystorm/openstreetmap-carto/commit/f4445a1fff63053fc77bc913659f03f3a4e30f36">in May</a>. I'm fairly sure that someone's been through the "packages" switch2osm instructions since then (though perhaps with a different stylesheet?) so maybe there wasn't a requirement for Mapnik 2.1 immediately.</p>
<p>The lines causing the error with your older Mapnik seem to have been introduced <a href="https://github.com/gravitystorm/openstreetmap-carto/commit/d8afe6fc0c4d5b104a7726d49634b1001a667a8e">on August 14th</a>. One workaround would be to get a local copy of openstreetmap-carto via "git clone <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto"</a> and then checkout an earlier version from there, perhaps via:</p>
<pre><code>git checkout `git rev-list -n 1 --before=&quot;2014-08-14 00:01&quot; master`</code></pre>
<p>That <em>might</em> work.</p>
<p>In the longer term an update to or a replacement for the "packages" version of the switch2osm instructions (which is under way, I believe) is probably what's needed.</p>
</div>
<div id="comment-37184-info" class="comment-info">
<span class="comment-age">(01 Oct '14, 14:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37183-form-container" class="comment-form-container">
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

<span id="37225"></span>

<div id="answer-container-37225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to upgrade your Mapnik version. Without knowing details about how you installed Mapnik and OS versions and other information, I can't suggest an exact course of action but you might want to</p>
<ul>
<li>Use the <a href="https://launchpad.net/~kakrueger/+archive/ubuntu/osm-unstable">osm-unstable</a> PPA</li>
<li>Use the <a href="https://launchpad.net/~mapnik/+archive/ubuntu/v2.2.0">Mapnik v2.2.0 PPA</a> or Ubuntu 14.04 and build mod_tile/renderd from source</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '14, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-37225" class="comments-container">
&#10;</div>
<div id="comment-tools-37225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37225-form-container" class="comment-form-container">
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

