+++
type = "question"
title = "Duplicate Features retrieved with Overpass QL"
description = '''I&#x27; running the following query [out:json][timeout:25]; ( nwr(poly:&quot;52.450426 13.286183 52.458324 13.286183 52.458324 13.299744 52.450426 13.299744 52.450426 13.286183&quot;); ); out body; &amp;gt;; out skel qt;  and I just found that some features (only one example handy right now) are retrieved twice possib...'''
date = "2021-02-01T12:20:00Z"
lastmod = "2022-01-09T00:34:00Z"
weight = 78620
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/78620" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Duplicate Features retrieved with Overpass QL](/questions/78620/duplicate-features-retrieved-with-overpass-ql)

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
<span id="post-78620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78620-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I' running the following query</p>
<pre><code>[out:json][timeout:25];
(
nwr(poly:&quot;52.450426 13.286183 52.458324 13.286183 52.458324 13.299744 52.450426 13.299744 52.450426 13.286183&quot;);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>and I just found that some features (only one example handy right now) are retrieved twice possibly even more.</p>
<p>The example in question:</p>
<p>{'type': 'way', 'id': 48590101, 'nodes': [2850024375, 3828309463, 3975571367, 3975571366, 5217921963, 3975568951, 617181077, 617181080, 2850024367, 3975568954, 3975571362, 2850024371, 3828309460, 2850024372, 3975571372, 2850024375], 'tags': {'area': 'yes', 'bench': 'yes', 'bin': 'yes', 'covered': 'partial', 'description': 'U Dahlem Dorf U3 Bahnsteig', 'layer': '-1', 'level': '-1', 'name': 'U Dahlem-Dorf', 'public_transport': 'platform', 'railway': 'platform', 'subway': 'yes', 'wheelchair': 'yes'}} {'type': 'way', 'id': 48590101, 'nodes': [2850024375, 3828309463, 3975571367, 3975571366, 5217921963, 3975568951, 617181077, 617181080, 2850024367, 3975568954, 3975571362, 2850024371, 3828309460, 2850024372, 3975571372, 2850024375]}</p>
<p>Even more curious that it is once retrieved with all tags and once without its tags. Anyone stumbled accross this before? Is my query maybe malformed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '21, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2c6db7781faaff0197abc51610071c4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thagor&#39;s gravatar image" />
<p><span>Thagor</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thagor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '21, 12:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span></p>
</div>
</div>
<div id="comments-container-78620" class="comments-container">
<span id="83012"></span>
<div id="comment-83012" class="comment">
<div id="post-83012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am seeing something similar: My query searches for primary, secondary, and tertiary roads within a bounding box.</p>
<p><code>data=[out:json];( node["highway"="primary"]${bBox}; way["highway"="primary"]${bBox}; relation["highway"="primary"]${bBox}; node["highway"="secondary"]${bBox}; way["highway"="secondary"]${bBox}; relation["highway"="secondary"]${bBox}; node["highway"="tertiary"]${bBox}; way["highway"="tertiary"]${bBox}; relation["highway"="tertiary"]${bBox}; );out body;&gt;;out skel qt;)</code></p>
<p>Though this has returned good data elsewhere, I am finding that when the bounding box is in Portugal (of all places), I am also getting multiple way records (for example) with the same id, but one record does not have <code>tags</code></p>
</div>
<div id="comment-83012-info" class="comment-info">
<span class="comment-age">(09 Jan '22, 00:34)</span> <span class="comment-user userinfo">nickiemoto</span>
</div>
</div>
</div>
<div id="comment-tools-78620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78620-form-container" class="comment-form-container">
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

<span id="78621"></span>

<div id="answer-container-78621" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78621-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thagor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't investigated closely, but I expect the <code>nwr</code> statement is picking up the relations that <a href="https://www.openstreetmap.org/way/48590101">https://www.openstreetmap.org/way/48590101</a> is part of, along with the way. So <code>out body;</code> prints the way as part of the set returned by <code>nwr</code> and then <code>out skel qt;</code> prints the way as part of the set returned by recursing down from the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '21, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78621" class="comments-container">
<span id="78625"></span>
<div id="comment-78625" class="comment">
<div id="post-78625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that might be it I was under the impression that if a feature is part of <code>out body;</code> it would be omitted in <code>skel qt;</code>. Thanks.</p>
</div>
<div id="comment-78625-info" class="comment-info">
<span class="comment-age">(01 Feb '21, 14:06)</span> <span class="comment-user userinfo">Thagor</span>
</div>
</div>
</div>
<div id="comment-tools-78621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78621-form-container" class="comment-form-container">
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

