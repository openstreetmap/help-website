+++
type = "question"
title = "[closed] All Cities in Germany with boundaries and relation to its county as CSV"
description = '''Hello to the community! as a complete newbie in OSM and its API I first tried to read all the docs and helps and this forum, of course. But I have a problem to build a query and I do not know how to solve it without help.. My goal is having a CSV of:   in Germany only (47,6,55,15 ??? or {{geocodeAre...'''
date = "2015-10-31T11:41:00Z"
lastmod = "2015-11-01T19:44:00Z"
weight = 46272
keywords = [ "openstreetmap", "overpass", "cities", "overpass-turbo", "overpass-api" ]
aliases = [ "/questions/46272" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] All Cities in Germany with boundaries and relation to its county as CSV](/questions/46272/all-cities-in-germany-with-boundaries-and-relation-to-its-county-as-csv)

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
<span id="post-46272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46272-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Hello</strong> to the community!</p>
<p>as a complete newbie in OSM and its API I first tried to read all the docs and helps and this forum, of course. But I have a problem to build a query and I do not know how to solve it without help..</p>
<p>My goal is having a <strong>CSV</strong> of:</p>
<ul>
<li>in Germany only (47,6,55,15 ??? or {{geocodeArea:Germany}} in overpass-turbo style</li>
<li>all city names (admin_level="8" and "name")</li>
<li>relation from each city to it's corresponding county (admin_level="6")</li>
<li>the boundaries of each city</li>
</ul>
<p>Example CSV header:</p>
<ul>
<li>county-name, city ,city-boundaries,</li>
</ul>
<p>My sadly tries:</p>
<ul>
<li><a href="http://overpass-api.de/api/interpreter?data=(rel%5Badmin_level=%228%22%5D(47,6,55,15););out;"><code>http://overpass-api.de/api/interpreter?data=(rel[admin_level=%228%22](47,6,55,15););out;</code></a> (no csv of course)</li>
<li><a href="http://overpass-turbo.eu/s/cnX"><code>http://overpass-turbo.eu/s/cnX</code></a></li>
</ul>
<p>My sources I tried:</p>
<ul>
<li>several sites in the official wiki like: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example"><code>http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example</code></a></li>
<li><a href="https://help.openstreetmap.org/questions/13877/how-to-find-cities-and-states-using-osm-overpass-api"><code>https://help.openstreetmap.org/questions/13877/how-to-find-cities-and-states-using-osm-overpass-api</code></a></li>
<li><a href="https://help.openstreetmap.org/questions/19063/get-city-nodes-within-a-country-using-overpass-api"><code>https://help.openstreetmap.org/questions/19063/get-city-nodes-within-a-country-using-overpass-api</code></a></li>
<li>several other sources by Google</li>
</ul>
<p>Obviously I have:</p>
<ol>
<li>a logical problem to understand how to build a correct query which achieves the above and</li>
<li>I don't know how to get it correctly formatted as CSV.</li>
</ol>
<p>If you can <strong>help</strong> please do so <strong>:)</strong></p>
<p>Thanks in advance</p>
<p>sediosm</p>
<p>.</p>
<p>.</p>
<p><strong>UPDATE:</strong></p>
<p>as mentioned I have opened a thread in the german forum here: <a href="http://forum.openstreetmap.org/viewtopic.php?id=52563">forum thread</a></p>
<p>.</p>
<p>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '15, 11:41</strong></p>
<img src="https://secure.gravatar.com/avatar/af554a18a762bc9c172b5af6fac13f4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sediosm&#39;s gravatar image" />
<p><span>sediosm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sediosm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>08 Nov '15, 17:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-46272" class="comments-container">
&#10;</div>
<div id="comment-tools-46272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46272-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Follow-up on German Forum." by mmd 08 Nov '15, 17:37

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46273"></span>

<div id="answer-container-46273" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46273-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm afraid, what you're trying to do is not possible with Overpass API. You cannot combine several OSM objects into one CSV line.</p>
<p>The only option I see at the moment is to split the response up into multiple lines, like in the <a href="http://wiki.openstreetmap.org/wiki/DE:Overpass_API/Beispielsammlung#Apotheken_je_Kreis_z.C3.A4hlen">following example</a> for pharmacies per country. You probably came across this one, as you mentioned Overpass API by example in your original question.</p>
<p>In addition, try to limit the scope of your query to smaller regions and split it up into several requests. Otherwise this will take way too much time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '15, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '15, 12:36</strong> </span></p>
</div>
</div>
<div id="comments-container-46273" class="comments-container">
<span id="46274"></span>
<div id="comment-46274" class="comment">
<div id="post-46274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First of all many thanks for the ultra quick response! :)</p>
<p>Hm ok.. that explains why I never got good results.</p>
<p>Could you provide a query which gets all cities in Germany with their boundaries as csv? And a second one which gets all cities with their relation to its county (without any boundaries, just their names) as second csv?</p>
<p>Would that be possible?</p>
<p>If that would work it would be ok for me because i can do a correlation between those both csv locally..</p>
<p>Well and have you taken a look at my overpass_turbo query? Thats multilined but I still not able to get it working...</p>
</div>
<div id="comment-46274-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 16:11)</span> <span class="comment-user userinfo">sediosm</span>
</div>
</div>
<span id="46278"></span>
<div id="comment-46278" class="comment">
<div id="post-46278-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In case that you are from Germayn or you can speak at least German, I recommend to ask all your questions in the German sub forum at <a href="http://forum.openstreetmap.org/">http://forum.openstreetmap.org/</a> ... log in there with your existing OSM account.</p>
<p>There are specialists about boundaries and data extractions ... there we can develop a solution for you.</p>
</div>
<div id="comment-46278-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 21:16)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="46288"></span>
<div id="comment-46288" class="comment">
<div id="post-46288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/99/stephan75"></a><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan75</a>: yes that's something I would also recommend. I believe there are still some topics open here and the forum format is much more suitable to discuss different details or find alternative approaches. We have some users with a dedicate osm2pgsql database and they may also be able to support.</p>
</div>
<div id="comment-46288-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 16:05)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="46290"></span>
<div id="comment-46290" class="comment">
<div id="post-46290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds great thanks I will do that :) !</p>
</div>
<div id="comment-46290-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 18:27)</span> <span class="comment-user userinfo">sediosm</span>
</div>
</div>
<span id="46291"></span>
<div id="comment-46291" class="comment">
<div id="post-46291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11636/sediosm">@sediosm</a>: please mention a link to the follow-up thread here</p>
</div>
<div id="comment-46291-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 19:44)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46273-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46287"></span>

<div id="answer-container-46287" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46287-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depending on what you want to achieve, a more user friendly way may be to use <a href="https://wambachers-osm.website/boundaries">Wambacher's boundaries service</a>. There you can select level 6 relations by level 4 area. You can then export to any number of formats. You could link level 6 to level 4 by hand, or you could use a free sowftware like QGIS to do a spacial join (calculate centroid of level 6 within their area, than spatial join of these points with the level 4)</p>
<p>You need to log in to the servicce with your OSM user to be able to download data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '15, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '18, 14:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-46287" class="comments-container">
<span id="46289"></span>
<div id="comment-46289" class="comment">
<div id="post-46289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your thoughts I didn't mentioned the Wambachers service but I also tried it -&gt; but I need a CSV at the end and regarding QGIS: I do not want to install a special software to doing those joins etc.. nevertheless thanks again for your reply</p>
</div>
<div id="comment-46289-info" class="comment-info">
<span class="comment-age">(01 Nov '15, 18:26)</span> <span class="comment-user userinfo">sediosm</span>
</div>
</div>
</div>
<div id="comment-tools-46287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46287-form-container" class="comment-form-container">
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

