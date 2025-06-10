+++
type = "question"
title = "How to add trails to the map"
description = '''As I hike, my gps automatically creates GPX files. Some of the trails I&#x27;m hiking don&#x27;t appear on the map. So I&#x27;d like to add them. However, I can&#x27;t find a good guide as to how to add the hiking trail to the map, starting with a GPX file. Is there such a guide? What I&#x27;d like to have is a step by step...'''
date = "2019-11-06T22:09:00Z"
lastmod = "2020-04-16T10:40:00Z"
weight = 71497
keywords = [ "trail", "gpx", "guide" ]
aliases = [ "/questions/71497" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [How to add trails to the map](/questions/71497/how-to-add-trails-to-the-map)

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
<span id="post-71497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71497-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As I hike, my gps automatically creates GPX files. Some of the trails I'm hiking don't appear on the map. So I'd like to add them.</p>
<p>However, I can't find a good guide as to how to add the hiking trail to the map, starting with a GPX file. Is there such a guide?</p>
<p>What I'd like to have is a step by step guide starting with the GPX file, importing it to the map, adding any necessary tags for the new trail, and what tags and settings should be used. Basically I'm looking for a combination "how-to" guide and a "best practices" document.</p>
<p>Does any such thing exist?</p>
<p>(I'm looking for the standards in the United States. I understand that standards are different in other counties.)</p>
<p>Thanks in advance for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-guide" rel="tag" title="see questions tagged &#39;guide&#39;">guide</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '19, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2cfd0bb46691a581540c6bc9403b674f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikC&#39;s gravatar image" />
<p><span>FredrikC</span><br />
<span class="score" title="118 reputation points">118</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71497" class="comments-container">
&#10;</div>
<div id="comment-tools-71497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71497-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="71508"></span>

<div id="answer-container-71508" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71508-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-71508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you don't want to import the GPS trace as-is. GPS isn't accurate enough. Consider <a href="https://help.openstreetmap.org/upfiles/GPS_traces.jpg">this set of traces from my hiking</a>: most of the trails are less than a meter wide, yet it's common for multiple traces to disagree with each other by ten to twenty meters. In particular, note the switchbacks in the center of the image: there are five traces there, and not one of them follows the actual route of the trail.</p>
<p>The best way to map a trail from a GPS trace is to use it as a background while drawing the trail. Open the GPX file in the editor (in iD, you do this through the "Custom Map Data" section of the "Map Data" tab; in JOSM, you open the GPX file using "File"-&gt;"Open"). Pick the best-aligned imagery in the area (the GPS trace may be helpful for this), and draw the trail on the map using a combination of the imagery, the GPS trace, and your memory of the hike. Then add appropriate tags and upload the result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-71508" class="comments-container">
<span id="72597"></span>
<div id="comment-72597" class="comment">
<div id="post-72597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also note that you can upload the GPX file itself directly to openstreetmap.org. In the top bar there's a link called "GPS Traces", and clicking that will take you to a page where you can upload.</p>
<p>This will NOT add the trace as a trail on the map. (As Carnildo says above, that's a bad idea.) Instead it will make the trace available as an additional background layer that you (or any other OSM user) can use to help draw the trail. It's similar to adding the file as custom map data, but in some ways better -- if you ever need to look at that trace again, it will be there without you having to find and load the file again. And other users will be able to see it too, which might help next time someone else is mapping in the area.</p>
<p>In iD (the default editor) you can toggle on these uploaded traces in the "Background" options box by scrolling down past the background imagery options to "Overlays" and checking the box next to "OpenStreetMap GPS traces." You might also discover that other OSM users have uploaded traces in the same area, which can be useful. (But don't assume that a trace implies a trail! Some people like to go offtrail.)</p>
</div>
<div id="comment-72597-info" class="comment-info">
<span class="comment-age">(21 Jan '20, 16:21)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="74214"></span>
<div id="comment-74214" class="comment">
<div id="post-74214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. How long after I add a path until it appears?</p>
</div>
<div id="comment-74214-info" class="comment-info">
<span class="comment-age">(16 Apr '20, 08:49)</span> <span class="comment-user userinfo">ZenBiddist</span>
</div>
</div>
<span id="74215"></span>
<div id="comment-74215" class="comment">
<div id="post-74215-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Depends on the zoom level. At the closest levels, it should show up in a few minutes, though with the way the servers have been overloaded lately, it may take longer. Zoom levels further out are updated less often.</p>
<p>Maps other than the one on the main site take varying amounts of time, with updates once a month being common.</p>
</div>
<div id="comment-74215-info" class="comment-info">
<span class="comment-age">(16 Apr '20, 10:06)</span> <span class="comment-user userinfo">Carnildo</span>
</div>
</div>
<span id="74216"></span>
<div id="comment-74216" class="comment">
<div id="post-74216-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you want to see something rendering things immediately, then have a look at <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> . The "Using a Docker container" link on there is designed for people to get something running quickly without any messing about. If you want more info on "what on earth Docker is" have a look at the links from <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/45070">https://www.openstreetmap.org/user/SomeoneElse/diary/45070</a> . Based on the data sizes at <a href="http://download.geofabrik.de/north-america.html">http://download.geofabrik.de/north-america.html</a> , a fairly normal spec desktop or laptop PC ought to be able to handle a reasonable area of the US.</p>
</div>
<div id="comment-74216-info" class="comment-info">
<span class="comment-age">(16 Apr '20, 10:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71508-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71502"></span>

<div id="answer-container-71502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71502-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My solution is to go to wherever you have your gpx, download it to your computer, open OpenStreetMap with the editor open, and then drag the gpx file into the editor. This will make the trace appear as a pink line in the background that can be traced over to add new trails, also known as "paths" in OpenStreetMap. Good luck!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '19, 23:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6c698d7d85600320ef050a56fb050f05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LeifRasmussen&#39;s gravatar image" />
<p><span>LeifRasmussen</span><br />
<span class="score" title="106 reputation points">106</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LeifRasmussen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71502" class="comments-container">
<span id="71507"></span>
<div id="comment-71507" class="comment">
<div id="post-71507-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Both answers so far already hint it: best practice is not to convert the GPX track directly into a OSM feature but to only use it as a background to draw a new object in OSM. That way you have the chance to use your track, tracks uploaded by others, background aerial images and already existing OSM objects to approximate the best course of the new path.</p>
</div>
<div id="comment-71507-info" class="comment-info">
<span class="comment-age">(07 Nov '19, 07:58)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71501"></span>

<div id="answer-container-71501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71501-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've been through this, but don't have it down pat.</p>
<p>Basically upload the gpx track and then trace over it. I've lately used the in browser app. I do this about once a year. Like many graphics apps, it's not easy to figure out how to add points or continue a line.</p>
<p>The annotations show up on the left side of the page.</p>
<p>A very incomplete answer, but I know my first inclination was to add the gpx and this method wasn't favored by the community.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '19, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/262ace94f9a2925629114f9260378be5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MtnBiker&#39;s gravatar image" />
<p><span>MtnBiker</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MtnBiker has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Nov '19, 22:37</strong> </span></p>
</div>
</div>
<div id="comments-container-71501" class="comments-container">
&#10;</div>
<div id="comment-tools-71501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71501-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71511"></span>

<div id="answer-container-71511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71511-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's a similar question i asked, i'm sure you will find the answers useful <a href="https://help.openstreetmap.org/questions/34347/i-want-to-add-a-new-long-distance-hiking-route-to-the-map">https://help.openstreetmap.org/questions/34347/i-want-to-add-a-new-long-distance-hiking-route-to-the-map</a> the above covers a way marked trail, but for adding an unmapped trail watch some of the utube videos, internet search. "Adding trails to OpenStreetMap (OSM) using GPS ... - YouTube" they can be quite a good way to learn OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '19, 10:23</strong> </span></p>
</div>
</div>
<div id="comments-container-71511" class="comments-container">
&#10;</div>
<div id="comment-tools-71511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71777"></span>

<div id="answer-container-71777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am hesitant about providing this answer but will. This is a free app unless you wish to pay extra. Download MapMyFitness on your phone. Walk the trail with that app tracking your route. You can sign in to your account on a laptop or desktop computer as I did. That lets you more easily know where to place the trail. Over a long distance, that will take time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '19, 06:09</strong></p>
<img src="https://secure.gravatar.com/avatar/aa42343d90c1dcdcf1a5e5ffabf80fd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dark_Valor&#39;s gravatar image" />
<p><span>Dark_Valor</span><br />
<span class="score" title="36 reputation points">36</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dark_Valor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71777" class="comments-container">
&#10;</div>
<div id="comment-tools-71777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71777-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72594"></span>

<div id="answer-container-72594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72594-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I put together a step-by-step video on this topic: <strong><a href="https://www.youtube.com/watch?v=3FqSYXxMCIs">Adding trails to OpenStreetMap (OSM) using GPS traces</a></strong></p>
<p>This brief overview shows how to add trails to <a href="https://www.openstreetmap.org/">OpenStreetMap</a> using a GPX file you have recorded from a hike/bike ride. It uses the in-browser "iD" editor. For more details see <a href="http://learnosm.org/">LearnOSM.org</a> and in particular the <a href="https://learnosm.org/en/mobile-mapping/using-gps/">mobile mapping guide</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '20, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/62995abb4e6e2a4531ea4fce15da86b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adamfranco&#39;s gravatar image" />
<p><span>adamfranco</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adamfranco has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72594" class="comments-container">
&#10;</div>
<div id="comment-tools-72594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72594-form-container" class="comment-form-container">
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

