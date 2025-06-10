+++
type = "question"
title = "Why does Nominatim return an error for queries from Internet Explorer?"
description = '''I am doing a request using jQuery: $.get(&quot;http://nominatim.openstreetmap.org/search?q=&quot; +  searchValue + &quot;&amp;amp;accept-language=hebformat=json&amp;amp;polygon=&#x27;true&#x27;&quot;,  {}, function (data)  where searchValue is the text string which I want to search for.  With Firefox this works perfectly and I am gettin...'''
date = "2010-08-31T15:29:00Z"
lastmod = "2010-08-31T16:50:00Z"
weight = 722
keywords = [ "nominatim", "javascript" ]
aliases = [ "/questions/722" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does Nominatim return an error for queries from Internet Explorer?](/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer)

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
<span id="post-722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-722-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am doing a request using jQuery:</p>
<pre><code>$.get(&quot;http://nominatim.openstreetmap.org/search?q=&quot; +
      searchValue + &quot;&amp;accept-language=hebformat=json&amp;polygon=&#39;true&#39;&quot;,
      {}, function (data)</code></pre>
<p>where searchValue is the text string which I want to search for.</p>
<p>With Firefox this works perfectly and I am getting a JSON result and everything running smoothly. My application is nearly finished and I decided to run this on IE but I found that the request takes a lot of time and instead of getting a JSON result I get an error back.</p>
<p>What I can about this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '10, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f8352b4d4740acbbebfff62191fc4f98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ItayEng&#39;s gravatar image" />
<p><span>ItayEng</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ItayEng has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>31 Aug '10, 17:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span></p>
</div>
</div>
<div id="comments-container-722" class="comments-container">
&#10;</div>
<div id="comment-tools-722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-722-form-container" class="comment-form-container">
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

<span id="723"></span>

<div id="answer-container-723" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-723-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ItayEng has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim expects parameters to be UTF-8 encoded and generates errors if the encoding is invalid.</p>
<p>Firefox correctly encodes parameters using UTF-8 encoding by default, but Internet Explorer doesn't, so you will need to explicitly encode it using the encodeURIComponent function. This will also work in Firefox and should work in other browsers.</p>
<pre><code>$.get(&quot;http://nominatim.openstreetmap.org/search?q=&quot; +
      encodeURIComponent(searchValue) + 
      &quot;&amp;accept-language=he&amp;format=json&amp;polygon=1&quot;,
      {}, function (data){});</code></pre>
<p>You should also ensure that your page uses a UTF-8 encoding so that results can be properly displayed. This can be done by adding using a suitable meta tag in your &lt;head&gt; block:</p>
<pre><code>&lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '10, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-723" class="comments-container">
&#10;</div>
<div id="comment-tools-723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-723-form-container" class="comment-form-container">
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

