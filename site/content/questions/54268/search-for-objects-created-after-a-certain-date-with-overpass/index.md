+++
type = "question"
title = "Search for objects created after a certain date with overpass"
description = '''does anyone know if it is possible to search for ways created after a given date with the overpass-api?'''
date = "2017-01-24T19:14:00Z"
lastmod = "2017-02-07T18:22:00Z"
weight = 54268
keywords = [ "overpass", "creation" ]
aliases = [ "/questions/54268" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Search for objects created after a certain date with overpass](/questions/54268/search-for-objects-created-after-a-certain-date-with-overpass)

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
<span id="post-54268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54268-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-54268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>does anyone know if it is possible to search for ways created after a given date with the overpass-api?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-creation" rel="tag" title="see questions tagged &#39;creation&#39;">creation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '17, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-54268" class="comments-container">
&#10;</div>
<div id="comment-tools-54268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54268-form-container" class="comment-form-container">
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

<span id="54536"></span>

<div id="answer-container-54536" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54536-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-54536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A guy on the talk-it list suggested to use the query down below, and it seems to properly work for me!</p>
<pre><code>[out:xml][timeout:250][adiff:&quot;2015-01-01T00:00:00Z&quot;,&quot;2016-01-01T00:00:00Z&quot;];
(
way[&quot;highway&quot;]({{bbox}});
);
out body;
out meta;
&gt;;
out skel qt;</code></pre>
<p>Thanks to Andrea Albani</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '17, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/17282eebcd8a14e0cb4a02fe44769460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Constable&#39;s gravatar image" />
<p><span>Constable</span><br />
<span class="score" title="642 reputation points">642</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Constable has 3 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '17, 13:50</strong> </span></p>
</div>
</div>
<div id="comments-container-54536" class="comments-container">
<span id="54544"></span>
<div id="comment-54544" class="comment">
<div id="post-54544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, this is even better. Thanks a lot.</p>
</div>
<div id="comment-54544-info" class="comment-info">
<span class="comment-age">(07 Feb '17, 18:22)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-54536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54536-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54317"></span>

<div id="answer-container-54317" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54317-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-54317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just add (newer:"yyyy-mm-ddThh:mm:ssZ") after node, way &amp; relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '17, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-54317" class="comments-container">
<span id="54318"></span>
<div id="comment-54318" class="comment">
<div id="post-54318-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Vielen Dank. Das hilft mir weiter.</p>
</div>
<div id="comment-54318-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 19:18)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
<span id="54328"></span>
<div id="comment-54328" class="comment">
<div id="post-54328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's not working for me; this thing returns the object created and edited after a given date but I'm only searching for the object created after that date. thanks</p>
</div>
<div id="comment-54328-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 10:54)</span> <span class="comment-user userinfo">Constable</span>
</div>
</div>
</div>
<div id="comment-tools-54317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54317-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54314"></span>

<div id="answer-container-54314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm searching for the same exact thing but I cant figure out how to build that query. Is there anyone who can help us out? thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '17, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/17282eebcd8a14e0cb4a02fe44769460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Constable&#39;s gravatar image" />
<p><span>Constable</span><br />
<span class="score" title="642 reputation points">642</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Constable has 3 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '17, 17:03</strong> </span></p>
</div>
</div>
<div id="comments-container-54314" class="comments-container">
<span id="54320"></span>
<div id="comment-54320" class="comment">
<div id="post-54320-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Here is a simple example using Overpass Turbo:<br />
<a href="http://overpass-turbo.eu/s/lxA">http://overpass-turbo.eu/s/lxA</a><br />
The newer filter selects all elements that have been changed since the given date.</p>
</div>
<div id="comment-54320-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 01:35)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="54329"></span>
<div id="comment-54329" class="comment">
<div id="post-54329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>same here; I'm only interested in objects created after a given date, the query shouldn't return the edited ones. thanks</p>
</div>
<div id="comment-54329-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 10:56)</span> <span class="comment-user userinfo">Constable</span>
</div>
</div>
<span id="54331"></span>
<div id="comment-54331" class="comment">
<div id="post-54331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I expect that you can extract the highways as they existed at two moments in time using Overpass Turbo, then open both in QGIS and get QGIS to display the difference. It may be possible to colour the difference according to whether the difference was added or extracted.</p>
</div>
<div id="comment-54331-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 12:44)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="54339"></span>
<div id="comment-54339" class="comment">
<div id="post-54339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I expect you cannot extract a moment in time as mentioned above. Maybe the only way to do it is to get the planet file for particular dates <a href="http://planet.osm.org/planet/">http://planet.osm.org/planet/</a> Then extract the area you need using Osmosis <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes">http://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes</a> Then compare in Qgis.</p>
</div>
<div id="comment-54339-info" class="comment-info">
<span class="comment-age">(28 Jan '17, 14:46)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-54314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54314-form-container" class="comment-form-container">
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

