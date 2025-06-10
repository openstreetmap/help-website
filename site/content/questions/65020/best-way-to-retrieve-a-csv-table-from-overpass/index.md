+++
type = "question"
title = "Best way to retrieve a CSV table from Overpass"
description = '''I net to run by terminal (eg. using wget or curl) an Overpass query... Something like  ( node[place]({{bbox}}); relation[boundary]({{bbox}}); );  but returning a CSV file with csv(id,user,type,wikidata,name,place, boundary) (perhaps with verbosity=&#x27;meta&#x27;). So, how to express this query in a standard...'''
date = "2018-07-30T15:34:00Z"
lastmod = "2018-07-30T17:28:00Z"
weight = 65020
keywords = [ "overpass", "csv" ]
aliases = [ "/questions/65020" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to retrieve a CSV table from Overpass](/questions/65020/best-way-to-retrieve-a-csv-table-from-overpass)

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
<span id="post-65020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I net to run by terminal (eg. using <code>wget</code> or <code>curl</code>) an Overpass query... Something like</p>
<pre><code>(  node[place]({{bbox}}); relation[boundary]({{bbox}});  );</code></pre>
<p>but returning a CSV file with <code>csv(id,user,type,wikidata,name,place, boundary)</code> (perhaps with <code>verbosity='meta'</code>).</p>
<p>So, how to express this query in a standard URL-API? What the best URL to use, <code>overpass-api.de</code>?</p>
<p>PS: I need a full URL to test, as <a href="http://overpass-api.de/api/interpreter?data=%5Bout:csv%5D;..."><code>http://overpass-api.de/api/interpreter?data=[out:csv];...</code></a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 15:35</strong> </span></p>
</div>
</div>
<div id="comments-container-65020" class="comments-container">
&#10;</div>
<div id="comment-tools-65020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65020-form-container" class="comment-form-container">
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

<span id="65022"></span>

<div id="answer-container-65022" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65022-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ppKrauss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simple answer is (if I understand question correctly)</p>
<blockquote>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bbbox%3A51%2E505049609500325%2C%2D0%2E11482000350952147%2C51%2E51091261939121%2C%2D0%2E10587215423583984%5D%5Bout%3Acsv%28%3A%3Aid%2C%3A%3Auser%2C%3A%3Atype%2C%22wikidata%22%2C%22name%22%2C%22place%22%2C%22boundary%22%29%5D%3B%28node%5B%22place%22%5D%3Brelation%5B%22boundary%22%5D%3B%29%3Bout%20meta%3B%0A">http://overpass-api.de/api/interpreter?data=%5Bbbox%3A51%2E505049609500325%2C%2D0%2E11482000350952147%2C51%2E51091261939121%2C%2D0%2E10587215423583984%5D%5Bout%3Acsv%28%3A%3Aid%2C%3A%3Auser%2C%3A%3Atype%2C%22wikidata%22%2C%22name%22%2C%22place%22%2C%22boundary%22%29%5D%3B%28node%5B%22place%22%5D%3Brelation%5B%22boundary%22%5D%3B%29%3Bout%20meta%3B%0A</a></p>
</blockquote>
<p>In a bit more detail I have rewritten your query and typed into overpass turbo (if this isnt quite what you want I hope you get the general idea)</p>
<pre><code>[out:csv(::id,::user,::type,wikidata,name,place, boundary)]
[bbox:{{bbox}}];   
(  node[place] ;
   relation[boundary];  
);     
out meta ;</code></pre>
<p>Running this gives</p>
<pre><code>@id @user   @type   wikidata    name    place   boundary
450524790   SK53    node    Q154322 South Bank  suburb  
51781   kalc    relation    Q179351 City of Westminster     administrative
51800   lefty74 relation    Q23311  City of London      administrative
......</code></pre>
<p>I then selected <strong>Export &gt; convert to (compact) OverpassQL</strong> Which opens new tab with the rather long URL quoted above</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '18, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 16:40</strong> </span></p>
</div>
</div>
<div id="comments-container-65022" class="comments-container">
<span id="65024"></span>
<div id="comment-65024" class="comment">
<div id="post-65024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks, near perfect! I need also restriction to "wikidata is not null". About BBOX I posted another question, because will be easy starting with a relation ID.</p>
</div>
<div id="comment-65024-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 17:03)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="65026"></span>
<div id="comment-65026" class="comment">
<div id="post-65026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Solved the "wikidata is not null" constraint by <code>node[place][wikidata]; relation[boundary][wikidata];</code></p>
</div>
<div id="comment-65026-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 17:28)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65022-form-container" class="comment-form-container">
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

