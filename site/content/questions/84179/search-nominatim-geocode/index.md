+++
type = "question"
title = "search nominatim geocode"
description = '''I installed Nominatim locally in my machine, the serve is running perfectly. I can make requests from my browser with &quot;http://localhost:8088/search.php?q=Example&quot; and it returns well, but when i try to use it in a python code i have a problem, the request comes as search?q=Example and not search.php...'''
date = "2022-04-14T04:49:00Z"
lastmod = "2022-04-14T08:33:00Z"
weight = 84179
keywords = [ "search", "geocode", "nominatim" ]
aliases = [ "/questions/84179" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [search nominatim geocode](/questions/84179/search-nominatim-geocode)

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
<span id="post-84179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed Nominatim locally in my machine, the serve is running perfectly. I can make requests from my browser with "http://localhost:8088/search.php?q=Example" and it returns well, but when i try to use it in a python code i have a problem, the request comes as search?q=Example and not search.php?q=Example so the serve cant complete the request.</p>
<p>My code:</p>
<p>from geopy.geocoders import Nominatim</p>
<p>geolocator = Nominatim(domain='localhost:8088', scheme='http')</p>
<p>location = geolocator.geocode('Rua Peru Indaiatuba SP')</p>
<p>Serve response:</p>
<p>[404]: GET /search?q=Rua+Peru+Indaiatuba+SP&amp;format=json&amp;limit=1%20-%20No%20such%20file%20or%20directory - No such file or directory</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-geocode" rel="tag" title="see questions tagged &#39;geocode&#39;">geocode</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '22, 04:49</strong></p>
<img src="https://secure.gravatar.com/avatar/58d888fa3a89f97b981fed4f5efa1609?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guilherme%20Gon%C3%A7alves%20Horta&#39;s gravatar image" />
<p><span>Guilherme Go...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guilherme Gonçalves Horta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '22, 05:00</strong> </span></p>
</div>
</div>
<div id="comments-container-84179" class="comments-container">
<span id="84180"></span>
<div id="comment-84180" class="comment">
<div id="post-84180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do you deploy Nominatim? Do you use Apache or nginx?</p>
</div>
<div id="comment-84180-info" class="comment-info">
<span class="comment-age">(14 Apr '22, 08:33)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-84179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84179-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

