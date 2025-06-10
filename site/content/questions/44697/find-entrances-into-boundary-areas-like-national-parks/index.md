+++
type = "question"
title = "Find entrances into boundary areas like national parks"
description = '''I&#x27;ve extracted some National Parks from Openstreetmap. But now I want to find out where the entrances are. Openstreetmap has some tags for it but it isn&#x27;t used that often. So I tought: An entrance into a national park is a road which crosses the border of that park. Must be true: You are going into ...'''
date = "2015-08-10T11:23:00Z"
lastmod = "2015-08-12T00:35:00Z"
weight = 44697
keywords = [ "openstreetmap", "overpass", "overpass-turbo", "algorithm" ]
aliases = [ "/questions/44697" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Find entrances into boundary areas like national parks](/questions/44697/find-entrances-into-boundary-areas-like-national-parks)

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
<span id="post-44697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44697-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've extracted some National Parks from Openstreetmap. But now I want to find out where the entrances are. Openstreetmap has some tags for it but it isn't used that often.</p>
<p>So I tought: An entrance into a national park is a road which crosses the border of that park. Must be true: You are going into the park. The only downside I can think off is that it could be a private road for staff or something but that should be a small percentage.</p>
<p><img src="http://i.stack.imgur.com/kjfFe.png" alt="alt text" /></p>
<p>So what is the best ways to find these points?</p>
<p>My guess: I know the boundaries of the park. So I can download all roads in that park. Then I can use the "Ray casting algorithm" for all sections of all roads in the parks to see if it crosses a border. When it does: that is a road that goes into the park. However, that might be very slow. If you have a large park with lots of roads inside it, it might take ages to check all segments. Is there a more clever way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '15, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLAnaconda&#39;s gravatar image" />
<p><span>NLAnaconda</span><br />
<span class="score" title="166 reputation points">166</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLAnaconda has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '15, 20:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-44697" class="comments-container">
<span id="44698"></span>
<div id="comment-44698" class="comment">
<div id="post-44698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/31909933/openstreetmap-get-all-entrances-in-a-park">https://stackoverflow.com/questions/31909933/openstreetmap-get-all-entrances-in-a-park</a></p>
</div>
<div id="comment-44698-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 11:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44697-form-container" class="comment-form-container">
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

<span id="44704"></span>

<div id="answer-container-44704" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44704-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NLAnaconda has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an Overpass API solution for it: it will find all ways, which intersect with boundary=national_park relations:</p>
<p>Try it in overpass turbo! <a href="http://overpass-turbo.eu/s/aS7">link</a></p>
<p>Just navigate to the area you're interested in and hit "Run". There's no need for a local DB or any other download.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '15, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '15, 15:03</strong> </span></p>
</div>
</div>
<div id="comments-container-44704" class="comments-container">
<span id="44705"></span>
<div id="comment-44705" class="comment">
<div id="post-44705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This works great!</p>
<p>One question: Some roads are the border/on the border. They light up as bordercorssing but some dont really go in the park. Is there a way to exclude these roads?</p>
</div>
<div id="comment-44705-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 16:22)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="44711"></span>
<div id="comment-44711" class="comment">
<div id="post-44711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you please try the following query: <a href="http://overpass-turbo.eu/s/aSN">http://overpass-turbo.eu/s/aSN</a> - this one should exclude highways which are part of the boundary relation itself. A detailed explanation for this query can be found on the linked stackoverflow page.</p>
</div>
<div id="comment-44711-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 20:40)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="44713"></span>
<div id="comment-44713" class="comment">
<div id="post-44713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess that some roads are on the boundary without being part of the boundary (like its an extra layer) Some are still highlighted. For example this one (north east) on Kruger National Park: <a href="http://overpass-turbo.eu/s/aSO">http://overpass-turbo.eu/s/aSO</a></p>
</div>
<div id="comment-44713-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 21:43)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="44715"></span>
<div id="comment-44715" class="comment">
<div id="post-44715-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://www.openstreetmap.org/way/327080110">Way 327080110</a> seems to be on the border. However, if you zoom in a bit, you'll notice that it actually crosses the border somewhere near node <a href="http://www.openstreetmap.org/node/3337923111">3337923111</a>.. that's why this way is also included in the result.</p>
</div>
<div id="comment-44715-info" class="comment-info">
<span class="comment-age">(11 Aug '15, 10:10)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="44724"></span>
<div id="comment-44724" class="comment">
<div id="post-44724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are right. Sorry. I think I can filter these roads out when I check if they have a node further into the parks.</p>
</div>
<div id="comment-44724-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 00:35)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
</div>
<div id="comment-tools-44704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44704-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44700"></span>

<div id="answer-container-44700" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44700-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could filter an OSM data file (e.g. for the whole planet or a region you care about) using <code>osmosis</code> to only include roads and parks. Then import it into postgis with <code>osm2pgsql</code>, then use a standard <code>ST_Intersection</code> SQL query to find places where a park is crossed with a road. Internally it uses something like the 'ray casting algorithm', but you don't have to care about that.</p>
<p>I don't know how slow it is, depending on the size of the data, that might be fast enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '15, 13:25</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-44700" class="comments-container">
&#10;</div>
<div id="comment-tools-44700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44700-form-container" class="comment-form-container">
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

