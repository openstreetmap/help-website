+++
type = "question"
title = "Osmosis warning &quot;Data being output lacks metadata&quot;"
description = '''Osmosis is giving me this warning message &quot;WARNING: Attention: Data being output lacks metadata. Please use omitmetadata=true&quot;  I am using a --write-pbf output and I see I can specify &#x27;omitmetadata=true&#x27; to stop it outputting version number, timestamp, user name, and user id, but what is the cause o...'''
date = "2012-11-12T00:48:00Z"
lastmod = "2012-11-12T07:05:00Z"
weight = 17651
keywords = [ "osmosis" ]
aliases = [ "/questions/17651" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis warning "Data being output lacks metadata"](/questions/17651/osmosis-warning-data-being-output-lacks-metadata)

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
<span id="post-17651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17651-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Osmosis is giving me this warning message</p>
<pre><code>&quot;WARNING: Attention: Data being output lacks metadata. Please use omitmetadata=true&quot;</code></pre>
<p>I am using a <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--write-pbf_.28--wb.29">--write-pbf</a> output and I see I can specify 'omitmetadata=true' to stop it outputting version number, timestamp, user name, and user id, but what is the cause of this warning?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '12, 00:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-17651" class="comments-container">
&#10;</div>
<div id="comment-tools-17651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17651-form-container" class="comment-form-container">
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

<span id="17653"></span>

<div id="answer-container-17653" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Harry Wood has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The cause of this warning is that some of your <em>input</em> data lacks metadata, and therefore the output data does, too. A clearer, but rather long, warning message would probably be: "WARNING! Some of your input data lacks metadata but you haven't specified omitmetadata=true which means that I am creating output partly with and partly without metadata! If you specified omitmetadata=true then at least my output would be consistent in not having any metadata."</p>
<p>The reason that some of your input data lacks metadata is likely that you're using a planet file and there are still a couple objects in there that have last been edited by an anonymous user and therefore lack user information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '12, 07:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '12, 07:06</strong> </span></p>
</div>
</div>
<div id="comments-container-17653" class="comments-container">
&#10;</div>
<div id="comment-tools-17653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17653-form-container" class="comment-form-container">
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

