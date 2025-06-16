+++
type = "question"
title = "Relation Filtering issue"
description = '''Hello, I&#x27;m trying to extract water bodies and I&#x27;m using Osmosis to filter the osm data for a certain area. When using the --way-key-value option, I specify things like waterway.riverbank for example. My problem is that sometimes, ways that are parts of rivers aren&#x27;t tagged as such and the only way t...'''
date = "2012-10-22T14:08:00Z"
lastmod = "2012-10-23T09:32:00Z"
weight = 17099
keywords = [ "ways", "filtering", "relations", "osmosis" ]
aliases = [ "/questions/17099" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Relation Filtering issue](/questions/17099/relation-filtering-issue)

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
<span id="post-17099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17099-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to extract water bodies and I'm using Osmosis to filter the osm data for a certain area.</p>
<p>When using the --way-key-value option, I specify things like waterway.riverbank for example. My problem is that sometimes, ways that are parts of rivers aren't tagged as such and the only way to know their type is when they are used in a relation.</p>
<p>Unfortunately, when I reach a relation that is tagged as a waterbody of some sort, all of its ways without proper tagging will have been stripped by the filter.</p>
<p>Is there a way to tell Osmosis to keep ways used in relations, regardless of the way tags? --used-way wouldn't work in my case as not all the ways are contained in relations...</p>
<p>Any ideas?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '12, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/de39a81776bc1e755a0ee4bed6954cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mlaban&#39;s gravatar image" />
<p><span>mlaban</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mlaban has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17099" class="comments-container">
&#10;</div>
<div id="comment-tools-17099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17099-form-container" class="comment-form-container">
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

<span id="17105"></span>

<div id="answer-container-17105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not so familiar with the filtering options of osmosis, but I recommend to try <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a></p>
<p>Sometimes it can be easier to use, IMHO.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-17105" class="comments-container">
<span id="17119"></span>
<div id="comment-17119" class="comment">
<div id="post-17119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I had found OsmFilter but it doesn't support the PBF file format at this point unfortunately. So I have to convert the files from PBF back to XML, then filter, then convert back to PBF.</p>
<p>I'll keep digging...</p>
</div>
<div id="comment-17119-info" class="comment-info">
<span class="comment-age">(23 Oct '12, 09:32)</span> <span class="comment-user userinfo">mlaban</span>
</div>
</div>
</div>
<div id="comment-tools-17105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17105-form-container" class="comment-form-container">
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

