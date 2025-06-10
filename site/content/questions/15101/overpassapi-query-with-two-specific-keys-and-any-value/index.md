+++
type = "question"
title = "OverpassAPI query with two specific keys and any value"
description = '''I am trying to retrieve a list of objects with at least two specific keys without specifying the values for those keys using the OverpassAPI. This is the query I thought should list me all ways with at least a highway and a name tag: http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way...'''
date = "2012-08-15T08:11:00Z"
lastmod = "2012-08-15T11:57:00Z"
weight = 15101
keywords = [ "overpass", "query" ]
aliases = [ "/questions/15101" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OverpassAPI query with two specific keys and any value](/questions/15101/overpassapi-query-with-two-specific-keys-and-any-value)

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
<span id="post-15101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15101-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to retrieve a list of objects with at least <em>two</em> specific keys <em>without</em> specifying the <em>values</em> for those keys using the OverpassAPI.</p>
<p>This is the query I thought should list me all ways with at least a <em>highway</em> and a <em>name</em> tag:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way[highway][name]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p>However, it just returns nothing. Specifying a <em>highway value</em> works as expected:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way[highway=residential][name]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p>Specifying <em>no highway value</em> but a specific <em>name</em> also works as expected:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way[highway][name=%22Langewiesener%20Straße%22]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p>So, why doesn't the first query work without a value for <em>both</em> the highway and name tag? Am I doing something wrong here or is this just not supported?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '12, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '12, 08:12</strong> </span></p>
</div>
</div>
<div id="comments-container-15101" class="comments-container">
&#10;</div>
<div id="comment-tools-15101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15101-form-container" class="comment-form-container">
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

<span id="15102"></span>

<div id="answer-container-15102" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15102-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, it is simply a bug. I have introduced an acceleration for that kind of queries a few days ago, and apparently haven't tested it enough. I'll check what is going wrong and then tell details.</p>
<p>As a temporary workaround, you can use a regular expression for one of the two conditions:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way[highway][name~%27.%27]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p><em>Update</em>: I just have realized that this only affects the rambler instance. Thus,</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];way[highway][name]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p>works fine. The rambler instance runs the pre-acceleration version, and thus this might be a good occasion to update the rambler instance as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '12, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '12, 08:23</strong> </span></p>
</div>
</div>
<div id="comments-container-15102" class="comments-container">
<span id="15103"></span>
<div id="comment-15103" class="comment">
<div id="post-15103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah I see, thanks for the quick answer :).</p>
</div>
<div id="comment-15103-info" class="comment-info">
<span class="comment-age">(15 Aug '12, 08:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15108"></span>
<div id="comment-15108" class="comment">
<div id="post-15108-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok, everything should be fine now. The workaround is no longer necessary.</p>
</div>
<div id="comment-15108-info" class="comment-info">
<span class="comment-age">(15 Aug '12, 11:42)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="15110"></span>
<div id="comment-15110" class="comment">
<div id="post-15110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again!</p>
</div>
<div id="comment-15110-info" class="comment-info">
<span class="comment-age">(15 Aug '12, 11:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15102-form-container" class="comment-form-container">
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

