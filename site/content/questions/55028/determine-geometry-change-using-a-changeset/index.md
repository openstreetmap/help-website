+++
type = "question"
title = "Determine geometry change using a changeset"
description = '''I want to know when the geometry of a Way was changed or deleted. To that end I downloaded the history of a specific Way via the API and within each version is the changeset number. However looking through the QA tools in the OSM wiki there are a number of tools to visualize changes but none appear ...'''
date = "2017-03-13T02:02:00Z"
lastmod = "2017-03-17T02:54:00Z"
weight = 55028
keywords = [ "geometry", "changeset", "way" ]
aliases = [ "/questions/55028" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Determine geometry change using a changeset](/questions/55028/determine-geometry-change-using-a-changeset)

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
<span id="post-55028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55028-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to know when the geometry of a Way was changed or deleted. To that end I downloaded the history of a specific Way via the API and within each version is the changeset number. However looking through the QA tools in the OSM wiki there are a number of tools to visualize changes but none appear to provide info in a downloadable fashion. Thanks for any help.</p>
<p>The use case is not that I want to be notified when a geometry has changed, but rather by having the ability to inspect a changeset and determine if geometry has been changed. My use case is you fetch the history of a Way, and in the fetched history is the changeset number associated with the history or version if you will. Then I want to fetch the changeset to determine what is the change to the Way object. I want to know has the geometry of the Way been moved or deleted? This information is in the changeset but I was hoping to find an OSM tool that interprets the contents of the changeset spitting out the exact change to the Way in question.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '17, 02:02</strong></p>
<img src="https://secure.gravatar.com/avatar/af6f2a3c46f2215ac4ae6285ddb66ad8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Helpwanted&#39;s gravatar image" />
<p><span>Helpwanted</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Helpwanted has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '17, 21:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55028" class="comments-container">
&#10;</div>
<div id="comment-tools-55028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55028-form-container" class="comment-form-container">
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

<span id="55050"></span>

<div id="answer-container-55050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55050-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Quality_assurance">https://wiki.openstreetmap.org/wiki/Quality_assurance</a> was the right start, and I assume that nearly all our tools are listed there.</p>
<p>Maybe you could built something with Overpass turbo since you want something "downloadable". Do you want raw data? Or do you want to download a visualization? End user or programmer? A visualization (not downloadable) based on geographical location (not on object id) would be <a href="https://tyrasd.github.io/latest-changes">https://tyrasd.github.io/latest-changes</a> . I guess others will have some more ideas.</p>
<p>Note that a changeset appears in a way's history only if the way object (tags or node memberships) has been changed. A way's geometry can be changed by just moving the existing nodes - that does not create an history entry on the way object. Example: <a href="https://pewu.github.io/osm-history/#/way/311406058">https://pewu.github.io/osm-history/#/way/311406058</a> (there have been two very recent changes to its geometry which are not listed here).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '17, 07:09</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55050" class="comments-container">
<span id="55137"></span>
<div id="comment-55137" class="comment">
<div id="post-55137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your advice and for digging up the last example.</p>
</div>
<div id="comment-55137-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 02:54)</span> <span class="comment-user userinfo">Helpwanted</span>
</div>
</div>
</div>
<div id="comment-tools-55050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55050-form-container" class="comment-form-container">
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

