+++
type = "question"
title = "How to download country and other boundaries and work out what boundaries a node is in"
description = '''Hi, I want to write a desktop application that allows visually impaired users to browse the world. The user starts at country level with one country having the focus. The user can then use keystrokes to find bordering countries with audio feedback on the direction to that country and its distance. T...'''
date = "2023-10-11T19:55:00Z"
lastmod = "2023-10-17T19:54:00Z"
weight = 87892
keywords = [ "boundaries", "country", "borders" ]
aliases = [ "/questions/87892" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to download country and other boundaries and work out what boundaries a node is in](/questions/87892/how-to-download-country-and-other-boundaries-and-work-out-what-boundaries-a-node-is-in)

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
<span id="post-87892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87892-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to write a desktop application that allows visually impaired users to browse the world. The user starts at country level with one country having the focus. The user can then use keystrokes to find bordering countries with audio feedback on the direction to that country and its distance. The user can jump to a neighbouring country and so navigate the world. Could also apply to oceans.</p>
<p>The user can choose to go down an administrative level and use the same process to navigate within a country. For examples, states in the US or counties in the UK. And again, could apply to the seas that make up oceans.</p>
<p>I also want to load cities and towns and other points of interest. These could be nodes like a railway station), a way (like a river) or a polygon (like a national park).</p>
<p>I have a little experience with OSM as I've written an application that lets the user navigate roads / highways by moving from intersection to intersection. For this I download nodes and ways to my application on the fly using an overpass query. As the user moves near the edge of the current data then more data is downloaded.</p>
<p>I was thinking of using a similar approach for my world navigating application but I have a couple of major problems.</p>
<p>Firstly, I can't work out what the query is to download boundary data for a country or internal administrative areas. I really struggle with the overpass API. I've also read that country boundaries on OSM include maritime boundaries and not the physical border of the land. And I only really need quite low res data.</p>
<p>Secondly, I have a query that downloads all the cities and towns in a country but then to work out what areas / polygons they are in sounds like a computationally heavy task to do on the fly.</p>
<p>So is my approach a good one or is there a better approach? Is doing it on the fly sensible or am I better off building a database? I mean, I could probably pack quite a lot of useful data into 10Mb. And is OSM a good source of boundary data? If it is, please can someone help with suitable overpass queries. And if not, what are alternatives?</p>
<p>I haven't yet written a line of code for this project although I'm very excited about it since it may lead to me being able to explore the world in a way I can't currently do any other way. So any help much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '23, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87892" class="comments-container">
&#10;</div>
<div id="comment-tools-87892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87892-form-container" class="comment-form-container">
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

<span id="87910"></span>

<div id="answer-container-87910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87910-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Downloading country boundaries with overpass is quite simple: <a href="https://overpass-turbo.eu/s/1C5x">https://overpass-turbo.eu/s/1C5x</a> but the amount of data is enormous, since all details are contained in the data.</p>
<p>Subunits can be loaded by setting the appropriate admin_level: 4 = states, 6 = counties, 8 = cities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '23, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/4a9f7e2c19add83a72dabcd00693cf93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fx99&#39;s gravatar image" />
<p><span>fx99</span><br />
<span class="score" title="196 reputation points">196</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fx99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87910" class="comments-container">
&#10;</div>
<div id="comment-tools-87910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87910-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87911"></span>

<div id="answer-container-87911" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many thanks for your reply. So forgive me but I couldn't follow the example to download Luxembourg's border. Can I highlight that I am blind so Overpasss turbo isn't that obvious a thing for me to use as I don't see the graphical output. The active part of the query seems to be: nwr["admin_level"="2"]["boundary"="administrative"]<a href="%7B%7Bbbox%7D%7D">"int_name"="Luxembourg"</a>; When I have used the overpass API to date I start a URL with: <a href="http://overpass-api.de/api/interpreter?data=">http://overpass-api.de/api/interpreter?data=</a> So I pasted the active part of the query to the end of this and added 'out;' The complete thing is: <a href="http://overpass-api.de/api/interpreter?data=nwr%5B">http://overpass-api.de/api/interpreter?data=nwr["admin_level"="2"]["boundary"="administrative"]</a><a href="%7B%7Bbbox%7D%7D">"int_name"="Luxembourg"</a>;out; And I paste this into my favourite browser. I get a parse error though. Where am I going wrong?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '23, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87911" class="comments-container">
&#10;</div>
<div id="comment-tools-87911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87911-form-container" class="comment-form-container">
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

