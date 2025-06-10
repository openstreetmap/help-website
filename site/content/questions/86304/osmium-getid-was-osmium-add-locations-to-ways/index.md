+++
type = "question"
title = "osmium getid (was osmium add-locations-to-ways)"
description = '''Hello everyone, I have a list of ways and I&#x27;d like to get the whole objects (ways with their nodes and coordinates). This operation, if I&#x27;m not wrong, should be done with osmium add-locations-to-ways I can&#x27;t figure out the right syntax, while I expect to have a list of ways (or an xml file), an extr...'''
date = "2022-12-05T13:46:00Z"
lastmod = "2022-12-05T21:10:00Z"
weight = 86304
keywords = [ "osmium" ]
aliases = [ "/questions/86304" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osmium getid (was osmium add-locations-to-ways)](/questions/86304/osmium-getid-was-osmium-add-locations-to-ways)

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
<span id="post-86304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, I have a list of ways and I'd like to get the whole objects (ways with their nodes and coordinates). This operation, if I'm not wrong, should be done with osmium add-locations-to-ways</p>
<p>I can't figure out the right syntax, while I expect to have a list of ways (or an xml file), an extract containing all the geometries needed (e.g. a whole country), and an output file.</p>
<p>In the manual <a href="https://docs.osmcode.org/osmium/latest/osmium-add-locations-to-ways.html">https://docs.osmcode.org/osmium/latest/osmium-add-locations-to-ways.html</a> there are two examples, but I'm a bit confused as just two (instead of 3) file OSM are used.</p>
<p>Thank you, Alessandro</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '22, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/878b7d711565f0d417d0f269adfc2233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ale_Zena_IT&#39;s gravatar image" />
<p><span>Ale_Zena_IT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ale_Zena_IT has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '22, 21:13</strong> </span></p>
</div>
</div>
<div id="comments-container-86304" class="comments-container">
&#10;</div>
<div id="comment-tools-86304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86304-form-container" class="comment-form-container">
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

<span id="86305"></span>

<div id="answer-container-86305" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you might be after the "osmium getid" command where, from a full OSM data file, you can extract a list of ways which are given by their IDs, and if desired you can extract the required nodes too. -- The add-locations-to-ways thing only means that the node coordinates will be folded into the way object, but still the node information needed for this must be present in the same input file as the ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '22, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86305" class="comments-container">
&#10;</div>
<div id="comment-tools-86305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86305-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86309"></span>

<div id="answer-container-86309" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86309-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello Frederik, thanks so much for your kind and prompt reply.</p>
<p>Yes, I've run the osmium getid command, but reading the command name add-locations-to-ways I shifted my focus on the latter command.</p>
<p>Reading again the osmium getid help, I realized I missed the recursive -r option.</p>
<p>So, running the command "osmium getid -r -f xml somalia-latest.osm.pbf w128441129 -o way-with-nodes.osm" I've got back the full way with its nodes.</p>
<p>Thank you, Alessandro</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '22, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/878b7d711565f0d417d0f269adfc2233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ale_Zena_IT&#39;s gravatar image" />
<p><span>Ale_Zena_IT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ale_Zena_IT has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '22, 21:10</strong> </span></p>
</div>
</div>
<div id="comments-container-86309" class="comments-container">
&#10;</div>
<div id="comment-tools-86309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86309-form-container" class="comment-form-container">
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

