+++
type = "question"
title = "Nominatim search failed in local installation"
description = '''Hi, I have Nominatim with the Spanish data set install in local. I have a server with Debian Squeeze 7 and a Ubuntu 14.04.2 desktop version. I can not make search working. The map is shown perfeclty and when I click on the search button it fails saying: Nominatim has encountered an error with your r...'''
date = "2015-05-14T14:08:00Z"
lastmod = "2015-05-21T09:58:00Z"
weight = 43078
keywords = [ "failed", "search", "nominatim" ]
aliases = [ "/questions/43078" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim search failed in local installation](/questions/43078/nominatim-search-failed-in-local-installation)

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
<span id="post-43078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43078-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have Nominatim with the Spanish data set install in local. I have a server with Debian Squeeze 7 and a Ubuntu 14.04.2 desktop version. I can not make search working. The map is shown perfeclty and when I click on the search button it fails saying:</p>
<pre><code>Nominatim has encountered an error with your request.
Details: Illegal query string (not an UTF-8 string): albacete</code></pre>
<p>The URL request is:</p>
<pre><code>http://my_server_ip/nominatim/search.php?q=albacete&amp;viewbox=-168.76%2C63.71%2C168.76%2C-63.71</code></pre>
<p>I already did tehe instalation in another server with ubuntu server but I do not know why it is failing in this two cases.</p>
<p>Any help? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '15, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff71fc907067296fbfac86e637faa50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanma%20MR&#39;s gravatar image" />
<p><span>Juanma MR</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanma MR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43078" class="comments-container">
<span id="43098"></span>
<div id="comment-43098" class="comment">
<div id="post-43098-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Run the query with the additional URL parameter debug=1. It should give you more detailed information on the data base error that is the root of the problem.</p>
</div>
<div id="comment-43098-info" class="comment-info">
<span class="comment-age">(17 May '15, 22:35)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="43140"></span>
<div id="comment-43140" class="comment">
<div id="post-43140-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, your sugestion gave me the key. I have different instalations and migrating database from one to another missed some functions from nominatim. Your solution pointed directly to the problem. The message thrown without debug was confusing and missleading.</p>
</div>
<div id="comment-43140-info" class="comment-info">
<span class="comment-age">(21 May '15, 09:58)</span> <span class="comment-user userinfo">Juanma MR</span>
</div>
</div>
</div>
<div id="comment-tools-43078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43078-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

