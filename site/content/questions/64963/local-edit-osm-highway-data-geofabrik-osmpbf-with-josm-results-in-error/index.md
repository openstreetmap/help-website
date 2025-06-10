+++
type = "question"
title = "Local edit OSM highway data (Geofabrik .osm.pbf) with JOSM results in error"
description = '''Heyo, Software of my company is using osm.pbf as input to a tool to calculate a network analysis. The goal is to calculate difference in accessibility if network nodes/edges are removed or added from the openstreetmap network. Therefore we want to be able to locally edit .osm files and export it bac...'''
date = "2018-07-27T11:49:00Z"
lastmod = "2018-07-30T09:45:00Z"
weight = 64963
keywords = [ "josm", "networkanalysis", "local", "highway", "gdpr" ]
aliases = [ "/questions/64963" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Local edit OSM highway data (Geofabrik .osm.pbf) with JOSM results in error](/questions/64963/local-edit-osm-highway-data-geofabrik-osmpbf-with-josm-results-in-error)

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
<span id="post-64963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64963-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Heyo,</p>
<p>Software of my company is using osm.pbf as input to a tool to calculate a network analysis. The goal is to calculate difference in accessibility if network nodes/edges are removed or added from the openstreetmap network. Therefore we want to be able to locally edit .osm files and export it back to .osm.pbf files.</p>
<p><strong>Workflow</strong>: We downloaded .osm.pbf files from Geofabrik, selected highways only with FME, selected spatial region, converted to .osm and then we want to remove one node/edge. This <a href="https://help.openstreetmap.org/questions/54827/editing-osm-files-locally">previous question</a> mentioned using JOSM to locally edit osm files. However JOSM only accepts .osm files with usernames and does not accept latest GDPR abiding osm files from Geofabrik. When giving JOSM files without user data, it throws <a href="https://josm.openstreetmap.de/ticket/16499">error</a>: Could not read file 'monaco.osm'. Error is: Illegal value for attribute 'changeset'. Got 0. (At line 4, column 114).</p>
<p>What is the best way to locally edit OSM files whilst abiding by GDPR, keeping network relations intact and exporting to osm.pbf?</p>
<p>Would aprreciate your help. We are kinda stuck :/</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-networkanalysis" rel="tag" title="see questions tagged &#39;networkanalysis&#39;">networkanalysis</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-gdpr" rel="tag" title="see questions tagged &#39;gdpr&#39;">gdpr</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '18, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0dc6b864d8142fcdab9e5dec50df38a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davmatic&#39;s gravatar image" />
<p><span>Davmatic</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davmatic has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '18, 21:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-64963" class="comments-container">
&#10;</div>
<div id="comment-tools-64963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64963-form-container" class="comment-form-container">
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

<span id="64973"></span>

<div id="answer-container-64973" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64973-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Davmatic has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This was reported as <a href="https://josm.openstreetmap.de/ticket/16499">a bug in JOSM</a> on July 19, and fixed the next day. Any JOSM with a version number of at least 14038 should be able to open GDPR-abiding .OSM files successfully. You can either download <a href="https://josm.openstreetmap.de/josm-latest.jar">the latest development version of JOSM</a> now, or wait until the next "tested" version is released.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '18, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-64973" class="comments-container">
<span id="64977"></span>
<div id="comment-64977" class="comment">
<div id="post-64977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... the next "tested" version very likely will be released in a few days. The schedule is about each month beginning. However, the "latest" dev version usually also is fine to work with.</p>
</div>
<div id="comment-64977-info" class="comment-info">
<span class="comment-age">(27 Jul '18, 21:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65010"></span>
<div id="comment-65010" class="comment">
<div id="post-65010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answers. Could have found that maybe myself, but good to know there is a fix</p>
</div>
<div id="comment-65010-info" class="comment-info">
<span class="comment-age">(29 Jul '18, 22:10)</span> <span class="comment-user userinfo">Davmatic</span>
</div>
</div>
<span id="65012"></span>
<div id="comment-65012" class="comment">
<div id="post-65012-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15444/davmatic">@Davmatic</a>: the new "tested" version is released, you can update to it and try again.</p>
</div>
<div id="comment-65012-info" class="comment-info">
<span class="comment-age">(29 Jul '18, 22:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65015"></span>
<div id="comment-65015" class="comment">
<div id="post-65015-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Downloaded latest JOSM version. Version 14066 works for me, I can open .osm files that are GDPR abiding</p>
</div>
<div id="comment-65015-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 07:17)</span> <span class="comment-user userinfo">Davmatic</span>
</div>
</div>
<span id="65018"></span>
<div id="comment-65018" class="comment">
<div id="post-65018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also you can 'fake' the user_id and other metadata using osmconvert.</p>
</div>
<div id="comment-65018-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 09:45)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64973-form-container" class="comment-form-container">
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

