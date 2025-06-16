+++
type = "question"
title = "Question about Osmosis tag-filter"
description = '''Hey, I am trying to filter out the following way types out of an osm.bz2-file (malta-latest.osm.bz2 from Geofrabrik): footway,path, cycleway. Until now I did this by the following command: C:..&#92;bin&amp;gt;osmosis --read-xml file=&quot;malta-latest.osm.bz2&quot; --tag-filter accept-ways highway=footway,cycleway,pa...'''
date = "2014-04-10T10:20:00Z"
lastmod = "2014-04-14T08:56:00Z"
weight = 32261
keywords = [ "filter", "osmosis" ]
aliases = [ "/questions/32261" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Question about Osmosis tag-filter](/questions/32261/question-about-osmosis-tag-filter)

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
<span id="post-32261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32261-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I am trying to filter out the following way types out of an osm.bz2-file (malta-latest.osm.bz2 from Geofrabrik): footway,path, cycleway. Until now I did this by the following command:</p>
<pre><code>C:..\bin&gt;osmosis --read-xml file=&quot;malta-latest.osm.bz2&quot; --tag-filter accept-ways highway=footway,cycleway,path --used-node --tag-filter reject-relations --write-xml file=&quot;malta-filtered.osm.bz2&quot;</code></pre>
<p>This works as it filters the right ways, but it also includes some nodes (mostly highway=bus_stop and public_transport=*, but also some others) that shouldn't be in there (imho), because there is no (visible) connection to any of the correct ways. I don't really understand, why this is done..!?! :-( Has anyone an idea and could help me?</p>
<p>Thanks in advance</p>
<p>Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '14, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9ea4ee5e88aaba4f03a740579f0e6597?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="49North&#39;s gravatar image" />
<p><span>49North</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="49North has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '14, 22:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-32261" class="comments-container">
&#10;</div>
<div id="comment-tools-32261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32261-form-container" class="comment-form-container">
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

<span id="32335"></span>

<div id="answer-container-32335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32335-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue is a simple ordering problem. By specifying <code>--used-node</code> before you drop the relations with <code>--tag-filter reject-relations</code>, you get all nodes either used by one of the ways you have selected, or used by <em>any</em> of the relations in the file. Swap these two arguments around, and all works as expected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '14, 22:19</strong> </span></p>
</div>
</div>
<div id="comments-container-32335" class="comments-container">
<span id="32355"></span>
<div id="comment-32355" class="comment">
<div id="post-32355-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hey Frederik, this sounds logical and it works..! ;-) Thanks a lot!</p>
</div>
<div id="comment-32355-info" class="comment-info">
<span class="comment-age">(14 Apr '14, 08:52)</span> <span class="comment-user userinfo">49North</span>
</div>
</div>
</div>
<div id="comment-tools-32335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32335-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32293"></span>

<div id="answer-container-32293" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32293-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you can have a closer look at <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> as an alternative tool.</p>
<p>Read its documentation in the OSM wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '14, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32293" class="comments-container">
<span id="32356"></span>
<div id="comment-32356" class="comment">
<div id="post-32356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, thanks for your reply - i will have a look at it, but as i have to do this as an assignment while doing an further training, i am bound at osmosis in this specific case.. ;-)</p>
</div>
<div id="comment-32356-info" class="comment-info">
<span class="comment-age">(14 Apr '14, 08:56)</span> <span class="comment-user userinfo">49North</span>
</div>
</div>
</div>
<div id="comment-tools-32293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32293-form-container" class="comment-form-container">
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

