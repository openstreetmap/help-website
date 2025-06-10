+++
type = "question"
title = "OSM data download"
description = '''Hi! I&#x27;m trying to download data from this particular site: http://www.openstreetmap.org/export#map=17/11.24875/125.0047 I get the osm file and them import it with QGIS 2.0.1. The program says the import has been succesfully done but when I open it with QGIS 2.0.1. only points appear to be there. No ...'''
date = "2013-12-20T08:46:00Z"
lastmod = "2013-12-20T20:12:00Z"
weight = 29208
keywords = [ "download", "data" ]
aliases = [ "/questions/29208" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data download](/questions/29208/osm-data-download)

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
<span id="post-29208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29208-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm trying to download data from this particular site: <a href="http://www.openstreetmap.org/export#map=17/11.24875/125.0047">http://www.openstreetmap.org/export#map=17/11.24875/125.0047</a> I get the osm file and them import it with QGIS 2.0.1. The program says the import has been succesfully done but when I open it with QGIS 2.0.1. only points appear to be there. No polyons, no lines. I'm sure there's something I'm not doing correctly, could anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '13, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5ce44dbf703bf8ddd04e69d3248fa560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udonezar&#39;s gravatar image" />
<p><span>udonezar</span><br />
<span class="score" title="45 reputation points">45</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udonezar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29208" class="comments-container">
<span id="29214"></span>
<div id="comment-29214" class="comment">
<div id="post-29214-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>When you view the downloaded OSM file, does it contain lines with "&lt;way="? If yes, then the data is present in the OSM and the problem has to do with QGIS.</p>
</div>
<div id="comment-29214-info" class="comment-info">
<span class="comment-age">(20 Dec '13, 11:41)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-29208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29208-form-container" class="comment-form-container">
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

<span id="29215"></span>

<div id="answer-container-29215" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29215-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A while ago QGIS suffered from a <a href="http://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin">serious bug</a>. In theory, it shouldn't affect your version, but maybe you are using unintentionally the outdated plugin instead of the trunk feature?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '13, 11:41</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-29215" class="comments-container">
<span id="29227"></span>
<div id="comment-29227" class="comment">
<div id="post-29227-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>that was fixed in QGIS 2.0, so it shouldn't be the issue here.</p>
</div>
<div id="comment-29227-info" class="comment-info">
<span class="comment-age">(20 Dec '13, 14:54)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-29215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29215-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29228"></span>

<div id="answer-container-29228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29228-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would recommend you download the data directly through the QGIS OSM plugin. I believe it is included by default in 2.0+. Then go to Vector &gt; OpenStreetMap &gt; Download Data. Include the bounding box values and name for the file. Then add the file as a vector layer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '13, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-29228" class="comments-container">
&#10;</div>
<div id="comment-tools-29228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29228-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29233"></span>

<div id="answer-container-29233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29233-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you also want to try shapefiles created from OSM data: <a href="http://www.geofabrik.de/data/shapefiles.html">http://www.geofabrik.de/data/shapefiles.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '13, 20:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-29233" class="comments-container">
&#10;</div>
<div id="comment-tools-29233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29233-form-container" class="comment-form-container">
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

