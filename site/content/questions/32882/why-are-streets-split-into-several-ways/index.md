+++
type = "question"
title = "Why are streets split into several ways?"
description = '''Why are streets often split into several ways on OSM? examples:  &quot;campus drive, stanford&quot; &quot;kirchengasse, vienna&quot; &quot;the bowery, nyc&quot; '''
date = "2014-05-05T20:13:00Z"
lastmod = "2016-03-01T19:11:00Z"
weight = 32882
keywords = [ "ways", "street", "split" ]
aliases = [ "/questions/32882" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Why are streets split into several ways?](/questions/32882/why-are-streets-split-into-several-ways)

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
<span id="post-32882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32882-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why are streets often split into several ways on OSM?</p>
<p>examples:</p>
<ul>
<li>"campus drive, stanford"</li>
<li>"kirchengasse, vienna"</li>
<li>"the bowery, nyc"</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '14, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/763e51406d48132ced03848e9e7b0fc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snupo&#39;s gravatar image" />
<p><span>snupo</span><br />
<span class="score" title="96 reputation points">96</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snupo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 01:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-32882" class="comments-container">
&#10;</div>
<div id="comment-tools-32882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32882-form-container" class="comment-form-container">
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

<span id="32889"></span>

<div id="answer-container-32889" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32889-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-32889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="snupo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Streets are split when one or more properties are different along the street. A non-exhaustive list of such properties would include:</p>
<ul>
<li>Speed Limits</li>
<li>Number of Lanes</li>
<li>Parking restrictions</li>
<li>Nature of street lighting</li>
<li>Bus routes along the street</li>
<li>One way sections</li>
<li>No left/right turn restrictions which require a via point</li>
<li>Changes of jurisdiction (where say, house numbering restarts)</li>
<li>Change of surface: asphalt to concrete, asphalt to dirt, etc.</li>
<li>Nature of the source data (some part may have been seen by a mapper, the rest completed from imagery)</li>
<li>Presence or absence of sidewalks</li>
<li>etc</li>
</ul>
<p>Streets are naturally represented as several ways if they are not linear, or if they are dual carriageways.</p>
<p>If a street is split it is best NOT to recombine sections unless using JOSM which forces a check on all mismatched tags. Creating multilinestring topologies representing all parts of a named street should be done outside OSM as a processing step on an extract. For most streets this is trivial, but there are a number of well-understood exceptions which can create problems and for which there are no good widely available solutions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '14, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-32889" class="comments-container">
&#10;</div>
<div id="comment-tools-32889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32889-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32888"></span>

<div id="answer-container-32888" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32888-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ways are split when the attributes/tags change (and when relation membership changes too).</p>
<p>A random example: the speed limit changes, you slplt the way and apply the new speed limit.</p>
<p>This does lead to sometimes very small segements (joke for old hands), but is perfectly OK.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '14, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '14, 21:45</strong> </span></p>
</div>
</div>
<div id="comments-container-32888" class="comments-container">
&#10;</div>
<div id="comment-tools-32888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32888-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32883"></span>

<div id="answer-container-32883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32883-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-32883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are they Dual-Carrage ways; with a barrier between the two one way parts? They can be split to help routeing especially when only one half of the road links to a paticular side road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '14, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-32883" class="comments-container">
<span id="32895"></span>
<div id="comment-32895" class="comment">
<div id="post-32895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How does splitting a road help the router?</p>
</div>
<div id="comment-32895-info" class="comment-info">
<span class="comment-age">(06 May '14, 07:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32914"></span>
<div id="comment-32914" class="comment">
<div id="post-32914-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I think they're referring to the separately-mapped oneway parts as opposed to a single way representing the entire dual-carriageway, but that has nothing to do with the original question.</p>
</div>
<div id="comment-32914-info" class="comment-info">
<span class="comment-age">(06 May '14, 18:39)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="48443"></span>
<div id="comment-48443" class="comment">
<div id="post-48443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the router can more easily handle when traffic can't cross between the carrageways at junctions</p>
</div>
<div id="comment-48443-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 19:11)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-32883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32883-form-container" class="comment-form-container">
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

