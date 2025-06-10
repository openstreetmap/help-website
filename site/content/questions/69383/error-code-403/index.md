+++
type = "question"
title = "Error code 403"
description = '''Hi We have been using openstreetmap for over a year now to present the location for some of our weather-stations in a windows application form. We use the gMap.net library and now all of the sudden we get Error code 403 (forbidden) in our application. This happen on Tuesday and is still the same, so...'''
date = "2019-05-31T08:52:00Z"
lastmod = "2019-06-03T10:48:00Z"
weight = 69383
keywords = [ "error403" ]
aliases = [ "/questions/69383" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Error code 403](/questions/69383/error-code-403)

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
<span id="post-69383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69383-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>We have been using openstreetmap for over a year now to present the location for some of our weather-stations in a windows application form. We use the gMap.net library and now all of the sudden we get Error code 403 (forbidden) in our application. This happen on Tuesday and is still the same, so this seems not to be any temporarily error.</p>
<p>Any suggestions for fixing this problem? Is there any way to check i we are "blocked" from OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error403" rel="tag" title="see questions tagged &#39;error403&#39;">error403</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '19, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/51bc76702aa55a6a7364bae282c82b53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KristoferK&#39;s gravatar image" />
<p><span>KristoferK</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KristoferK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69383" class="comments-container">
&#10;</div>
<div id="comment-tools-69383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69383-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="69388"></span>

<div id="answer-container-69388" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69388-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This has been discussed at length on the <a href="https://lists.openstreetmap.org/pipermail/dev/2019-May/thread.html#30629">dev</a> list.</p>
<p>The issue was raised with "greatmaps" <a href="https://github.com/radioman/greatmaps/issues/132">here</a>. Their response suggested that they just want to continue leeching free map tiles.</p>
<p>As Mike N has already noted, If you are using OSM's own hosted tiles, you will need to read <a href="https://operations.osmfoundation.org/policies/tiles/">OpenStreetMap Tile Usage Policy</a>. In this case you appear to have been adversely affected by the actions of "greatmaps"' maintainer. The problem is likely to continue until they change their attitude.</p>
<p>Can I suggest that you consider another source of map tiles? If you don't want to create your own then numerous <a href="https://switch2osm.org/providers/">providers</a> are available. Depending on your usage these will cost money - someone, somewhere has to host the servers and maintain them. If that isn't an option then <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">creating your own tile server</a> is pretty straightforward - I'd expect the level of background detail you need on a weather map is relatively low, which should reduce the database size needed to something relatively affordable in hosting terms.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '19, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69388" class="comments-container">
&#10;</div>
<div id="comment-tools-69388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69388-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69387"></span>

<div id="answer-container-69387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69387-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GreatMaps has used OpenStreetMap tiles as a free provider, which is no longer possible due to excessive usage which is blocking the intended use as help for map editors. See the <a href="https://operations.osmfoundation.org/policies/tiles/">OpenStreetMap Tile Usage Policy</a>.</p>
<p>It would be logical to modify the GreatMaps library to add a provider such as <a href="https://www.mapbox.com/">MapBox</a> as an alternate source. Note that while they are free to use for development, volume usage will require a paid plan.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '19, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '19, 13:20</strong> </span></p>
</div>
</div>
<div id="comments-container-69387" class="comments-container">
<span id="69389"></span>
<div id="comment-69389" class="comment">
<div id="post-69389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do Mapbox offer a drop-in tile server replacement for e.g. gMap.net? A brief check of their website doesn't suggest that they do, but I don't speak their language (I'm English, they're American) so I may be wrong.</p>
<p>The bigger "problem" with Mapbox is probably that they aren't "free" at volume - I've seen complaints (e.g. to the DWG) saying "yes we want lots of tiles, but we can't afford to pay" to which the answer is "I'm sorry, but OSM doesn't exist in order to reduce the cost base of your company".</p>
<p>(for the avoidance of any doubt - this is not a criticism of any commercial tile provider for not providing free tiles - it's a criticism of people asking for lots of them, without understanding that someone, somewhere, has to pay for them).</p>
</div>
<div id="comment-69389-info" class="comment-info">
<span class="comment-age">(31 May '19, 12:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69392"></span>
<div id="comment-69392" class="comment">
<div id="post-69392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mapbox doesn't offer this - it would seem to be worth their time to offer a GreatMaps fork as an option. But logically, it should be easy for the GreatMaps repo to offer Mapbox as a paid alternative source. I'll update my answer to note the pay at volume problem.</p>
</div>
<div id="comment-69392-info" class="comment-info">
<span class="comment-age">(31 May '19, 13:18)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="69426"></span>
<div id="comment-69426" class="comment">
<div id="post-69426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>But logically, it should be easy for the GreatMaps repo to offer Mapbox as a paid alternative source</p>
</blockquote>
<p>I'm not sure that that's actually an option - what I was trying to say above (perhaps not very clearly) was that I don't think that Mapbox offers a compatible source of tiles to e.g. <a href="https://a.tile.openstreetmap.org/2/1/1.png">https://a.tile.openstreetmap.org/2/1/1.png</a> . You could certainly argue that what they do offer is a better fit on mobile (their clients and libraries that use vector tiles) but I don't think that it would be "easy for the GreatMaps repo to offer Mapbox as a paid alternative source" - unless you can point to a way to do that?</p>
</div>
<div id="comment-69426-info" class="comment-info">
<span class="comment-age">(03 Jun '19, 10:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69387-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69424"></span>

<div id="answer-container-69424" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69424-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the replies. Making my own User-Agent string describing name and version of application and providing company page in the refererUrl solves the problem.</p>
<p>Am I thinking right in these things? User-agent and referer url? This way OSM should be able to identify our application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '19, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/51bc76702aa55a6a7364bae282c82b53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KristoferK&#39;s gravatar image" />
<p><span>KristoferK</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KristoferK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69424" class="comments-container">
&#10;</div>
<div id="comment-tools-69424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69424-form-container" class="comment-form-container">
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

