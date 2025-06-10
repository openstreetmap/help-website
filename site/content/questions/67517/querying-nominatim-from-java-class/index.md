+++
type = "question"
title = "querying nominatim from Java class"
description = '''Hello, I&#x27;m trying to geocode some addresses querying Nominatim. If I enter one address like https://nominatim.openstreetmap.org/search.php?q=31+muntaner%2C+Barcelona%2C+Spain&amp;amp;polygon_geojson=1&amp;amp;viewbox=&amp;amp;format=xml, any web browser runs OK and I get the results. But when trying to do the s...'''
date = "2019-01-08T21:22:00Z"
lastmod = "2019-01-09T15:55:00Z"
weight = 67517
keywords = [ "java", "nominatim", "geocoding" ]
aliases = [ "/questions/67517" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [querying nominatim from Java class](/questions/67517/querying-nominatim-from-java-class)

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
<span id="post-67517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to geocode some addresses querying Nominatim. If I enter one address like <a href="https://nominatim.openstreetmap.org/search.php?q=31+muntaner%2C+Barcelona%2C+Spain&amp;polygon_geojson=1&amp;viewbox=&amp;format=xml,">https://nominatim.openstreetmap.org/search.php?q=31+muntaner%2C+Barcelona%2C+Spain&amp;polygon_geojson=1&amp;viewbox=&amp;format=xml,</a> any web browser runs OK and I get the results.</p>
<p>But when trying to do the same from a Java class:</p>
<pre><code>URL u;
InputStream is = null;
&#10;u = new URL(&quot;https://nominatim.openstreetmap.org/search.php?q=31+muntaner%2C+Barcelona%2C+Spain&amp;polygon_geojson=1&amp;viewbox=&amp;format=xml&quot;);
&#10;is = u.openStream();</code></pre>
<p>I always get a <code>ConnectionTimedOut</code> exception, and no results given.</p>
<p>Has anyone tried to do something similar with success? The timeout exception could be due to the absence on UsertAgent headers into the request? If so, what UserAgents are valid?</p>
<p>If somebody could post some code to query Nominatim from Java, I will greatly appreciate.</p>
<p>Thanks in advance, Joan.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '19, 21:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1f761fbdd6a47871e98a460450e039e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joan%20Segura&#39;s gravatar image" />
<p><span>Joan Segura</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joan Segura has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '19, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-67517" class="comments-container">
&#10;</div>
<div id="comment-tools-67517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67517-form-container" class="comment-form-container">
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

<span id="67518"></span>

<div id="answer-container-67518" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67518-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Java library likely uses a default user agent string. Set it to something unique. See second requirement on <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '19, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-67518" class="comments-container">
<span id="67520"></span>
<div id="comment-67520" class="comment">
<div id="post-67520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer mtmail.</p>
<p>I'm not using the osmapi from westnordost because when I've copied it into my project appeared a lot of dependencies I hadn't been able to solve. I was trying to open the URL directly.</p>
<p>Best regards. Joan.</p>
</div>
<div id="comment-67520-info" class="comment-info">
<span class="comment-age">(08 Jan '19, 22:20)</span> <span class="comment-user userinfo">Joan Segura</span>
</div>
</div>
</div>
<div id="comment-tools-67518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67518-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67528"></span>

<div id="answer-container-67528" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67528-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>URL openStream does exactly what the name says, it returns an InputStream (over the underlying TCP connection) to the server in question. It doesn't do any of the bits and pieces of the HTTP protocol (which why you are simply seeing timeouts) and except if you want to do that yourself you are using the the wrong classes and methods.</p>
<p>Have a look at <a href="https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html">https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html</a></p>
<p>PS: ~~nowdays you would normally use the OkHttp library but as long as performance is not a concern there is no problem with being old fashioned.~~ OkHttp can no longer be recommended</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '19, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '19, 18:37</strong> </span></p>
</div>
</div>
<div id="comments-container-67528" class="comments-container">
&#10;</div>
<div id="comment-tools-67528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67528-form-container" class="comment-form-container">
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

