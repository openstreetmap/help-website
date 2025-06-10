+++
type = "question"
title = "Mapping application"
description = '''I am thinking of making a mapping application using Peter Laurence&#x27;s MapView on Android using OSM tiles; however, I am aware that creating mapping mobile applications can put a heaving load on tile servers. If I limited each user to, say, 100 tiles per day, would this be enough to address this probl...'''
date = "2024-01-01T20:58:00Z"
lastmod = "2024-01-01T21:18:00Z"
weight = 88108
keywords = [ "load", "mapping", "server" ]
aliases = [ "/questions/88108" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping application](/questions/88108/mapping-application)

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
<span id="post-88108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am thinking of making a mapping application using Peter Laurence's MapView on Android using OSM tiles; however, I am aware that creating mapping mobile applications can put a heaving load on tile servers. If I limited each user to, say, 100 tiles per day, would this be enough to address this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jan '24, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/23f02f4dec9219cf2e46ebdf840afbb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Brossard&#39;s gravatar image" />
<p><span>Chris Brossard</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Brossard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88108" class="comments-container">
&#10;</div>
<div id="comment-tools-88108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88108-form-container" class="comment-form-container">
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

<span id="88109"></span>

<div id="answer-container-88109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88109-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-88109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's actually an official OSM tile usage policy <a href="https://operations.osmfoundation.org/policies/tiles/">here</a> that should take the guesswork out of things. If you want to display raster map tiles in an Android application you can of course host your own tiles - see <a href="https://switch2osm.org/serving-tiles/">here</a> for details of that.</p>
<p>However, for an Android application that you're starting to write now, raster map tiles may not be the best approach. As an example, probably the most widely-used example, <a href="https://wiki.openstreetmap.org/wiki/StreetComplete">StreetComplete</a>, uses vector map tiles (from <a href="https://wiki.openstreetmap.org/wiki/Jawg">Jawg</a> I believe).</p>
<p>Whichever makes most sense to you at this point depends on what you're trying to do - as an introduction to Android development raster map tiles would be a great "way in" as you get to see something on screen fairly quickly and get useful experience with the Android WebView. A "test app" built like this isn't going to trouble the scorers looking to enforce the tile usage policy since only a couple of people would use it. A commercial app made in this way absolutely would be a problem, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '24, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-88109" class="comments-container">
&#10;</div>
<div id="comment-tools-88109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88109-form-container" class="comment-form-container">
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

