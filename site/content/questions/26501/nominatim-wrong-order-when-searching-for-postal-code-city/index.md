+++
type = "question"
title = "Nominatim wrong order when searching for postal code + city"
description = '''Hello, I got a tool that detects longitude and latitude of specific cities with postal code + city name in the query. I took the first place that is returned automatically, because there are many requests I had to do one time for our database. Unfortunately, when I search for München in Germany, the...'''
date = "2013-09-19T14:19:00Z"
lastmod = "2013-09-23T07:45:00Z"
weight = 26501
keywords = [ "nominatim" ]
aliases = [ "/questions/26501" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim wrong order when searching for postal code + city](/questions/26501/nominatim-wrong-order-when-searching-for-postal-code-city)

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
<span id="post-26501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I got a tool that detects longitude and latitude of specific cities with postal code + city name in the query. I took the first place that is returned automatically, because there are many requests I had to do one time for our database.</p>
<p>Unfortunately, when I search for München in Germany, the first result is not the correct city, even when I request it with the right postal code and the first result got another postal code:</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=81660+M%C3%BCnchen+DE&amp;format=xml&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=81660+M%C3%BCnchen+DE&amp;format=xml&amp;addressdetails=1</a></p>
<p>Can anybody provide me any solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '13, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ebe2c85736d8bb23673d4e015c71ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="modiX&#39;s gravatar image" />
<p><span>modiX</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="modiX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26501" class="comments-container">
&#10;</div>
<div id="comment-tools-26501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26501-form-container" class="comment-form-container">
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

<span id="26502"></span>

<div id="answer-container-26502" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26502-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="modiX has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you know that you are looking for a postcode + city, it is better to use structured requests (see <a href="https://wiki.openstreetmap.org/wiki/Nominatim">search parameters in the Nominatim docs</a> for details). So your example should be:</p>
<p><a href="http://nominatim.openstreetmap.org/search?postalcode=81660&amp;city=M%C3%BCnchen&amp;country=de&amp;format=xml&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?postalcode=81660&amp;city=M%C3%BCnchen&amp;country=de&amp;format=xml&amp;addressdetails=1</a></p>
<p>Although this specific postcode seems to be missing in OSM, so the query does not give any results at all. A word of warning at this point: support for postcodes in Nominatim is very rudimentary still, so results should always be taken with a grain of salt.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '13, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-26502" class="comments-container">
<span id="26543"></span>
<div id="comment-26543" class="comment">
<div id="post-26543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wished this would solve my problem :/</p>
</div>
<div id="comment-26543-info" class="comment-info">
<span class="comment-age">(20 Sep '13, 11:46)</span> <span class="comment-user userinfo">modiX</span>
</div>
</div>
<span id="26614"></span>
<div id="comment-26614" class="comment">
<div id="post-26614-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>hey modiX,</p>
<p>Please check your postalcode: 81660 is NOT a geographical postalcode in Germany. It is more a Postalcode for big institutions like companies, banks or authorities inside Germany, a so called "Großkunden-Postleitzahl" in German.</p>
<p>Thus you can address an institution without mentioneing a street name.</p>
<p>These special postalcodes should NOT be stored in OSM. So you will not find it there. Please retry with a postalcode that covers a kind of area like a suburb of Munich or similar.</p>
</div>
<div id="comment-26614-info" class="comment-info">
<span class="comment-age">(22 Sep '13, 10:32)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26631"></span>
<div id="comment-26631" class="comment">
<div id="post-26631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are right, thanks. the real postal code 81671 results the correct München in Bayern at both cases (full query and OSM). So my only work-around would be to replace the industry postal code with the geographic postal code. Unfortunately I cannot find any list in the web, but this is another problem case. Thanks so much! :)</p>
</div>
<div id="comment-26631-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 07:45)</span> <span class="comment-user userinfo">modiX</span>
</div>
</div>
</div>
<div id="comment-tools-26502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26502-form-container" class="comment-form-container">
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

