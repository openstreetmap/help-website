+++
type = "question"
title = "Motorway Layout"
description = '''Hello Dear All,  I would like to export a .osm file in which only the Motorways (which are shown in red in open street map) are available for a whole small country like Belgium.  How can I export the above-mentioned file from the open street map?  Thank you all in advance for helping me with this is...'''
date = "2020-04-02T10:48:00Z"
lastmod = "2020-04-09T15:18:00Z"
weight = 73953
keywords = [ "motorway", "layer", "osm" ]
aliases = [ "/questions/73953" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Motorway Layout](/questions/73953/motorway-layout)

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
<span id="post-73953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73953-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Dear All,</p>
<p>I would like to export a .osm file in which only the Motorways (which are shown in red in open street map) are available for a whole small country like Belgium.</p>
<p>How can I export the above-mentioned file from the open street map?</p>
<p>Thank you all in advance for helping me with this issue.</p>
<p>Regards, Behzad</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '20, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5d2df93f3a8dd83567ceb009bb176b5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Behzad&#39;s gravatar image" />
<p><span>Behzad</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Behzad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73953" class="comments-container">
&#10;</div>
<div id="comment-tools-73953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73953-form-container" class="comment-form-container">
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

<span id="73954"></span>

<div id="answer-container-73954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73954-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-73954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can run this <a href="http://overpass-turbo.eu/s/SfN">Overpass query</a> in OverpassTurbo (the link takes you there). Then press Run (or Execute, I have the UI in Dutch). Then click Export and choose the format you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '20, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-73954" class="comments-container">
<span id="73957"></span>
<div id="comment-73957" class="comment">
<div id="post-73957-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You might want to add highway=motorway_link to also fetch the interlinks of crossing motorways if you need those. It will also give you the ramps on/off the motorway, though. In the end you might need to do some cleaning.</p>
</div>
<div id="comment-73957-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 14:37)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73958"></span>
<div id="comment-73958" class="comment">
<div id="post-73958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for providing the links. it is very healful.</p>
<ul>
<li>I cannot export an.OSM file. How can I do so?</li>
<li>what if I want two maps? One that includes only Motorways and the other one includes motorways (Shown in red) and Main roads (shown in yellow)?</li>
</ul>
</div>
<div id="comment-73958-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 14:38)</span> <span class="comment-user userinfo">Behzad</span>
</div>
</div>
<span id="73962"></span>
<div id="comment-73962" class="comment">
<div id="post-73962-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To be able to export to OSM format we need the query result in xml. Try the <a href="http://overpass-turbo.eu/s/Sgn">updated query</a>. I also added lines to include motorway links and primary highways.</p>
<p>This extract could become huge. So watch out when trying to run it (I didn't). You can remove the respective lines again if you want.</p>
</div>
<div id="comment-73962-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 15:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73984"></span>
<div id="comment-73984" class="comment">
<div id="post-73984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear TZom, Thank you very much. I really appreciate your favor. This is exactly what I want!</p>
<p>Besides, How can I add other elements (for instance: railways)!? Regards,</p>
</div>
<div id="comment-73984-info" class="comment-info">
<span class="comment-age">(03 Apr '20, 10:11)</span> <span class="comment-user userinfo">Behzad</span>
</div>
</div>
</div>
<div id="comment-tools-73954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73954-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73985"></span>

<div id="answer-container-73985" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73985-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To expand on your additional question (<em>How can I add other elements (for instance: railways)!?</em>):</p>
<p>Objects in OSM are attributed by a main tag. For any sorts of highways that is <a href="https://wiki.openstreetmap.org/wiki/Key:highway"><code>highway=</code></a>, e.g. you have seen <code>highway=motorway</code> and <code>highway=motorway</code> in the Overpass queries now. Other useful main tags you might be interested in are <a href="https://wiki.openstreetmap.org/wiki/Key:railway"><code>railway=</code></a> and <a href="https://wiki.openstreetmap.org/wiki/Key:waterway"><code>waterway=</code></a>. If you look at the linked pages you find the mostly used values for these tags. I suppose you can change the Overpass query yourself. For other types of objects just search around on the OpenStreetMap Wiki.</p>
<p>Maybe worth noting that sometimes these features are not mapped as simple lines but as multipolygons. Then you would have to query not only for <code>way["highway"="xyz"]</code> but also for <code>relation["highway"="xyz"]</code>. I don't expect this to happen much for these kind of features, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '20, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-73985" class="comments-container">
<span id="73991"></span>
<div id="comment-73991" class="comment">
<div id="post-73991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you again dear TZorn, I tried to make some modification in the quarry that you provided and I come up with the above error:</p>
<p>"An error occured during the execution of the overpass query! This is what overpass API returned: Error: runtime error: […] Please check /api/status for the quota of your IP address."</p>
<p>Besides, is it possible to indicate a specific speed limit for a highway type?</p>
</div>
<div id="comment-73991-info" class="comment-info">
<span class="comment-age">(03 Apr '20, 14:58)</span> <span class="comment-user userinfo">Behzad</span>
</div>
</div>
<span id="73992"></span>
<div id="comment-73992" class="comment">
<div id="post-73992-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are some limits on usage so not to overload the servers. Best contact the server maintainers to find out more (if no one reading here knows more than me).</p>
</div>
<div id="comment-73992-info" class="comment-info">
<span class="comment-age">(03 Apr '20, 17:06)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="74023"></span>
<div id="comment-74023" class="comment">
<div id="post-74023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much</p>
</div>
<div id="comment-74023-info" class="comment-info">
<span class="comment-age">(06 Apr '20, 08:50)</span> <span class="comment-user userinfo">Behzad</span>
</div>
</div>
<span id="74076"></span>
<div id="comment-74076" class="comment">
<div id="post-74076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's because you're downloading 60mb each time you run it. Try this: <a href="http://overpass-turbo.eu/s/SCQ">http://overpass-turbo.eu/s/SCQ</a></p>
<p>[bbox:{{bbox}}]; way[highway~"^(motorway|motorway_link|primary)$"]; out geom;</p>
<p>bbox limits the output to the size of your window. out:xml isn't really required as it's converted when you export it as raw OSM data.</p>
</div>
<div id="comment-74076-info" class="comment-info">
<span class="comment-age">(09 Apr '20, 15:18)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-73985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73985-form-container" class="comment-form-container">
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

