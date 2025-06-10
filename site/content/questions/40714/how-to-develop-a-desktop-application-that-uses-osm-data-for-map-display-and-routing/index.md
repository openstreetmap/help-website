+++
type = "question"
title = "How to develop a Desktop Application that uses OSM data for map display and routing?"
description = '''I understand that OSM is just the data. For using this data I would need some other API to use it with. I am developing a desktop application (WPF), its a cab booking application so i would need to somehow show a map in my application. Over the map a route of multiple addresses (5, 10, 20 or more) w...'''
date = "2015-01-30T11:30:00Z"
lastmod = "2015-01-30T16:39:00Z"
weight = 40714
keywords = [ "c#", "wpf", "mileage-calculation", ".net4", "routing" ]
aliases = [ "/questions/40714" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to develop a Desktop Application that uses OSM data for map display and routing?](/questions/40714/how-to-develop-a-desktop-application-that-uses-osm-data-for-map-display-and-routing)

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
<span id="post-40714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I understand that OSM is just the data. For using this data I would need some other API to use it with.</p>
<p>I am developing a desktop application (WPF), its a cab booking application so i would need to somehow show a map in my application. Over the map a route of multiple addresses (5, 10, 20 or more) will be shown. I would need the mileage calculation... driving time.. etc etc. I need this all OFFLINE (as there will be massive bookings going on, so is mileage calculation) so we need it really fast as well.</p>
<p>Environment: Windows 7, .net4, WPF, MVVM Pattern, C#</p>
<p>Please guide me in detail.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-wpf" rel="tag" title="see questions tagged &#39;wpf&#39;">wpf</span> <span class="post-tag tag-link-mileage-calculation" rel="tag" title="see questions tagged &#39;mileage-calculation&#39;">mileage-calculation</span> <span class="post-tag tag-link-.net4" rel="tag" title="see questions tagged &#39;.net4&#39;">.net4</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '15, 11:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5d510ab272f75f1c603dce891e647f5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sohaib%20Ahmed&#39;s gravatar image" />
<p><span>Sohaib Ahmed</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sohaib Ahmed has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '15, 12:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-40714" class="comments-container">
&#10;</div>
<div id="comment-tools-40714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40714-form-container" class="comment-form-container">
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

<span id="40716"></span>

<div id="answer-container-40716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40716-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The components you need are</p>
<ol>
<li>Map (or map tile) server</li>
<li>Geocoding</li>
<li>Routing (which you call mileage calculation)</li>
</ol>
<p>Open Source solutions exist for all these components, which you can re-use (i.e. set up a map server, geocoding server, and routing server in your local environment), or you could use libraries or code fragments to implement these things in your software directly.</p>
<p>Generally speaking, most of these things are easy as long as you are dealing with a small area and become more difficult if you want to serve a whole country or more, simply because of the increased data volume.</p>
<p>Even if you use ready made servers (for example, a tile server as described on switch2osm.org, a routing server from project-osrm.org, and the Nominatim software for geocoding), throwing it all together into one application will be considerable integration work which we at help.openstreetmap.org can't do for you.</p>
<p>If you'd like to use a library, perhaps check out the Open Source <a href="http://osmsharp.com/">http://osmsharp.com/</a> for which commercial support is available from the author.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '15, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40716" class="comments-container">
&#10;</div>
<div id="comment-tools-40716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40716-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40717"></span>

<div id="answer-container-40717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40717-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check out the <span>commercial service providers in the OSM world</span>. Volunteers like here in this help forum are not your non-paid workers (@"guide me in detail") for a (assumed) non-<span>free</span> application development.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '15, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '15, 16:47</strong> </span></p>
</div>
</div>
<div id="comments-container-40717" class="comments-container">
&#10;</div>
<div id="comment-tools-40717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40717-form-container" class="comment-form-container">
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

