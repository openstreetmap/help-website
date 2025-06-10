+++
type = "question"
title = "how to use data in &quot;the ESRI format&quot; with potlatch?"
description = '''Hello everybody, I&#x27;m a OSM contributor and I use potlatch2 as editor since years now. Last year, I have added some syrian refugee camps (in Turkey) and these days when going back to the Unitar web site to get information and coordonates of new camps, I discover that sometime a link named &quot;download d...'''
date = "2013-09-03T14:33:00Z"
lastmod = "2013-09-06T22:10:00Z"
weight = 26095
keywords = [ "potlatch2", "import", "osm", "esri" ]
aliases = [ "/questions/26095" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use data in "the ESRI format" with potlatch?](/questions/26095/how-to-use-data-in-the-esri-format-with-potlatch)

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
<span id="post-26095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26095-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody,</p>
<p>I'm a OSM contributor and I use potlatch2 as editor since years now.<br />
Last year, I have added some syrian refugee camps (in Turkey) and these days when going back to the Unitar web site to get information and coordonates of new camps, I discover that sometime a link named "download data in the ESRI format" is available. (e.g. <a href="http://www.unitar.org/unosat/node/44/1802/" title="Al Azraq Refugee Camp">here</a>).<br />
After download, I tried to view the data in potlatch using "vector file"/"shapefile"/file open ..." but I saw nothing. The files downloaded are mainly .gdbtable, .gdbtablx, .atx files, not sure they are understood formats by potlatchs (as shapefile or something else). Any idea?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-esri" rel="tag" title="see questions tagged &#39;esri&#39;">esri</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '13, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/df56a3250b216c7bd62b7252e8a5c4f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bazgal&#39;s gravatar image" />
<p><span>bazgal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bazgal has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-26095" class="comments-container">
&#10;</div>
<div id="comment-tools-26095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26095-form-container" class="comment-form-container">
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

<span id="26096"></span>

<div id="answer-container-26096" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26096-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you'd need to convert this to a different format like shapefile. Assuming you don't have an ESRI product (like ArcGIS) it is theoretically possible to convert it with <a href="http://www.gdal.org/ogr2ogr.html">ogr2ogr</a>--the <a href="http://www.gdal.org/ogr/drv_filegdb.html">ESRI File Geodatabase</a> is a supported format if you also get the FileGDB API SDK. Kind of a pain, though. You might contact UNOSAT and see if you could get it in a different format?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '13, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-26096" class="comments-container">
<span id="26166"></span>
<div id="comment-26166" class="comment">
<div id="post-26166-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your feedback , I'm going to test it.</p>
</div>
<div id="comment-26166-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 22:10)</span> <span class="comment-user userinfo">bazgal</span>
</div>
</div>
</div>
<div id="comment-tools-26096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26096-form-container" class="comment-form-container">
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

