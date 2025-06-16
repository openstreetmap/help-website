+++
type = "question"
title = "Load data from SQLServer and display markers on Map"
description = '''Hi, I am new to OSM. For my requirement, I need to read Airport locations (IATA codes) from the database - SQLServer (from all over the world)and show a world map with markers on the Airport locations. Does OSM support it? I need this for a commercial application. I have googled a lot on the subject...'''
date = "2011-01-03T11:17:00Z"
lastmod = "2011-01-05T05:29:00Z"
weight = 1989
keywords = [ "airport", "locations" ]
aliases = [ "/questions/1989" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Load data from SQLServer and display markers on Map](/questions/1989/load-data-from-sqlserver-and-display-markers-on-map)

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
<span id="post-1989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am new to OSM. For my requirement, I need to read Airport locations (IATA codes) from the database - SQLServer (from all over the world)and show a world map with markers on the Airport locations. Does OSM support it? I need this for a commercial application.</p>
<p>I have googled a lot on the subject and find GoogleMaps to be a bit expensive - Hence searching for solutions from other Map services. Can somebody in the know advise?</p>
<p>Thanks in advance!! Indira</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-locations" rel="tag" title="see questions tagged &#39;locations&#39;">locations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '11, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/eb78c4af93208bbb8e6a29675813da8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="indira&#39;s gravatar image" />
<p><span>indira</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="indira has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1989" class="comments-container">
<span id="2001"></span>
<div id="comment-2001" class="comment">
<div id="post-2001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you wanting to read the locations from your own SQLServer database and display them on your web site (on an OSM map)?</p>
</div>
<div id="comment-2001-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 05:40)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
<span id="2029"></span>
<div id="comment-2029" class="comment">
<div id="post-2029-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the information / queries. Yes, I have the data of Airport destinations (of PNRs) in our own database. Once the webpage is loaded, these Airport locations have to be read and markers have to be shown for these locations on a world map ( include major Airports from all over the world). We have them in the database as 3 letter IATA Codes.</p>
</div>
<div id="comment-2029-info" class="comment-info">
<span class="comment-age">(05 Jan '11, 05:29)</span> <span class="comment-user userinfo">indira</span>
</div>
</div>
</div>
<div id="comment-tools-1989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1989-form-container" class="comment-form-container">
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

<span id="1996"></span>

<div id="answer-container-1996" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1996-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure what "SQLServer" is or how it ended up in the question, but in principle this is possible. You can query the <a href="https://wiki.openstreetmap.org/wiki/Osmxapi">XAPI</a> for all objects tagged with the key <code>iata</code> and display them on to of Openstreetmap based tiles using <a href="http://openlayers.org/">openlayers</a> i.e. a <a href="http://dev.openlayers.org/docs/files/OpenLayers/Layer/Markers-js.html">marker layer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '11, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-1996" class="comments-container">
<span id="2003"></span>
<div id="comment-2003" class="comment">
<div id="post-2003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand that I can query the XAPI for all the objects tagged with the key iata. But I need to show markers only for the Airport locations from my own database and not for all the Airports. Is there a way out with XAPI?</p>
<p>Thanks, Indira</p>
</div>
<div id="comment-2003-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 06:44)</span> <span class="comment-user userinfo">indira</span>
</div>
</div>
<span id="2006"></span>
<div id="comment-2006" class="comment">
<div id="post-2006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure. Instead of querying XAPI for locations you can query your own SQLServer and display them. But that is so far outside of the scope of Openstreetmap that we wont support that. Especially as you get payed for your job and we are all volunteers.</p>
</div>
<div id="comment-2006-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 07:27)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-1996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1996-form-container" class="comment-form-container">
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

