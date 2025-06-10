+++
type = "question"
title = "Converting a changeset file to csv"
description = '''Hello,  I&#x27;m trying to use osmconvert to get a csv file from the changesets-latest.osm dump. I did the following: osmconvert changesets-latest.osm --csv=&quot;@id @created_at @numchange_changes @closed_at @min_lat @min_lon @max_lat @max_lon @user @uid&quot; --csv-headline -o=changesets.csv  But this gave me no...'''
date = "2013-12-13T15:53:00Z"
lastmod = "2014-05-26T21:50:00Z"
weight = 29036
keywords = [ "osmconvert" ]
aliases = [ "/questions/29036" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Converting a changeset file to csv](/questions/29036/converting-a-changeset-file-to-csv)

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
<span id="post-29036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29036-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to use osmconvert to get a csv file from the changesets-latest.osm dump. I did the following:</p>
<pre><code>osmconvert changesets-latest.osm --csv=&quot;@id @created_at @numchange_changes @closed_at @min_lat @min_lon @max_lat @max_lon @user @uid&quot; --csv-headline -o=changesets.csv</code></pre>
<p>But this gave me nothing -- i just got an empty csv file. I dont think osmosis can be used to generate CSV files either. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '13, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/47aed415daf0dfc05391f0791fd0a504?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="figuringout&#39;s gravatar image" />
<p><span>figuringout</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="figuringout has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29036" class="comments-container">
&#10;</div>
<div id="comment-tools-29036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29036-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="29076"></span>

<div id="answer-container-29076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29076-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmconvert can only convert OSM files (which contain nodes, ways, relations) - not changeset files (which only contain meta data about who edited where when, but not real geodata).</p>
<p>If you need a CSV file with geodata, don't use changesets-latest, use the planet file or an exctract of that. If you need a CSV file with the metadata from changesets-latest, it looks like you'll have to write a few lines in a scripting language of your choice. Or XSLT, even.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '13, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29076" class="comments-container">
&#10;</div>
<div id="comment-tools-29076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29076-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33497"></span>

<div id="answer-container-33497" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33497-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wrote a script, in case it helps someone: <a href="https://github.com/dalek2point3/jmpscripts/blob/master/python/parsechange.py">https://github.com/dalek2point3/jmpscripts/blob/master/python/parsechange.py</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/47aed415daf0dfc05391f0791fd0a504?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="figuringout&#39;s gravatar image" />
<p><span>figuringout</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="figuringout has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33497" class="comments-container">
&#10;</div>
<div id="comment-tools-33497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33497-form-container" class="comment-form-container">
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

