+++
type = "question"
title = "Export all boundaries in an area via overpass"
description = '''I want to export all relations with tags such as boundary=administrative and all childs of those relations in a certain area. I&#x27;m using Overpass API, but I get stuck with the variables. My current code looks as following (with Staden as an example, bigger areas will be used once it works): area[name...'''
date = "2012-12-11T14:52:00Z"
lastmod = "2012-12-17T12:13:00Z"
weight = 18368
keywords = [ "overpass", "export", "area" ]
aliases = [ "/questions/18368" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export all boundaries in an area via overpass](/questions/18368/export-all-boundaries-in-an-area-via-overpass)

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
<span id="post-18368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18368-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to export all relations with tags such as boundary=administrative and all childs of those relations in a certain area.</p>
<p>I'm using Overpass API, but I get stuck with the variables. My current code looks as following (with Staden as an example, bigger areas will be used once it works):</p>
<pre><code>area[name=&quot;Staden&quot;];
(
  node(area);
  &lt;;
) -&gt; .a;
(
  .a rel[&quot;boundary&quot;=&quot;administrative&quot;];
);
out meta qt;</code></pre>
<p>But it doesn't work. 'a' is supposed to be a variable holding all features in Staden. And then, according to the documentation I've read, I should be able to use 'a' to get all relations with specific tags in it.</p>
<p>Once I have the relations, they should be completed again so I have an OSM file that can be displayed.</p>
<p>And I hope, once the syntax error is resolved, that the query doesn't include boundaries of neighbour villages. If anyone has an idea on how to get those out, you would be very welcome.</p>
<p>It might also be a good example to put on the wiki.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '12, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '12, 14:52</strong> </span></p>
</div>
</div>
<div id="comments-container-18368" class="comments-container">
<span id="18411"></span>
<div id="comment-18411" class="comment">
<div id="post-18411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ping, are there no OpenLayers specialists here?</p>
</div>
<div id="comment-18411-info" class="comment-info">
<span class="comment-age">(13 Dec '12, 13:09)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="18414"></span>
<div id="comment-18414" class="comment">
<div id="post-18414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OverpassAPI, not OpenLayers. Be a bit more patient, Roland Olbricht is stopping by from time to time. He should be able to help you.</p>
</div>
<div id="comment-18414-info" class="comment-info">
<span class="comment-age">(13 Dec '12, 13:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18368-form-container" class="comment-form-container">
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

<span id="18510"></span>

<div id="answer-container-18510" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18510-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sanderd17 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please put the ".a" after "rel". Otherwise, you should have seen a syntax error:</p>
<pre><code>area[name=&quot;Staden&quot;];
(
  node(area);
  &lt;;
) -&gt; .a;
(
  rel.a[&quot;boundary&quot;=&quot;administrative&quot;];
);
out meta qt;</code></pre>
<p>The syntax is here different from the syntax of "out", because it does something different: It reads "take all relations that are contained in .a and have a tag with the given values". In particular, you could intersect in a query multiple sets like "rel.a.b" which is not possible in the context of "out".</p>
<p>Thank you for asking this question. I'll copy this explanation to the documentation. Please add a link fomr the wiki to this question meanwhile to remind me on this.</p>
<p>I'm sorry for the late answer. I try in general a 24h hour check about relevant questions, but for no apparent reason I missed this one. In such a case, please feel free to write me an email to roland.olbricht at gmx.de.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '12, 07:15</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '12, 07:17</strong> </span></p>
</div>
</div>
<div id="comments-container-18510" class="comments-container">
<span id="18518"></span>
<div id="comment-18518" class="comment">
<div id="post-18518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem, I wasn't in a hurry, it's just that I didn't want the question to fall of the first page.</p>
<p>It works great now.</p>
</div>
<div id="comment-18518-info" class="comment-info">
<span class="comment-age">(17 Dec '12, 12:13)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18510-form-container" class="comment-form-container">
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

