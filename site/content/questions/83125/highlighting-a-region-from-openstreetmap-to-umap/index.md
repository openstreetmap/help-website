+++
type = "question"
title = "Highlighting a region from Openstreetmap to Umap"
description = '''Hello everyone, I would like to be able to highlight a state/region in umap by importing it from Openstreetmaps, rather than manually inputting it.  Below, I use Colorado, USA as an example.   Currently, I have to use the create polygon tool to highlight a region  Colorado already exists in Openstre...'''
date = "2022-01-19T21:57:00Z"
lastmod = "2022-01-20T08:56:00Z"
weight = 83125
keywords = [ "regions", "umap", "rendering", "easy", "import" ]
aliases = [ "/questions/83125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Highlighting a region from Openstreetmap to Umap](/questions/83125/highlighting-a-region-from-openstreetmap-to-umap)

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
<span id="post-83125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83125-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I would like to be able to highlight a state/region in umap by importing it from Openstreetmaps, rather than manually inputting it.</p>
<p>Below, I use Colorado, USA as an example.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_from_2022-01-18_16-53-35.png" alt="alt text" /></p>
<p><strong>Currently, I have to use the create polygon tool to highlight a region</strong></p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_from_2022-01-18_16-53-56.png" alt="alt text" /></p>
<p><strong>Colorado already exists in Openstreetmap. How do I use what Openstreetmap has highlighted, so I don't have to manually input it?</strong></p>
<p>Let me know if I need to clarify. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regions" rel="tag" title="see questions tagged &#39;regions&#39;">regions</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-easy" rel="tag" title="see questions tagged &#39;easy&#39;">easy</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '22, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/396fc939e0ecb84382a4d3a23f8c531e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GhostlyT&#39;s gravatar image" />
<p><span>GhostlyT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GhostlyT has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-83125" class="comments-container">
&#10;</div>
<div id="comment-tools-83125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83125-form-container" class="comment-form-container">
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

<span id="83128"></span>

<div id="answer-container-83128" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83128-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an import feature in uMap. When you are editing the map click on the upward arrow to open the import screen.</p>
<p>One way to do it is to create an Overpass query that fetches the Colorado geometry and dynamically load it in uMap. Given that Colorado borders will rarely change this is probably just an unnecessary drain on OSM server resources. Instead you can use the same query in <a href="http://overpass-turbo.eu/">Overpass Turbo</a> and download the geometry to a local file. You can upload this file in the same import dialogue in uMap in any layer you chose.</p>
<p>Check the wizard and help in Overpass Turbo and have a first go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '22, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</img>
</div>
</div>
<div id="comments-container-83128" class="comments-container">
&#10;</div>
<div id="comment-tools-83128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83128-form-container" class="comment-form-container">
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

