+++
type = "question"
title = "Osmosis - merge issue (Pipeline entities are not sorted or contain multiple versions)"
description = '''OsmosisRuntimeException: Pipeline entities are not sorted or contain multiple versions of a single entity, previous entity type=Node, id=191805, version=5 current entity type=Node, id=191805, version=6. Im having trouble with Osmosis when I try to apply a change set to a OSM file. I tried the follow...'''
date = "2012-05-01T07:46:00Z"
lastmod = "2012-05-01T09:33:00Z"
weight = 12469
keywords = [ "merge", "osmosis" ]
aliases = [ "/questions/12469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis - merge issue (Pipeline entities are not sorted or contain multiple versions)](/questions/12469/osmosis-merge-issue-pipeline-entities-are-not-sorted-or-contain-multiple-versions)

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
<span id="post-12469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12469-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OsmosisRuntimeException: Pipeline entities are not sorted or contain multiple versions of a single entity, previous entity type=Node, id=191805, version=5 current entity type=Node, id=191805, version=6.</p>
<p>Im having trouble with Osmosis when I try to apply a change set to a OSM file. I tried the following:</p>
<ol>
<li>Extract a City data as OSM file from Planet OSM (using bounding poly file)</li>
<li>Sort the generated OSM</li>
<li>Get the immediate next change set file (OSC file) from Planet OSM website</li>
<li>Sort the Change set file</li>
<li>Run the osmosis apply-change command like below: <code>$&gt;osmosis --rxc d:\change_set_15Apr_sorted.osc --rx d:\myCity_sorted.osm --ac --wx d:\myCity_merged.osm</code></li>
</ol>
<blockquote>
<p>Osmosis throws the following exception: org.openstreetmap.osmosis.core.OsmosisRuntimeException: Pipeline entities are not sorted or contain multiple versions of a single entity, previous entity type=Node, id=191805, version=5 current entity type=Node, id=191805, version=6. at org.openstreetmap.osmosis.core.sort.v0_6.SortedDeltaChangePipeValidator.process(SortedDeltaChangePipeValidato r.java:49) at org.openstreetmap.osmosis.xml.v0_6.impl.ChangeSourceElementProcessor$ChangeSinkAdapter.process(ChangeSourceEl ementProcessor.java:134) at org.openstreetmap.osmosis.xml.v0_6.impl.NodeElementProcessor.end(NodeElementProcessor.java:118) at org.openstreetmap.osmosis.xml.v0_6.impl.OsmChangeHandler.endElement(OsmChangeHandler.java:94) at org.apache.xerces.parsers.AbstractSAXParser.endElement(Unknown Source) at org.apache.xerces.parsers.AbstractXMLDocumentParser.emptyElement(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElement(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContentDispatcher.dispatch(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)</p>
</blockquote>
<p><em>How do I eliminate the duplicated nodes?</em></p>
<p>Appreciate your help.</p>
<p>Thank you Kris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '12, 07:46</strong></p>
<img src="https://secure.gravatar.com/avatar/382f63907e37a769341f345c01d8e8df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kris&#39;s gravatar image" />
<p><span>kris</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kris has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '14, 14:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-12469" class="comments-container">
&#10;</div>
<div id="comment-tools-12469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12469-form-container" class="comment-form-container">
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

<span id="12470"></span>

<div id="answer-container-12470" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12470-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the solution. I used the --simc task and extracted the unique/latest node set from the change files; sorted the change set and then applied it on the existing city file. It works now! Note: Use the respective bounding box/poly file so that the change set is applied for the specified area - otherwise the --apply-change task merges the change set/osc file to the OSM file.</p>
<p>Kris</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '12, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/382f63907e37a769341f345c01d8e8df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kris&#39;s gravatar image" />
<p><span>kris</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kris has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '12, 09:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-12470" class="comments-container">
&#10;</div>
<div id="comment-tools-12470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12470-form-container" class="comment-form-container">
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

