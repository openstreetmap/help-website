+++
type = "question"
title = "How to get data for two countries ?"
description = '''Hello, I need to create a routable map for Czech and Slovak republic combined. I have had success in doing this by getting the shapefile downloads from cloudmade or geofabrik.  Cloudmade is great because the cutouts are actually extending over the borders and thus you can combine two countries after...'''
date = "2011-01-18T06:42:00Z"
lastmod = "2011-01-18T11:41:00Z"
weight = 2252
keywords = [ "import", "czechoslovakia", "data" ]
aliases = [ "/questions/2252" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get data for two countries ?](/questions/2252/how-to-get-data-for-two-countries)

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
<span id="post-2252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2252-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I need to create a routable map for Czech and Slovak republic combined. I have had success in doing this by getting the shapefile downloads from cloudmade or geofabrik.</p>
<p>Cloudmade is great because the cutouts are actually extending over the borders and thus you can combine two countries after getting rid of duplicate shapes. This works fine with lot of processing steps,but there is a crucial problem - the osm_id is not in the extract. This is a major problem for me as I would like to add lot of speed information into my data and I need to periodically update the data from OpenStreetMap. I assume this is going to be an issue without unique reference id that is provided by OpenStreetMap.</p>
<p>Geofabrik extracts do contain the OSM reference plus some more important values (such as maxspeed and road numbers), but they don't overlap and if I combine the two extracts (one for Czech and other for Slovak republic) they do not seem to connect. The links that are in both countries are missing. This is obviously a big problem.</p>
<p>What would you think would be a best way to proceed ?</p>
<p>I am at this moment trying to upload both bz2 files into a PostgresSql database to be able to extract the shapefiles myself. Is that a viable path ?</p>
<p>Thanks for any hints given.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-czechoslovakia" rel="tag" title="see questions tagged &#39;czechoslovakia&#39;">czechoslovakia</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '11, 06:42</strong></p>
<img src="https://secure.gravatar.com/avatar/bbe97c3fa23d557d5cdaec1fef8e28db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomas%20Pajonk&#39;s gravatar image" />
<p><span>Tomas Pajonk</span><br />
<span class="score" title="191 reputation points">191</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomas Pajonk has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '11, 06:42</strong> </span></p>
</div>
</div>
<div id="comments-container-2252" class="comments-container">
&#10;</div>
<div id="comment-tools-2252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2252-form-container" class="comment-form-container">
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

<span id="2253"></span>

<div id="answer-container-2253" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2253-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tomas Pajonk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ideal solution would be to have a planet PBF file with data split into a grid or some other way. Then you'd be able to download the planet, but relatively quickly extract the areas you're interested in.</p>
<p>The only current solution I know of is to download planet.osm and use osmosis to extract the rectangle around Czech and Slovak republics. Then you could additionally remove areas outside of those two countries (again using osmosis). But I don't know how long that would take.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '11, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-2253" class="comments-container">
<span id="2255"></span>
<div id="comment-2255" class="comment">
<div id="post-2255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So far this seems to be the only way. I am downloading europe.b2z and plan to use osmosis to achieve my goal as you said.</p>
</div>
<div id="comment-2255-info" class="comment-info">
<span class="comment-age">(18 Jan '11, 11:41)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
</div>
<div id="comment-tools-2253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2253-form-container" class="comment-form-container">
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

