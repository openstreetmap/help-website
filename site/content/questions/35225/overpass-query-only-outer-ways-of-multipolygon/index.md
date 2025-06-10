+++
type = "question"
title = "Overpass: query only outer ways of multipolygon"
description = '''Hi,  I&#x27;m trying to find out how to get all outer ways of a set of multipolygon relationships. This is what my query looks like right now: http://www.overpass-api.de/api/interpreter?data=[out:json]; relation[&quot;type&quot;=&quot;multipolygon&quot;](52.51,13.36,52.52,13.39); way(r)[&quot;building&quot;]; out qt;  It selects all ...'''
date = "2014-07-26T20:38:00Z"
lastmod = "2014-07-26T22:00:00Z"
weight = 35225
keywords = [ "overpass", "multipolygon" ]
aliases = [ "/questions/35225" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: query only outer ways of multipolygon](/questions/35225/overpass-query-only-outer-ways-of-multipolygon)

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
<span id="post-35225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to find out how to get all outer ways of a set of multipolygon relationships.</p>
<p>This is what my query looks like right now:</p>
<pre><code>http://www.overpass-api.de/api/interpreter?data=[out:json];
relation[&quot;type&quot;=&quot;multipolygon&quot;](52.51,13.36,52.52,13.39);
way(r)[&quot;building&quot;];
out qt;</code></pre>
<p>It selects all building ways that are part of a multipolygon. How can I remove the ones the are set to <code>role: "outer"</code>?</p>
<p><strong>EDIT</strong></p>
<p>The last part should read: How can I remove the ones the are set to <code>role: "inner"</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '14, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/56864a5bd5dd6b551131ccaca1b1935b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burgerer&#39;s gravatar image" />
<p><span>burgerer</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burgerer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '14, 13:38</strong> </span></p>
</div>
</div>
<div id="comments-container-35225" class="comments-container">
&#10;</div>
<div id="comment-tools-35225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35225-form-container" class="comment-form-container">
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

<span id="35227"></span>

<div id="answer-container-35227" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35227-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="burgerer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is not entirely clear/ a bit of a contradiction. I guess what you're looking for is the first part of this answer. Just in case you want to remove some ways with a specific role from your result set, you can check out the second part of this answer.</p>
<p>In your question summary, you mentioned that only want to retrieve buildings with role outer:</p>
<pre><code>relation[&quot;type&quot;=&quot;multipolygon&quot;](52.51,13.36,52.52,13.39) -&gt; .relation;
way(r.relation:&quot;outer&quot;)[&quot;building&quot;]; 
out qt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/4lZ">Overpass Turbo link 1</a></p>
<p>Then you asked "How can I <strong>remove</strong> the ones the are set to role: "outer"?"</p>
<p>You can use the difference operator for this purpose:</p>
<pre><code>relation[&quot;type&quot;=&quot;multipolygon&quot;](52.51,13.36,52.52,13.39) -&gt; .relation;
( way(r.relation)[&quot;building&quot;]; -
  way(r.relation:&quot;outer&quot;); );
out qt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/4lX">Overpass Turbo link 2</a></p>
<p>BTW: Don't forget to also check out the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">documentation on the Wiki page</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '14, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '14, 22:17</strong> </span></p>
</div>
</div>
<div id="comments-container-35227" class="comments-container">
&#10;</div>
<div id="comment-tools-35227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35227-form-container" class="comment-form-container">
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

