+++
type = "question"
title = "Regarding GPX data import to database private server"
description = '''Hello, I have successfully uploaded GPX tracks to my private OSM server. While these tracks are shown as entries in the gpx_files table in the API DB, the have not been populated as individual GPS points in the gps_points table. I understand that the points from all GPX files must be extracted and s...'''
date = "2014-10-10T15:52:00Z"
lastmod = "2014-10-31T13:21:00Z"
weight = 37501
keywords = [ "api", "gpx", "upload", "private", "tileserver" ]
aliases = [ "/questions/37501" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Regarding GPX data import to database private server](/questions/37501/regarding-gpx-data-import-to-database-private-server)

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
<span id="post-37501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have successfully uploaded GPX tracks to my private OSM server. While these tracks are shown as entries in the gpx_files table in the API DB, the have not been populated as individual GPS points in the gps_points table.</p>
<p>I understand that the points from all GPX files must be extracted and stored inorder for the API to be able to query them.</p>
<p>In my own openstreetmap website running on ruby on rails these tracks show a status as pending.</p>
<p>From what i understand in the code the deamon which populates the data into the database is not running.</p>
<p>Could anyone help me with the respective settings or changes that need to be made in order to populate all points?</p>
<p>Your help is highly appreciated.</p>
<p>Arjun</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '14, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37501" class="comments-container">
<span id="37569"></span>
<div id="comment-37569" class="comment">
<div id="post-37569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can anyone who has set up a private server and has populated gps pints from the gpx traces into the osm database please help me with this ?</p>
</div>
<div id="comment-37569-info" class="comment-info">
<span class="comment-age">(13 Oct '14, 09:20)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
<span id="37608"></span>
<div id="comment-37608" class="comment">
<div id="post-37608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, after doing some research on google i found out the gpx_import.rb in the rails website is not supported anymore, instead there is a c program to to do the gpx import</p>
<p><a href="https://github.com/ericfischer/gpx-import">https://github.com/ericfischer/gpx-import</a></p>
<p>I cant seem to get this working either!</p>
<p>Anyone with experience regarding GPX import kindly help me .</p>
<p>Thanks</p>
</div>
<div id="comment-37608-info" class="comment-info">
<span class="comment-age">(14 Oct '14, 09:28)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
</div>
<div id="comment-tools-37501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37501-form-container" class="comment-form-container">
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

<span id="38166"></span>

<div id="answer-container-38166" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38166-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For all those who need to upload their GPX files to the private OSM database here is a wonderful c program that is extremely helpful</p>
<p><a href="http://git.openstreetmap.org/gpx-import.git/">http://git.openstreetmap.org/gpx-import.git/</a></p>
<p>It works great!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '14, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38166" class="comments-container">
&#10;</div>
<div id="comment-tools-38166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38166-form-container" class="comment-form-container">
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

