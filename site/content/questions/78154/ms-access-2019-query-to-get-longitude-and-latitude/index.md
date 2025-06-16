+++
type = "question"
title = "MS Access 2019 query to get longitude and latitude"
description = '''Hi I am writing an MS Access query to get the longitude and latitude for Canadian addresses. Can I use open street map for this? If yes, how? Is there a code example I can work off on? Thank you'''
date = "2020-12-30T23:11:00Z"
lastmod = "2020-12-31T14:11:00Z"
weight = 78154
keywords = [ "longtitude" ]
aliases = [ "/questions/78154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MS Access 2019 query to get longitude and latitude](/questions/78154/ms-access-2019-query-to-get-longitude-and-latitude)

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
<span id="post-78154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am writing an MS Access query to get the longitude and latitude for Canadian addresses. Can I use open street map for this? If yes, how? Is there a code example I can work off on?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-longtitude" rel="tag" title="see questions tagged &#39;longtitude&#39;">longtitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '20, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/daad507f412b16ca8ddb1f2e9f294298?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manny213&#39;s gravatar image" />
<p><span>Manny213</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manny213 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78154" class="comments-container">
&#10;</div>
<div id="comment-tools-78154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78154-form-container" class="comment-form-container">
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

<span id="78163"></span>

<div id="answer-container-78163" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are geocoding services that use OpenStreetMap data, these are listed on the <a href="https://wiki.openstreetmap.org/wiki/Search_engines">Search Engines</a> page on the wiki. The second list on that page contains a list of software you can run on your own server if your data is particularly sensitive.</p>
<p>I'm not aware of any OSM specific tutorials for Access, but a quick search found <a href="http://www.mkrgeo-blog.com/the-costless-way-to-geocoding-addresses-in-excel-part-3-bulk-data-geocoding-with-nominatim-and-others-geocoding-tools/">this</a> and <a href="https://github.com/gramener/geocode-excel">this</a> for Nominatim and Excel, which might be adaptable (I can't vouch for the safety of the files they link to, I've only just found them).</p>
<p>Please note that for the initial bulk lookup you may need to be careful with <a href="/questions/30056/onetime-bulk-reverse-geocoding-which-amout-is-okay">usage policies</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '20, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-78163" class="comments-container">
&#10;</div>
<div id="comment-tools-78163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78163-form-container" class="comment-form-container">
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

