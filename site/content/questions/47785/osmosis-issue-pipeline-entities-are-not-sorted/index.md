+++
type = "question"
title = "Osmosis issue : Pipeline entities are not sorted"
description = '''Hi all I&#x27;m using the following cli to create a diff file with osmosis : osmosis --rri workingDirectory=$dir --simc --wxc $diff_file It works globally fine, but sometimes failed with the following error message :  SEVERE: Thread for task 1-rri failed org.openstreetmap.osmosis.core.OsmosisRuntimeExcep...'''
date = "2016-02-01T10:43:00Z"
lastmod = "2016-11-28T10:58:00Z"
weight = 47785
keywords = [ "diff", "osmosis" ]
aliases = [ "/questions/47785" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis issue : Pipeline entities are not sorted](/questions/47785/osmosis-issue-pipeline-entities-are-not-sorted)

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
<span id="post-47785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47785-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I'm using the following cli to create a diff file with osmosis :</p>
<p>osmosis --rri workingDirectory=$dir --simc --wxc $diff_file</p>
<p>It works globally fine, but sometimes failed with the following error message : SEVERE: Thread for task 1-rri failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Pipeline entities are not sorted, previous entity type=Node, id=3976375557, version=1 current entity type=Node, id=3976375557, version=1.</p>
<p>In that case, removing --simc option seems to work fine and generate a correct osc file but it contains several changes for the same id (which is expected because of removing simplify-changes option !). I had a look at the generated file and it seems --simc option is failing when an id is created and deleted in the same osc file compilation (from 2016-01-28 to 2016-02-01 in my case) :</p>
<p>&lt;create&gt; ... &lt;node id="3976375557" version="1" timestamp="2016-01-29T17:16:56Z" uid="3577326" user="Alain 9-0" changeset="36883598" lat="47.5435886" lon="6.8328761"/&gt; &lt;/create&gt; &lt;delete&gt; &lt;node id="3976375557" version="1" timestamp="2016-01-31T05:04:40Z" uid="3577326" user="Alain 9-0" changeset="36883598" lat="47.5435886" lon="6.8328761"/&gt; &lt;/delete&gt;</p>
<p>Any idea on how to keep --simc option in any case ?</p>
<p>Thanks a lot for any help</p>
<h2 id="kind-regards">Kind regards,</h2>
<p>David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '16, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/878fd3d25e7dd8ba8c0fb59e7e450587?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmercier90&#39;s gravatar image" />
<p><span>dmercier90</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmercier90 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47785" class="comments-container">
<span id="47792"></span>
<div id="comment-47792" class="comment">
<div id="post-47792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used osmosis Version 0.40.1 and tried latest 0.44.1 with the same results.</p>
<p>Test files : <a href="http://download.geofabrik.de/europe/france/franche-comte-updates/000/001/052.osc.gz">http://download.geofabrik.de/europe/france/franche-comte-updates/000/001/052.osc.gz</a> to 054.osc.gz</p>
</div>
<div id="comment-47792-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 12:49)</span> <span class="comment-user userinfo">dmercier90</span>
</div>
</div>
<span id="47796"></span>
<div id="comment-47796" class="comment">
<div id="post-47796-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It seems I've found a piece of answer hier : <a href="http://gis.19327.n5.nabble.com/osmosis-dev-Error-on-a-node-modified-and-deleted-in-the-same-changeset-td5759351.html">http://gis.19327.n5.nabble.com/osmosis-dev-Error-on-a-node-modified-and-deleted-in-the-same-changeset-td5759351.html</a></p>
<p>"I'm currently using a workaround, which is to set maxInterval in configuration.txt to 0.5 day to make sure that osmosis is not trying to merge two diffs. Then I had to add a loop to run osmosis until there are no recent diffs."</p>
<p>Hope this should help someone who's facing the same issue when trying to merge several geofrabrik's file with osmosis</p>
</div>
<div id="comment-47796-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 13:19)</span> <span class="comment-user userinfo">dmercier90</span>
</div>
</div>
<span id="53145"></span>
<div id="comment-53145" class="comment">
<div id="post-53145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ran into the same problem (also with Geofabrik diffs). The "0.5 day" workaround (setting <code>maxInterval</code> to <code>43200</code> in <code>configuration.txt</code>) works for me. Thanks for posting this!</p>
</div>
<div id="comment-53145-info" class="comment-info">
<span class="comment-age">(28 Nov '16, 10:58)</span> <span class="comment-user userinfo">inkatlas</span>
</div>
</div>
</div>
<div id="comment-tools-47785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47785-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

