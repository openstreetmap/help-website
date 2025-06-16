+++
type = "question"
title = "List of streets and name of city/town it belongs to"
description = '''Hi,  Before that, I already read that one, https://help.openstreetmap.org/questions/32163/how-to-filter-only-street-names-and-city-id-in-osmfilter, and to my knowledge, didn&#x27;t see any answer.  So I am willing to use osmfilter and extract the list of street alongside the lat and alt and the city/town...'''
date = "2014-05-21T11:51:00Z"
lastmod = "2015-03-03T17:12:00Z"
weight = 33348
keywords = [ "openstreetmap", "streetnames", "osm", "city" ]
aliases = [ "/questions/33348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [List of streets and name of city/town it belongs to](/questions/33348/list-of-streets-and-name-of-citytown-it-belongs-to)

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
<span id="post-33348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33348-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Before that, I already read that one, <a href="/questions/32163/how-to-filter-only-street-names-and-city-id-in-osmfilter,">https://help.openstreetmap.org/questions/32163/how-to-filter-only-street-names-and-city-id-in-osmfilter,</a> and to my knowledge, didn't see any answer.</p>
<p>So I am willing to use osmfilter and extract the list of street alongside the lat and alt and the city/town/whatever it belongs to.</p>
<p>So for streets it is that: osmfilter 1.o5m --keep="highway=cycleway highway=path highway=primary highway=residential highway=tertiary highway=living_street"</p>
<p>Cities: spain.o5m --keep-nodes="place=city =town =village =hamlet =suburb =province" --keep-ways= --keep-relations= &gt;mycity.osm which I got from here: <a href="/questions/29597/write-error-when-filtering-nodes-with-osmfilter-on-windows">https://help.openstreetmap.org/questions/29597/write-error-when-filtering-nodes-with-osmfilter-on-windows</a></p>
<p>Now, how do I mix them and afterwards I am able to extract the list in a csv of the street, its lat and alt and the city it belongs to.</p>
<p>Thanks for the help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '14, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/56e2b481efdbc4c76664921091bb49ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shikiso&#39;s gravatar image" />
<p><span>Shikiso</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shikiso has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33348" class="comments-container">
<span id="40810"></span>
<div id="comment-40810" class="comment">
<div id="post-40810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried mixing them but I just keep getting the list of streets with just the lat and alt, really can't figure this out. Please some help.</p>
<p>I think that it can also probably be done by just one file instead of mixing two of them.</p>
<p>Thanks in advance.</p>
</div>
<div id="comment-40810-info" class="comment-info">
<span class="comment-age">(05 Feb '15, 17:55)</span> <span class="comment-user userinfo">Shikiso</span>
</div>
</div>
<span id="41424"></span>
<div id="comment-41424" class="comment">
<div id="post-41424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect that someone's going to need to do a complete worked example here.</p>
</div>
<div id="comment-41424-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 16:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33348-form-container" class="comment-form-container">
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

<span id="33361"></span>

<div id="answer-container-33361" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33361-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The one answer to your two questions is <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a>.</p>
<p>Do a search on that wiki page about "merge" and "csv".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '14, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-33361" class="comments-container">
<span id="41421"></span>
<div id="comment-41421" class="comment">
<div id="post-41421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried mixing them but I just keep getting the list of streets with just the lat and alt, really can't figure this out. Please some help.</p>
<p>I think that it can also probably be done by just one file instead of mixing two of them.</p>
<p>Thanks in advance.</p>
<p>Help please!!</p>
</div>
<div id="comment-41421-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 16:08)</span> <span class="comment-user userinfo">Shikiso</span>
</div>
</div>
<span id="41474"></span>
<div id="comment-41474" class="comment">
<div id="post-41474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please tell us in DETAIL:</p>
<p>How did you mix what files exactly? what is the result you get in detail? What is the result you want to have?</p>
<p>PS: if you need to post bigger files or text, consider to ask this again in OSM forum at <a href="http://forum.openstreetmap.org">http://forum.openstreetmap.org</a> -&gt; "Questions and Answers"</p>
</div>
<div id="comment-41474-info" class="comment-info">
<span class="comment-age">(03 Mar '15, 17:12)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-33361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33361-form-container" class="comment-form-container">
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

