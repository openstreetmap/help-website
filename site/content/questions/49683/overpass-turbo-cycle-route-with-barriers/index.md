+++
type = "question"
title = "Overpass Turbo - Cycle route with barriers?"
description = '''Hi -  I&#x27;m looking for help on crafting a query on Overpass Turbo. I&#x27;m asking for help because I think the query is one which if I get it right will be of real use to people. I want to look at cycle routes, and access barriers (for wheelchair use). I&#x27;m interested in barriers to entry/exit to the rout...'''
date = "2016-05-12T13:09:00Z"
lastmod = "2016-05-16T22:07:00Z"
weight = 49683
keywords = [ "overpassapi", "overpass", "wheelchair", "overpass-turbo", "accessibility" ]
aliases = [ "/questions/49683" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo - Cycle route with barriers?](/questions/49683/overpass-turbo-cycle-route-with-barriers)

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
<span id="post-49683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi -</p>
<p>I'm looking for help on crafting a query on Overpass Turbo. I'm asking for help because I think the query is one which if I get it right will be of real use to people. I want to look at cycle routes, and access barriers (for wheelchair use). I'm interested in barriers to entry/exit to the route, not just barriers actually on the route.</p>
<p>I've made an attempt at this already: <a href="http://overpass-turbo.eu/s/gaR">http://overpass-turbo.eu/s/gaR</a></p>
<p>There was some substantial guesswork involved, and any Overpass expert will quickly see what's wrong with this I'm sure. It works, but not particularly well. I see the issues as problems in styling - but I'm assuming that the problems are actually because of my very limited understanding when it comes to recursion and combining queries.</p>
<p>Tips would be appreciated - and if anyone feels like crafting the query properly I'll not complain either. Many thanks in advance.</p>
<p>Thanks Rostranimin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-wheelchair" rel="tag" title="see questions tagged &#39;wheelchair&#39;">wheelchair</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-accessibility" rel="tag" title="see questions tagged &#39;accessibility&#39;">accessibility</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d1814013676af3d0c7f9706c209d09d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rostranimin&#39;s gravatar image" />
<p><span>Rostranimin</span><br />
<span class="score" title="245 reputation points">245</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rostranimin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49683" class="comments-container">
<span id="49686"></span>
<div id="comment-49686" class="comment">
<div id="post-49686-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I read your question a couple of times now. Unfortunately I still couldn't figure out, what you're trying to achieve.</p>
<p>Could you explain in simple words, what problem you want to solve? Please don't think about any solutions yet, let alone any Overpass queries, only tell us about the real world problem you had in mind.</p>
<p>In particular, I didn't get what you mean by "barriers to entry/exit to the route" and in what way they are relevant to your problem. Can you provide some illustrative example, maybe even a picture or something?</p>
</div>
<div id="comment-49686-info" class="comment-info">
<span class="comment-age">(12 May '16, 16:40)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="49701"></span>
<div id="comment-49701" class="comment">
<div id="post-49701-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi mmd. Sorry if I wasn't clear. The existing Overpass query is probably the quickest way to explain as it's close to what I want, but not very good (styling doesn't work properly for a start).</p>
<p>I want to use Openstreetmap to look for access barriers (related to disability) around cycle routes (i.e. routes mapped by relation). I want to find steps, bollards, gates, and cycle barriers (cycle_barrier) on the actual route, but preferably also beside it.</p>
<p>I'd like to display this on a map to the public.</p>
<p>I want to do this to answer a question I've been asked about a particular cycle route - so I'm proposing to provide a link to a pre-written Overpass-turbo query rather than trying to set up anything more long-term.... although longer term solutions would be interesting too.</p>
<p>I'm keen to use mapcss to give a basic style to the output from Overpass-turbo.</p>
<p>I'd like to set up the query so that the results are as easy to interpret as possible for a new user (so clicking on a displayed point shows the background data).</p>
<p>Thanks for any ideas on this.</p>
</div>
<div id="comment-49701-info" class="comment-info">
<span class="comment-age">(15 May '16, 12:58)</span> <span class="comment-user userinfo">Rostranimin</span>
</div>
</div>
</div>
<div id="comment-tools-49683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49683-form-container" class="comment-form-container">
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

<span id="49705"></span>

<div id="answer-container-49705" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49705-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rostranimin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your detailed explanations! We'll start with fixing the query, once that is done, we can continue styling the results.</p>
<p>I've changed your query in the following ways:</p>
<ul>
<li>Cycling network is only returned for the bbox selected, instead of the whole cycling network, which happens to have a small portion within your bbox. This should highly reduce the amount of data returned.</li>
<li>Fixed the query part for barriers to properly take regular expressions into account ("~" operator instead of "=")</li>
<li>Instead of returning all barriers in your current bbox, I changed to query to only return barriers and steps within close proximity of the cycling network ways (up to 5 meters). This should reduce the number of non-relevant barriers.</li>
<li>To restrict the output to a certain cycling route, simply add an additional <code>[ref=...]</code> to the relation part of the query, like in the following example: <code>relation["route"="bicycle"]["network"="ncn"][ref="62"]</code></li>
</ul>
<p>[see query in overpass turbo, can't copy it here, as it gets completely mangled by the help site]</p>
<p>overpass turbo link: <a href="http://overpass-turbo.eu/s/gfb">http://overpass-turbo.eu/s/gfb</a></p>
<p><em>Note:</em> it is important to not show small features as POI in overpass turbo, otherwise the map will be cluttered with lots of irrelevant details. That's in the Menu underneath Settings -&gt; Map -&gt; Don't display small features as POIs. Enable this setting by clicking on it.</p>
<p>Regarding the styling:</p>
<ul>
<li>highway=crossing etc. is currently shown on the map. Not sure what you want to do with those node on the cycling way, which already have some (unrelated) tags. Assuming you don't want to show those on the map, you could use the following query as a starting point: <a href="http://overpass-turbo.eu/s/gfe">http://overpass-turbo.eu/s/gfe</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '16, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '16, 11:08</strong> </span></p>
</div>
</div>
<div id="comments-container-49705" class="comments-container">
<span id="49707"></span>
<div id="comment-49707" class="comment">
<div id="post-49707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you. I'll need to take a little while to read through these to understand them, but they certainly seem to do the job. These could be really useful to a number of people for real, and it'll be relatively easy for me to work forward with these as a basis (for instance selecting a particular cycle route just as you suggest). I couldn't have done this without help... too many separate ideas to juggle.</p>
</div>
<div id="comment-49707-info" class="comment-info">
<span class="comment-age">(16 May '16, 22:07)</span> <span class="comment-user userinfo">Rostranimin</span>
</div>
</div>
</div>
<div id="comment-tools-49705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49705-form-container" class="comment-form-container">
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

