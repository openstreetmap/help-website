+++
type = "question"
title = "My query to retrieve nodes and ways is not returning all the nodes..."
description = '''I am using this query :  &quot;GET /cgi/interpreter?data=[out:json]; (node(20.25527,85.8244,20.26632,85.83685);way(20.25527,85.8244,20.26632,85.83685);node(w)-&amp;gt;.x;);out; HTTP/1.1&#92;r&#92;n&quot;  And for example there is this way : {  &quot;type&quot;: &quot;way&quot;,  &quot;id&quot;: 26764919,  &quot;nodes&quot;: [  293465191,  293465090,  293465086...'''
date = "2013-01-29T13:34:00Z"
lastmod = "2013-01-30T06:36:00Z"
weight = 19419
keywords = [ "openstreetmap", "overpass", "newbie", "rendering", "query" ]
aliases = [ "/questions/19419" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [My query to retrieve nodes and ways is not returning all the nodes...](/questions/19419/my-query-to-retrieve-nodes-and-ways-is-not-returning-all-the-nodes)

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
<span id="post-19419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using this query :</p>
<pre><code>&quot;GET /cgi/interpreter?data=[out:json];   (node(20.25527,85.8244,20.26632,85.83685);way(20.25527,85.8244,20.26632,85.83685);node(w)-&gt;.x;);out; HTTP/1.1\r\n&quot;</code></pre>
<p>And for example there is this way :</p>
<pre><code>{
  &quot;type&quot;: &quot;way&quot;,
  &quot;id&quot;: 26764919,
  &quot;nodes&quot;: [
    293465191,
    293465090,
    293465086,
    293465082,
    293465081
  ],
  &quot;tags&quot;: {
    &quot;highway&quot;: &quot;secondary&quot;
  }</code></pre>
<p>In the nodes returned by query some nodes in above list eg, 293465086 is missing. So I am unable to completely render the way. Am I using the correct query ? If not what query should I use to render all ways in my bounding box ? Is the above query not returning the nodes out of the bounding box ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '13, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/bd411afe7563961a31610b5f4d40dfd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anubha&#39;s gravatar image" />
<p><span>Anubha</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anubha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '13, 13:35</strong> </span></p>
</div>
</div>
<div id="comments-container-19419" class="comments-container">
&#10;</div>
<div id="comment-tools-19419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19419-form-container" class="comment-form-container">
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

<span id="19422"></span>

<div id="answer-container-19422" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19422-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anubha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you execute your query <a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout:json%5D;(node(20.25527,85.8244,20.26632,85.83685);way(20.25527,85.8244,20.26632,85.83685);node(w)-%3E.x;);out;">here</a>? Please re-run the query. I get node 293465086 in the results as well as 33 member nodes for way 26764919, so I cannot yet reproduce the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '13, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-19422" class="comments-container">
<span id="19423"></span>
<div id="comment-19423" class="comment">
<div id="post-19423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well, thanks so much, the nodes are really all present, so I debugged my code and found out why the nodes were not found. after executing the query, I saved the results in a text file. In that text file, some nodes were not in proper format, eg. { "type": "node", "id": 293454101 1000 / <em>this 1000 value is extra</em> / , "lat": 20.2622200, "lon": 85.8301700 }, and so my program could not parse due to this 1000, this 1000 was inserted unwanted in other places too. my line to write to file fprintf(fp,"%s",&amp;buf[0]); why could this be happening ?</p>
</div>
<div id="comment-19423-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 05:27)</span> <span class="comment-user userinfo">Anubha</span>
</div>
</div>
<span id="19425"></span>
<div id="comment-19425" class="comment">
<div id="post-19425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>to state the above problem more clearly than in a comment I asked the following question :</p>
<p><a href="https://help.openstreetmap.org/questions/19424/this-program-to-retrieve-the-nodes-and-ways-returns-some-extra-garbage-values">https://help.openstreetmap.org/questions/19424/this-program-to-retrieve-the-nodes-and-ways-returns-some-extra-garbage-values</a></p>
</div>
<div id="comment-19425-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 06:36)</span> <span class="comment-user userinfo">Anubha</span>
</div>
</div>
</div>
<div id="comment-tools-19422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19422-form-container" class="comment-form-container">
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

