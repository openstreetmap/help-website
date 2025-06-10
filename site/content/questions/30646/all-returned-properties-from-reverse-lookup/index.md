+++
type = "question"
title = "All returned properties from reverse lookup."
description = '''I am currently looping through all returned properties and writing them to a DB with the key as row name and the value as the rows value. However, it seems that every time I use it in a new area there are new properties appearing, which means my db table does not have a row for them: &quot;address&quot;: { &quot;s...'''
date = "2014-02-11T15:20:00Z"
lastmod = "2014-02-12T17:14:00Z"
weight = 30646
keywords = [ "geolocation", "reversegeocoding", "reverse" ]
aliases = [ "/questions/30646" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [All returned properties from reverse lookup.](/questions/30646/all-returned-properties-from-reverse-lookup)

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
<span id="post-30646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30646-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently looping through all <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=48.2074764&amp;lon=16.3871043&amp;zoom=18">returned properties</a> and writing them to a DB with the <code>key</code> as row name and the value as the rows value.</p>
<p>However, it seems that every time I use it in a new area there are new properties appearing, which means my db table does not have a row for them:</p>
<pre><code>&quot;address&quot;: {
&quot;supermarket&quot;: &quot;Billa&quot;,
&quot;road&quot;: &quot;Marxergasse&quot;,
&quot;suburb&quot;: &quot;Erdberg&quot;,
&quot;city_district&quot;: &quot;Landstra\u00dfe&quot;,
&quot;city&quot;: &quot;Gemeinde Wien&quot;,
&quot;county&quot;: &quot;W&quot;,
&quot;state&quot;: &quot;Vienna&quot;,
&quot;postcode&quot;: &quot;1030&quot;,
&quot;country&quot;: &quot;Austria&quot;,
&quot;country_code&quot;: &quot;at&quot;</code></pre>
<p>}</p>
<p>So, is there in the documentation a place where I might find all of the possible properties? Tried looking but couldn't find anything sadly.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '14, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e57ddb14f23a80ca2de80331039a037e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hutber&#39;s gravatar image" />
<p><span>hutber</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hutber has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '14, 15:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-30646" class="comments-container">
&#10;</div>
<div id="comment-tools-30646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30646-form-container" class="comment-form-container">
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

<span id="30687"></span>

<div id="answer-container-30687" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30687-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently there is no documentation about these properties as far as I can tell. You have to look at the <a href="https://github.com/twain47/Nominatim">source code</a> instead. I <em>guess</em>(!) these properties originate somehow from <a href="https://github.com/twain47/Nominatim/blob/master/lib/lib.php">lib/lib.php</a> but I don't know any details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30687" class="comments-container">
&#10;</div>
<div id="comment-tools-30687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30687-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30684"></span>

<div id="answer-container-30684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you have a look at the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Map_Features">Map Features</a> ?</p>
<p>And <a href="http://wiki.openstreetmap.org/wiki/Taginfo">Taginfo</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-30684" class="comments-container">
<span id="30686"></span>
<div id="comment-30686" class="comment">
<div id="post-30686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>These aren't the usual OSM tags but Nominatim's own key-value pairs. Map Features or taginfo doesn't help.</p>
</div>
<div id="comment-30686-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 17:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30684-form-container" class="comment-form-container">
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

