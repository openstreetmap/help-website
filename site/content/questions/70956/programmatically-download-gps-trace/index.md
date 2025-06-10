+++
type = "question"
title = "programmatically download gps trace"
description = '''No luck with help.openstreetmap.org, so I am asking what is probably a very elementary question. How can I download programmatically a GPS trace file which is available at  https://www.openstreetmap.org/trace/traceidnumber/data i.e. how can I do this with a script? I presume the answer is somewhere ...'''
date = "2019-09-29T16:44:00Z"
lastmod = "2019-09-29T17:16:00Z"
weight = 70956
keywords = [ "download", "api", "traces", "gps" ]
aliases = [ "/questions/70956" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [programmatically download gps trace](/questions/70956/programmatically-download-gps-trace)

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
<span id="post-70956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>No luck with <code>help.openstreetmap.org</code>, so I am asking what is probably a very elementary question.</p>
<p>How can I download programmatically a GPS trace file which is available at</p>
<p><a href="https://www.openstreetmap.org/trace/traceidnumber/data"><code>https://www.openstreetmap.org/trace/traceidnumber/data</code></a></p>
<p>i.e. how can I do this with a script?</p>
<p>I presume the answer is somewhere in the <a href="https://wiki.openstreetmap.org/wiki/API">API wiki documentation</a> , but it's outside of my zone of familiarity (e.g. <code>python</code> or <code>bash</code>).</p>
<p><strong>Note:</strong> I don't want to download bulk data, I simply want to be able to automate the download of, say, a dozen GPS trace files.</p>
<hr />
<p><strong>Edit:</strong> The reason of my failure was that I had made a mistake in constructing the URL...</p>
<p>For the record, the following python code snippet works just fine:<br />
<code>import requests from pathlib import Path url = "https://www.openstreetmap.org/trace/3116621/data" path = Path.home()/'datasets' r = requests.get(url) with path.open('wb') as f: f.write(r.content)</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '19, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/7645c70e5a141f9b512f7dac0b37fe60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Antoine%20C&#39;s gravatar image" />
<p><span>Antoine C</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Antoine C has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '19, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-70956" class="comments-container">
&#10;</div>
<div id="comment-tools-70956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70956-form-container" class="comment-form-container">
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

<span id="70958"></span>

<div id="answer-container-70958" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70958-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The top public trace at the moment just happens to be <a href="https://www.openstreetmap.org/user/dimitryos/traces/3116621">this one</a>. On that page is a download link, which is <a href="https://www.openstreetmap.org/trace/3116621/data">https://www.openstreetmap.org/trace/3116621/data</a>. If you get that (via e.g. "wget" or within your programming language of choice) I'd expect that you'll get that trace. I've just done this:</p>
<pre><code>wget https://www.openstreetmap.org/trace/3116621/data</code></pre>
<p>and what I get looks like a GPX file to me. You could do that as part of a script. Does this answer the question, or do you need to know how to find out the trace ID, or something else?</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '19, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-70958" class="comments-container">
<span id="70960"></span>
<div id="comment-70960" class="comment">
<div id="post-70960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that answers my question!</p>
<p>I was not able to do this in <code>python</code> using its <code>requests</code> package - don't know why. (It downloads an html file which somewhere says "File not found".)</p>
<p>To answer your question, I am fine finding trace id (in python using an html parser).</p>
</div>
<div id="comment-70960-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 17:16)</span> <span class="comment-user userinfo">Antoine C</span>
</div>
</div>
</div>
<div id="comment-tools-70958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70958-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

