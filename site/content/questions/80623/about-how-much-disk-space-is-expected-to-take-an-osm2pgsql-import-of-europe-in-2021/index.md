+++
type = "question"
title = "About how much disk space is expected to take an osm2pgsql import of Europe in 2021?"
description = '''I did a osm2pgsql import of Europe (by running a switch2osm docker image) and it took ~500GB disk space. I expected to take less, because I&#x27;ve read a post of a guy who claimed that in 2018 it took him ~200GB. Is that normal?'''
date = "2021-06-18T13:11:00Z"
lastmod = "2021-06-18T13:50:00Z"
weight = 80623
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/80623" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [About how much disk space is expected to take an osm2pgsql import of Europe in 2021?](/questions/80623/about-how-much-disk-space-is-expected-to-take-an-osm2pgsql-import-of-europe-in-2021)

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
<span id="post-80623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80623-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did a osm2pgsql import of Europe (by running a switch2osm docker image) and it took ~500GB disk space. I expected to take less, because I've read a post of a guy who claimed that in 2018 it took him ~200GB. Is that normal?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '21, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/036f20e163418d550d068b6a907bc7f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ptrtdrv&#39;s gravatar image" />
<p><span>ptrtdrv</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ptrtdrv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80623" class="comments-container">
<span id="80624"></span>
<div id="comment-80624" class="comment">
<div id="post-80624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crossspot: <a href="https://gis.stackexchange.com/questions/401509/how-much-disk-space-is-expected-to-take-an-osm2pgsql-import-of-europe-in-2021/401893#401893">https://gis.stackexchange.com/questions/401509/how-much-disk-space-is-expected-to-take-an-osm2pgsql-import-of-europe-in-2021/401893#401893</a></p>
</div>
<div id="comment-80624-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 13:11)</span> <span class="comment-user userinfo">ptrtdrv</span>
</div>
</div>
</div>
<div id="comment-tools-80623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80623-form-container" class="comment-form-container">
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

<span id="80625"></span>

<div id="answer-container-80625" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80625-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ptrtdrv has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is to be expected. You might be able to save a little space with the "flatnodes" option. Also if you do not need to update your database later on, use the "drop" option which will only marginally reduce the disk space used during import, but can delete some unused data afterwards.</p>
<p>Very recent versions of osm2pgsql have also massively reduced their RAM requirements for importing without the "slim" option. If you have 96 GB RAM and latest osm2pgsql then you can import Europe without "slim" which will drastically reduce disk usage. (You can try with 64 GB but it's a gamble.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '21, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80625" class="comments-container">
&#10;</div>
<div id="comment-tools-80625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80625-form-container" class="comment-form-container">
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

