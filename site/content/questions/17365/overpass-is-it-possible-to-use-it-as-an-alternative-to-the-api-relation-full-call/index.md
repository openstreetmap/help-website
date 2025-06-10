+++
type = "question"
title = "Overpass:  Is it possible to use it as an alternative to the API relation /full call?"
description = '''(prompted by this question and this question) Imagine that I&#x27;d like a .osm file containing every sub-relation, way and node that&#x27;s part of relation 50288. I could do an API call to: http://www.openstreetmap.org/api/0.6/relation/RELATION/full But I don&#x27;t really want the API taking the time to sort ou...'''
date = "2012-11-01T17:28:00Z"
lastmod = "2012-11-01T21:44:00Z"
weight = 17365
keywords = [ "overpass", "api", "xapi", "full", "relation" ]
aliases = [ "/questions/17365" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Is it possible to use it as an alternative to the API relation /full call?](/questions/17365/overpass-is-it-possible-to-use-it-as-an-alternative-to-the-api-relation-full-call)

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
<span id="post-17365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17365-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>(prompted by <a href="https://help.openstreetmap.org/questions/17311/missing-way-in-a-relation">this question</a> and <a href="https://help.openstreetmap.org/questions/17336/overpass-api-query-question">this question</a>)</p>
<p>Imagine that I'd like a .osm file containing every sub-relation, way and node that's part of relation <a href="http://www.openstreetmap.org/browse/relation/50288">50288</a>. I could do an API call to:</p>
<p><a href="http://www.openstreetmap.org/api/0.6/relation/RELATION/full">http://www.openstreetmap.org/api/0.6/relation/RELATION/full</a></p>
<p>But I don't really want the API taking the time to sort out that rather large result for me rather than processing time-critical requests for mappers.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> looks like it can do things like this, but there doesn't seem to be an example of it on the wiki. Can anyone suggest an Overpass query that would return the same data as an API relation /full call? If not Overpass, is there anything else out there that can?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-full" rel="tag" title="see questions tagged &#39;full&#39;">full</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '12, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17365" class="comments-container">
&#10;</div>
<div id="comment-tools-17365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17365-form-container" class="comment-form-container">
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

<span id="17369"></span>

<div id="answer-container-17369" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17369-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it is possible. Please use</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel(50288);%3E;);out+meta;">http://overpass-api.de/api/interpreter?data=(rel(RELATION);&gt;;);out meta;</a></p>
<p>The example from above:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel(50288);%3E;);out+meta;">http://overpass-api.de/api/interpreter?data=(rel(50288);&gt;;);out meta;</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-17369" class="comments-container">
<span id="17371"></span>
<div id="comment-17371" class="comment">
<div id="post-17371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent - thanks.</p>
</div>
<div id="comment-17371-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 19:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17369-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17379"></span>

<div id="answer-container-17379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17379-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If for any reasons you don't want to learn the overpass API syntax, or you use a tool that allready talk the API 0.6 syntax and don't want to/can't convert.</p>
<p>I wrote an API 0.6 to Overpass API converter that you can query here :</p>
<p><a href="http://api.openstreetmap.fr/api/0.6/relation/RELATION">http://api.openstreetmap.fr/api/0.6/relation/RELATION</a> ID/full</p>
<p>-&gt; <a href="http://api.openstreetmap.fr/api/0.6/relation/50288/full">http://api.openstreetmap.fr/api/0.6/relation/50288/full</a></p>
<p>wiki doc : <a href="http://wiki.openstreetmap.org/wiki/Servers/api.openstreetmap.fr">http://wiki.openstreetmap.org/wiki/Servers/api.openstreetmap.fr</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0137f3597f9ca0efbda5c3b1e2678aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sly&#39;s gravatar image" />
<p><span>sly</span><br />
<span class="score" title="290 reputation points">290</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sly has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-17379" class="comments-container">
&#10;</div>
<div id="comment-tools-17379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17379-form-container" class="comment-form-container">
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

