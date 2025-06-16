+++
type = "question"
title = "Overpass API, differentiating results from parallel requests"
description = '''Hi there,  Suppose I have a request to fetch all ways in a bounding box E.g. way(30.474290463301,-92.427999973297,30.493133455774,-92.403044700623); out;  and I need to make the same request in a different location:  way(30.48913956382,-92.41911649704,30.507979681231,-92.394161224365); out;  Right n...'''
date = "2017-10-01T00:43:00Z"
lastmod = "2017-10-02T01:42:00Z"
weight = 59902
keywords = [ "request", "overpass", "api", "osm", "parallel" ]
aliases = [ "/questions/59902" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API, differentiating results from parallel requests](/questions/59902/overpass-api-differentiating-results-from-parallel-requests)

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
<span id="post-59902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>Suppose I have a request to fetch all ways in a bounding box E.g.</p>
<pre><code>way(30.474290463301,-92.427999973297,30.493133455774,-92.403044700623);
out;</code></pre>
<p>and I need to make the same request in a different location:</p>
<pre><code>way(30.48913956382,-92.41911649704,30.507979681231,-92.394161224365);
out;</code></pre>
<p>Right now, I am querying in two separate requests as I need to know which elements belong to which request. What I want to do it to perform both queries in a single request (to avoid querying the server multiple times which is a bottleneck), but I need to know which found elements belong to which request.</p>
<p>For example: I want to call:</p>
<pre><code>//Request A
way(30.474290463301,-92.427999973297,30.493133455774,-92.403044700623);
out;
//Request B
way(30.48913956382,-92.41911649704,30.507979681231,-92.394161224365);
out;</code></pre>
<p>Which I want to produce the following result (note the "request" tag):</p>
<pre><code>{
  &quot;type&quot;: &quot;way&quot;,
  &quot;request&quot;: &quot;B&quot;,
  &quot;id&quot;: 12574244,
  &quot;nodes&quot;: [
    114699604,
    114699607,
&#10;  ],
  &quot;tags&quot;: {
    &quot;highway&quot;: &quot;residential&quot;,
    &quot;name&quot;: &quot;South Tanglewood Drive&quot;,
    &quot;tiger:cfcc&quot;: &quot;A41&quot;,
    &quot;tiger:county&quot;: &quot;Acadia, LA&quot;,
    &quot;tiger:name_base&quot;: &quot;Tanglewood&quot;,
    &quot;tiger:name_direction_prefix&quot;: &quot;S&quot;,
    &quot;tiger:name_type&quot;: &quot;Dr&quot;,
    &quot;tiger:reviewed&quot;: &quot;no&quot;,
    &quot;tiger:zip_left&quot;: &quot;70535&quot;,
    &quot;tiger:zip_right&quot;: &quot;70535&quot;
  }
},
{
  &quot;type&quot;: &quot;way&quot;,
  &quot;request&quot;: &quot;A&quot;,
  &quot;id&quot;: 12574385,
  &quot;nodes&quot;: [
    114700993,
    114700994,
    114700997,
    114700999
  ],
  &quot;tags&quot;: {
    &quot;highway&quot;: &quot;residential&quot;,
    &quot;name&quot;: &quot;James Place&quot;,
  }
}</code></pre>
<p>Is what I want to achieve possible? Or do I need to keep using separate requests.</p>
<p>Thanks a lot for the help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-parallel" rel="tag" title="see questions tagged &#39;parallel&#39;">parallel</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '17, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1382f87fca144452793d096a71d332da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister41&#39;s gravatar image" />
<p><span>gmeister41</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister41 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59902" class="comments-container">
&#10;</div>
<div id="comment-tools-59902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59902-form-container" class="comment-form-container">
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

<span id="59904"></span>

<div id="answer-container-59904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59904-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could inject a marker element:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_make_statement">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_make_statement</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '17, 04:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-59904" class="comments-container">
<span id="59912"></span>
<div id="comment-59912" class="comment">
<div id="post-59912-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect, this will do the job. Thanks!</p>
</div>
<div id="comment-59912-info" class="comment-info">
<span class="comment-age">(02 Oct '17, 01:42)</span> <span class="comment-user userinfo">gmeister41</span>
</div>
</div>
</div>
<div id="comment-tools-59904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59904-form-container" class="comment-form-container">
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

