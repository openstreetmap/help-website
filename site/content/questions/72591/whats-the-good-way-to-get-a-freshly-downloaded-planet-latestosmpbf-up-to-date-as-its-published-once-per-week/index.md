+++
type = "question"
title = "What&#x27;s the good way to get a freshly downloaded planet-latest.osm.pbf up to date as it&#x27;s published once per week ?"
description = '''EDIT: see next question please (reformulated as I did not have answers to the first one) Hi, I don&#x27;t really understand what Osmosis &#x27;maxInterval&#x27; configuration option does when using osmosis --read-replication-interval workingDirectory=. --simplify-change --write-xml-change changes.osc.gz. My unders...'''
date = "2020-01-21T10:45:00Z"
lastmod = "2020-03-05T04:57:00Z"
weight = 72591
keywords = [ "planet", "replication", ".osc", "changes", "osmosis" ]
aliases = [ "/questions/72591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What's the good way to get a freshly downloaded planet-latest.osm.pbf up to date as it's published once per week ?](/questions/72591/whats-the-good-way-to-get-a-freshly-downloaded-planet-latestosmpbf-up-to-date-as-its-published-once-per-week)

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
<span id="post-72591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72591-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>EDIT: see next question please (reformulated as I did not have answers to the first one)</p>
<p>Hi,</p>
<p>I don't really understand what Osmosis 'maxInterval' configuration option does when using <code>osmosis --read-replication-interval workingDirectory=. --simplify-change --write-xml-change changes.osc.gz</code>.</p>
<p>My understanding is: it helps to merge multiple <code>.osc.gz</code> files available at the replication tree <code>baseUrl</code> to a merged <code>changes.osc.gz</code> file.</p>
<p>For instance, if Osmosis configuration options are set to</p>
<ul>
<li><code>maxInterval=345600</code> which corresponds to 1 week in seconds</li>
<li><code>baseUrl=</code><a href="https://planet.osm.org/replication/day/"><code>https://planet.osm.org/replication/day/</code></a></li>
</ul>
<p>the behaviour will be: Osmosis get all available <code>xxx.osc.gz</code> daily changes at <a href="https://planet.osm.org/replication/day/">/replication/day/</a> for which the corresponding <code>xxx.state.txt</code> file</p>
<ul>
<li>indicates a <code>sequenceNumber</code> higher than the <code>sequenceNumber</code> of <code>$osmosis_workind_dir_state.txt</code></li>
<li>indicates a <code>timestamp</code> higher than the <code>'timestamp_1'</code> of <code>$osmosis_workind_dir_state.txt</code> and lower than <code>'timestamp_1' + 345600</code></li>
</ul>
<p>and then produce a <code>changes.osc.gz</code> file merging all these changes which are "simplified" (result file contains "a maximum of one change per entity"). With these settings, the limit is 7 <code>.osc.gz</code> daily changes for each Osmosis run.</p>
<p>Is it correct ?</p>
<p>Hope it is clear, thanks in advance.</p>
<p>Augustin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '20, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '20, 18:38</strong> </span></p>
</div>
</div>
<div id="comments-container-72591" class="comments-container">
<span id="73380"></span>
<div id="comment-73380" class="comment">
<div id="post-73380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Augustin - did you end up solving this? I'm trying to do much the same thing and struggling to get changes downloaded. Be interested in your solution</p>
<p>Cheers</p>
</div>
<div id="comment-73380-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 04:57)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
</div>
<div id="comment-tools-72591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72591-form-container" class="comment-form-container">
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

<span id="72692"></span>

<div id="answer-container-72692" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72692-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Just to pull up the question .. does anybody has an idea if last statement is correct ?</p>
<p>My main goal is to apply in one shot all the diffs available to planet-osm-latest.osm.pbf (because it's published only once per week) to get the freshest data as possible, regardless the day of the week I download it.</p>
<p>My solution for now is:</p>
<ol>
<li>get the latest available planet-latest.osm.pbf and /replication/day/state.txt file at <a href="https://planet.osm.org/">https://planet.osm.org/</a></li>
<li>get the corresponding replication number X</li>
<li>download all the Y.osc.gz available where X - 7 &lt; Y &lt;= X</li>
<li>use osmium merge-changes to merge all Y.osc.gz files to a merge.osc.gz</li>
<li>use osmium apply-changes to apply merge.osc.gz to the latest available <code>planet-latest.osm.pbf</code></li>
</ol>
<p>but I guess I could use <code>osmosis --read-replication-interval workingDirectory=. --simplify-change --write-xml-change merge.osc.gz</code> to avoid steps 1 to 4 by getting in one shot desired <code>merge.osc.gz</code>.</p>
<p>I tried last settings (<code>maxInterval=345600</code> - one week in seconds - with the Planet OSM daily replication tree) but I got errors like "Pipeline entities are not sorted", like here</p>
<ul>
<li><a href="/questions/47785/osmosis-issue-pipeline-entities-are-not-sorted">Osmosis issue : Pipeline entities are not sorted</a></li>
<li><a href="/questions/12469/osmosis-merge-issue-pipeline-entities-are-not-sorted-or-contain-multiple-versions">Osmosis - merge issue (Pipeline entities are not sorted or contain multiple versions)</a></li>
</ul>
<p>Hope you can help :) thanks,</p>
<p>Augustin</p>
<p>PS: I will retitle the question to make it more clear</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '20, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '20, 18:40</strong> </span></p>
</div>
</div>
<div id="comments-container-72692" class="comments-container">
&#10;</div>
<div id="comment-tools-72692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72692-form-container" class="comment-form-container">
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

