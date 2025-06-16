+++
type = "question"
title = "Render a political area exclusively"
description = '''Hello OSM folks! I would like to render a map of a political region without the streets, etc. outside it. How am I doing this? Eg. selecting a state or province. Many thanks, Matthias'''
date = "2011-11-13T09:22:00Z"
lastmod = "2011-11-20T15:47:00Z"
weight = 8954
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/8954" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Render a political area exclusively](/questions/8954/render-a-political-area-exclusively)

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
<span id="post-8954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSM folks!</p>
<p>I would like to render a map of a political region without the streets, etc. outside it.</p>
<p>How am I doing this? Eg. selecting a state or province.</p>
<p>Many thanks, Matthias</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '11, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/5d3a061827ff551c76c706055e638475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthias_&#39;s gravatar image" />
<p><span>matthias_</span><br />
<span class="score" title="55 reputation points">55</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthias_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>14 Nov '11, 17:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span></p>
</div>
</div>
<div id="comments-container-8954" class="comments-container">
<span id="9136"></span>
<div id="comment-9136" class="comment">
<div id="post-9136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for your answers!</p>
<p><a href="http://weait.com/content/combine-openstreetmap-extracts">osmosis</a> and <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Applying_Geographical_Borders">osmconvert</a> are the only necessary tools!</p>
<p>It eventually worked out wonderfully: I've created an extract with a poly-file and then rerun Mapnik.</p>
<ol>
<li>Download country extract from somewhere</li>
<li>Download poly-file of a city from somewhere</li>
<li>Extract subsection with osmconvert <code>bzcat ../../planet/switzerland.osm.bz2 | ./osmconvert - -B=zurich.poly &gt;../../planet/zurich-only.osm</code></li>
</ol>
<p>You can also merge other stuff to it (in case there was subtracted too much stuff): <code>./osmosis --rx ~/planet/switzerland.coastline.osm.bz2 --rx ~/planet/zurich-only.osm.bz2 --merge --wx ~/planet/kanton-zh-with-lakes.osm</code></p>
</div>
<div id="comment-9136-info" class="comment-info">
<span class="comment-age">(20 Nov '11, 15:47)</span> <span class="comment-user userinfo">matthias_</span>
</div>
</div>
</div>
<div id="comment-tools-8954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8954-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="8997"></span>

<div id="answer-container-8997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8997-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, Are you looking to map that you would like to have a copy of on your computer as a PNG or SVG or to later print out <strong>or</strong> a map that can be viewed online (called a slippy map) with multiple zoom levels, similar to google maps ?</p>
<p>If you're looking for something to print out on paper or as an image on your computer, <a href="/questions/3494/create-a-wall-map-of-an-area-50-kilometers-by-120-kilometers">this question</a> can help you answer your question. Note that in this situation, you'll have to download an extract of OSM data (extracts are offered by country, state/province, and metropolitan area.<br />
</p>
<p>If you're looking to make a map to embed on your own website, there's been several other users who have done this and <a href="/questions/136/how-do-i-render-my-own-maps-for-my-website">this question</a> lays out the options of which renderer to use. There may be an existing service that already creates this type of map.</p>
<p>If you have a specific question or are confused about something after reading that over, feel free to ask here, <a href="http://forum.osm.org">forum.osm.org</a>, or on the OSM IRC channel. <a href="http://irc.oftc.net">irc.oftc.net</a> - #osm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span> </br></p>
</div>
</div>
<div id="comments-container-8997" class="comments-container">
<span id="9004"></span>
<div id="comment-9004" class="comment">
<div id="post-9004-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks Skorasaurus.</p>
<p>It's true, my initial question was pretty inprecise.</p>
<p>I would like to have a tile server which serves global tiles, but only has features for the Canton of Zurich.</p>
<p>I found a <a href="http://downloads.cloudmade.com/europe/western_europe/switzerland/zurich#downloads_breadcrumbs">Zurich extract on cloudmade</a>. However, it's pretty outdated (from August).</p>
<p>It's why I downloaded the Switzerland extract from geofabrik. And I thought there is a possibility to render only the features within the political region through a query in Mapniks osm.xml.</p>
<p>Is it possible to adapt the query to something related to this relation <a href="https://www.openstreetmap.org/browse/relation/27970?">https://www.openstreetmap.org/browse/relation/27970?</a></p>
<p>Many thanks again for your fast response! It's very much appreciated!</p>
<p>Best,</p>
<p>Matthias</p>
</div>
<div id="comment-9004-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 10:56)</span> <span class="comment-user userinfo">matthias_</span>
</div>
</div>
<span id="9129"></span>
<div id="comment-9129" class="comment">
<div id="post-9129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Matthias, you should probably look for local support on the talk-ch mailing list. I noticed that you posted on the Swiss forum however that is essentially dormant.</p>
<p>Simon</p>
</div>
<div id="comment-9129-info" class="comment-info">
<span class="comment-age">(19 Nov '11, 21:55)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8997-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9018"></span>

<div id="answer-container-9018" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9018-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">Osmconvert</a> to extract the data from within a bounding polygon.</p>
<p>The bounding polygon needs to be specified in <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">Polygon Filter File Format</a>. That page has links to tools from converting from .osm format to poly format. So you can download the Zurich boundary relation, then convert it to a polygon file.</p>
<p>Then you could download the Switzerland extract, and use Osmosis or Osmconvert to extract just Zurich from that. Then load that extract into your database, and render it as usual with Mapnik.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '11, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9018" class="comments-container">
&#10;</div>
<div id="comment-tools-9018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9018-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9023"></span>

<div id="answer-container-9023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You rather want to use the current boundary-relation of the Canton Zürich to cut your file: <a href="https://www.openstreetmap.org/browse/relation/1690941">https://www.openstreetmap.org/browse/relation/1690941</a></p>
<p>The one you mentioned does not contain any borders.</p>
<p>If the whole cutting procedure by means of Osmosis is too complicated you may just download the data via JOSM and cut it manually, although not being overly elegant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '11, 07:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d732dd313768bd27c4ecc89ab4898c69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FischersFritz&#39;s gravatar image" />
<p><span>FischersFritz</span><br />
<span class="score" title="191 reputation points">191</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FischersFritz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9023" class="comments-container">
&#10;</div>
<div id="comment-tools-9023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9023-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9088"></span>

<div id="answer-container-9088" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mathias,</p>
<p>I've also trying to create a political area as well although I have been unsuccessful so far.</p>
<p>I outlined how to do it in a diary entry - <a href="https://www.openstreetmap.org/user/skorasaurus/diary/15250">https://www.openstreetmap.org/user/skorasaurus/diary/15250</a> although I wouldn't expect it to work for you because it didn't for me, but it may be worth a shot to try.</p>
<p>As FischersFritz mentioned, you'll want to use the boundary-relation that consists of the boundaries of Zurich. <a href="https://www.openstreetmap.org/browse/relation/1690941">https://www.openstreetmap.org/browse/relation/1690941</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '11, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-9088" class="comments-container">
&#10;</div>
<div id="comment-tools-9088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9088-form-container" class="comment-form-container">
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

