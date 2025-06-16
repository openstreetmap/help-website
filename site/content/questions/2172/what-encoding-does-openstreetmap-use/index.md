+++
type = "question"
title = "What encoding does OpenStreetMap use ?"
description = '''Hello, I have downloaded shapefiles from http://download.geofabrik.de/osm/europe/. I am after Czech and Slovak republic data, when I look into the files with any shapefiles viewer the name values have odd characters instead of diacritics. I would like to know what encoding is the underlying data in ...'''
date = "2011-01-13T16:26:00Z"
lastmod = "2015-03-02T02:51:00Z"
weight = 2172
keywords = [ "encoding" ]
aliases = [ "/questions/2172" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [What encoding does OpenStreetMap use ?](/questions/2172/what-encoding-does-openstreetmap-use)

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
<span id="post-2172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2172-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have downloaded shapefiles from <a href="http://download.geofabrik.de/osm/europe/"></a><a href="http://download.geofabrik.de/osm/europe/"></a><a href="http://download.geofabrik.de/osm/europe/">http://download.geofabrik.de/osm/europe/</a>. I am after Czech and Slovak republic data, when I look into the files with any shapefiles viewer the name values have odd characters instead of diacritics. I would like to know what encoding is the underlying data in so I could transform it to Unicode or the proper character set.</p>
<p>Thanks for any advice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '11, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/bbe97c3fa23d557d5cdaec1fef8e28db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomas%20Pajonk&#39;s gravatar image" />
<p><span>Tomas Pajonk</span><br />
<span class="score" title="191 reputation points">191</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomas Pajonk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2172" class="comments-container">
&#10;</div>
<div id="comment-tools-2172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2172-form-container" class="comment-form-container">
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

<span id="2173"></span>

<div id="answer-container-2173" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2173-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tomas Pajonk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The shapefiles on <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> are not an official OSM service, and the general OSM community would not know, nor be able to influence, the process that builds them.</p>
<p>Having said that, however, the shape files use UTF-8 encoding like the rest of OSM does. Depending on what system you are using, you should be able to process them correctly if you add a .cpg file like so:</p>
<pre><code> echo &quot;UTF-8&quot; &gt; nameofshapefile.cpg</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '11, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-2173" class="comments-container">
<span id="2177"></span>
<div id="comment-2177" class="comment">
<div id="post-2177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This may be a very daft question. Where can I find the official OSM service ?</p>
</div>
<div id="comment-2177-info" class="comment-info">
<span class="comment-age">(13 Jan '11, 18:15)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="2184"></span>
<div id="comment-2184" class="comment">
<div id="post-2184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no export of shapefiles made by <a href="http://Openstreetmap.org">Openstreetmap.org</a>. There are other ways of solving this e.g. using PostgreSQL + PostGIS, which is as close to a standard way of reading OSM data in GIS applications as you can come.</p>
</div>
<div id="comment-2184-info" class="comment-info">
<span class="comment-age">(14 Jan '11, 00:33)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2185"></span>
<div id="comment-2185" class="comment">
<div id="post-2185-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this. I got confused by the sentence that geofabrik isn't an official service, thinking there may be one.</p>
</div>
<div id="comment-2185-info" class="comment-info">
<span class="comment-age">(14 Jan '11, 08:06)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
</div>
<div id="comment-tools-2173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2173-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2174"></span>

<div id="answer-container-2174" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2174-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Openstreetmap uses Unicode in UTF-8 encoding. The shapefiles however are not the native format of Openstreetmap and could be in some other encoding. Either check if they decode correctly using UTF-8 or check with the geofabrik guys.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '11, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2174" class="comments-container">
&#10;</div>
<div id="comment-tools-2174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2174-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41444"></span>

<div id="answer-container-41444" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41444-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems like you might use <a href="http://osm.kyblsoft.cz/archiv/">http://osm.kyblsoft.cz/archiv/</a> for the Czech republic.</p>
<p>Taken from <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Downloading">https://wiki.openstreetmap.org/wiki/Planet.osm#Downloading</a> -&gt; Regional extract sources.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '15, 02:51</strong></p>
<img src="https://secure.gravatar.com/avatar/78de5d9b760dcdada3d8922b14f892be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkonecny&#39;s gravatar image" />
<p><span>mkonecny</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkonecny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41444" class="comments-container">
&#10;</div>
<div id="comment-tools-41444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41444-form-container" class="comment-form-container">
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

