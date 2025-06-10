+++
type = "question"
title = "Overpasss-API request with Regex doesn&#x27;t match exactly"
description = '''Hi, I want to filter of recycling rontainers with recycling:*=* tags but no recycling_type=container. In the test region are two Containers which have all the tags so they both should not match the regex but one of them is in the result. Maybe I&#x27;m missing something obvios here but at the moment I ca...'''
date = "2016-03-24T14:34:00Z"
lastmod = "2016-03-24T17:45:00Z"
weight = 48820
keywords = [ "regex", "overpass", "negation" ]
aliases = [ "/questions/48820" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpasss-API request with Regex doesn't match exactly](/questions/48820/overpasss-api-request-with-regex-doesnt-match-exactly)

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
<span id="post-48820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48820-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to filter of recycling rontainers with <code>recycling:*=*</code> tags but no <code>recycling_type=container</code>. In the test region are two Containers which have all the tags so they both should not match the regex but one of them is in the result. Maybe I'm missing something obvios here but at the moment I cant figure out what it is.</p>
<pre><code>node(51.710002,10.520173,51.710210,10.520822)
  [~&quot;^recycling:.&quot;~&quot;.&quot;]
  [&quot;recycling_type&quot;!~&quot;container&quot;];
out body;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-negation" rel="tag" title="see questions tagged &#39;negation&#39;">negation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '16, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-48820" class="comments-container">
&#10;</div>
<div id="comment-tools-48820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48820-form-container" class="comment-form-container">
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

<span id="48824"></span>

<div id="answer-container-48824" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48824-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm pretty sure this is the same bug I reported here: <a href="https://github.com/drolbr/Overpass-API/issues/192">https://github.com/drolbr/Overpass-API/issues/192</a></p>
<p>The fix has only been committed 4 days ago, so it might take a bit of time until it is available on one of the public Overpass instances.</p>
<p>For the time being please use the difference block statement:</p>
<pre><code>(
  node(51.710002,10.520173,51.710210,10.520822)
       [~&quot;^recycling:.&quot;~&quot;.&quot;];
&#10;  -
&#10;  node(51.710002,10.520173,51.710210,10.520822)
  [&quot;recycling_type&quot;~&quot;container&quot;];
&#10;);
&#10;out body;</code></pre>
<p>Obligatory overpass turbo link: <a href="http://overpass-turbo.eu/s/fec">http://overpass-turbo.eu/s/fec</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '16, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '16, 17:41</strong> </span></p>
</div>
</div>
<div id="comments-container-48824" class="comments-container">
<span id="48826"></span>
<div id="comment-48826" class="comment">
<div id="post-48826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, thaks a lot. A bug is a relief. I had already begun to question my mind.</p>
</div>
<div id="comment-48826-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 17:45)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-48824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48824-form-container" class="comment-form-container">
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

