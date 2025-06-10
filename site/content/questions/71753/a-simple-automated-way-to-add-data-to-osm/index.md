+++
type = "question"
title = "A simple automated way to add data to OSM?"
description = '''I want to add data to OSM, which i have found missing surrounding my locality. I have collected data using Google&#x27;s API(places,directions, etc.) This data is now stored in csv format and now i want to upload it to OSM, but is there any simple automated way to upload data to OSM db. I read about edit...'''
date = "2019-11-21T07:48:00Z"
lastmod = "2019-11-21T10:03:00Z"
weight = 71753
keywords = [ "openstreetmap", "editing", "osm", "bulk_editing" ]
aliases = [ "/questions/71753" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [A simple automated way to add data to OSM?](/questions/71753/a-simple-automated-way-to-add-data-to-osm)

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
<span id="post-71753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71753-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-71753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to add data to OSM, which i have found missing surrounding my locality. I have collected data using Google's API(places,directions, etc.) This data is now stored in csv format and now i want to upload it to OSM, but is there any simple automated way to upload data to OSM db. I read about editing OSM and most of the process seems to be manual. Is there any other way to edit OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '19, 07:48</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71753" class="comments-container">
&#10;</div>
<div id="comment-tools-71753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71753-form-container" class="comment-form-container">
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

<span id="71754"></span>

<div id="answer-container-71754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71754-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-71754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vsaadnet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We are normally not interested in bulk uploads because they have a tendency to break things - duplicate existing data, overlap existing data, not connect to existing data properly, and so on. The preferred way to work with external data sources is to load them up in your editor of choice and manually transfer objects to OSM.</p>
<p>Having said that, it is technically possible to load a large amount of data into an editor and just upload to OSM. This usually counts as a data import and needs to follow some guidelines, see <a href="https://wiki.openstreetmap.org/wiki/Import.">https://wiki.openstreetmap.org/wiki/Import.</a></p>
<p>Most of all however, we need to respect copyright and intellectual property when adding things to OSM. If you have copied anything from Google maps or traced anything with the help of Google aerial imagery, then that data is not admissible in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '19, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '19, 09:15</strong> </span></p>
</div>
</div>
<div id="comments-container-71754" class="comments-container">
&#10;</div>
<div id="comment-tools-71754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71754-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71755"></span>

<div id="answer-container-71755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71755-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I addition To Frederik's answer, It is simple for you to edit locally with your local knowledge and observation. You can use the excellent Bing and DG to add local stuff with one of the editors, This was the plan when OSM was first thought of. ( although Bing and DG weren't available then). Happy Mapping</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '19, 15:32</strong> </span></p>
</div>
</div>
<div id="comments-container-71755" class="comments-container">
&#10;</div>
<div id="comment-tools-71755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71755-form-container" class="comment-form-container">
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

