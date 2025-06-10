+++
type = "question"
title = "How to transfer lon&amp;lat of the table planet_osm_nodes into the right form?"
description = '''I have downloaded the osm data and imported to my local database. There is a table called planet_osm_node and two columns lon and lat. As the description of the osm doc, latitude and longitude are stored as scaled integers with a scale factor of 1e7, so an integer latitude of -412870685 equates to -...'''
date = "2016-12-22T03:04:00Z"
lastmod = "2020-07-15T05:05:00Z"
weight = 53651
keywords = [ "convert", "planet_osm_node", "coordinates", "database" ]
aliases = [ "/questions/53651" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to transfer lon&lat of the table planet_osm_nodes into the right form?](/questions/53651/how-to-transfer-lonlat-of-the-table-planet_osm_nodes-into-the-right-form)

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
<span id="post-53651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the osm data and imported to my local database. There is a table called planet_osm_node and two columns lon and lat. As the description of the osm doc, latitude and longitude are stored as scaled integers with a scale factor of 1e7, so an integer latitude of -412870685 equates to -41.2870685.But I do this to the data, there is still difference with the real coordinate,for example the data is from (485231938,1295641506) to (48.5231938,129.5641506) while the real one is (116.389456757943,39.9061897544305). Is there a function or something to transform between these two forms?</p>
<p>Please help and thank you very much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-planet_osm_node" rel="tag" title="see questions tagged &#39;planet_osm_node&#39;">planet_osm_node</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '16, 03:04</strong></p>
<img src="https://secure.gravatar.com/avatar/35f384f89bed297390f4cf396589594f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Connie%20Wang&#39;s gravatar image" />
<p><span>Connie Wang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Connie Wang has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '16, 12:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-53651" class="comments-container">
&#10;</div>
<div id="comment-tools-53651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53651-form-container" class="comment-form-container">
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

<span id="53654"></span>

<div id="answer-container-53654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53654-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ignore the information about scaled integers, it is not relevant to your use case. If you have imported with osm2pgsql then observe the following:</p>
<ul>
<li><code>planet_osm_nodes</code> is almost certainly not what you are interested in as it has raw coordinates for nodes but no <em>other</em> information (is this node a tree? a shop? a city? etc)</li>
<li>Instead, use the tables <code>planet_osm_point</code>, <code>planet_osm_polygon</code>, and <code>planet_osm_line</code>, where the coordinates are stored in the "way" column. Read up on PostGIS functions. You can use st_astext to display the "way" column in a human readable format.</li>
<li>Your database is in "spherical Mercator" coordinates, not lat/lon degrees. Hence the confusion. Use the PostGIS function <code>st_transform(way,4326)</code> to convert these coordinates to lat/lon degrees, or alternatively use the <code>-l</code> command line option when importing with osm2pgsql.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '16, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '16, 07:03</strong> </span></p>
</div>
</div>
<div id="comments-container-53654" class="comments-container">
<span id="53656"></span>
<div id="comment-53656" class="comment">
<div id="post-53656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answering. I actually use the roads and nodes to partitioning the city into small areas. Then I need to reflect my order records into different area. So I need to know the right coordinate to confirm the scope of an area. I have tried the functions you mentioned above but I haven't gotten the format that I want.</p>
</div>
<div id="comment-53656-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 07:36)</span> <span class="comment-user userinfo">Connie Wang</span>
</div>
</div>
</div>
<div id="comment-tools-53654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54856"></span>

<div id="answer-container-54856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Connie,</p>
<p>I have the same problem. Did you manage to get a solution?</p>
<p>Best Regards, Varun.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '17, 03:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6133a6a9df816287c808c1a5bf6577d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VarunDhr&#39;s gravatar image" />
<p><span>VarunDhr</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VarunDhr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54856" class="comments-container">
<span id="54857"></span>
<div id="comment-54857" class="comment">
<div id="post-54857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes,you can use the function of postgis,which is a opensource program of postgreSQL. Something like this:select id,ST_X(ST_AsText(st_transform(st_geomfromtext('POINT ('||lon/100||' '||lat/100||')',900913),4326))) as longi, ST_Y(ST_AsText(st_transform(st_geomfromtext('POINT ('||lon/100||' '||lat/100||')',900913),4326))) as lati from new_nodes</p>
</div>
<div id="comment-54857-info" class="comment-info">
<span class="comment-age">(02 Mar '17, 04:16)</span> <span class="comment-user userinfo">Connie Wang</span>
</div>
</div>
</div>
<div id="comment-tools-54856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54856-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73394"></span>

<div id="answer-container-73394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For anyone else who stumbles here looking for the answer. It depends on how the values were imported. My data was created by Nominatim, which simply converts lat/lon to an integer by multiplying by 10000000. This looks like the same case as the OP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '20, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/4f377b36e190cbd3b5a0c57d981e38b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neilireson&#39;s gravatar image" />
<p><span>neilireson</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neilireson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73394" class="comments-container">
&#10;</div>
<div id="comment-tools-73394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75711"></span>

<div id="answer-container-75711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>for those who ask for : lon, lat from planet_osm_nodes, here is your response : "select lon::numeric/10000000 as lon, lat::numeric/10000000 as lat from planet_osm_nodes".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '20, 05:05</strong></p>
<img src="https://secure.gravatar.com/avatar/dfa634dabd6dbf14e4eb454ff60740d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdelkader&#39;s gravatar image" />
<p><span>Abdelkader</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdelkader has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75711" class="comments-container">
&#10;</div>
<div id="comment-tools-75711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75711-form-container" class="comment-form-container">
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

