+++
type = "question"
title = "Local Nominatim sometimes returns no results"
description = '''Hello, I followed these instructions to install Nominatim on a local server: https://wiki.openstreetmap.org/wiki/Nominatim/Installation  I used the stable version 2.4.0 I added the optional data from Wikipedia and Postcodes added the special phrases after the import was done  The planet import was do...'''
date = "2015-12-15T13:51:00Z"
lastmod = "2015-12-15T13:51:00Z"
weight = 47165
keywords = [ "nominatim", "local", "results" ]
aliases = [ "/questions/47165" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Local Nominatim sometimes returns no results](/questions/47165/local-nominatim-sometimes-returns-no-results)

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
<span id="post-47165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47165-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I followed these instructions to install Nominatim on a local server: <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
<ul>
<li>I used the stable version 2.4.0</li>
<li>I added the optional data from Wikipedia and Postcodes</li>
<li>added the special phrases after the import was done</li>
</ul>
<p>The planet import was done after 3 days and most queries return results. However for some addresses I get no results at all. The official Nominatim server returns results for the same addresses. What is wrong with my server? How can I get the same results as the official Nominatim server? Did I miss something in the import?</p>
<p>Here are some examples:</p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/search/?q=7%20Rue%20Madeleine%20Br%C3%A8s%2025000%20Besan%C3%A7on&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/search/?q=7%20Rue%20Madeleine%20Br%C3%A8s%2025000%20Besan%C3%A7on&amp;format=json&amp;addressdetails=1</a></li>
<li><a href="http://192.168.2.93/nominatim/search?q=7%20Rue%20Madeleine%20Br%C3%A8s%2025000%20Besan%C3%A7on&amp;format=json&amp;addressdetails=1">http://192.168.2.93/nominatim/search?q=7%20Rue%20Madeleine%20Br%C3%A8s%2025000%20Besan%C3%A7on&amp;format=json&amp;addressdetails=1</a></li>
<li><a href="http://nominatim.openstreetmap.org/search/?q=Rue%20de%20Logelbach%2068920%20Wintzenheim&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/search/?q=Rue%20de%20Logelbach%2068920%20Wintzenheim&amp;format=json&amp;addressdetails=1</a></li>
<li><a href="http://192.168.2.93/nominatim/search?q=Rue%20de%20Logelbach%2068920%20Wintzenheim&amp;format=json&amp;addressdetails=1">http://192.168.2.93/nominatim/search?q=Rue%20de%20Logelbach%2068920%20Wintzenheim&amp;format=json&amp;addressdetails=1</a></li>
</ul>
<p>I checked if the place is in my database with the osmid <a href="http://nominatim.openstreetmap.org/details?osmid=52517028&amp;osmtype=W">http://nominatim.openstreetmap.org/details?osmid=52517028&amp;osmtype=W</a> &amp; <a href="http://192.168.2.93/nominatim/details?osmid=52517028&amp;osmtype=W">http://192.168.2.93/nominatim/details?osmid=52517028&amp;osmtype=W</a> both have the place. So it should be there, right? But on my server the geocoder gives no results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-results" rel="tag" title="see questions tagged &#39;results&#39;">results</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '15, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/2b2c4fde9361e348907f0386c3f64197?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicole_&#39;s gravatar image" />
<p><span>Nicole_</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicole_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47165" class="comments-container">
&#10;</div>
<div id="comment-tools-47165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47165-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

