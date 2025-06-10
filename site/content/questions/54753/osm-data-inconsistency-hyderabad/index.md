+++
type = "question"
title = ".osm data inconsistency - Hyderabad"
description = '''I was looking at the .osm data for the city of Hyderabad, India. I found that the addr:street key contained full addresses instead of just the street name. for example: k=&quot;addr:street&quot; v=&quot;Akbar Arcade, Auto Sainagar Road, Near Nri Concept School, Vanasthalipuram,&quot;  and not: k=&quot;addr:street&quot; v=&quot;Auto S...'''
date = "2017-02-20T19:27:00Z"
lastmod = "2017-02-24T04:28:00Z"
weight = 54753
keywords = [ "hyderabad", ".osm", "inconsistency" ]
aliases = [ "/questions/54753" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [.osm data inconsistency - Hyderabad](/questions/54753/osm-data-inconsistency-hyderabad)

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
<span id="post-54753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was looking at the .osm data for the city of Hyderabad, India. I found that the <code>addr:street</code> key contained full addresses instead of just the street name.</p>
<p>for example:</p>
<pre><code>k=&quot;addr:street&quot; v=&quot;Akbar Arcade, Auto Sainagar Road, Near Nri Concept School, Vanasthalipuram,&quot;</code></pre>
<p>and not:</p>
<pre><code>k=&quot;addr:street&quot; v=&quot;Auto Sainagar Road&quot;</code></pre>
<p>Shouldn't full addresses be contained in <code>addr:full</code> key and not <code>addr:street</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hyderabad" rel="tag" title="see questions tagged &#39;hyderabad&#39;">hyderabad</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-inconsistency" rel="tag" title="see questions tagged &#39;inconsistency&#39;">inconsistency</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '17, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d061be152de8456bfed5e9e97f7648c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kimidec&#39;s gravatar image" />
<p><span>kimidec</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kimidec has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54753" class="comments-container">
<span id="54789"></span>
<div id="comment-54789" class="comment">
<div id="post-54789-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately things are not always as they <em>should</em> be. I've found tagging errors to be somewhat more common in India than in Canada (the other country I do most of my mapping in), but nowhere is the data perfect.</p>
<p>Feel free to fix things! More people mapping in India would be great, and one of the great things about OSM is that it <em>is</em> possible to fix problems, and fill in missing information.</p>
</div>
<div id="comment-54789-info" class="comment-info">
<span class="comment-age">(24 Feb '17, 03:56)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="54790"></span>
<div id="comment-54790" class="comment">
<div id="post-54790-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>and try to contact the previous mapper, inform him/her friendly about the proper tagging, especially when the one mapper makes the same mistake over and over</p>
</div>
<div id="comment-54790-info" class="comment-info">
<span class="comment-age">(24 Feb '17, 04:28)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-54753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54753-form-container" class="comment-form-container">
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

<span id="54754"></span>

<div id="answer-container-54754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54754-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kimidec has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are correct. I don't have local knowledge, but it looks like it might have the name of a shopping area ("Akbar Arcade") which could go on a building or area polygon, a note ("Near Nri Concept School) and possibly a city/town/village ("Vanasthalipuram") which could go into addr:city=*</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '17, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-54754" class="comments-container">
<span id="54761"></span>
<div id="comment-54761" class="comment">
<div id="post-54761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
<p>Yesterday was my first day exploring Openstreetmap. I read the wiki, however the dataset was replete with the above mentioned errors - hence the doubt. :D</p>
</div>
<div id="comment-54761-info" class="comment-info">
<span class="comment-age">(21 Feb '17, 12:49)</span> <span class="comment-user userinfo">kimidec</span>
</div>
</div>
</div>
<div id="comment-tools-54754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54754-form-container" class="comment-form-container">
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

