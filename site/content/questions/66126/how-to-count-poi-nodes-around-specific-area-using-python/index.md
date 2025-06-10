+++
type = "question"
title = "How to count POI nodes around specific area using Python?"
description = '''Hi, OSM crew. I&#x27;m newbie here. I try to count each POI nodes around specific GPS coordinates. This is my code for loading node around specific lat and lon using Python overpass_url = &quot;http://overpass-api.de/api/interpreter&quot; overpass_query = &quot;&quot;&quot; [out:json][timeout:25]; ( node(around:60.0,13.74567157,...'''
date = "2018-10-02T11:41:00Z"
lastmod = "2018-10-02T21:25:00Z"
weight = 66126
keywords = [ "python", "tags", "coordinates", "poi" ]
aliases = [ "/questions/66126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to count POI nodes around specific area using Python?](/questions/66126/how-to-count-poi-nodes-around-specific-area-using-python)

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
<span id="post-66126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, OSM crew. I'm newbie here. I try to count each POI nodes around specific GPS coordinates. This is my code for loading node around specific lat and lon using Python</p>
<pre><code>overpass_url = &quot;http://overpass-api.de/api/interpreter&quot;
overpass_query = &quot;&quot;&quot;
[out:json][timeout:25];
(
node(around:60.0,13.74567157,100.53371655);
);
out body;
    &quot;&quot;&quot;
response = requests.get(overpass_url,
                        params={&#39;data&#39;: overpass_query})
data = response.json()</code></pre>
<p>From this code, I get every nodes around that specific area. But I have more than 50,000 place to find. I want to know how can I use some variables instead of typing every coordinates in my code.</p>
<p>Moreover, I just want to count every POI node separated by its amenity tag such as 'drinking_water' or 'cafe' but I can't find tag index in data</p>
<p>Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '18, 11:41</strong></p>
<img src="https://secure.gravatar.com/avatar/5a75b1bc58972998e43a4db3b795ec65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krawan&#39;s gravatar image" />
<p><span>Krawan</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krawan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66126" class="comments-container">
&#10;</div>
<div id="comment-tools-66126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66126-form-container" class="comment-form-container">
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

<span id="66136"></span>

<div id="answer-container-66136" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66136-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your current query is for <em>all</em> nodes, so most of them don't have tags. You probably want to restrict that a bit.</p>
<p>Something like this will only return nodes with an amenity tag or a tourism tag (they don't have to have both):</p>
<pre><code>(
node(around:60.0,13.74567157,100.53371655)[amenity];
node(around:60.0,13.74567157,100.53371655)[tourism];
);</code></pre>
<p>Generating the query is more a python question, there's lots of ways to do string substitution over there. In Python 3 I tend to use <a href="https://docs.python.org/3/library/string.html#formatexamples">format strings</a> anymore, so you could replace the coordinates in your query with some variables:</p>
<pre><code>...
node(around:60.0,{lat},{lon});
...</code></pre>
<p>Then you'd substitute in the values:</p>
<pre><code>filled_query=overpass_query.format(lat=&quot;13.74567157&quot;,lon=&quot;100.53371655&quot;)</code></pre>
<p>You might also consider using the <code>nwr</code> query operator (along with <code>out center;</code>) instead of <code>node</code> . Then your results will include POIs that are modeled as ways or relations instead of as nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '18, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-66136" class="comments-container">
&#10;</div>
<div id="comment-tools-66136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66136-form-container" class="comment-form-container">
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

