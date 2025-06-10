+++
type = "question"
title = "Could not create datasource for type"
description = '''An error occurred while loading the map layer &#x27;ajt&#x27;: Could not create datasource for type: &#x27;shape&#x27; encountered during parsing of layer &#x27;world&#x27; in Layer at line 245 of &#x27;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#x27;renderd[2600]: An error occurred while loading the map layer &#x27;ajt&#x27;: Could not...'''
date = "2017-04-18T12:24:00Z"
lastmod = "2017-12-02T01:01:00Z"
weight = 55674
keywords = [ "mapnik" ]
aliases = [ "/questions/55674" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Could not create datasource for type](/questions/55674/could-not-create-datasource-for-type)

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
<span id="post-55674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55674-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An error occurred while loading the map layer 'ajt': Could not create datasource for type: 'shape' encountered during parsing of layer 'world' in Layer at line 245 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml'renderd[2600]: An error occurred while loading the map layer 'ajt': Could not create datasource for type: 'shape' encountered during parsing of layer 'world' in Layer at line 245 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml'renderd[2600]: An error occurred while loading the map layer 'ajt': Could not create datasource for type: 'shape' encountered during parsing of layer 'world' in Layer at line 245 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml'renderd[2600]: An error occurred while loading the map layer 'ajt': Could not create datasource for type: 'shape' encountered during parsing of layer 'world' in Layer at line 245 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '17, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f9d8c17b22a009b622cd86dfbe42cf20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abakali&#39;s gravatar image" />
<p><span>abakali</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abakali has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55674" class="comments-container">
<span id="55675"></span>
<div id="comment-55675" class="comment">
<div id="post-55675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing that this is following <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> or similar? If not that, which were you following?</p>
<p>Are there any differences between what you're doing and what is written in those instructions (are you using a different style, perhaps, or are you running a different OS?</p>
<p>What's the full "World" layer definition look like in XML? I'd expect that there would be a file attribute such as "[data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp" - does a file with that name exist, and if so where?</p>
</div>
<div id="comment-55675-info" class="comment-info">
<span class="comment-age">(18 Apr '17, 12:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60932"></span>
<div id="comment-60932" class="comment">
<div id="post-60932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another possibility here is that the mapnik "plugins_dir" in renderd.conf is incorrect. The current github version is:</p>
<pre><code>plugins_dir=/usr/lib/mapnik/3.0/input</code></pre>
<p>which is correct for Ubuntu 16.04, but if you're running an older version of mapnik it might be perhaps:</p>
<pre><code>plugins_dir=/usr/lib/mapnik/2.2/input</code></pre>
</div>
<div id="comment-60932-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 01:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55674-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

