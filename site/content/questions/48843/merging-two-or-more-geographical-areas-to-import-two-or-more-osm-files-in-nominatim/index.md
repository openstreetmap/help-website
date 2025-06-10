+++
type = "question"
title = "Merging two or more Geographical Areas to import two or more osm files in Nominatim"
description = '''I have installed nominatim for Maldives and now I want to install for Sri Lanka in the same db. According to lonvia i found it is fast that i merge below both files and then do the import. I have sri-lanka-latest.osm.pbf and maldives-latest.osm.pbf two pbf files and i tried to merge these two with o...'''
date = "2016-03-25T09:54:00Z"
lastmod = "2019-12-03T15:14:00Z"
weight = 48843
keywords = [ "merge", "osmconvert", "nominatim", "pbf", "o5m" ]
aliases = [ "/questions/48843" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Merging two or more Geographical Areas to import two or more osm files in Nominatim](/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim)

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
<span id="post-48843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48843-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed nominatim for Maldives and now I want to install for Sri Lanka in the same db. According to <strong>lonvia</strong> i found it is fast that i merge below both files and then do the import.</p>
<p>I have sri-lanka-latest.osm.pbf and maldives-latest.osm.pbf two pbf files and i tried to merge these two with osmconvert command. I have read <span>Osmconvert</span> in the wiki and osm help questions but could not find the answer.</p>
<p>Then i converted these two files to <span>.o5m</span> files separately using osmconvert and then merged those both files. Is that what I should do?</p>
<p>Thanks in Advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-o5m" rel="tag" title="see questions tagged &#39;o5m&#39;">o5m</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '16, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/226294f6552d8c74ee10799c893da4e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tharaka%20Rajith&#39;s gravatar image" />
<p><span>Tharaka Rajith</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tharaka Rajith has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '16, 08:08</strong> </span></p>
</div>
</div>
<div id="comments-container-48843" class="comments-container">
&#10;</div>
<div id="comment-tools-48843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48843-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="48857"></span>

<div id="answer-container-48857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48857-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-48857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Merging two PBF files can be done in one run, using concatenated processes:</p>
<p>osmconvert region1.pbf --out-o5m | osmconvert - region2.pbf -o=all.pbf</p>
<p>Further examples and explanations can be found at OSM Wiki page:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Parallel_Processing">https://wiki.openstreetmap.org/wiki/Osmconvert#Parallel_Processing</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '16, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48857" class="comments-container">
<span id="48870"></span>
<div id="comment-48870" class="comment">
<div id="post-48870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even better, thanks. I added a link from the Nominatim documentation to this thread.</p>
</div>
<div id="comment-48870-info" class="comment-info">
<span class="comment-age">(27 Mar '16, 19:08)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="48876"></span>
<div id="comment-48876" class="comment">
<div id="post-48876-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>this is the answer i was looking for, works like a charm, thanks</p>
</div>
<div id="comment-48876-info" class="comment-info">
<span class="comment-age">(28 Mar '16, 07:12)</span> <span class="comment-user userinfo">Tharaka Rajith</span>
</div>
</div>
</div>
<div id="comment-tools-48857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48857-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48851"></span>

<div id="answer-container-48851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48851-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should work:</p>
<ol>
<li>osmconvert country1.osm.pbf -o=country1.o5m</li>
<li>osmconvert country2.osm.pbf -o=country2.o5m</li>
<li>osmconvert country1.o5m country2.o5m -o=together.o5m</li>
<li>osmconvert together.o5m -o=together.osm.pbf</li>
</ol>
<p>and then import together.osm.pbf with Nominatim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '16, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-48851" class="comments-container">
<span id="67008"></span>
<div id="comment-67008" class="comment">
<div id="post-67008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want to merge more than one file, the most voted option isn't really working for me. It only stores the content of the last 2 files.</p>
<p>You could make this shorter by converting all your .osm.pbf to .o5m and then do osmconvert *.o5m -o=together.osm.pbf so it gets all .o5m files.</p>
</div>
<div id="comment-67008-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 13:36)</span> <span class="comment-user userinfo">xarly89</span>
</div>
</div>
<span id="71966"></span>
<div id="comment-71966" class="comment">
<div id="post-71966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This answer should be treated with more love!:)</p>
</div>
<div id="comment-71966-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 15:14)</span> <span class="comment-user userinfo">CuriosityBeg...</span>
</div>
</div>
</div>
<div id="comment-tools-48851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56309"></span>

<div id="answer-container-56309" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56309-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Or you can use <a href="http://osmcode.org/osmium-tool/">osmium-tool</a>:</p>
<p><code>osmium merge country1.osm.pbf country2.osm.pbf -o together.osm.pbf</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '17, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-56309" class="comments-container">
&#10;</div>
<div id="comment-tools-56309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56309-form-container" class="comment-form-container">
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

