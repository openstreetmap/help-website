+++
type = "question"
title = "(OSM, overpass-turbo) How to get parent relation ID of each relation?"
description = '''[out:csv(::type, ::id, name, admin_level)];  area[name=&quot;Portugal&quot;]; rel(area)[admin_level=4][name]; out;  I have this but I also wanted a column with the id of the relation to which each relation listed immediately belongs (parent). A search on OSM has in the result &quot;...part of relation x&quot;, but how ...'''
date = "2018-07-28T15:17:00Z"
lastmod = "2018-07-30T16:00:00Z"
weight = 64985
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/64985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [(OSM, overpass-turbo) How to get parent relation ID of each relation?](/questions/64985/osm-overpass-turbo-how-to-get-parent-relation-id-of-each-relation)

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
<span id="post-64985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>[out:csv(::type, ::id, name, admin_level)]; 
area[name=&quot;Portugal&quot;];
rel(area)[admin_level=4][name];
out;</code></pre>
<p>I have this but I also wanted a column with the id of the relation to which each relation listed immediately belongs (parent). A search on OSM has in the result "...part of relation x", but how can I get that kind of information here through overpass-turbo?</p>
<p>A parent of a relation x is the relation at the admin_level above which has that relation x as a child.</p>
<p>I wanted something like: ::type, ::id, name, admin_level, <strong><em>::parent id</em></strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '18, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/7dcc267e54465a74eea1ce059e3432f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrefrsilva&#39;s gravatar image" />
<p><span>andrefrsilva</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrefrsilva has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64985" class="comments-container">
&#10;</div>
<div id="comment-tools-64985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64985-form-container" class="comment-form-container">
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

<span id="64987"></span>

<div id="answer-container-64987" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64987-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the <code>convert</code> statement to modify each element with the parent relation id:</p>
<pre><code>[out:csv(::type, ::id, name, admin_level,parent)]; 
rel[name=&quot;Portugal&quot;][admin_level=2]-&gt;.c;
.c map_to_area;
rel(area)[admin_level=4][name];
convert rel ::id = id(), ::=::,parent=c.set(id());
out;</code></pre>
<p>It is necessary to save the country into a result set, so that the set can be named in the convert statement.</p>
<p>An alternate strategy is to make a second script where you recurse up relations and then post-process the json to get the parent information. This is ultimately the strategy the OSM website is using, the canonical information about relation membership is the list of children in each relation. It might be caching the reverse information somewhere, but that would be rebuilt each time a relation is edited.</p>
<p>(edited to move answer up from comment)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '18, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '18, 18:14</strong> </span></p>
</div>
</div>
<div id="comments-container-64987" class="comments-container">
<span id="64988"></span>
<div id="comment-64988" class="comment">
<div id="post-64988-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also thought about using something like this:</p>
<p>[out:csv(::type, ::id, name, admin_level, ::parent_id)]; area["name"="Portugal"][admin_level=2]-&gt;.parent; //somehow saving the id of this parent to parent_id//</p>
<p>then:<br />
rel <a href="area.parent">admin_level = 4</a> ; out;</p>
<p>but how?</p>
</div>
<div id="comment-64988-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 17:15)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
<span id="64989"></span>
<div id="comment-64989" class="comment">
<div id="post-64989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I didn't realize that the parent would be available. Here's a step in the right direction, <a href="http://overpass-turbo.eu/s/ACK">http://overpass-turbo.eu/s/ACK</a> just need to figure out how to pull the Portugal id into it instead of writing "blah".</p>
<p>(Which I'm not sure is currently possible)</p>
</div>
<div id="comment-64989-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 17:36)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64990"></span>
<div id="comment-64990" class="comment">
<div id="post-64990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And here you go: <a href="http://overpass-turbo.eu/s/ACT">http://overpass-turbo.eu/s/ACT</a></p>
<p>I found the answer in <a href="https://dev.overpass-api.de/blog/final_0_7_54.html">https://dev.overpass-api.de/blog/final_0_7_54.html</a>, the <a href="https://dev.overpass-api.de/blog/">blog there</a> is I think still the best place for information about the recently released features.</p>
</div>
<div id="comment-64990-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 18:00)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64992"></span>
<div id="comment-64992" class="comment">
<div id="post-64992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot maxerickson! However, this way it just ends up as some "manual" input, and not the actual "parent" id. If I use admin_level=5 it continues to give out as "parent" what is now "grandparent".<br />
The goal would be to use this with several levels (in my initial case, using admin_level bigger and then &lt;&lt;; to have layers of family before).<br />
::id, name, admin_level, ::parent_id</p>
<hr />
<p>id 1, name 1, level 1, parent 1 ... id 2, name 2, level 2, parent 2 (its actual parent) ...</p>
</div>
<div id="comment-64992-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 18:35)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
<span id="64993"></span>
<div id="comment-64993" class="comment">
<div id="post-64993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The technique should work using other flow control, you'd just have to use lots of named sets and foreach loops to keep track of everything.</p>
<p>I'm pretty sure I'd do it in Python using json, where it'd be easy to build up mapping between children and parents.</p>
</div>
<div id="comment-64993-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 18:42)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64994"></span>
<div id="comment-64994" class="comment not_top_scorer">
<div id="post-64994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. And do you know if it is possible to use id instead of "name", since there might be different relations with the same "name" and ending up causing mistakes?</p>
</div>
<div id="comment-64994-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 18:48)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
<span id="64995"></span>
<div id="comment-64995" class="comment not_top_scorer">
<div id="post-64995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>rel(id) will fetch the relation with that id.</p>
</div>
<div id="comment-64995-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 18:55)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="64996"></span>
<div id="comment-64996" class="comment not_top_scorer">
<div id="post-64996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Instead of rel[name="Portugal"][admin_level=2]-&gt;.c; .c map_to_area; rel(area)[admin_level=6][name]; what should I use? (Being id=295480)</p>
</div>
<div id="comment-64996-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 19:03)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
<span id="64998"></span>
<div id="comment-64998" class="comment not_top_scorer">
<div id="post-64998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You'd replace <code>rel[name="Portugal"][admin_level=2]-&gt;.c;</code> with <code>rel(295480)-&gt;.c;</code> and keep the rest of it.</p>
</div>
<div id="comment-64998-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 20:24)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="65021"></span>
<div id="comment-65021" class="comment not_top_scorer">
<div id="post-65021-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks. This is what's lacking: <a href="https://overpass-turbo.eu/s/AFo">https://overpass-turbo.eu/s/AFo</a></p>
</div>
<div id="comment-65021-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 16:00)</span> <span class="comment-user userinfo">andrefrsilva</span>
</div>
</div>
</div>
<div id="comment-tools-64987" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64987-form-container" class="comment-form-container">
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

