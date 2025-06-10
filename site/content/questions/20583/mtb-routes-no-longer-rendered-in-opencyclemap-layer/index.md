+++
type = "question"
title = "MTB Routes no longer rendered in Opencyclemap layer"
description = '''Hey Just noticed that the opencyclemap no longer renders mtb routes anymore (the green thin lines) when zoomed out. Anybody know why? i couldn&#x27;t find any updates or info on this and i use this functionality a lot. Currently missing it :o( Cheers Nick'''
date = "2013-03-08T03:46:00Z"
lastmod = "2013-03-08T09:16:00Z"
weight = 20583
keywords = [ "mtb", "rendering", "route", "routing" ]
aliases = [ "/questions/20583" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MTB Routes no longer rendered in Opencyclemap layer](/questions/20583/mtb-routes-no-longer-rendered-in-opencyclemap-layer)

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
<span id="post-20583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20583-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey</p>
<p>Just noticed that the opencyclemap no longer renders mtb routes anymore (the green thin lines) when zoomed out. Anybody know why? i couldn't find any updates or info on this and i use this functionality a lot. Currently missing it :o(</p>
<p>Cheers</p>
<p>Nick</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mtb" rel="tag" title="see questions tagged &#39;mtb&#39;">mtb</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '13, 03:46</strong></p>
<img src="https://secure.gravatar.com/avatar/21d2c947f1bc6897a9a688e4cbffaa5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickbarker&#39;s gravatar image" />
<p><span>nickbarker</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickbarker has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-20583" class="comments-container">
&#10;</div>
<div id="comment-tools-20583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20583-form-container" class="comment-form-container">
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

<span id="20585"></span>

<div id="answer-container-20585" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20585-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-20585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Originally OpenCycleMap treated any route with "mtb=yes" as a signed mountain biking route, in the same way it treats "ncn=yes", "rcn=yes" or "lcn=yes" as being part of signed national, regional and local routes. Additionally, you can tag signed routes with the appropriate route relations, and OCM picks them up too.</p>
<p>Unfortunately the meaning of "mtb=yes" has been re-interpreted by many mappers to more of an access tag - e.g. highway=path,mtb=yes meaning that mountain bikes are permitted (or, often it's about suitability rather than permission) but losing any indication that there's a mountain biking route. This meant that in some places (especially around the Swiss/German border) vast tracts of paths and tracks were getting the route highlighting; none of them were signed mountain biking routes. I changed the rendering a few weeks ago.</p>
<p>So if you have a signed route, please use a route relation. They're much better supported, and much more widely used, than when I last reworked the mtb rendering in OCM.</p>
<p>As a random aside, you can tell how long since I last thought about it - the green route highlighting clashes with the green landscape in many areas, since the mtb highlighting predates the use of hillcolouring in OCM!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '13, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-20585" class="comments-container">
&#10;</div>
<div id="comment-tools-20585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20585-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20584"></span>

<div id="answer-container-20584" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20584-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I couldn't find the repository for the OpenCycleMap stylesheet (maybe it is not publicly available) but I can confirm that MTB routes are only rendered from zoom level 12 on compared to regular cycle routes which already start to show at zoom level 5. I suggest to contact <a href="http://www.gravitystorm.co.uk/andy/">Andy Allan</a> (the author) directly.</p>
<p>An alternative is to use the <a href="http://mtb.waymarkedtrails.org">MTB map from waymarkedtrails</a> which also shows additional information about specific routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '13, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '13, 07:51</strong> </span></p>
</div>
</div>
<div id="comments-container-20584" class="comments-container">
&#10;</div>
<div id="comment-tools-20584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20584-form-container" class="comment-form-container">
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

