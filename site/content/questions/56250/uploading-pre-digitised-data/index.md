+++
type = "question"
title = "Uploading pre-digitised data?"
description = '''Hi, I&#x27;m just new to OpenStreeMap and would like to upload some data that I&#x27;ve digitised in another GIS application. Can I do this or do I need to digitise it again in OSM? Thanks for your help... '''
date = "2017-05-22T10:44:00Z"
lastmod = "2017-05-22T13:04:00Z"
weight = 56250
keywords = [ "data", "upload" ]
aliases = [ "/questions/56250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Uploading pre-digitised data?](/questions/56250/uploading-pre-digitised-data)

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
<span id="post-56250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm just new to OpenStreeMap and would like to upload some data that I've digitised in another GIS application. Can I do this or do I need to digitise it again in OSM? Thanks for your help...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '17, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d439e2431c73ea6cf61fc25660966779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AA2017&#39;s gravatar image" />
<p><span>AA2017</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AA2017 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56250" class="comments-container">
&#10;</div>
<div id="comment-tools-56250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56250-form-container" class="comment-form-container">
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

<span id="56255"></span>

<div id="answer-container-56255" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56255-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As your question has essentially no details the answer can't be specific, so:</p>
<ul>
<li>you need to understand that OSM has no layer concept, anything you add to the database needs to be merged properly with the existing data (that means you can and should not upload directly with the API).</li>
<li>depending on the amount of data, coverage and source, adding the data may be considered an import and you will need to follow the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a></li>
<li>if your application supports shapefiles output, you could convert to OSM data by using <a href="https://wiki.openstreetmap.org/wiki/Ogr2osm">ogr2osm</a> and then load that as a separate layer in JOSM for conflation</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '17, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 May '17, 11:47</strong> </span></p>
</div>
</div>
<div id="comments-container-56255" class="comments-container">
<span id="56256"></span>
<div id="comment-56256" class="comment">
<div id="post-56256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Simon, Thanks for your answer - the data is relatively small - new roads and buildings not yet on OS mapping. I'm happy to digitise again but would like to see my data to make sure the position is accurate. Aerial is not up to date for our area. Do I have to be using JOSM to do this? I'm using ID editor at the moment.</p>
</div>
<div id="comment-56256-info" class="comment-info">
<span class="comment-age">(22 May '17, 11:51)</span> <span class="comment-user userinfo">AA2017</span>
</div>
</div>
<span id="56257"></span>
<div id="comment-56257" class="comment">
<div id="post-56257-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Currently your only choice for uploading the data would be with JOSM. If the areas is very small naturally re-tracing might be the best solution, you can directly load a shape file as a layer in JOSM if that helps.</p>
<p>Note: the source you are using needs to have terms of use/a licence that is compatible with use for OSM.</p>
</div>
<div id="comment-56257-info" class="comment-info">
<span class="comment-age">(22 May '17, 13:04)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56255-form-container" class="comment-form-container">
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

