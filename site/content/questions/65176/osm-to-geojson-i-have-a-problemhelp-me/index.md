+++
type = "question"
title = "osm to geojson ,i have a problem.help me!"
description = '''I added some buildings to the osm website and set the height,and export the osm, and then I converted the osm to geojson, but there was a problem with the height attribute in the geojson code! MapBox can&#x27;t get this property normally, so who can help me solve this problem! The conversion tool is free...'''
date = "2018-08-07T10:13:00Z"
lastmod = "2018-08-09T04:33:00Z"
weight = 65176
keywords = [ "osm" ]
aliases = [ "/questions/65176" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm to geojson ,i have a problem.help me!](/questions/65176/osm-to-geojson-i-have-a-problemhelp-me)

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
<span id="post-65176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I added some buildings to the osm website and set the height,and export the osm, and then I converted the osm to geojson, but there was a problem with the height attribute in the geojson code! MapBox can't get this property normally, so who can help me solve this problem!</p>
<p>The conversion tool is freely downloaded from the Internet</p>
<p><img src="https://pbs.twimg.com/media/Dj_LbvDU0AAApUo.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '18, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a67f4097364e083aa87f490275ffa607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unity007&#39;s gravatar image" />
<p><span>unity007</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unity007 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '18, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-65176" class="comments-container">
<span id="65177"></span>
<div id="comment-65177" class="comment">
<div id="post-65177-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The image you added is essentially illegible. You haven't told us what you are using to convert from OSM format to geojson, without that it is a bit difficult to help (any sane converter should simply keep the tags one way or the other).</p>
</div>
<div id="comment-65177-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 10:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="65178"></span>
<div id="comment-65178" class="comment">
<div id="post-65178-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"freely downloaded from the Internet" is not particularly helpful, a name or a URL would be much more.</p>
</div>
<div id="comment-65178-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 10:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65176-form-container" class="comment-form-container">
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

<span id="65180"></span>

<div id="answer-container-65180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65180-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to tell the conversion program to treat height as an attribute. This blog discusses how to configure ogr2ogr to treat additional tags as attributes, other systems will have different ways of doing it:</p>
<p><a href="https://www.compose.com/articles/how-to-transform-and-use-openstreetmap-data-into-geojson-using-gdal/">https://www.compose.com/articles/how-to-transform-and-use-openstreetmap-data-into-geojson-using-gdal/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '18, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65180" class="comments-container">
<span id="65214"></span>
<div id="comment-65214" class="comment">
<div id="post-65214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did not learn to use the command line tool,Is there a direct conversion tool?</p>
</div>
<div id="comment-65214-info" class="comment-info">
<span class="comment-age">(08 Aug '18, 13:20)</span> <span class="comment-user userinfo">unity007</span>
</div>
</div>
</div>
<div id="comment-tools-65180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65180-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65227"></span>

<div id="answer-container-65227" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved the problem using the FME tool</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '18, 04:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a67f4097364e083aa87f490275ffa607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unity007&#39;s gravatar image" />
<p><span>unity007</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unity007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65227" class="comments-container">
&#10;</div>
<div id="comment-tools-65227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65227-form-container" class="comment-form-container">
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

