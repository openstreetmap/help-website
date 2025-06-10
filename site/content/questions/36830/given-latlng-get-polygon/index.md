+++
type = "question"
title = "Given Lat/Lng get polygon"
description = '''Is there a way to know a specific point in which region it exists and get the polygon for that region? I am interested in knowing the Region name and boundaries. Preferably i would like something to use in a console application.'''
date = "2014-09-15T09:35:00Z"
lastmod = "2014-09-22T18:52:00Z"
weight = 36830
keywords = [ "overpassapi" ]
aliases = [ "/questions/36830" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Given Lat/Lng get polygon](/questions/36830/given-latlng-get-polygon)

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
<span id="post-36830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to know a specific point in which region it exists and get the polygon for that region?</p>
<p>I am interested in knowing the Region name and boundaries.</p>
<p>Preferably i would like something to use in a console application.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1073728a2a23188cb754da8247990f63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jyparask&#39;s gravatar image" />
<p><span>jyparask</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jyparask has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '14, 09:36</strong> </span></p>
</div>
</div>
<div id="comments-container-36830" class="comments-container">
<span id="36831"></span>
<div id="comment-36831" class="comment">
<div id="post-36831-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You added the Overpass API tag but it sounds like you want to perform a reverse geocoding query using <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> instead? A second query will be necessary for retrieving the polygon of the area returned by Nominatim.</p>
</div>
<div id="comment-36831-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 11:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36832"></span>
<div id="comment-36832" class="comment">
<div id="post-36832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> I am more than new in this thing, so you may be correct. I really do not know what my options are though :-) . I will check out this link. Thanks.</p>
</div>
<div id="comment-36832-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 11:09)</span> <span class="comment-user userinfo">jyparask</span>
</div>
</div>
</div>
<div id="comment-tools-36830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36830-form-container" class="comment-form-container">
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

<span id="36835"></span>

<div id="answer-container-36835" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36835-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to <a href="http://help.openstreetmap.org/users/158/scai">@scai</a> and a bit of reading on the documentation he provided, i found out the actual solution.</p>
<p>Having <code>lat</code> and <code>lng</code> i am doing a reverse call on <a href="http://nominatim.openstreetmap.org/reverse">nominatim reverse</a> providing <code>lat</code> and <code>lon</code> as parameters. Then i do a second call on <a href="http://nominatim.openstreetmap.org/search">nominatim search</a> providing <code>country</code> and <code>county</code> from the previous result. This will give me the polygon if request it.</p>
<p>Since i use <code>json</code>, i add <code>polygon_geojson=1</code> in the query string.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '14, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/1073728a2a23188cb754da8247990f63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jyparask&#39;s gravatar image" />
<p><span>jyparask</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jyparask has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36835" class="comments-container">
<span id="36978"></span>
<div id="comment-36978" class="comment">
<div id="post-36978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>also see some more options at <a href="http://wiki.openstreetmap.org/wiki/Search_engines">http://wiki.openstreetmap.org/wiki/Search_engines</a></p>
</div>
<div id="comment-36978-info" class="comment-info">
<span class="comment-age">(22 Sep '14, 18:52)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-36835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36835-form-container" class="comment-form-container">
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

