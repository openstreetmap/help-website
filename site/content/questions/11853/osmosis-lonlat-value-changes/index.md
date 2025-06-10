+++
type = "question"
title = "Osmosis lon/lat value changes"
description = '''Hi, I have &#x27;successfully&#x27; extracted the data from my planet.osm into my DB using Osmosis but have noticed that the lon/lat values have been altered. For example: -1.297504, 50.964552 has now become -15112163, 513073058. Am I just being stupid or does this seem a little wrong? Any help would be great...'''
date = "2012-04-09T23:24:00Z"
lastmod = "2012-04-10T11:26:00Z"
weight = 11853
keywords = [ "latitude", "changes", "longitude", "osmosis" ]
aliases = [ "/questions/11853" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis lon/lat value changes](/questions/11853/osmosis-lonlat-value-changes)

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
<span id="post-11853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11853-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have 'successfully' extracted the data from my planet.osm into my DB using Osmosis but have noticed that the lon/lat values have been altered. For example: -1.297504, 50.964552 has now become -15112163, 513073058.</p>
<p>Am I just being stupid or does this seem a little wrong? Any help would be greatly appreciated.</p>
<p>Many Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '12, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8eed33fb797dd7f32b1bd6654bafce0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevethepenguin&#39;s gravatar image" />
<p><span>stevethepenguin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevethepenguin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11853" class="comments-container">
&#10;</div>
<div id="comment-tools-11853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11853-form-container" class="comment-form-container">
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

<span id="11857"></span>

<div id="answer-container-11857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,<br />
this definitely does not look right. Can you provide more information about your database projection and the command with parameters you used to import? How did you get those coordinate values? Did you use ST_AsText() on the geometry column?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '12, 07:29</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-11857" class="comments-container">
<span id="11862"></span>
<div id="comment-11862" class="comment">
<div id="post-11862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I'm using a mySQL DB as my host doesn't provide PostgreSQL. The coordinates I have provided are for my local pub and have been obtained from the XAPI web service (and double checked with Google Maps). I used the following command/parameters for the import:</p>
</div>
<div id="comment-11862-info" class="comment-info">
<span class="comment-age">(10 Apr '12, 09:55)</span> <span class="comment-user userinfo">stevethepenguin</span>
</div>
</div>
<span id="11863"></span>
<div id="comment-11863" class="comment">
<div id="post-11863-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osmosis --read-xml file=hampshire.osm --node-key-value keyValueList="railway.station,railway.subway_entrance,amenity.parking, amenity.bar,amenity.pub,amenity.fast_food,amenity.restaurant,amenity.atm,amenity.bank" --write-apidb authFile=auth.config</p>
<p>The above code runs through without any errors and all information is inserted into the DB but the coordinates are heavily altered.</p>
<p>Thanks.</p>
</div>
<div id="comment-11863-info" class="comment-info">
<span class="comment-age">(10 Apr '12, 09:55)</span> <span class="comment-user userinfo">stevethepenguin</span>
</div>
</div>
</div>
<div id="comment-tools-11857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11857-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11864"></span>

<div id="answer-container-11864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11864-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know MySQL very well, but of what type is your geometry column? I believe there is a conversion error while inserting the coordinates from osmosis into the database ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '12, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11864" class="comments-container">
<span id="11865"></span>
<div id="comment-11865" class="comment">
<div id="post-11865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The mySQL DB doesn't use a single geometry column - it use two separate columns (one for lon, one for lat) with the double data type.</p>
</div>
<div id="comment-11865-info" class="comment-info">
<span class="comment-age">(10 Apr '12, 11:26)</span> <span class="comment-user userinfo">stevethepenguin</span>
</div>
</div>
</div>
<div id="comment-tools-11864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11864-form-container" class="comment-form-container">
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

