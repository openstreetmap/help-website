+++
type = "question"
title = "Find and get boundary for admin_level=4 territory"
description = '''Hi. Have some questions:  Can i get list of admin_level=4 territories? How to get selected territory boundary via osm_id or something like that? '''
date = "2023-06-05T09:35:00Z"
lastmod = "2023-06-07T10:09:00Z"
weight = 87347
keywords = [ "osm_id" ]
aliases = [ "/questions/87347" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find and get boundary for admin_level=4 territory](/questions/87347/find-and-get-boundary-for-admin_level4-territory)

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
<span id="post-87347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. Have some questions:</p>
<ol>
<li>Can i get list of admin_level=4 territories?</li>
<li>How to get selected territory boundary via osm_id or something like that?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '23, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/4ae016c93e51f23bbc20947cdad7f9da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitry2023&#39;s gravatar image" />
<p><span>Dmitry2023</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitry2023 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jun '23, 11:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-87347" class="comments-container">
&#10;</div>
<div id="comment-tools-87347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87347-form-container" class="comment-form-container">
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

<span id="87356"></span>

<div id="answer-container-87356" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87356-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To reply to point 1:</p>
<p>If you want all of them you can use <a href="https://sophox.org">sophox</a> with the following query:</p>
<pre><code>SELECT ?bound ?name ?wikidata WHERE {
  ?bound osmt:admin_level &quot;4&quot; .
  ?bound osmt:type &quot;boundary&quot; .
  ?bound osmt:name ?name .
  ?bound osmt:wikidata ?wikidata
}</code></pre>
<p><a href="https://tinyurl.com/2plkwpd2">Try it</a></p>
<p>Or with <a href="https://overpass-turbo.eu/">overpass</a> if you want a bounding box selection with the query:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  relation[admin_level=4]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p><a href="https://overpass-turbo.eu/s/1vO5">Try it</a></p>
<p>With overpass you can download the result of the query in different formats using the button "Export" which maybe replies to point 2.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '23, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/124a49f5989a9d0969beefeb78c2bcc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ernsterwinwg&#39;s gravatar image" />
<p><span>ernsterwinwg</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ernsterwinwg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '23, 10:24</strong> </span></p>
</div>
</div>
<div id="comments-container-87356" class="comments-container">
&#10;</div>
<div id="comment-tools-87356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87356-form-container" class="comment-form-container">
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

