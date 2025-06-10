+++
type = "question"
title = "urlencoding the street and address parameters for Nominatim breaks response"
description = '''Not sure what&#x27;s going on, but if I make a request to Nominatim from the browser for this address ( 5145 Beltway Drive, Grand Rapids ) like this then it work fine, but if I do it through php and wrap the city and street details in urlencode, then I get no response. The encoded URL format is this, but...'''
date = "2020-06-08T19:09:00Z"
lastmod = "2020-06-08T20:37:00Z"
weight = 75210
keywords = [ "nominatim" ]
aliases = [ "/questions/75210" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [urlencoding the street and address parameters for Nominatim breaks response](/questions/75210/urlencoding-the-street-and-address-parameters-for-nominatim-breaks-response)

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
<span id="post-75210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75210-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Not sure what's going on, but if I make a request to Nominatim from the browser for this address ( 5145 Beltway Drive, Grand Rapids ) like <a href="https://nominatim.openstreetmap.org/search?street=5145+Beltway+Drive&amp;city=Grand+Rapids&amp;format=json&amp;addressdetails=1&amp;limit=1">this</a> then it work fine, but if I do it through php and wrap the city and street details in <a href="https://www.php.net/manual/en/function.urlencode.php">urlencode</a>, then I get no response.</p>
<p>The encoded URL format is <a href="https://nominatim.openstreetmap.org/search?street%3D5145+Beltway+Drive%26city%3DGrand+Rapids&amp;format=json&amp;addressdetails=1&amp;limit=1">this</a>, but somehow this is not accepted. The http response is 200, so that's not the issue.</p>
<p>Does it simply not accept encoded data? I can't find anything about it in the documentation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '20, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ff0f153759f11353a7e969a7de37f4df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tijmens&#39;s gravatar image" />
<p><span>Tijmens</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tijmens has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75210" class="comments-container">
&#10;</div>
<div id="comment-tools-75210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75210-form-container" class="comment-form-container">
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

<span id="75218"></span>

<div id="answer-container-75218" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75218-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tijmens has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>urlencode</code> of a full URL also encodes <code>=</code> (as <code>%3D</code>) and I think <code>&amp;</code>, too . What you probably want to do is urlencode the values only. E.g.</p>
<pre><code>$street = &#39;5145 Beltway Drive&#39;;
$city = &#39;Grand Rapids&#39;;
$url = &#39;https://nominatim.openstreetmap.org/search?street=&#39;.urlencode($street).&#39;&amp;city=&#39;.urlencode($city).&#39;&amp;format=json&amp;addressdetails=1&amp;limit=1&#39;;</code></pre>
<p>For best results I suggest using the unstructured query format and add the country if possible. jsonv2 format also has a couple of additional field.</p>
<pre><code>$address = $street . &#39;, &#39; . $city . &#39;, USA&#39;;
$url = &#39;https://nominatim.openstreetmap.org/search?q=&#39;.urlencode($address).&#39;&amp;format=jsonv2&amp;addressdetails=1&amp;limit=1&#39;;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '20, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '20, 20:37</strong> </span></p>
</div>
</div>
<div id="comments-container-75218" class="comments-container">
&#10;</div>
<div id="comment-tools-75218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75218-form-container" class="comment-form-container">
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

