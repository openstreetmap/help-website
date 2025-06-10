+++
type = "question"
title = "Import shapefile as .osm"
description = '''Hi, I want to edit my shapefile using OSM editor (Potlatch2/iD). For this, we need to upload the data (shapefile data) in the server. Do we need to convert it into .osm format? If so, how? Thanks in advance.'''
date = "2013-12-05T09:31:00Z"
lastmod = "2013-12-06T09:35:00Z"
weight = 28799
keywords = [ "shapefile", ".osm" ]
aliases = [ "/questions/28799" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import shapefile as .osm](/questions/28799/import-shapefile-as-osm)

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
<span id="post-28799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to edit my shapefile using OSM editor (Potlatch2/iD). For this, we need to upload the data (shapefile data) in the server. Do we need to convert it into .osm format? If so, how?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '13, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c59921537afd0b14f63f47aac9b4b600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GoldenCompass&#39;s gravatar image" />
<p><span>GoldenCompass</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GoldenCompass has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28799" class="comments-container">
<span id="28804"></span>
<div id="comment-28804" class="comment">
<div id="post-28804-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>There are lots of issues associated with importing beyond the purely technical ones (where did the data come from; does it duplicate anything already in OSM etc.) - I'd read through the list of <a href="https://help.openstreetmap.org/search/?q=import&amp;Submit=Search&amp;t=question">previous import questions</a> first before deciding that this is really what you want to do.</p>
</div>
<div id="comment-28804-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 11:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28806"></span>
<div id="comment-28806" class="comment">
<div id="post-28806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks.. I could find out some tools which could be useful for my case. ogr2osm/shp2osm/polyshp2osm are there which can be handy for my requirements. Thanks again.</p>
</div>
<div id="comment-28806-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 11:20)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
</div>
<div id="comment-tools-28799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28799-form-container" class="comment-form-container">
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

<span id="28807"></span>

<div id="answer-container-28807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28807-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-28807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch and iD are not general-purpose shapefile editors and are not really suitable for your task. They are intended for editing the single worldwide OpenStreetMap database.</p>
<p>If you intend to add information from the shapefile to the OpenStreetMap database, such that everyone can see and edit it, you must make sure that you follow the <a href="http://wiki.openstreetmap.org/wiki/Import_guidelines">Import Guidelines</a>.</p>
<p>However, if you simply need to edit a shapefile, you should choose a more appropriate tool, such as <a href="http://qgis.org/en/site/">QGIS</a>. (At a pinch you could install the full "Rails port" OpenStreetMap server stack on your own machine, but this would be massive overkill.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '13, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-28807" class="comments-container">
<span id="28809"></span>
<div id="comment-28809" class="comment">
<div id="post-28809-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Richard</span> Thanks.. I did have "Rails port" deployed in the public domain (you may visit <a href="http://bhuvan-mapper.nrsc.gov.in">http://bhuvan-mapper.nrsc.gov.in</a>). To provide editing facility to geographically distributed persons, I asked the above question. However as I mentioned in my, I did found few useful tools which can do the required tasks. Thanks again. :)</p>
</div>
<div id="comment-28809-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 11:33)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
<span id="28820"></span>
<div id="comment-28820" class="comment">
<div id="post-28820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@GoldenCompass</span>: So, do you also have an own database running to which you like to import the shapefile data?</p>
</div>
<div id="comment-28820-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 13:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28842"></span>
<div id="comment-28842" class="comment">
<div id="post-28842-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> Yes. I have setup rails port at my end. URL is in previous comment. Check it once. :)</p>
</div>
<div id="comment-28842-info" class="comment-info">
<span class="comment-age">(06 Dec '13, 09:35)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
</div>
<div id="comment-tools-28807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28807-form-container" class="comment-form-container">
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

