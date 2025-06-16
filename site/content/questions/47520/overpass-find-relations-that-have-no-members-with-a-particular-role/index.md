+++
type = "question"
title = "Overpass: find relations that have no members with a particular role"
description = '''How do I make a query that returns me every admin_level=7 relation in Poland that doesn&#x27;t have a member with admin_centre role? This is a pre-requisite to another thing - After fixing these (if needed, I wanna find out) I want to list every place in Poland that should feature amenity=townhall, but h...'''
date = "2016-01-15T01:58:00Z"
lastmod = "2016-01-15T20:11:00Z"
weight = 47520
keywords = [ "overpass" ]
aliases = [ "/questions/47520" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: find relations that have no members with a particular role](/questions/47520/overpass-find-relations-that-have-no-members-with-a-particular-role)

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
<span id="post-47520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I make a query that returns me every admin_level=7 relation in Poland that doesn't have a member with admin_centre role?</p>
<p><del>This is a pre-requisite to another thing - After fixing these (if needed, I wanna find out) I want to list every place in Poland that should feature amenity=townhall, but has none. This is what I've got currently: <a href="http://overpass-turbo.eu/s/dJo">http://overpass-turbo.eu/s/dJo</a></del></p>
<del></del>
<p><del>In this second query I also have to solve a problem: Some rural municipalities have their seat outside them, how do I exclude these? cf. <a href="https://en.wikipedia.org/wiki/Gmina">https://en.wikipedia.org/wiki/Gmina</a></del></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '16, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '16, 21:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47520" class="comments-container">
&#10;</div>
<div id="comment-tools-47520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47520-form-container" class="comment-form-container">
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

<span id="47525"></span>

<div id="answer-container-47525" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47525-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RicoElectrico has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I will focus on your first question atm. If possible, please move your other question to dedicated threads.</p>
<p>Here's how the query should look like</p>
<pre><code>[timeout:600];
&#10;area[admin_level=2][&quot;name&quot;=&quot;Polska&quot;][boundary=administrative]-&gt;.boundaryarea;
&#10;( rel(area.boundaryarea)[boundary=administrative][admin_level=7]; -
&#10;  ( node(r:&quot;admin_centre&quot;)-&gt;.a;
    rel(bn.a)[boundary=administrative][admin_level=7]; 
  );
);
&#10;out geom;</code></pre>
<p>Overpass Turbo Link: <a href="http://overpass-turbo.eu/s/dLT">http://overpass-turbo.eu/s/dLT</a></p>
<p>A few words how this works:</p>
<ul>
<li>We initially get a <code>boundaryarea</code> as defined per Poland's admin_level=2 boundary</li>
<li>Now we determine difference of all <code>admin_level=7</code> boundaries in that area MINUS those <code>admin_level=7</code> boundaries having an admin_centre node.</li>
</ul>
<p>Read more about the recurse functions used in this query <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">here</a>.</p>
<p>Note that there are some relations returned outside of Poland. This is not a bug in the query, but rather some outdated areas on overpass-api.de. See <a href="/questions/47080/areas-broken-on-all-overpass-servers">this thread</a> for details. It works just fine on our dev box with up-to-date areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '16, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-47525" class="comments-container">
&#10;</div>
<div id="comment-tools-47525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47525-form-container" class="comment-form-container">
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

