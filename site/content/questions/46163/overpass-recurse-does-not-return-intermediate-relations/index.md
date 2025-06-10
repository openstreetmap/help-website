+++
type = "question"
title = "Overpass: recurse does not return intermediate relations?"
description = '''I want to use overpass to get all relations in a specific relation. I know there will be at least three levels: relation A holds relation B which holds relation C. But when I use the relation recurse in overpass twice, I do not get relation B, I only get the relations that do not hold any relations ...'''
date = "2015-10-28T10:12:00Z"
lastmod = "2015-10-28T14:47:00Z"
weight = 46163
keywords = [ "overpass", "recurse", "relations" ]
aliases = [ "/questions/46163" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: recurse does not return intermediate relations?](/questions/46163/overpass-recurse-does-not-return-intermediate-relations)

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
<span id="post-46163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use overpass to get all relations in a specific relation. I know there will be at least three levels: relation A holds relation B which holds relation C. But when I use the relation recurse in overpass twice, I do not get relation B, I only get the relations that do not hold any relations in them.<br />
My query is:</p>
<pre><code>relation
  [&quot;name&quot;=&quot;Twente&quot;]
  [&quot;network&quot;=&quot;public_transport&quot;];
rel(r);
rel(r);
out;</code></pre>
<p>Without recurse, the relation that gets returned is 360309. With one recurse I get all the relations in it, e.g. 5617486 which is a relation that holds two relations. With two recurses, I get the relations that are held by 5617486, but I do not get 5617486 anymore.<br />
Is there a way to get also relation 5617486 (and similar "intermediate" relations)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-recurse" rel="tag" title="see questions tagged &#39;recurse&#39;">recurse</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '15, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/e03d7686c5a52656c9bc7b559467bfb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maarten%20Deen&#39;s gravatar image" />
<p><span>Maarten Deen</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maarten Deen has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-46163" class="comments-container">
&#10;</div>
<div id="comment-tools-46163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46163-form-container" class="comment-form-container">
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

<span id="46180"></span>

<div id="answer-container-46180" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46180-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Maarten Deen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>out;</code> will only return the current inputset, in this case the result of the last <code>rel(r);</code>. If you want the result of both <code>rel(r);</code> you need to put both statements inside a <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union">union block</a>:</p>
<pre><code>relation
  [&quot;name&quot;=&quot;Twente&quot;]
  [&quot;network&quot;=&quot;public_transport&quot;];
( rel(r); rel(r); );
out;</code></pre>
<p>Maybe you should also take a look at <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_relations_.28.3E.3E.29">recurse down relations</a> (or for short: <code>&gt;&gt;;</code> ). This avoids manual resolution of nested relations, like you did in your example. Please refer to the wiki for details.</p>
<p>Another option would the <a href="https://github.com/mmd-osm/Overpass-API/wiki/Overpass-API-test754#new-statement-complete"><code>complete</code> statement</a>, which is <strong>currently only available on the test instance</strong>: it can be leveraged to automatically resolve the nested relation only (ignoring and ways/nodes contained in the relation). Here's a link to the preview version: <a href="http://overpass-turbo.eu/s/cmw">http://overpass-turbo.eu/s/cmw</a> (returns 102 relations, which are only visible in overpass turbo's data tab).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '15, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '15, 18:17</strong> </span></p>
</div>
</div>
<div id="comments-container-46180" class="comments-container">
&#10;</div>
<div id="comment-tools-46180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46180-form-container" class="comment-form-container">
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

