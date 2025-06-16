+++
type = "question"
title = "Union 2 or more queries to one"
description = '''Helo, I Have this query area[&quot;name&quot;=&quot;London&quot;]; node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&amp;gt;.all; ( .all; - ._;); (._;); out;  but for less queries to overpass server i want to join more categories to one query, I think this should be like this node(area)[&quot;amenity&quot;=&quot;bar&quot; || &quot;amenity&quot;=&quot;restaurant&quot;]-&amp;gt;.all;  but...'''
date = "2018-01-25T14:12:00Z"
lastmod = "2018-11-08T12:56:00Z"
weight = 61806
keywords = [ "union", "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/61806" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Union 2 or more queries to one](/questions/61806/union-2-or-more-queries-to-one)

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
<span id="post-61806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Helo, I Have this query</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;];
node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&gt;.all;
( .all; - ._;);
(._;);
out;</code></pre>
<p>but for less queries to overpass server i want to join more categories to one query, I think this should be like this</p>
<pre><code>node(area)[&quot;amenity&quot;=&quot;bar&quot; || &quot;amenity&quot;=&quot;restaurant&quot;]-&gt;.all;</code></pre>
<p>but i have error there.</p>
<p>can you please show me true syntax for getting both categories?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-union" rel="tag" title="see questions tagged &#39;union&#39;">union</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '18, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '18, 21:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61806" class="comments-container">
&#10;</div>
<div id="comment-tools-61806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61806-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="61808"></span>

<div id="answer-container-61808" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61808-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct syntax is</p>
<blockquote>
<p>node["amenity"~"hotel|restaurant"]({{bbox}});</p>
</blockquote>
<p>This is an <a href="http://overpass-turbo.eu/s/vnd">example query</a></p>
<p>more info on the syntax can be found in the Overpass documentation on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#One_or_another_name">One or the other name</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '18, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61808" class="comments-container">
&#10;</div>
<div id="comment-tools-61808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61808-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61807"></span>

<div id="answer-container-61807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should write this:</p>
<pre><code>[&quot;amenity&quot;~&quot;bar|restaurant&quot;]</code></pre>
<p>instead of:</p>
<pre><code>[&quot;amenity&quot;=&quot;bar&quot; || &quot;amenity&quot;=&quot;restaurant&quot;]</code></pre>
<p>If you want to add more, like fast_food, pub, cafe, etc, you can do it easily:</p>
<pre><code>[&quot;amenity&quot;~&quot;bar|restaurant|fast_food|pub|cafe&quot;]</code></pre>
<p>You have infinite other possibilities using regular expressions in overpass...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '18, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '18, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-61807" class="comments-container">
<span id="61814"></span>
<div id="comment-61814" class="comment">
<div id="post-61814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for anwser, this is works well, but in case if i should get one form amenity and another from shop?</p>
<p>["amenity"="bar" || "shop"="supermarket"] ...</p>
<p>?</p>
</div>
<div id="comment-61814-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 07:18)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61817"></span>
<div id="comment-61817" class="comment">
<div id="post-61817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In that case, you better separate the queries and then union them:</p>
<p>area["name"="London"];</p>
<p>node(area)["amenity"~"bar|restaurant"]-&gt;.amenities;</p>
<p>node(area)["shop"~"supermarket|clothes"]-&gt;.shops;</p>
<p>(</p>
<p>.amenities;</p>
<p>.shops;</p>
<p>)-&gt;.all;</p>
<p>( .all; - ._;);</p>
<p>(._;);</p>
<p>out;</p>
</div>
<div id="comment-61817-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 10:55)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
<span id="61818"></span>
<div id="comment-61818" class="comment">
<div id="post-61818-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would also change "London" by "Greater London" to avoid getting some nodes in North America, that you probably don't want: <a href="http://overpass-turbo.eu/s/voH">http://overpass-turbo.eu/s/voH</a></p>
<p>Or you could use the relation code instead: <a href="http://overpass-turbo.eu/s/voG">http://overpass-turbo.eu/s/voG</a></p>
</div>
<div id="comment-61818-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 11:01)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
<span id="61820"></span>
<div id="comment-61820" class="comment">
<div id="post-61820-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3339/edvac"></a><a href="https://help.openstreetmap.org/users/3339/edvac">@edvac</a> thanks a lot for your quick and good answer, this is great solution for me, thanks again. I have one another question but don't want add to this topic. If you can, please see this question also <a href="/questions/61819/how-get-all-ways-without-nd-tags">https://help.openstreetmap.org/questions/61819/how-get-all-ways-without-nd-tags</a></p>
</div>
<div id="comment-61820-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 14:30)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61824"></span>
<div id="comment-61824" class="comment">
<div id="post-61824-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are welcome ;)</p>
<p>I gave you an answer to that new query. Hope it is what you want...</p>
</div>
<div id="comment-61824-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 15:09)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
</div>
<div id="comment-tools-61807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61809"></span>

<div id="answer-container-61809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61809-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-61809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An alternative to the regex solution given in the other answers is to use the union operator, which is specified by grouping queries inside of parentheses:</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;];
(
node(area)[&quot;amenity&quot;=&quot;bar&quot;];
node(area)[&quot;amenity&quot;=&quot;restaurant&quot;];
);
out;</code></pre>
<p>This will likely be clearer if the query involves several different keys.</p>
<p>The output of the union can also be saved in a named set:</p>
<pre><code>(
node(area)[&quot;amenity&quot;=&quot;bar&quot;];
node(area)[&quot;amenity&quot;=&quot;restaurant&quot;];
)-&gt;.all;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '18, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-61809" class="comments-container">
<span id="61813"></span>
<div id="comment-61813" class="comment">
<div id="post-61813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for answer,</p>
<p>but when i trying to get bars and restaurants with this query</p>
<p>area["name"="London"];</p>
<p>( node(area)["amenity"="bar"]; node(area)["amenity"="restaurant"]; )-&gt;.all;</p>
<p>( .all; - .<em>; ); (.</em>;&gt;;);</p>
<p>out;</p>
<p>i see in results ONLY bars....</p>
<p>where is my mistake?</p>
</div>
<div id="comment-61813-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 07:16)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="66724"></span>
<div id="comment-66724" class="comment">
<div id="post-66724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to name the area and then reference the name, see <a href="https://help.openstreetmap.org/answer_link/48795/">https://help.openstreetmap.org/answer_link/48795/</a></p>
</div>
<div id="comment-66724-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 12:56)</span> <span class="comment-user userinfo">reubot</span>
</div>
</div>
</div>
<div id="comment-tools-61809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61809-form-container" class="comment-form-container">
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

