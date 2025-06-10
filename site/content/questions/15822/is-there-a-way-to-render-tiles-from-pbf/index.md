+++
type = "question"
title = "Is there a way to render tiles from PBF"
description = '''Basically, I would like to load the OSM data and render tiles directly from the source data using Java. I imagine there are a lot of steps in between. However, I&#x27;m just looking for some direction to get me started. Some examples would be nice, if available. Otherwise, specifics on what tools and fra...'''
date = "2012-09-05T16:40:00Z"
lastmod = "2012-09-06T23:12:00Z"
weight = 15822
keywords = [ "rendering", "database", "java", "osm", "josm" ]
aliases = [ "/questions/15822" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to render tiles from PBF](/questions/15822/is-there-a-way-to-render-tiles-from-pbf)

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
<span id="post-15822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15822-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Basically, I would like to load the OSM data and render tiles directly from the source data using Java. I imagine there are a lot of steps in between. However, I'm just looking for some direction to get me started. Some examples would be nice, if available. Otherwise, specifics on what tools and frameworks are needed. So far, I've figured I need the following tools and frameworks to get stareted:</p>
<ul>
<li><p><a href="http://download.geofabrik.de/osm/north-america/">OSM Data</a></p></li>
<li><p>A <a href="http://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Choice_of_DBMS">Database</a></p></li>
<li><a href="http://postgis.refractions.net/download/">PostGIS</a> schema or equivalent</li>
<li><p><a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema">http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema</a></p></li>
<li><p>Osmosis framework for parsing PBF files and loading to database or <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/README">preexisting loader</a></p></li>
<li><a href="http://wiki.openstreetmap.org/wiki/OSM_file_formats">http://wiki.openstreetmap.org/wiki/OSM_file_formats</a></li>
<li><a href="http://wiki.openstreetmap.org/wiki/PBF_Format#The_code">http://wiki.openstreetmap.org/wiki/PBF_Format#The_code</a></li>
<li><p><a href="https://github.com/openstreetmap/osmosis">https://github.com/openstreetmap/osmosis</a></p></li>
<li><p>Mapnik Java framework for rendering tiles from database</p></li>
<li><a href="https://github.com/SpatialInteractive/mapnik-jni">https://github.com/SpatialInteractive/mapnik-jni</a></li>
<li><p>Example: <a href="http://svn.openstreetmap.org/applications/utils/mod_tile/gen_tile.cpp">http://svn.openstreetmap.org/applications/utils/mod_tile/gen_tile.cpp</a></p></li>
<li><p>Use <a href="http://josm.openstreetmap.de/">JOSM</a> for display</p></li>
</ul>
<p>I'm aware i could manually build a <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">local map server</a>. However, that just seems a bit overkill for what I'm trying to accomplish. I'm not serving a huge network of users, only the local application. I haven't been able to find much out there, previous examples, for implementing such. Any info is greatly appreciated.</p>
<h2 id="update-9-6-12">Update 9-6-12</h2>
<blockquote>
<p>Can you provide more details on your use-case and requirements?</p>
</blockquote>
<p>Some, I've been using JOSM for some time now. I've created a 2D Scenegraph overlay for rendering 2d objects over the map. The're are three things we are looking to accomplish:</p>
<ul>
<li>Have tiles load faster</li>
<li>Make tiles available offline for demo and local rendering purposes.</li>
<li>Keep a small footprint</li>
</ul>
<blockquote>
<p>What operating system are you using?</p>
</blockquote>
<p>Windows 7 and Mac OS X</p>
<blockquote>
<p>Why Java?</p>
</blockquote>
<p>The customized version of JOSM has to integrate with other tools and frameworks we've written in Java. What I'd eventually like to do is extend JOSM TileSource interface and provide a source which allows JOSM to load from local data. Either directly from a database or binary source.</p>
<blockquote>
<p>Are you planning to integrate rendering and/or viewing into an existing Java application?</p>
</blockquote>
<p>Yes, a flight simulator. The component we use JOSM for allows customers an independent view of airport layouts with runway makers and sensor markers. It's for evaluating airport layouts before loading them into our 3D renderer. Kindof like a preview for missions prior to game-play.</p>
<blockquote>
<p>What kind of (standalone or client/server)?</p>
</blockquote>
<p>Standalone and client-mode.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '12, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/1d6ef3dabfe9d81ca95de1a1d9c32c34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhuntley&#39;s gravatar image" />
<p><span>jhuntley</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhuntley has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '12, 15:35</strong> </span></p>
</div>
</div>
<div id="comments-container-15822" class="comments-container">
<span id="15840"></span>
<div id="comment-15840" class="comment">
<div id="post-15840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide more details on your use-case and requirements? That would help narrowing down possible solutions: What operating system are you using? Why Java? Are you planning to integrate rendering and/or viewing into an existing Java application? What kind of (standalone or client/server)?</p>
</div>
<div id="comment-15840-info" class="comment-info">
<span class="comment-age">(06 Sep '12, 08:06)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
<span id="15861"></span>
<div id="comment-15861" class="comment">
<div id="post-15861-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>About Java usage I can only hint at <a href="http://wiki.openstreetmap.org/wiki/Category:Java">http://wiki.openstreetmap.org/wiki/Category:Java</a></p>
</div>
<div id="comment-15861-info" class="comment-info">
<span class="comment-age">(06 Sep '12, 21:02)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-15822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15822-form-container" class="comment-form-container">
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

<span id="15824"></span>

<div id="answer-container-15824" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15824-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also have a look at <a href="http://mapbox.com/tilemill/">Tilemill</a>.</p>
<p>There are tutorials and howtos about using it on their website, too.</p>
<p>EDIT: or even <a href="http://wiki.openstreetmap.org/wiki/Tirex">Tirex</a></p>
<p>and you already know <a href="http://switch2osm.org">switch2OSM</a>?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '12, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '12, 06:03</strong> </span></p>
</div>
</div>
<div id="comments-container-15824" class="comments-container">
&#10;</div>
<div id="comment-tools-15824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15824-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15834"></span>

<div id="answer-container-15834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15834-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If "Java" is not a high priority requirement, you may have a look at <a href="http://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a>, which is a desktop application for rendering maps. It has a specialized language (kind of DSL) for the rendering rules and a scripting language to control the rendering process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '12, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmehl has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-15834" class="comments-container">
&#10;</div>
<div id="comment-tools-15834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15834-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15871"></span>

<div id="answer-container-15871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you have already integrated JOSM, would it be an option to directly render in JOSM using a <a href="http://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">MapCSS</a> <a href="http://josm.openstreetmap.de/wiki/Styles">style</a>? There also seems to be a <a href="http://wiki.openstreetmap.org/wiki/JOSM/">PBF Plugin</a>.</p>
<p>To avoid loading large files at once, <a href="http://wiki.openstreetmap.org/wiki/OSM2World">OSM2World</a> uses <a href="http://wiki.openstreetmap.org/wiki/Mapsplit">Mapsplit</a> to generate vector tiles.</p>
<p>The <a href="https://github.com/SpatialInteractive/mapnik-jni">mapnik-jni</a> seems <a href="https://groups.google.com/forum/?fromgroups=#!topic/mapnik/yW2fYN84124">not to work</a> on Windows.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '12, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-15871" class="comments-container">
&#10;</div>
<div id="comment-tools-15871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15871-form-container" class="comment-form-container">
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

