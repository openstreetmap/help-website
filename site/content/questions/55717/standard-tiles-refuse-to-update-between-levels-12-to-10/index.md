+++
type = "question"
title = "Standard tiles refuse to update between levels 12 to 10"
description = '''Hi,  I am struggling to attempt to get levels 12 to 10 of the standard mapnik displaying the latest changes. Take for example this farmland at http://www.openstreetmap.org/#map=12/-34.3281/141.2430 If you zoom in one level you will see it in detail whilst content now over 2 months old is not display...'''
date = "2017-04-20T15:33:00Z"
lastmod = "2017-04-23T12:06:00Z"
weight = 55717
keywords = [ "zoomlevel", "tileserver", "update", "mapnik", "standard" ]
aliases = [ "/questions/55717" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Standard tiles refuse to update between levels 12 to 10](/questions/55717/standard-tiles-refuse-to-update-between-levels-12-to-10)

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
<span id="post-55717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55717-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am struggling to attempt to get levels 12 to 10 of the standard mapnik displaying the latest changes. Take for example this farmland at <a href="http://www.openstreetmap.org/#map=12/-34.3281/141.2430">http://www.openstreetmap.org/#map=12/-34.3281/141.2430</a></p>
<p>If you zoom in one level you will see it in detail whilst content now over 2 months old is not displayed. I have attempted appending /dirty to the individual tile urls by using <a href="http://www.informationfreeway.org/">http://www.informationfreeway.org/</a> to no avail. These are not small changes either so it's not activity is too poor to have it activate a render.</p>
<p>Any ideas please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-standard" rel="tag" title="see questions tagged &#39;standard&#39;">standard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '17, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a8dbda930e9da736915267cbe67e5f05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewen%20Hill&#39;s gravatar image" />
<p><span>Ewen Hill</span><br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewen Hill has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '17, 17:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55717" class="comments-container">
&#10;</div>
<div id="comment-tools-55717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55717-form-container" class="comment-form-container">
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

<span id="55748"></span>

<div id="answer-container-55748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55748-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tile level 12 and higher are only rerendered every few months, so this behaviour is expected.</p>
<p>You can try another OSM renderer, e.g. <a href="https://www.openstreetmap.de/karte.html">https://www.openstreetmap.de/karte.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/545d479d671eeaf68d3eb37d373d7188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ff5722&#39;s gravatar image" />
<p><span>ff5722</span><br />
<span class="score" title="141 reputation points">141</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ff5722 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55748" class="comments-container">
<span id="55753"></span>
<div id="comment-55753" class="comment">
<div id="post-55753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks! Could you please link to a source of the "every few months" for 12+ zoom levels fact - if possible? I have in my mind that lower zoom levels are done by batch jobs, too - but do not know the source currently.</p>
</div>
<div id="comment-55753-info" class="comment-info">
<span class="comment-age">(22 Apr '17, 17:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55754"></span>
<div id="comment-55754" class="comment">
<div id="post-55754-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I don't have a source, just experience.</p>
<p>I found this confirming my own experiences too: <a href="http://gis.19327.n8.nabble.com/No-updates-on-zoom-level-12-td5894698.html">http://gis.19327.n8.nabble.com/No-updates-on-zoom-level-12-td5894698.html</a></p>
</div>
<div id="comment-55754-info" class="comment-info">
<span class="comment-age">(22 Apr '17, 18:38)</span> <span class="comment-user userinfo">ff5722</span>
</div>
</div>
<span id="55759"></span>
<div id="comment-55759" class="comment">
<div id="post-55759-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far as I know (which is very little I admit) zoom levels up to 12 are updated at every new stylesheet release; usual timing is once every 1/2 months at least, but there's some technical issue right now: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2605">https://github.com/gravitystorm/openstreetmap-carto/issues/2605</a> <a href="https://github.com/openstreetmap/chef/issues/120">https://github.com/openstreetmap/chef/issues/120</a> <a href="https://github.com/openstreetmap/operations/issues/143">https://github.com/openstreetmap/operations/issues/143</a></p>
</div>
<div id="comment-55759-info" class="comment-info">
<span class="comment-age">(23 Apr '17, 12:06)</span> <span class="comment-user userinfo">Alecs01</span>
</div>
</div>
</div>
<div id="comment-tools-55748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55748-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55719"></span>

<div id="answer-container-55719" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55719-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might have got unlucky and sent the re-render requests when the queue was too full and the request got dropped. <a href="http://tile.openstreetmap.org/12/3653/2463.png/status">http://tile.openstreetmap.org/12/3653/2463.png/status</a> shows for example:</p>
<pre><code>Tile is clean. Last rendered at Thu Feb 02 01:26:18 2017. Last accessed at Thu Apr 20 04:40:38 2017. Stored in file:///srv/tile.openstreetmap.org/tiles/default/12/0/0/233/73/8.meta</code></pre>
<p>I did wonder if perhaps zoom levels 12 and under are handled differently maybe, but the <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map">wiki example I found suggesting adding /dirty</a> used zoom level 7.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '17, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-55719" class="comments-container">
&#10;</div>
<div id="comment-tools-55719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55719-form-container" class="comment-form-container">
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

