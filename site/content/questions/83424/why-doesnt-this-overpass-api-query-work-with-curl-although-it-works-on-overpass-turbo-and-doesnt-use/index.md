+++
type = "question"
title = "Why doesn&#x27;t this overpass-api query work with curl although it works on Overpass Turbo and doesn&#x27;t use {{}}?"
description = '''I have a query that works alright in Overpass Turbo, which I can&#x27;t run directly by sending it with curl (it says &quot;Your browser sent a request that this server could not understand.&quot;). As far as I can tell it&#x27;s not using Overpass Turbo&#x27;s extended syntax. The query is meant to get the buildings, shops...'''
date = "2022-02-09T12:55:00Z"
lastmod = "2022-02-13T20:52:00Z"
weight = 83424
keywords = [ "overpass-api" ]
aliases = [ "/questions/83424" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why doesn't this overpass-api query work with curl although it works on Overpass Turbo and doesn't use {{}}?](/questions/83424/why-doesnt-this-overpass-api-query-work-with-curl-although-it-works-on-overpass-turbo-and-doesnt-use)

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
<span id="post-83424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83424-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a query that works alright in Overpass Turbo, which I can't run directly by sending it with curl (it says "Your browser sent a request that this server could not understand."). As far as I can tell it's not using Overpass Turbo's extended syntax.</p>
<p>The query is meant to get the buildings, shops etc, and adjoining streets, along a street.</p>
<p>Here is the query that works only in Overpass Turbo:</p>
<pre><code>area[name=&quot;Bratislava&quot;];
way(area)[name=&quot;Štúrova&quot;]-&gt;.my_street;
(
        nw[amenity](around.my_street:25);
        nwr[building](around.my_street:25);
        wr[highway](around.my_street:25);
);
(._;&gt;;);
out;</code></pre>
<p>and here is the biggest piece of it that I have been able to get working with curl --- it has only one of the original three parts of the "union" construct:</p>
<pre><code>area[name=&quot;Bratislava&quot;];
way[name=&quot;Štúrova&quot;]-&gt;.my_street;
(node[amenity](around.my_street:25););
(._;&gt;;);
out;</code></pre>
<p>Also, I tried some other subsets of the original query, and they ran for a relatively long time and I killed them to avoid excessive server use; the whole thing runs in about 18 seconds under Overpass Turbo.</p>
<p>How can I get this to work under curl (eventually, I will be using it from ClojureScript in a client-side app)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '22, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/b5dde08a01a477fd07768db41e1ed48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HillWithSmallFields&#39;s gravatar image" />
<p><span>HillWithSmal...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HillWithSmallFields has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83424" class="comments-container">
<span id="83425"></span>
<div id="comment-83425" class="comment">
<div id="post-83425-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you show us how you tried to run the curl command? I have a hunch you might have a problem with quoting on the shell command line.</p>
</div>
<div id="comment-83425-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 12:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="83427"></span>
<div id="comment-83427" class="comment">
<div id="post-83427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but I don't think that'll be it. I'm using the command line:</p>
<pre><code>curl --output r1 --get --data @q1 https://overpass-api.de/api/interpreter</code></pre>
<p>and the contents of the file q1 are as follows:</p>
<pre><code>[out:json][timeout:25];
area[name=&quot;Bratislava&quot;];
way(area)[name=&quot;Štúrova&quot;]-&gt;.my_street;
(
        nw[amenity](around.my_street:25);
        nwr[building](around.my_street:25);
        wr[highway](around.my_street:25);
);
(._;&gt;;);
out;</code></pre>
</div>
<div id="comment-83427-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 15:53)</span> <span class="comment-user userinfo">HillWithSmal...</span>
</div>
</div>
<span id="83432"></span>
<div id="comment-83432" class="comment">
<div id="post-83432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a side note, if I remember correctly, killing curl won't stop the request on the server, so you might as well wait for the result.</p>
</div>
<div id="comment-83432-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 18:37)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83435"></span>
<div id="comment-83435" class="comment">
<div id="post-83435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hadn't realized that, thanks. Now I've got the query working with curl, it's taking the same length of time as it does on Overpass Turbo, so there may have been something wrong in the ones that were taking longer.</p>
</div>
<div id="comment-83435-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 18:52)</span> <span class="comment-user userinfo">HillWithSmal...</span>
</div>
</div>
</div>
<div id="comment-tools-83424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83424-form-container" class="comment-form-container">
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

<span id="83428"></span>

<div id="answer-container-83428" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83428-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="HillWithSmallFields has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Remove all indentation whitespace from q1.</p>
<p>PS Unsure if <code>--get</code> is essential. I <em>think</em> it's the default action.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '22, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '22, 16:36</strong> </span></p>
</div>
</div>
<div id="comments-container-83428" class="comments-container">
<span id="83429"></span>
<div id="comment-83429" class="comment">
<div id="post-83429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks --- that fixed it!</p>
<p>I guess Overpass Turbo must be doing that for me.</p>
</div>
<div id="comment-83429-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 16:28)</span> <span class="comment-user userinfo">HillWithSmal...</span>
</div>
</div>
<span id="83433"></span>
<div id="comment-83433" class="comment">
<div id="post-83433-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>According to the manual page on debian, POST is the default action if --data is given.</p>
</div>
<div id="comment-83433-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 18:46)</span> <span class="comment-user userinfo">HillWithSmal...</span>
</div>
</div>
<span id="83466"></span>
<div id="comment-83466" class="comment">
<div id="post-83466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you test something? I added the indents back in &amp; it ran. what results do you get?</p>
</div>
<div id="comment-83466-info" class="comment-info">
<span class="comment-age">(13 Feb '22, 20:52)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-83428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83428-form-container" class="comment-form-container">
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

