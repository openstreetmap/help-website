+++
type = "question"
title = "Overpass query for a name with different possible keys/tags/features"
description = '''Hello, with overpasss-turbo I want to query different names. Problem is: I don&#x27;t know exactly which key/tag/feature the name has (I mean that I don&#x27;t know if it&#x27;s the name of a &quot;natural:peak&quot; or a &quot;natural:glacier&quot; or a &quot;place:region&quot; etc). But what I know is, that not all keys/tags/features should ...'''
date = "2020-02-19T15:52:00Z"
lastmod = "2020-02-20T10:34:00Z"
weight = 73145
keywords = [ "overpass", "name", "key", "query" ]
aliases = [ "/questions/73145" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass query for a name with different possible keys/tags/features](/questions/73145/overpass-query-for-a-name-with-different-possible-keystagsfeatures)

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
<span id="post-73145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73145-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, with overpasss-turbo I want to query different names. Problem is: I don't know exactly which key/tag/feature the name has (I mean that I don't know if it's the name of a "natural:peak" or a "natural:glacier" or a "place:region" etc). But what I know is, that not all keys/tags/features should be searched (for example I know that it's not the name of a building, a bus stop or a highway). I figured out how to query a name e.g. as peak or glacier, as both are natural features:</p>
<pre><code>nwr[name~&quot;Dreitorspitze&quot;][natural~&quot;peak|glacier&quot;];
out geom;</code></pre>
<p>But how can I query a name for example in region and peak? I tried different versions of concatenating these expression together according to the expression above with "|" like e.g.:</p>
<pre><code>nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][[natural~&quot;peak|glacier&quot;]|[place=&quot;region&quot;]];
out geom;</code></pre>
<p>But this doesn't work (obviously). Is there a way to concatenate different keys/tags/features as expression together? Or do I really need to ask each name for each key individually like:</p>
<pre><code>nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][natural~&quot;peak|glacier&quot;];
out geom;
nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][place=&quot;region&quot;];
out geom;
nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][boundary=&quot;administrative&quot;];
out geom;</code></pre>
<p>Thank you very much in advance for all your help :-)</p>
<p>Best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '20, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/b68d7eda3b2603d5e1c188e524f2f004?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="4Kala&#39;s gravatar image" />
<p><span>4Kala</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="4Kala has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '20, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-73145" class="comments-container">
&#10;</div>
<div id="comment-tools-73145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73145-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="73146"></span>

<div id="answer-container-73146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73146-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the union of several queries at once, you can group the query statements inside parentheses like this:</p>
<pre><code>(
 nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][natural~&quot;peak|glacier&quot;];
 nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][place=region];
 nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][boundary=administrative];
);
out geom;</code></pre>
<p>Another useful technique is to specify only the key and not the value, like this:</p>
<pre><code>nwr[name~&quot;Dreitorspitze&quot;][natural];
out geom;</code></pre>
<p>This will return anything tagged with <strong><code>natural</code></strong> whose name contains "Dreitorspitze", in particular it finds <a href="https://www.openstreetmap.org/way/718323342">https://www.openstreetmap.org/way/718323342</a> which is <strong><code>natural=bare_rock</code></strong>.</p>
<p>You can also search just by name without any additional tags:</p>
<pre><code>nwr[name~&quot;Dreitorspitze&quot;];
out geom;</code></pre>
<p>But you might end up finding, for example, a restaurant whose name contains "Dreitorspitze" (though it doesn't appear any such restaurant is currently on the map.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '20, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '20, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-73146" class="comments-container">
&#10;</div>
<div id="comment-tools-73146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73152"></span>

<div id="answer-container-73152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73152-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To apply 2 sets of conditions, use a named set for the output of the first set of features:</p>
<p><a href="http://overpass-turbo.eu/s/QSl">http://overpass-turbo.eu/s/QSl</a></p>
<pre><code>[bbox:{{bbox}}];
(
  nwr[highway];
  nwr[waterway];
 ) -&gt; .byfeature;
&#10; (
   nwr.byfeature[name=&quot;West Elizabeth Street&quot;];
  nwr.byfeature[name=&quot;Pleasant Valley and Lake Canal&quot;];
  );
out geom;</code></pre>
<p>You probably want to go in the other direction, querying by name and then filtering on feature, but that should work fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '20, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-73152" class="comments-container">
&#10;</div>
<div id="comment-tools-73152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73158"></span>

<div id="answer-container-73158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73158-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please consult <a href="https://dev.overpass-api.de/overpass-doc/en/criteria/per_tag.html">the documentation</a></p>
<p>If you want to search for a single value then use the equal sign:</p>
<pre><code>node[name=&quot;Karnische Alpen&quot;];
out;</code></pre>
<p>If you want to search for lists of values then you can use a list as regular expression:</p>
<pre><code>node[name~&quot;^(Karnische Alpen|Dreitorspitze)$&quot;];
out;</code></pre>
<p><a href="https://dev.overpass-api.de/overpass-doc/en/criteria/union.html">Other variants exist</a>, depending on the exact aim. If you want to combine multiple criteria per or then use parentheses, as maxerickson has just explained.</p>
<p>Finally, you can use as extra criteria also free-form logic</p>
<pre><code>node[name~&quot;^(Karnische Alpen|Dreitorspitze)$&quot;]
    (if:t[&quot;natural&quot;]==&quot;glacier&quot; || t[&quot;natural&quot;]==&quot;peak&quot; || t[&quot;place&quot;]==&quot;region&quot;);
out;</code></pre>
<p>Please note that there is currently no node with name <code>Karnische Alpen</code> or <code>Dreitorspitze</code> in the database. Thus all the queries have empty results anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '20, 04:35</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '20, 04:39</strong> </span></p>
</div>
</div>
<div id="comments-container-73158" class="comments-container">
&#10;</div>
<div id="comment-tools-73158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73158-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73147"></span>

<div id="answer-container-73147" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73147-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks jmapb for your quick answer. This will save me several lines of code :-)</p>
<p>so, if I understand you right, its not possible to search for something like:</p>
<pre><code>name = &quot;Karnische Alpen&quot; AND [(natural = peak) OR (natural = glacier) OR (place = region)]</code></pre>
<p>The possibility to search a key without value is also very interesting, thanks very much. I just tried, if these could be concatenated, but also failed with different version of a code like this (there is no error message, but the map is empty):</p>
<pre><code>nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;][&quot;natural|place|boundary&quot;];
out geom;</code></pre>
<p>As I need to query several hunderts of names I try to find a query with as less code as possible. So would there be a way to query each name just one time within several keys/tags/features (as a matter of fact I think - as jmapb suggested - the key without the value would be enough)? So something like this:</p>
<pre><code>name = &quot;a name&quot; AND (&quot;natural&quot; OR &quot;place&quot; OR &quot;boundary&quot;)</code></pre>
<p>Thanks very much again :-)</p>
<p>Edit: just saw our edit now: the problem with a query without additional tags is, that there would be too much results. And because I know for sure, that it's not the name for e.g. a restaurant, I would like to limit the query to the possible features.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '20, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/b68d7eda3b2603d5e1c188e524f2f004?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="4Kala&#39;s gravatar image" />
<p><span>4Kala</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="4Kala has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '20, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-73147" class="comments-container">
&#10;</div>
<div id="comment-tools-73147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73161"></span>

<div id="answer-container-73161" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you very much for your answers maxerickson and Roland Olbricht :-)</p>
<p>With the help of you all I found the solution I need:</p>
<pre><code>  (
    nwr[&quot;name:de&quot;~&quot;Karnische Alpen&quot;](if:t[&quot;natural&quot;]==&quot;glacier&quot; || t[&quot;natural&quot;]==&quot;peak&quot; || t[&quot;place&quot;]==&quot;region&quot;); 
  nwr[name~&quot;Alpspitze&quot;](if:t[&quot;natural&quot;]==&quot;glacier&quot; || t[&quot;natural&quot;]==&quot;peak&quot; || t[&quot;place&quot;]==&quot;region&quot;);
    );
out geom;</code></pre>
<p>Thats what I was looking for, because I can generate this query automatically for all needed names and can query for specific keys/tags/features.</p>
<p>Thank you all three very much again for your help :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '20, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b68d7eda3b2603d5e1c188e524f2f004?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="4Kala&#39;s gravatar image" />
<p><span>4Kala</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="4Kala has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73161" class="comments-container">
&#10;</div>
<div id="comment-tools-73161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73161-form-container" class="comment-form-container">
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

