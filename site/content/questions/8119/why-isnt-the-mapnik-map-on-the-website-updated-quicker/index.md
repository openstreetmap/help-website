+++
type = "question"
title = "Why isn&#x27;t the mapnik map on the website updated quicker?"
description = '''When people edit the OpenStreetMap with editors like Potlatch or JOSM and save their edits, it&#x27;s often taken long time before the main map (Mapnik) on the main website (openstreetmap.org) is updated. The map around e.g. zoom level 14 is updated quite quick (in hours) while on zoom level 11 and lower...'''
date = "2011-09-24T14:56:00Z"
lastmod = "2013-10-08T07:23:00Z"
weight = 8119
keywords = [ "openstreetmap", "rendering", "updates", "mapnik", "map" ]
aliases = [ "/questions/8119" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Why isn't the mapnik map on the website updated quicker?](/questions/8119/why-isnt-the-mapnik-map-on-the-website-updated-quicker)

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
<span id="post-8119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When people edit the OpenStreetMap with editors like Potlatch or JOSM and save their edits, it's often taken long time before the main map (Mapnik) on the main website (<a href="http://openstreetmap.org">openstreetmap.org</a>) is updated. The map around e.g. zoom level 14 is updated quite quick (in hours) while on zoom level 11 and lower it often takes many weeks (or months?) before the map is updated.</p>
<p>I feel this is a <strong>big problem</strong>. When people do something, they want quick feedback. If it takes to long time, people lose motivation to contribute, because it's not rewarding. Simple, contributing to OpenStreetMap is not rewarding when it takes so long time to get the visual map feedback.</p>
<p>What is the reason to why the mapnik map on the main website is not updated more often? Is it just some settings or is it simply lack of CPU power?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '11, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '11, 19:23</strong> </span></p>
</div>
</div>
<div id="comments-container-8119" class="comments-container">
&#10;</div>
<div id="comment-tools-8119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8119-form-container" class="comment-form-container">
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

<span id="8120"></span>

<div id="answer-container-8120" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8120-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-8120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main mapnik map is redered by a single computer (<a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html">yevaud</a>). You can help speed up the servers by <a href="http://donate.openstreetmap.org/">donating to OSMF</a>.</p>
<p>As you have mentioned, tiles on higher zoom levels are usually rendered anew when viewed after a change has been made in their area. Due to the amount of data required to render tiles at low zoom levels and the relatively small changes in these tiles over time, they are rendered less frequently. (Often, a change that affects a z17 or z18 tile is not even visible on a lower zoom, so no reason to re-render the lower zooms on every change.) Sadly there is no mechanism that would tell us when a change is visible on a lower zoom level and when not; such a mechanism could help making better decisions about re-rendering but it will likely use the same amount of time as simply rendering the tile.</p>
<p>(Side note: coastlines are an exception to this; they are processed seperatly, error checked and saved to shapefiles for rendering. This is done on an irregular basis.)</p>
<p>If there are major changes to the data like a new country or landmass or major visual improvements you can contact administrators over <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC</a> and they might rerender the tiles.</p>
<p>The main map is just one of the many ways of providing feedback to the contributors. Osmarender renders zoom levels 12 and up at once.</p>
<p>As a programmer you might also help by speeding up <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> the database importer used for mapnik. Or you can try to speed up mapnik itself. Aside from that there are a lot of problems we need developers for so you are welcome to pick an area you want to help develop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '11, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '11, 18:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-8120" class="comments-container">
<span id="8132"></span>
<div id="comment-8132" class="comment">
<div id="post-8132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like also Osmarender has this big problem on the mainsite. The tiles in level z0-z12 are not rendered for a long time. You are right about Mapnik, level z0-z12 is never rendered by yevaud this year: <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_zoom.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_zoom.html</a></p>
</div>
<div id="comment-8132-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 12:54)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
</div>
<div id="comment-tools-8120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8120-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27009"></span>

<div id="answer-container-27009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Interesting point about the dependencies at a lower level. If the net change is insignificant at a lower (nearer Z0 level)then re-rendering could be avoided. One possible strategy is to use Merkle trees (<a href="http://en.wikipedia.org/wiki/Merkle_tree)">http://en.wikipedia.org/wiki/Merkle_tree)</a> to determine impact to the parent image via use of reverse hashes. If the changes made to the current rendered tile has net change to the parent (or ancestors) then a dirty bit could be applied to an Z/X/Y hierarchical index so subsequent impact can be determined ahead of planet updates.</p>
<p>(now moving somewhat off topic)</p>
<p>The use of hashes can also reduce the effort in rendering and storing duplicate tiles. For example, the ocean tiles will invariably render the same (or similar hashes). Creating the equivalent of symlinks to fixed tiles would result in a reduced saturated rendered filesystem. There are transmission benefits to recognising duplicated tiles by maintaining a map of hash-to-tiles so that duplicated tiles can be referenced rather than explicitly instantiated by server filesystem AND client (possibly by the use of a return code and a reference to the hash).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '13, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a77126808802b84219d4d152e898fc75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geo-san&#39;s gravatar image" />
<p><span>geo-san</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geo-san has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27009" class="comments-container">
<span id="27010"></span>
<div id="comment-27010" class="comment">
<div id="post-27010-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is an interesting approach but not suited for this help site, see Richard's answer.</p>
</div>
<div id="comment-27010-info" class="comment-info">
<span class="comment-age">(08 Oct '13, 07:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8139"></span>

<div id="answer-container-8139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8139-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is really the wrong place to be offering help as a software developer. By definition this site is focused towards more basic questions.</p>
<p>You should post to the <a href="http://lists.openstreetmap.org/listinfo/dev">dev@ mailing list</a> instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '11, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8139" class="comments-container">
<span id="8140"></span>
<div id="comment-8140" class="comment">
<div id="post-8140-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I just wanted to know why the main map wasn't updated for long time. In level z0-z12 (both mapnik and osmarender)</p>
</div>
<div id="comment-8140-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 19:22)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
<span id="8141"></span>
<div id="comment-8141" class="comment">
<div id="post-8141-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Maybe, but you sounded more as if you wanted to open a discussion - elaborating why you think it is a problem and inviting comments -, and again, that would have been a good posting on the mailing list and a less good posting for help.</p>
</div>
<div id="comment-8141-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 19:54)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8139-form-container" class="comment-form-container">
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

