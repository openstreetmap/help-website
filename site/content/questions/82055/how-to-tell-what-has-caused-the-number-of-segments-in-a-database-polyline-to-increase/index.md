+++
type = "question"
title = "How to tell what has caused the number of segments in a database polyline to increase?"
description = '''A bit of background - I&#x27;m keeping an eye on accidental breakages of some long distance paths in the UK as described here. I&#x27;ve recently noticed that the results of  SELECT count(*) FROM planet_osm_line WHERE (osm_id = &#x27;-112695&#x27;);  has gone up from 41 to 42 in the last 24 hours. That relation is the ...'''
date = "2021-10-07T13:48:00Z"
lastmod = "2021-10-08T10:33:00Z"
weight = 82055
keywords = [ "josm", "relations" ]
aliases = [ "/questions/82055" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tell what has caused the number of segments in a database polyline to increase?](/questions/82055/how-to-tell-what-has-caused-the-number-of-segments-in-a-database-polyline-to-increase)

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
<span id="post-82055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82055-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A bit of background - I'm keeping an eye on accidental breakages of some long distance paths in the UK as described <a href="https://www.openstreetmap.org/user/SomeoneElse/diary">here</a>. I've recently noticed that the results of</p>
<pre><code>SELECT count(*) FROM planet_osm_line WHERE (osm_id = &#39;-112695&#39;);</code></pre>
<p>has gone up from 41 to 42 in the last 24 hours. That relation is the <a href="https://www.openstreetmap.org/relation/112695">Midshires Way</a>. I can see how many pieces it is really in by using <a href="https://ra.osmsurround.org/">this</a> external relation analyser, but I don't want to use that more than I have to to avoid a significant load on an external site. I can look at the relation history <a href="https://www.openstreetmap.org/relation/112695/history">in OSM</a> and <a href="https://www.openstreetmap.org/relation/112695/history">externally</a>, and I can see that the relation itself has not changed; the change must have been to one of the constituent ways in the relation.</p>
<p>How can I easily see which ways that make up a relation have been recently changed, preferably using something I can install and run locally?</p>
<p>What I normally do is to look at the graphs in the graph from osmsurround and go through them one by one, but with a relation in many pieces, that's a lot of work. I can see 7 "obvious" gaps to fill in; the breakages range from 11 months to 6 years ago. None seem to be more recent than that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '21, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82055" class="comments-container">
<span id="82056"></span>
<div id="comment-82056" class="comment">
<div id="post-82056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One method that does work of course is to "manually look at each of the 964 ways in the relation and see what was updated recently".</p>
<p>I've just done that for the first 40 or so and found a changeset that I think introduced the <a href="https://overpass-turbo.eu/s/1bQ7">break</a> that I'm looking for.</p>
<p>The question still stands though - clearly manually checking 964 relation way components (or writing a script to do it) is harder work than necessary of something already exists.</p>
</div>
<div id="comment-82056-info" class="comment-info">
<span class="comment-age">(07 Oct '21, 13:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82073"></span>
<div id="comment-82073" class="comment">
<div id="post-82073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not really an answer, but perhaps using an OSH file, osmosis-tool &amp; the OPL format may work. I've not tried keeping an OSH file up-to-date with changes which would meet the "install &amp; run locally" criterion.</p>
<p>Perhaps Overpass offers something, this is an attempt to do a daily diff on the relation <a href="https://overpass-turbo.eu/s/1bQS">https://overpass-turbo.eu/s/1bQS</a> , but I'm sure there are multiple other ways.</p>
</div>
<div id="comment-82073-info" class="comment-info">
<span class="comment-age">(07 Oct '21, 21:29)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82055-form-container" class="comment-form-container">
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

<span id="82084"></span>

<div id="answer-container-82084" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82084-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass does allow examination of what has changed between two dates. For Midshires Way this looks like <a href="https://overpass-turbo.eu/s/1bRO">this</a> (also below). <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_date_of_change_.28changed.29">Changed</a> allows two dates so changes in a specific period can be filtered.</p>
<pre><code>rel(112695); // Midshires Way
(._;&gt;&gt;;); // recurse down for relation members
way._(changed:&quot;2021-10-06T07:00:00Z&quot;); // only select ways which have changed since 6 October
(._;&gt;;); // get geometry of the ways</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '21, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82084" class="comments-container">
&#10;</div>
<div id="comment-tools-82084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82084-form-container" class="comment-form-container">
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

