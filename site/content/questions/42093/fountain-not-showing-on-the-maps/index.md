+++
type = "question"
title = "Fountain not showing  on the maps"
description = '''I have mapped a fountain but it doesn&#x27;t show on the maps. What am i doing wrong? https://www.openstreetmap.org/#map=19/18.44170/-66.01388 Also, Islands are not showing?? https://www.openstreetmap.org/edit#map=17/18.44821/-66.01501'''
date = "2015-04-01T16:08:00Z"
lastmod = "2015-04-01T16:48:00Z"
weight = 42093
keywords = [ "not_shown", "fountain" ]
aliases = [ "/questions/42093" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Fountain not showing on the maps](/questions/42093/fountain-not-showing-on-the-maps)

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
<span id="post-42093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have mapped a fountain but it doesn't show on the maps. What am i doing wrong?</p>
<p><a href="https://www.openstreetmap.org/#map=19/18.44170/-66.01388">https://www.openstreetmap.org/#map=19/18.44170/-66.01388</a></p>
<p>Also, Islands are not showing?? <a href="https://www.openstreetmap.org/edit#map=17/18.44821/-66.01501">https://www.openstreetmap.org/edit#map=17/18.44821/-66.01501</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-fountain" rel="tag" title="see questions tagged &#39;fountain&#39;">fountain</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '15, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/90cd6be9d90d1eac2f55b1d485410a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce%20B&#39;s gravatar image" />
<p><span>Bruce B</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce B has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '15, 18:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42093" class="comments-container">
&#10;</div>
<div id="comment-tools-42093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42093-form-container" class="comment-form-container">
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

<span id="42095"></span>

<div id="answer-container-42095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42095-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-42095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard layer <a href="http://stefanosabatini.eu/doesitrender/#amenity=fountain">doesn't render amenity=fountain</a>. However you can list <a href="https://www.openstreetmap.org/way/335253694">your fountain</a> via the <a href="http://wiki.openstreetmap.org/wiki/Query_features_tool">query features tool</a> (number 11 in the <a href="http://wiki.openstreetmap.org/wiki/Browsing">browsing</a> documentation).</p>
<p>The <a href="https://www.openstreetmap.org/way/335572781">island</a> is not rendered because it misses the <a href="http://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">natural=coastline</a> tag. See <a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Disland">place=island</a> for more information about mapping islands. Also the way of the island's coastline must be drawn <em>counterclockwise</em>. Currently this is not the case for your island, so you have to reverse the way! But apparently iD doesn't allow to reverse areas. So either you have to split it, reverse both parts individually and then combine them again. Or just delete it and draw it again, this time counterclockwise.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '15, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '15, 16:55</strong> </span></p>
</div>
</div>
<div id="comments-container-42095" class="comments-container">
&#10;</div>
<div id="comment-tools-42095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42095-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42096"></span>

<div id="answer-container-42096" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42096-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fountains are not currently being rendered on the default map style. A request to render them has been under discussion over on the style's GitHub project page <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/705">here</a>, so it may not be much longer until they are rendered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '15, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-42096" class="comments-container">
&#10;</div>
<div id="comment-tools-42096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42096-form-container" class="comment-form-container">
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

