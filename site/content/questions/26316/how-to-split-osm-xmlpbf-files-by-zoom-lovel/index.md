+++
type = "question"
title = "how to split osm xml/pbf files by zoom lovel?"
description = '''Is there a way to split osm xml/pbf files in small pieces by zoom level?'''
date = "2013-09-13T00:03:00Z"
lastmod = "2013-09-16T16:42:00Z"
weight = 26316
keywords = [ "zoomlevel", "pbf", ".osm", "split" ]
aliases = [ "/questions/26316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to split osm xml/pbf files by zoom lovel?](/questions/26316/how-to-split-osm-xmlpbf-files-by-zoom-lovel)

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
<span id="post-26316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26316-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to split osm xml/pbf files in small pieces by zoom level?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '13, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/61bc4c5ccc22fbf2654459eda674cda8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raku_cmr&#39;s gravatar image" />
<p><span>raku_cmr</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raku_cmr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 01:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-26316" class="comments-container">
<span id="26323"></span>
<div id="comment-26323" class="comment">
<div id="post-26323-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It would help if you could explain what you mean by "by zoom level". Do you mean "so that the resulting file contains all the data that is within the bounds of an OSM tile at zoom X" or "contains only the data that would be rendered by the standard map at zoom X"?</p>
</div>
<div id="comment-26323-info" class="comment-info">
<span class="comment-age">(13 Sep '13, 09:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="26329"></span>
<div id="comment-26329" class="comment">
<div id="post-26329-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I want the result osm file at certain zoom level to contain only the data that will be rendered by standard map at that zoom level</p>
</div>
<div id="comment-26329-info" class="comment-info">
<span class="comment-age">(13 Sep '13, 20:26)</span> <span class="comment-user userinfo">raku_cmr</span>
</div>
</div>
<span id="26395"></span>
<div id="comment-26395" class="comment">
<div id="post-26395-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>IMHO such a splitting feature has necer been implemented in any solution.</p>
<p>If you want to filter raw OSM data, have a look at <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
<p>The "filtering" inside any rendering program is realized by style files ... there you define for each zoom level what raw data should be displayed, and what not.</p>
</div>
<div id="comment-26395-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 16:42)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-26316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26316-form-container" class="comment-form-container">
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

<span id="26321"></span>

<div id="answer-container-26321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the search bar with the word 'split' and you find some similar questions, e.g.</p>
<p><a href="/questions/14151/split-osm-file-without-fragmenting-ways-and-relations">https://help.openstreetmap.org/questions/14151/split-osm-file-without-fragmenting-ways-and-relations</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '13, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '13, 14:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span></p>
</div>
</div>
<div id="comments-container-26321" class="comments-container">
&#10;</div>
<div id="comment-tools-26321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26321-form-container" class="comment-form-container">
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

