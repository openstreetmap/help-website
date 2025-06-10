+++
type = "question"
title = "How do I know the projection of a osm export data?"
description = '''Hi, I need to know the projection of a osm data that I just export to shape file.  Thanks  Moy'''
date = "2012-04-24T22:18:00Z"
lastmod = "2012-05-14T22:51:00Z"
weight = 12343
keywords = [ "shape", "projection" ]
aliases = [ "/questions/12343" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I know the projection of a osm export data?](/questions/12343/how-do-i-know-the-projection-of-a-osm-export-data)

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
<span id="post-12343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I need to know the projection of a osm data that I just export to shape file. Thanks Moy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shape" rel="tag" title="see questions tagged &#39;shape&#39;">shape</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '12, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/154c51faf96501915677fe958da06fb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moymj&#39;s gravatar image" />
<p><span>moymj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moymj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '12, 12:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-12343" class="comments-container">
<span id="12344"></span>
<div id="comment-12344" class="comment">
<div id="post-12344-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>How are you creating the shape file?</p>
</div>
<div id="comment-12344-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 22:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="12359"></span>
<div id="comment-12359" class="comment">
<div id="post-12359-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>shape file by itself contains coordinates but does not say if they are projected or not. That's why Frederik is asking you how you generate your shape file. Usually, a .prj file contains the projection information.</p>
</div>
<div id="comment-12359-info" class="comment-info">
<span class="comment-age">(25 Apr '12, 15:20)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="12360"></span>
<div id="comment-12360" class="comment">
<div id="post-12360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik / Pieren, I'm creating the shape file using OSM2SHP.exe, but when I create the shape file doesn't creat the .prj file, just create .dbf , .shp and .shx.</p>
<p>Thanks for your kindness</p>
<p>Moy</p>
</div>
<div id="comment-12360-info" class="comment-info">
<span class="comment-age">(25 Apr '12, 16:18)</span> <span class="comment-user userinfo">moymj</span>
</div>
</div>
</div>
<div id="comment-tools-12343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12343-form-container" class="comment-form-container">
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

<span id="12361"></span>

<div id="answer-container-12361" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12361-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are three different programs that all are called osm2shp. Most probably none of theese do any reprojection and uses the same projection as the original .osm file.</p>
<p>Osm uses WGS84 projection for all .osm files, and that is probably the projection your shapefile is in. You can download a .prj file for WGS84 at <a href="http://spatialreference.org/ref/epsg/4326/prj/">spartialreference.org</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '12, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12361" class="comments-container">
<span id="12362"></span>
<div id="comment-12362" class="comment">
<div id="post-12362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Gnonthgol, so I'm going to use wgs84.</p>
<p>Moy</p>
</div>
<div id="comment-12362-info" class="comment-info">
<span class="comment-age">(25 Apr '12, 17:48)</span> <span class="comment-user userinfo">moymj</span>
</div>
</div>
<span id="12371"></span>
<div id="comment-12371" class="comment">
<div id="post-12371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just one note about the semantic : WGS84 is not a "projection" but a Geodetic System. Coordinates are not "projected" on a plane but on the earth (ellipsoid).</p>
</div>
<div id="comment-12371-info" class="comment-info">
<span class="comment-age">(26 Apr '12, 12:10)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-12361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12361-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12731"></span>

<div id="answer-container-12731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12731-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have tried working with osm state files for us north america and open them in QGIS which converts the data to a shape file. The problem is it is either unprojected and/or lacks a regional conversion as well. I need to have the layer play well with other layers from Tiger Census US which is what my project is set to, however the osm conversion, when queried, says it is using that project datum,that is not the case, however. Is there a simple way to get into, say, EPSG 4326 -- WGS 84?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9f7befbf40ef9e944dd83ba2cef0a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lewis_pusey&#39;s gravatar image" />
<p><span>lewis_pusey</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lewis_pusey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12731" class="comments-container">
&#10;</div>
<div id="comment-tools-12731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12733"></span>

<div id="answer-container-12733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12733-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>I am trying to get the planar projection, not the ellipsoid</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9f7befbf40ef9e944dd83ba2cef0a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lewis_pusey&#39;s gravatar image" />
<p><span>lewis_pusey</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lewis_pusey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12733" class="comments-container">
&#10;</div>
<div id="comment-tools-12733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12733-form-container" class="comment-form-container">
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

