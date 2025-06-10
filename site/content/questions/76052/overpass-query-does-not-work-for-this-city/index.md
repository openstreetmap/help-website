+++
type = "question"
title = "Overpass query does not work for this city"
description = '''Hello! I am querying an Overpass API in order to get the closest cities to another one with the following request: [out:json];node[&#x27;place&#x27;=&#x27;city&#x27;][&#x27;name&#x27;=&#x27;Malaga&#x27;]-&amp;gt;.center; node(around.center:100000)[&#x27;place&#x27;=&#x27;city&#x27;]; out; However, the above does not return anything unless I change Malaga with Má...'''
date = "2020-08-07T20:46:00Z"
lastmod = "2020-08-09T07:45:00Z"
weight = 76052
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/76052" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query does not work for this city](/questions/76052/overpass-query-does-not-work-for-this-city)

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
<span id="post-76052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76052-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I am querying an Overpass API in order to get the closest cities to another one with the following request: [out:json];node['place'='city']['name'='Malaga']-&gt;.center; node(around.center:100000)['place'='city']; out;</p>
<p>However, the above does not return anything unless I change Malaga with Málaga. Is this expected? I thought multilingual city names would be supported.</p>
<p>Thank you in advance and regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '20, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ec542e6179c2408e61aa79ad9cf7b121?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dejavits&#39;s gravatar image" />
<p><span>dejavits</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dejavits has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76052" class="comments-container">
&#10;</div>
<div id="comment-tools-76052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76052-form-container" class="comment-form-container">
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

<span id="76058"></span>

<div id="answer-container-76058" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76058-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dejavits has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think Overpass uses exactly what you asks him. So if you want to use an international name you should either use <code>name:xx=Malaga</code> (with XX being the code of the language, i.e. en, fr, de, it, etc.) or use a regex and write something like <code>~"name:[a-z][a-z]"~"Malaga"</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '20, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-76058" class="comments-container">
<span id="76065"></span>
<div id="comment-76065" class="comment">
<div id="post-76065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I have checked and name:en does not exist for this city, however, it works with name:de. I think the most convenient for me would be to use [a-z][a-z] but it does not work either: [out:json];node['place'='city']['name:[a-z][a-z]'='Malaga']-&gt;blablabla</p>
<p>Any idea why?</p>
</div>
<div id="comment-76065-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 09:56)</span> <span class="comment-user userinfo">dejavits</span>
</div>
</div>
<span id="76066"></span>
<div id="comment-76066" class="comment">
<div id="post-76066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You forgot the ~ before and after "name:[a-z][a-z]"</p>
</div>
<div id="comment-76066-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 10:01)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
<span id="76068"></span>
<div id="comment-76068" class="comment">
<div id="post-76068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In <a href="https://overpass-turbo.eu/s/WRh">this example</a> i used this query <code>[out:json];node['place'='city'][~"name:[a-z][a-z]"~"Malaga"]-&gt;.center; node(around.center:100000)['place'='city']; out;</code> and it worked.</p>
</div>
<div id="comment-76068-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 12:31)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
<span id="76077"></span>
<div id="comment-76077" class="comment">
<div id="post-76077-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! It worked :)</p>
</div>
<div id="comment-76077-info" class="comment-info">
<span class="comment-age">(09 Aug '20, 07:45)</span> <span class="comment-user userinfo">dejavits</span>
</div>
</div>
</div>
<div id="comment-tools-76058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76058-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76059"></span>

<div id="answer-container-76059" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76059-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally speaking the <a href="https://wiki.openstreetmap.org/wiki/Key:name"><code>name</code> tag</a> should carry the name in the local language, diacritics and all. Where this language isn't English there may be an additional <code>name:en</code> tag for the English name (and so on for other languages). The main exception to this rule is in a few places where there are several local languages and the local community have decided on a convention or a "neutral" language instead.</p>
<p>If you want to use overpass for this query you will probably need to look at the <code>name</code> and <code>name:__</code> tags.</p>
<p>Alternately you may want to do the initial geocoding with something like <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> and pass its response to Overpass for the second part of your query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '20, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76059" class="comments-container">
<span id="76064"></span>
<div id="comment-76064" class="comment">
<div id="post-76064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I have tried with name: en but still does not work. I believe this city does not have "en" tag because if I use name:de (German) it works!. Is there a way to search for the city name matching any of the available languages available for the city?</p>
</div>
<div id="comment-76064-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 09:55)</span> <span class="comment-user userinfo">dejavits</span>
</div>
</div>
</div>
<div id="comment-tools-76059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76059-form-container" class="comment-form-container">
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

