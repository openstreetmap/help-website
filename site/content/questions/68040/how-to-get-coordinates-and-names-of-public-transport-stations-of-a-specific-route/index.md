+++
type = "question"
title = "How to get coordinates and names of public transport stations of a specific route?"
description = '''I am attempting to use the Overpass API to retrieve data about a public transport route: the list of bus stops, their names and coordinates (ideally, in CSV format). This query shows me all the stations in the selected area, which is not specific enough: [out:json][timeout:25]; // gather results (  ...'''
date = "2019-02-18T14:42:00Z"
lastmod = "2019-02-20T08:09:00Z"
weight = 68040
keywords = [ "overpass", "public-transport", "poi" ]
aliases = [ "/questions/68040" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get coordinates and names of public transport stations of a specific route?](/questions/68040/how-to-get-coordinates-and-names-of-public-transport-stations-of-a-specific-route)

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
<span id="post-68040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68040-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am attempting to use the Overpass API to retrieve data about a public transport route: the list of bus stops, their names and coordinates (ideally, in CSV format).</p>
<p>This query shows me all the stations in the selected area, which is not specific enough:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “public_transport=stop_position”
  node[&quot;public_transport&quot;=&quot;stop_position&quot;]({{bbox}});
  way[&quot;public_transport&quot;=&quot;stop_position&quot;]({{bbox}});
  relation[&quot;public_transport&quot;=&quot;stop_position&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
<p>I know that the relation I need is 8649765, so ideally I would just run a query that says <em>show me all nodes that match "public_transport"="stop_position" and for which the relation is 8649765</em>. However, I did not find any examples that explicitly provide a relation ID.</p>
<p>The reason I think this approach is necessary is because the route in question covers several cities, so I want the query not to be tied to the location, but to the... well... relation.</p>
<p>How can this be accomplished?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '19, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f670011755afca7029c6be1f9abe2c98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralien&#39;s gravatar image" />
<p><span>ralien</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralien has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68040" class="comments-container">
&#10;</div>
<div id="comment-tools-68040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68040-form-container" class="comment-form-container">
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

<span id="68045"></span>

<div id="answer-container-68045" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68045-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>relation (8649765);
&gt;&gt;;
node._ [public_transport=stop_position];
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '19, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
</div>
<div id="comments-container-68045" class="comments-container">
<span id="68051"></span>
<div id="comment-68051" class="comment">
<div id="post-68051-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, this works, though I had to replace <code>stop_position</code> with <code>platform</code> to get the names of the stations too.</p>
</div>
<div id="comment-68051-info" class="comment-info">
<span class="comment-age">(19 Feb '19, 12:44)</span> <span class="comment-user userinfo">ralien</span>
</div>
</div>
<span id="68062"></span>
<div id="comment-68062" class="comment">
<div id="post-68062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad it pointed in right direction. I will modify to put out a CSV</p>
</div>
<div id="comment-68062-info" class="comment-info">
<span class="comment-age">(20 Feb '19, 08:09)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
</div>
<div id="comment-tools-68045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68045-form-container" class="comment-form-container">
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

