+++
type = "question"
title = "Mapping journey on OSM from live GPS data and extracting route info"
description = '''Wondering if there is a way to feed in data that is being logged on an external device and get information from the nearest tagged coordinate.'''
date = "2014-02-11T11:40:00Z"
lastmod = "2014-02-11T13:13:00Z"
weight = 30628
keywords = [ "route", "reversegeocoding", "data_processing" ]
aliases = [ "/questions/30628" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping journey on OSM from live GPS data and extracting route info](/questions/30628/mapping-journey-on-osm-from-live-gps-data-and-extracting-route-info)

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
<span id="post-30628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Wondering if there is a way to feed in data that is being logged on an external device and get information from the nearest tagged coordinate.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-data_processing" rel="tag" title="see questions tagged &#39;data_processing&#39;">data_processing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '14, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/1a7106e1bd2d5ab3edf26035a27e7b90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichaB&#39;s gravatar image" />
<p><span>RichaB</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichaB has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '14, 14:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30628" class="comments-container">
<span id="30629"></span>
<div id="comment-30629" class="comment">
<div id="post-30629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Presumably you want some sort of web service to do this? If so you might want to be a little more specific about what you actually want, as there are dozens of OSM-based services that could potentially answer your question as stated.</p>
</div>
<div id="comment-30629-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30631"></span>
<div id="comment-30631" class="comment">
<div id="post-30631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your comment. Sorry I am still getting to grips with OSM. What I have is a lot of GPS data in a .csv file. Which I would like to run through OSM and get route information (like information that is tagged for the coordinate nearest to my data coordinate.)</p>
</div>
<div id="comment-30631-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:17)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
<span id="30632"></span>
<div id="comment-30632" class="comment">
<div id="post-30632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@RichaB</span>: please try to be more clear on your inputs and wanted outputs.</p>
</div>
<div id="comment-30632-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30633"></span>
<div id="comment-30633" class="comment">
<div id="post-30633-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, sorry about that. My input is a .csv file with GPS data logged i.e time stamp, alt, lat, long coordinates. I am looking for a way to 1. use this input 2. process it through the OSM database 3. and then gain route information. for eg. If my coordinate is 53.62491, -2.20178 which is tagged road type-''highway'' or the nearest tag for this coordinate is ''highway'' then be able to retrieve this road information as output.</p>
<p>Thank you guys for commenting!..hope you'll can help....</p>
</div>
<div id="comment-30633-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:30)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
</div>
<div id="comment-tools-30628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30628-form-container" class="comment-form-container">
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

<span id="30634"></span>

<div id="answer-container-30634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30634-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We have a "reverse geocoding" service that, for a given coordinate, tells you something like "this is near house number 13, A road, B town, C country". Type "reverse geocoding" in the search box above and you will see some information about this.</p>
<p>If you intend to process a large number of points - tens/hundreds of thousands - that way, we would expect you to set up your own geocoding server instead of using ours, but of course you are free to load our data into that server. The software used for reverse geocoding is called Nominatim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '14, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30634" class="comments-container">
<span id="30635"></span>
<div id="comment-30635" class="comment">
<div id="post-30635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey @Fredreik thank you very much for that.</p>
<p>Yes unfortunately I do have a lot of data to process but I will have a look at Nominatim....thanks again.</p>
</div>
<div id="comment-30635-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:36)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
<span id="30637"></span>
<div id="comment-30637" class="comment">
<div id="post-30637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry just to clarify, would there be a way to continuously feed data into nominatim from a .csv file with lat, long coordinates logged and have the result stored into another file?</p>
</div>
<div id="comment-30637-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 12:52)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
<span id="30640"></span>
<div id="comment-30640" class="comment">
<div id="post-30640-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><span>@RichaB</span> Of course, just create an application/script that (continuously) reads the file and creates corresponding requests to Nominatim. But you should install a local Nominatim instace or you will very likely violate the <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">usage policy of OSM's Nominatim instance</a>.</p>
</div>
<div id="comment-30640-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 13:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30634-form-container" class="comment-form-container">
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

