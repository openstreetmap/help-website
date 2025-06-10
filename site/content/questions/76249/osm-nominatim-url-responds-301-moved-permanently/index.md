+++
type = "question"
title = "OSM nominatim url responds 301 moved permanently"
description = '''Hi, Our application is using the URL: http://nominatim.openstreetmap.org/search.php to search for locations on the OSM. It was working as expected until last week. Now, the response from the URL is &quot;301 moved permanently&quot;. Can someone please tell if anything has changed in OSM map server? '''
date = "2020-08-21T07:54:00Z"
lastmod = "2020-08-21T12:12:00Z"
weight = 76249
keywords = [ "search", "nominatim" ]
aliases = [ "/questions/76249" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM nominatim url responds 301 moved permanently](/questions/76249/osm-nominatim-url-responds-301-moved-permanently)

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
<span id="post-76249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76249-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Our application is using the URL: <a href="http://nominatim.openstreetmap.org/search.php">http://nominatim.openstreetmap.org/search.php</a> to search for locations on the OSM. It was working as expected until last week. Now, the response from the URL is "301 moved permanently". Can someone please tell if anything has changed in OSM map server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '20, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ce02a7f48e12785909702d22c229b0fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shwetha4194&#39;s gravatar image" />
<p><span>Shwetha4194</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shwetha4194 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76249" class="comments-container">
&#10;</div>
<div id="comment-tools-76249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76249-form-container" class="comment-form-container">
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

<span id="76250"></span>

<div id="answer-container-76250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>301 indicates a permanent redirect that your app should be following instead of throwing an error.</p>
<p>It redirects to <a href="https://nominatim.openstreetmap.org/ui/search.html">https://nominatim.openstreetmap.org/ui/search.html</a> which is simply the new url for the same thing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '20, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '20, 08:24</strong> </span></p>
</div>
</div>
<div id="comments-container-76250" class="comments-container">
<span id="76252"></span>
<div id="comment-76252" class="comment">
<div id="post-76252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought so too, thank you for the confirmation.</p>
</div>
<div id="comment-76252-info" class="comment-info">
<span class="comment-age">(21 Aug '20, 08:24)</span> <span class="comment-user userinfo">Shwetha4194</span>
</div>
</div>
</div>
<div id="comment-tools-76250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76250-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76254"></span>

<div id="answer-container-76254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76254-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A browser will ask the server for a HTML (content-type) response. Your application is probably requesting either JSON or XML.</p>
<p>When look at the HTTP reponse headers for a JSON request:</p>
<p><code>curl -I -H "Content-Type: application/json" "http://nominatim.openstreetmap.org/search.php?q=london&amp;format=jsonv2"</code></p>
<p><code>HTTP/1.1 301 Moved Permanently</code></p>
<p><code>Location: </code><a href="https://nominatim.openstreetmap.org/search.php?q=london&amp;format=jsonv2"><code>https://nominatim.openstreetmap.org/search.php?q=london&amp;format=jsonv2</code></a></p>
<p>So in your application you should either follow the redirect (many software libraries have options to do that automatically) or replace http: with https:</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '20, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76254" class="comments-container">
&#10;</div>
<div id="comment-tools-76254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76254-form-container" class="comment-form-container">
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

