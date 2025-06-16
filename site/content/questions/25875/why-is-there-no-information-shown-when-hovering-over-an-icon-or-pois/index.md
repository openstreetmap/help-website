+++
type = "question"
title = "Why is there no information shown when hovering over an icon or POIs?"
description = '''I added some points to OSM. Why is the data not visible like on Google-maps when you hover over an icon or any POI for that matter?'''
date = "2013-08-27T21:14:00Z"
lastmod = "2013-08-28T09:26:00Z"
weight = 25875
keywords = [ "rendering", "hovertext", "webmap", "poi" ]
aliases = [ "/questions/25875" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is there no information shown when hovering over an icon or POIs?](/questions/25875/why-is-there-no-information-shown-when-hovering-over-an-icon-or-pois)

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
<span id="post-25875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25875-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I added some points to OSM. Why is the data not visible like on Google-maps when you hover over an icon or any POI for that matter?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-hovertext" rel="tag" title="see questions tagged &#39;hovertext&#39;">hovertext</span> <span class="post-tag tag-link-webmap" rel="tag" title="see questions tagged &#39;webmap&#39;">webmap</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '13, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a48b13f2dd6eadd0d53d2eba1cf07a5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20Venema&#39;s gravatar image" />
<p><span>Daniel Venema</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel Venema has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '13, 11:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-25875" class="comments-container">
&#10;</div>
<div id="comment-tools-25875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25875-form-container" class="comment-form-container">
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

<span id="25884"></span>

<div id="answer-container-25884" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25884-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-25884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer: Because no-one has programmed that feature yet.</p>
<p>Long answer: This is a <a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks#Clickable_POIs_on_the_frontpage">long-term ambition for OSM</a>. However, the map rendering software that we use (Mapnik) does not currently support it: the feature is <a href="https://github.com/mapnik/mapnik/wiki/MetaWriter">currently disabled</a> in Mapnik and <a href="https://github.com/mapnik/mapnik/issues/1240">needs to be rewritten</a>. If you have software development skills and can lend them to the project, I'm sure the Mapnik team would be delighted to benefit from your help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '13, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-25884" class="comments-container">
&#10;</div>
<div id="comment-tools-25884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25884-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25878"></span>

<div id="answer-container-25878" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25878-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In short: because OSM.org is (at least currently) not meant as a google maps replacement. By the way, you will notice also no adverts, no tracking all over the web, …</p>
<p>Try for example <a href="http://overpass.apis.dev.openstreetmap.org">http://overpass.apis.dev.openstreetmap.org</a> (you can click on a location and get listed all objects there; note that this is a development version!). And please also see the still valid answers at <a href="/questions/16741/">can-the-web-interface-show-pois?</a> (listing other options). Also there are many <span>services which use the OSM data</span> (however, currently there is none supporting that many POI types like google maps, as far as I know).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '13, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '13, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-25878" class="comments-container">
&#10;</div>
<div id="comment-tools-25878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25878-form-container" class="comment-form-container">
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

