+++
type = "question"
title = "How do i extract osm_type from Nominatim result using PHP?"
description = '''Using a basic reverse geocode request like:   http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;amp;lat=-22.77175&amp;amp;lon=-50.211006  how do i extract the osm_type from the result using PHP?'''
date = "2013-11-12T21:39:00Z"
lastmod = "2013-11-12T21:53:00Z"
weight = 28014
keywords = [ "osm_type", "php", "osm", "nominatim" ]
aliases = [ "/questions/28014" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i extract osm_type from Nominatim result using PHP?](/questions/28014/how-do-i-extract-osm_type-from-nominatim-result-using-php)

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
<span id="post-28014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28014-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using a basic reverse geocode request like:</p>
<blockquote>
<p><a href="http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;lat=-22.77175&amp;lon=-50.211006">http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;lat=-22.77175&amp;lon=-50.211006</a></p>
</blockquote>
<p>how do i extract the osm_type from the result using PHP?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm_type" rel="tag" title="see questions tagged &#39;osm_type&#39;">osm_type</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '13, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/dde3251e03f13e55e9221fc11dd29590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonygil&#39;s gravatar image" />
<p><span>tonygil</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonygil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28014" class="comments-container">
&#10;</div>
<div id="comment-tools-28014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28014-form-container" class="comment-form-container">
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

<span id="28016"></span>

<div id="answer-container-28016" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28016-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>using php</p>
<pre><code>$feedUrl = &#39;http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;lat=-22.77175&amp;lon=-50.211006&#39;;
$rawFeed = file_get_contents($feedUrl);
$xml = new SimpleXmlElement($rawFeed);
&#10;foreach($xml-&gt;result as $result){
        $roadType = $result[&#39;osm_type&#39;];
        $osmId = $result[&#39;osm_id&#39;];
&#10;        echo &quot;Type: $roadType Id: $osmId&lt;br&gt;&quot;;
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '13, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/dde3251e03f13e55e9221fc11dd29590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonygil&#39;s gravatar image" />
<p><span>tonygil</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonygil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28016" class="comments-container">
&#10;</div>
<div id="comment-tools-28016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28016-form-container" class="comment-form-container">
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

