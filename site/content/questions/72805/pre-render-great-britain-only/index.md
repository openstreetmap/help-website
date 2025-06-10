+++
type = "question"
title = "Pre-Render Great Britain Only"
description = '''Hi :)  My server has been pre-rendering tiles for awhile now. When i setup my server i only downloaded the Great Britain Map since this is all that is required. I started the pre-rendering process via the following command  &quot;render_list -m default -a -z 0 -Z 15 --num-threads=12&quot; After some research ...'''
date = "2020-02-01T10:56:00Z"
lastmod = "2020-02-02T03:12:00Z"
weight = 72805
keywords = [ "rendering" ]
aliases = [ "/questions/72805" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Pre-Render Great Britain Only](/questions/72805/pre-render-great-britain-only)

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
<span id="post-72805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72805-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi :)</p>
<p>My server has been pre-rendering tiles for awhile now.</p>
<p>When i setup my server i only downloaded the Great Britain Map since this is all that is required.</p>
<p>I started the pre-rendering process via the following command</p>
<p>"render_list -m default -a -z 0 -Z 15 --num-threads=12"</p>
<p>After some research i believe this is not ideal, so my question is how would i pre-render the whole of Great Britain to a zoom level of 18?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '20, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/82b0a7779df35ca1a1d406f82ce98249?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CableGuy5555&#39;s gravatar image" />
<p><span>CableGuy5555</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CableGuy5555 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72805" class="comments-container">
&#10;</div>
<div id="comment-tools-72805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72805-form-container" class="comment-form-container">
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

<span id="72807"></span>

<div id="answer-container-72807" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CableGuy5555 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I use <a href="https://github.com/alx77/render_list_geo.pl">render_list_geo.pl</a>. For zoom 1-12, the actual script that I run from cron is:</p>
<pre><code>PATH=/home/renderaccount/bin:/home/renderaccount/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
/home/renderaccount/src/render_list_geo.pl/render_list_geo.pl -n 1 -z 1 -Z 12 -x -9.5 -X 2.72 -y 49.39 -Y 61.26 -m ajt</code></pre>
<p>If you want to pre-render everything once you'd probably want more threads, and you will want to keep an eye on memory usage, as there have been reports of this sort of "pre-render everything" approach having problems with that. Rendering everything to Z18 will get you a <em>lot</em> of tiles - if you want that amount of data offline (or able to be statically served) I might be tempted to look at another option for serving data, depending on what your goal is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '20, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '20, 11:22</strong> </span></p>
</div>
</div>
<div id="comments-container-72807" class="comments-container">
<span id="72813"></span>
<div id="comment-72813" class="comment">
<div id="post-72813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this :)</p>
</div>
<div id="comment-72813-info" class="comment-info">
<span class="comment-age">(02 Feb '20, 03:12)</span> <span class="comment-user userinfo">CableGuy5555</span>
</div>
</div>
</div>
<div id="comment-tools-72807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72807-form-container" class="comment-form-container">
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

