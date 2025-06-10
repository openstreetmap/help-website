+++
type = "question"
title = "OSM public transport directions"
description = '''I am looking for a service that uses OSM public transport data and combines walking and bus directions. Essentially I&#x27;d like to be able to give a departure point and a arrival point and then the server would determine the quickest public transport route from the departure point to the destination. D...'''
date = "2015-07-09T10:22:00Z"
lastmod = "2015-07-09T12:14:00Z"
weight = 44058
keywords = [ "directions", "map", "osm" ]
aliases = [ "/questions/44058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM public transport directions](/questions/44058/osm-public-transport-directions)

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
<span id="post-44058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44058-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a service that uses OSM public transport data and combines walking and bus directions. Essentially I'd like to be able to give a departure point and a arrival point and then the server would determine the quickest public transport route from the departure point to the destination.</p>
<p>Does anyone know of a directions library that offers this other than Google Maps API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '15, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/62af1de8bdba81e7ec1f16e87f26f083?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoelK3&#39;s gravatar image" />
<p><span>JoelK3</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoelK3 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '15, 11:05</strong> </span></p>
</div>
</div>
<div id="comments-container-44058" class="comments-container">
&#10;</div>
<div id="comment-tools-44058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44058-form-container" class="comment-form-container">
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

<span id="44061"></span>

<div id="answer-container-44061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44061-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://www.opentripplanner.org/">OpenTripPlanner</a>. They provide the software to create a multi-modal journey planner like what you are looking for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '15, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-44061" class="comments-container">
<span id="44064"></span>
<div id="comment-44064" class="comment">
<div id="post-44064-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What implementations of that outside of <a href="http://maps.trimet.org/#/">Portland</a> are there? A <a href="http://www.google.co.uk/search?q=opentripplanner+implementation+-site:github.com&amp;tbs=li:1&amp;prmd=ivns&amp;ei=11WeVdHkOcbW7AbCoIaIAQ&amp;start=10&amp;sa=N">quick web search</a> doesn't find much (although it does turn up "how to set up your own" links like <a href="http://pleasantprogrammer.com/posts/open-trip-planner.html">this</a> and <a href="http://stackoverflow.com/questions/15596271/offline-transit-routing-algorithm">this</a>). As I read it the questioner's looking for a preexisting service rather than how to create their own.</p>
<p>(asking because I'm genuinely interested in the answer too!)</p>
</div>
<div id="comment-44064-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 12:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44061-form-container" class="comment-form-container">
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

