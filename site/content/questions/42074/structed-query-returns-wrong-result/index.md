+++
type = "question"
title = "Structed Query returns wrong result"
description = '''Hi, when I search for the city &quot;München&quot; in Germany, the web service returns not the correct city by using: http://nominatim.openstreetmap.org/search.php?format=xml&amp;amp;addressdetails=1&amp;amp;limit=1&amp;amp;polygon=0&amp;amp;countrycodes=de&amp;amp;city=M%C3%BCnchen  Otherwise by using query string, the web serv...'''
date = "2015-03-31T16:15:00Z"
lastmod = "2015-04-09T01:34:00Z"
weight = 42074
keywords = [ "nominatim" ]
aliases = [ "/questions/42074" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Structed Query returns wrong result](/questions/42074/structed-query-returns-wrong-result)

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
<span id="post-42074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42074-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, when I search for the city "München" in Germany, the web service returns not the correct city by using: <a href="http://nominatim.openstreetmap.org/search.php?format=xml&amp;addressdetails=1&amp;limit=1&amp;polygon=0&amp;countrycodes=de&amp;city=M%C3%BCnchen">http://nominatim.openstreetmap.org/search.php?format=xml&amp;addressdetails=1&amp;limit=1&amp;polygon=0&amp;countrycodes=de&amp;city=M%C3%BCnchen</a></p>
<p>Otherwise by using query string, the web service return the correct city <a href="http://nominatim.openstreetmap.org/search.php?format=xml&amp;addressdetails=1&amp;limit=1&amp;polygon=0&amp;q=de,M%C3%BCnchen">http://nominatim.openstreetmap.org/search.php?format=xml&amp;addressdetails=1&amp;limit=1&amp;polygon=0&amp;q=de,M%C3%BCnchen</a></p>
<p>Any suggestion why and/or how I can fix the it?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '15, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a1330cd569d65db6ee7a4dad84d5da3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jppond&#39;s gravatar image" />
<p><span>jppond</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jppond has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '15, 16:17</strong> </span></p>
</div>
</div>
<div id="comments-container-42074" class="comments-container">
<span id="42075"></span>
<div id="comment-42075" class="comment">
<div id="post-42075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe because München is both a city and a <a href="http://nominatim.openstreetmap.org/search.php?format=xml&amp;addressdetails=1&amp;limit=1&amp;polygon=0&amp;countrycodes=de&amp;county=M%C3%BCnchen">county</a>? Still sounds like a bug to me.</p>
</div>
<div id="comment-42075-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 16:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42079"></span>
<div id="comment-42079" class="comment">
<div id="post-42079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If nobody has any ideas, I will report this as a bug.</p>
</div>
<div id="comment-42079-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 18:32)</span> <span class="comment-user userinfo">jppond</span>
</div>
</div>
<span id="42226"></span>
<div id="comment-42226" class="comment">
<div id="post-42226-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>… now there: <a href="https://trac.openstreetmap.org/ticket/5300">https://trac.openstreetmap.org/ticket/5300</a> (please always mention such crosslinks at the new AND old location)</p>
</div>
<div id="comment-42226-info" class="comment-info">
<span class="comment-age">(09 Apr '15, 01:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42074-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

