+++
type = "question"
title = "Overpass Turbo: How to exclude POI types from search results?"
description = '''Hey I&#x27;m currently trying to prepare my Garmins with some POIs for Weather Shelters from the DACH region. After some hours of Trial and Error, I ended up looking here on the Question section for a script that could search for POIs in Multiple Countries. I edited the script so it would find Shelters, ...'''
date = "2022-02-22T03:41:00Z"
lastmod = "2022-02-22T06:44:00Z"
weight = 83547
keywords = [ "exclude", "overpass-turbo", "poi" ]
aliases = [ "/questions/83547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: How to exclude POI types from search results?](/questions/83547/overpass-turbo-how-to-exclude-poi-types-from-search-results)

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
<span id="post-83547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey I'm currently trying to prepare my Garmins with some POIs for Weather Shelters from the DACH region. After some hours of Trial and Error, I ended up looking here on the Question section for a script that could search for POIs in Multiple Countries. I edited the script so it would find Shelters, but now I am stuck at the task to exclude "public_transportaion" shelters from it, since getting Bus Stops isn't that helpful in the Forest, but these show up nonetheless.</p>
<p>The Script I found and edited is this one: <a href="https://pastebin.com/4GvajSW7">https://pastebin.com/4GvajSW7</a></p>
<p>I'm thankful for any help or hints in how to exclude results (I'm no expert in these things at all, but I like to make things right at the first time so I don't have to spend time with it twice)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-exclude" rel="tag" title="see questions tagged &#39;exclude&#39;">exclude</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '22, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/b20179ee9e1ae4bc0d65cc2aa4198376?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nukra&#39;s gravatar image" />
<p><span>Nukra</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nukra has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83547" class="comments-container">
&#10;</div>
<div id="comment-tools-83547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83547-form-container" class="comment-form-container">
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

<span id="83548"></span>

<div id="answer-container-83548" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83548-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>Please see the "negation" section of this <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">page</a>.</p>
<p>But, as you'll read everywhere in the docs, the XML version of overpass is kind of deprecated. You should switch to OverpassQL.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '22, 06:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83548" class="comments-container">
&#10;</div>
<div id="comment-tools-83548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83548-form-container" class="comment-form-container">
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

