+++
type = "question"
title = "Export OSM poi with all data available in a region"
description = '''Hi is there a way that i can export a list of pois in a region i choose with all data available for the pois, like address, opening times, homepage and so on? best output would be xml or so. i tried to understand the overpass api but didn&#x27;t get it and i think that&#x27;s not what i am searching for, righ...'''
date = "2014-04-02T02:16:00Z"
lastmod = "2015-04-23T16:53:00Z"
weight = 32056
keywords = [ "overpass", "region", "export", "poi" ]
aliases = [ "/questions/32056" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export OSM poi with all data available in a region](/questions/32056/export-osm-poi-with-all-data-available-in-a-region)

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
<span id="post-32056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32056-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi is there a way that i can export a list of pois in a region i choose with all data available for the pois, like address, opening times, homepage and so on? best output would be xml or so.</p>
<p>i tried to understand the overpass api but didn't get it and i think that's not what i am searching for, right?</p>
<p>would be great if you can help me. thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '14, 02:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6d5298b5e75c1340cb1b33e288b22d50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Crag&#39;s gravatar image" />
<p><span>Crag</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Crag has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '16, 14:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-32056" class="comments-container">
&#10;</div>
<div id="comment-tools-32056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32056-form-container" class="comment-form-container">
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

<span id="32061"></span>

<div id="answer-container-32061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32061-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-32061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> is perfectly fine for your problem. Just use <a href="http://overpass-turbo.eu/">overpass turbo</a>, go to the area you are interested in, and choose <em>Load</em> -&gt; <em>Examples</em> -&gt; <em>Map Call</em> via the menu. This query will return all data in your current view. After hitting <em>Run</em> you can <em>Export</em> it in several different formats, including XML.</p>
<p>The data returned will probably contain more information than you are interested in so you will have to do some post-filtering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '14, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '14, 07:52</strong> </span></p>
</div>
</div>
<div id="comments-container-32061" class="comments-container">
<span id="32201"></span>
<div id="comment-32201" class="comment">
<div id="post-32201-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>do you mean this page? <a href="http://overpass-api.de/">http://overpass-api.de/</a> or where can i just select a city and export the pois with their data. I think its a bit more difficult. I dont understand the structure of the overpassing api</p>
</div>
<div id="comment-32201-info" class="comment-info">
<span class="comment-age">(08 Apr '14, 14:47)</span> <span class="comment-user userinfo">Crag</span>
</div>
</div>
<span id="42558"></span>
<div id="comment-42558" class="comment">
<div id="post-42558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! Hope that it works!</p>
</div>
<div id="comment-42558-info" class="comment-info">
<span class="comment-age">(23 Apr '15, 16:53)</span> <span class="comment-user userinfo">Hans-Peter-G...</span>
</div>
</div>
</div>
<div id="comment-tools-32061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32061-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32207"></span>

<div id="answer-container-32207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try starting with <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> by downloading raw OSM data, perhabs do filtering and cropping with osmfilter or osmosis, and convert the result file to a CSV file with osmconvert.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '14, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32207" class="comments-container">
&#10;</div>
<div id="comment-tools-32207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32207-form-container" class="comment-form-container">
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

