+++
type = "question"
title = "Exporting behavior for areas partially outside export bounds"
description = '''I have an application that processes exported OSM files, and I would like to know how exporting handles areas (that is closed &amp;lt;way&amp;gt;&amp;lt;/way&amp;gt; elements with the appropriate tags) that are partially outside of the export bounds. So if we consider this example, where green circles represent the...'''
date = "2021-07-18T13:03:00Z"
lastmod = "2021-07-18T13:03:00Z"
weight = 81023
keywords = [ "export", "area" ]
aliases = [ "/questions/81023" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting behavior for areas partially outside export bounds](/questions/81023/exporting-behavior-for-areas-partially-outside-export-bounds)

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
<span id="post-81023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an application that processes exported OSM files, and I would like to know how exporting handles areas (that is closed &lt;way&gt;&lt;/way&gt; elements with the appropriate tags) that are partially outside of the export bounds.</p>
<p>So if we consider this example, where green circles represent the area nodes (the green lines are there just to make clear how the nodes make up the area) and the red rectangle represents the export region: <img src="/upfiles/diagram-all_bumfYUl.png" alt="Example" /></p>
<p>I imagine exporting could only behave in one of the following ways:</p>
<ul>
<li>It includes the entire area nodes in the exported OSM file: <img src="/upfiles/diagram-all_bumfYUl.png" alt="All nodes" /></li>
<li>It does not include the area at all in the exported OSM file: <img src="/upfiles/diagram-none.png" alt="No nodes" /></li>
<li>It includes only those nodes of the area that are inside the export bounds: <img src="/upfiles/diagram-contain.png" alt="Nodes inside only" /></li>
<li>It includes those nodes of the area that are inside the export bounds, as well as one additional node for every way segment that "enters" or "leaves" the export rectangle: <img src="/upfiles/diagram-cover.png" alt="Nodes inside and around only" /></li>
</ul>
<p>The last two scenarios seem unlikely to me, cause in these scenarios, the output area would not always correctly represent the portion of the original area that is within the export bounds (it does not in the examples above). And the second scenario would be problematic to me, cause it means that you cannot export a specific region and be guaranteed that you will have ALL the elements that are either fully or partially within that region in the output OSM file. For that you would have to export a larger region that covers all the areas, but generally you don't know, for each area that is partially outside of the region of interest, how far out does it go...</p>
<p>So <strong>how exactly does exporting handle an area that is partially outside of the export bounds?</strong> I use the built-in export feature of the interactive openstreetmap.org map (manually select an area then click on "Export" button) as well as the overpass API, so I'm interested to know what the behavior is for each of those solutions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '21, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/5a1c4fef238bbe32f7f78944dd436cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Namefie&#39;s gravatar image" />
<p><span>Namefie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Namefie has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '21, 14:50</strong> </span></p>
</div>
</div>
<div id="comments-container-81023" class="comments-container">
&#10;</div>
<div id="comment-tools-81023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81023-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

