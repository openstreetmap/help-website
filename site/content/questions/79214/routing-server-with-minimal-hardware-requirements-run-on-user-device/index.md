+++
type = "question"
title = "Routing server with minimal hardware requirements (run on user device)"
description = '''I&#x27;m looking for a routing server/library with minimal hardware requirements. The software needs to be run offline on user&#x27;s PC (preferably 4GB RAM and mediocre CPU).It doesn&#x27;t need to be the most accurate nor the fastest. I just need snapping feature and &#x27;best&#x27; route between two coordinates as a lis...'''
date = "2021-03-11T00:22:00Z"
lastmod = "2021-03-13T14:53:00Z"
weight = 79214
keywords = [ "offline", "standalone", "routing", "server" ]
aliases = [ "/questions/79214" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Routing server with minimal hardware requirements (run on user device)](/questions/79214/routing-server-with-minimal-hardware-requirements-run-on-user-device)

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
<span id="post-79214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79214-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a routing server/library with minimal hardware requirements. The software needs to be run offline on user's PC (preferably 4GB RAM and mediocre CPU).It doesn't need to be the most accurate nor the fastest. I just need snapping feature and 'best' route between two coordinates as a list of waypoints. I won't use adresses, turn by turn navigation etc...</p>
<p>For my webservice I use OSRM, it's great and robust but running it on the user machine would be a huge overkill and it would require enormous amounts of RAM (like 64GB for Europe) to even start it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-standalone" rel="tag" title="see questions tagged &#39;standalone&#39;">standalone</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '21, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4f865fdddf91e5e9727ec0958c2858?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adamsc&#39;s gravatar image" />
<p><span>adamsc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adamsc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79214" class="comments-container">
&#10;</div>
<div id="comment-tools-79214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79214-form-container" class="comment-form-container">
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

<span id="79229"></span>

<div id="answer-container-79229" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79229-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Graphhopper has a variant that should work on mobile devices <a href="https://github.com/graphhopper/graphhopper/">https://github.com/graphhopper/graphhopper/</a> However this seems to be no longer actively maintained.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '21, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-79229" class="comments-container">
&#10;</div>
<div id="comment-tools-79229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79229-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79233"></span>

<div id="answer-container-79233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79233-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://github.com/Tristramg/osm4routing2">https://github.com/Tristramg/osm4routing2</a> to extract the routing graph from OSM, then any A* library to do reasonable point-to-point routing - pretty much every language has an A* implementation somewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '21, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '21, 09:26</strong> </span></p>
</div>
</div>
<div id="comments-container-79233" class="comments-container">
&#10;</div>
<div id="comment-tools-79233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79246"></span>

<div id="answer-container-79246" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79246-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/abrensch/brouter">BRouter</a> was made to run on smartphones (Android), so it has low memory requirements by design. It has a server component (requires Java runtime) and can also be embedded in a Java application.</p>
<p>For a quick start, see the <a href="https://github.com/nrenner/brouter-web/blob/master/INSTALL.md#installation">standalone bundle</a> with the BRouter-Web client.</p>
<p>As routing profiles are evaluated at runtime, the data files can be used for all modes of transport. This flexibility comes at the cost of speed, it's way slower than OSRM.</p>
<p><em>[Disclaimer: I'm a maintainer of the BRouter-Web client]</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '21, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-79246" class="comments-container">
&#10;</div>
<div id="comment-tools-79246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79246-form-container" class="comment-form-container">
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

