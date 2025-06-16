+++
type = "question"
title = "Public transport paths"
description = '''Hi OSM users! I&#x27;m currently trying to figure out how OSM works. I&#x27;ve been lurking around in the OSM wiki i just get more confused than before.  I would like to get help with the following. Not asking for direct answers but rather directions.  Am i supposed to host the OSM on local machine. Is there ...'''
date = "2014-07-12T15:35:00Z"
lastmod = "2014-07-13T13:49:00Z"
weight = 34845
keywords = [ "path", "public-transport", "subway", "providers" ]
aliases = [ "/questions/34845" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Public transport paths](/questions/34845/public-transport-paths)

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
<span id="post-34845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM users! I'm currently trying to figure out how OSM works. I've been lurking around in the OSM wiki i just get more confused than before. I would like to get help with the following. Not asking for direct answers but rather directions.</p>
<ol>
<li>Am i supposed to host the OSM on local machine.</li>
<li>Is there any third-party providers.</li>
<li>Is it possible to get the nearest public transport station by providing long, latitude. How?</li>
<li>Is it possible to get the most possible subways "number"(i.e the transport number eg. U1, buss 51) and direction by giving two long+lat, with X intervals.</li>
</ol>
<p>Feel free to answer all or only some question. Every comment is appreciated.</p>
<p>Hope this is not to obvious questions, i've tried to google many times and tried, reading the wiki and reading stack exchange posts without any success.</p>
<p>Regards br</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-subway" rel="tag" title="see questions tagged &#39;subway&#39;">subway</span> <span class="post-tag tag-link-providers" rel="tag" title="see questions tagged &#39;providers&#39;">providers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '14, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bac1f0379dcf89ceee32faa268fa03b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdheb&#39;s gravatar image" />
<p><span>sdheb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdheb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '14, 08:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-34845" class="comments-container">
&#10;</div>
<div id="comment-tools-34845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34845-form-container" class="comment-form-container">
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

<span id="34860"></span>

<div id="answer-container-34860" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Concerning your technical questions about public transport:<br />
</p>
<p>You might want to use a reverse geocoder as nominatim for finding the closest busstop. You can also do a lot of processing, if you learned about the PT model schema(s) and play with Overpass API queries. If you want to go into multimodal routing, you might want to look for existing solutions as <a href="http://www.opentripplanner.org">http://www.opentripplanner.org</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '14, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-34860" class="comments-container">
&#10;</div>
<div id="comment-tools-34860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34852"></span>

<div id="answer-container-34852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34852-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-34852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Sdheb, Welcome<br />
</p>
<ol>
<li>use OSM as you like it live on its own server and ad anything conform these rules, read <a href="https://wiki.openstreetmap.org/wiki/Legal">https://wiki.openstreetmap.org/wiki/Legal</a> If you go a different way please start your own map at a local server, after reading those rules.</li>
<li>no there's no third party providers, only supporters, read this as well <a href="https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap">https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap</a> and <a href="https://wiki.openstreetmap.org/wiki/Contribute_map_data">https://wiki.openstreetmap.org/wiki/Contribute_map_data</a> as well</li>
<li>since OSM is a database, you’ll be able to make any selection you like or wish to see. Use a rendering type you like. But as long as someone has added that data to the system you could use it. Otherwise you’ll have to add the data yourself or ask a lot of people politely to do so. 4 Almost the same answer if it’s in OSM you could get it out. It all comes down on the query you use. Please read the beginners pages as well, <a href="https://wiki.openstreetmap.org/wiki/Beginners%27_Guide">https://wiki.openstreetmap.org/wiki/Beginners%27_Guide</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '14, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '14, 13:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-34852" class="comments-container">
&#10;</div>
<div id="comment-tools-34852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34852-form-container" class="comment-form-container">
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

