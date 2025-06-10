+++
type = "question"
title = "Getting a list of colonies/neighborhoods for a particular city"
description = '''Hi My goal is to get a list of all possible colonies/neighborhoods for particular indian city along with their coordinates. I plan to fetch this data from openstreetmap (if its allowed) once, and then use it on my own site. Is there a way to fetch this data from OSM ? I tried looking through the xap...'''
date = "2012-05-28T06:58:00Z"
lastmod = "2012-05-29T17:38:00Z"
weight = 12991
keywords = [ "colonies", "api" ]
aliases = [ "/questions/12991" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting a list of colonies/neighborhoods for a particular city](/questions/12991/getting-a-list-of-coloniesneighborhoods-for-a-particular-city)

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
<span id="post-12991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>My goal is to get a list of all possible colonies/neighborhoods for particular indian city along with their coordinates. I plan to fetch this data from openstreetmap (if its allowed) once, and then use it on my own site. Is there a way to fetch this data from OSM ?</p>
<p>I tried looking through the xapi documentation, but didn't understand whether OSM xapi can do what I want.</p>
<p>Thanks</p>
<p>Edit: I tried this command to import into a database, but its not working. Can someone tell me whats wrong? osmosis --read-xml file="NewDelhi.osm" --write-apidb host="localhost" dbType="mysql" database="os" user= "root"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-colonies" rel="tag" title="see questions tagged &#39;colonies&#39;">colonies</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '12, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f2bc428e0b4f60ddc964dcec7370d845?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goddamnit&#39;s gravatar image" />
<p><span>goddamnit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goddamnit has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '12, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-12991" class="comments-container">
<span id="13064"></span>
<div id="comment-13064" class="comment">
<div id="post-13064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I should try explaining my question again: All I want is the lat/long of the places in the marked circles:<img src="http://i.imgur.com/ehfUB.jpg" alt="marked circles:" /></p>
<p>Please someone just give me a kick in the right direction please. Thanks</p>
</div>
<div id="comment-13064-info" class="comment-info">
<span class="comment-age">(29 May '12, 12:49)</span> <span class="comment-user userinfo">goddamnit</span>
</div>
</div>
</div>
<div id="comment-tools-12991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12991-form-container" class="comment-form-container">
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

<span id="13077"></span>

<div id="answer-container-13077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13077-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking an example of "Lajpat Nagar", which is one of those that you highlighted, I:</p>
<ol>
<li>Searched for it to find out that you were talking about New Delhi, then</li>
<li>Viewed the map for that location</li>
<li>Selected "browse map data" on the edit menu</li>
<li>Clicked on the green dot associated with "Lajpat Nagar"</li>
<li>Then clicked on details, which displays <a href="http://wiki.openstreetmap.org/wiki/Xapi">this</a></li>
</ol>
<p>There we can see that it's a "place=suburb" (and we can see its coordinates). If you want to extract multiple suburbs from an area you can use one of the options on the <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> page.</p>
<p>An XAPI query using Mapquest's instance would be something like this:</p>
<pre><code>wget http://open.mapquestapi.com/xapi/api/0.6/*[place=suburb][bbox=77.1883,28.5743,77.2476,28.627]</code></pre>
<p>That fetches back a .OSM XML file - if you open that in a text editor you can figure out what's what.</p>
<p>Similarly, we can see that the <a href="http://www.openstreetmap.org/browse/way/80513396">Asiad Games Sports Complex</a> is a "leisure=sports_centre". This one's a little more complex because it's a closed way (an area) - you can click on each node to get a series of coordinates of the outside of it, and if you do an XAPI query you'll get the way and constituent nodes.</p>
<p>A quick way to figure out the coordinates you need for the XAPI is to click the "Export" tab on the OSM map and size the window to cover the area you want - then just copy the values from the export pane.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-13077" class="comments-container">
<span id="13082"></span>
<div id="comment-13082" class="comment">
<div id="post-13082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much for answering, I'll try this method asap!</p>
</div>
<div id="comment-13082-info" class="comment-info">
<span class="comment-age">(29 May '12, 17:38)</span> <span class="comment-user userinfo">goddamnit</span>
</div>
</div>
</div>
<div id="comment-tools-13077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13077-form-container" class="comment-form-container">
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

