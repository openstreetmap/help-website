+++
type = "question"
title = "nominatim file_get_contents php"
description = '''Hi, Does file_get_contents require api key? Currently the below statement doesnt work from PHP. $json= file_get_contents(&quot;https://nominatim.openstreetmap.org/search?q=&quot;.$address.&quot;&amp;amp;format=json&amp;amp;polygon=1&amp;amp;addressdetails=1&quot;); I could use file_get_contents with other geocode api. What could b...'''
date = "2020-11-30T07:06:00Z"
lastmod = "2020-11-30T13:40:00Z"
weight = 77788
keywords = [ "nominatim", "php" ]
aliases = [ "/questions/77788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim file_get_contents php](/questions/77788/nominatim-file_get_contents-php)

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
<span id="post-77788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77788-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Does file_get_contents require api key?</p>
<p>Currently the below statement doesnt work from PHP.</p>
<p>$json= file_get_contents("https://nominatim.openstreetmap.org/search?q=".$address."&amp;format=json&amp;polygon=1&amp;addressdetails=1");</p>
<p>I could use file_get_contents with other geocode api.</p>
<p>What could be the problem? with nominatim Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '20, 07:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b3db659dcfa917f68405b65e3642f239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="migandhi&#39;s gravatar image" />
<p><span>migandhi</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="migandhi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77788" class="comments-container">
&#10;</div>
<div id="comment-tools-77788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77788-form-container" class="comment-form-container">
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

<span id="77791"></span>

<div id="answer-container-77791" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77791-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>file_get_contents can open a file or a URL. For a URL the setting <code>allow_url_fopen</code> needs to be enabled on your system. I think that's enabled by default, but doublecheck. See <a href="https://www.php.net/manual/en/filesystem.configuration.php#ini.allow-url-fopen">https://www.php.net/manual/en/filesystem.configuration.php#ini.allow-url-fopen</a></p>
<p>Make sure you're sending the HTTP UserAgent or Referer as required by <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> , see <a href="https://help.openstreetmap.org/questions/59788/calling-nominatim-with-file_get_contents">https://help.openstreetmap.org/questions/59788/calling-nominatim-with-file_get_contents</a></p>
<p><code>$address</code> might contain special characters or spaces, the value needs to be URI encoded, see <a href="https://www.php.net/manual/en/function.urlencode.php">https://www.php.net/manual/en/function.urlencode.php</a></p>
<p><code>&amp;polygon=1</code> still works but is deprecated, instead specify which format the polygon would have, see <a href="https://nominatim.org/release-docs/latest/api/Search/#polygon-output">https://nominatim.org/release-docs/latest/api/Search/#polygon-output</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-77791" class="comments-container">
<span id="77794"></span>
<div id="comment-77794" class="comment">
<div id="post-77794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Thanks,</p>
<p>I saw all the links,</p>
<p>The below link has information that email address is required.</p>
<p><a href="https://help.openstreetmap.org/questions/59788/calling-nominatim-with-file_get_contents/65036">https://help.openstreetmap.org/questions/59788/calling-nominatim-with-file_get_contents/65036</a></p>
<p>This worked for me.</p>
<p>Regards.</p>
</div>
<div id="comment-77794-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 13:40)</span> <span class="comment-user userinfo">migandhi</span>
</div>
</div>
</div>
<div id="comment-tools-77791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77791-form-container" class="comment-form-container">
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

