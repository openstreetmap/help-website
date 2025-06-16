+++
type = "question"
title = "Show duplicated nodes via Overpass"
description = '''How to show the duplicated nodes, such as this, via the Overpass (API, Turbo)?'''
date = "2014-12-20T20:34:00Z"
lastmod = "2018-06-07T12:47:00Z"
weight = 39745
keywords = [ "overpass" ]
aliases = [ "/questions/39745" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Show duplicated nodes via Overpass](/questions/39745/show-duplicated-nodes-via-overpass)

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
<span id="post-39745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39745-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to show the duplicated nodes, such as <a href="https://www.openstreetmap.org/edit?editor=potlatch2#map=23/45.01972/39.02164" title="Don&#39;t fix this, please :)">this</a>, via the Overpass (API, Turbo)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '14, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e7ab0e74a89c411904b7077d5b1ddcff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chilin&#39;s gravatar image" />
<p><span>chilin</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chilin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '14, 20:37</strong> </span></p>
</div>
</div>
<div id="comments-container-39745" class="comments-container">
<span id="39756"></span>
<div id="comment-39756" class="comment">
<div id="post-39756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an aside, if you want to link to problem data that won't get accidentally fixed, you could use a link to a location via <a href="http://api06.dev.openstreetmap.org">http://api06.dev.openstreetmap.org</a> . That has a separate set of test data, and no one will fix your example problem by accident.</p>
</div>
<div id="comment-39756-info" class="comment-info">
<span class="comment-age">(21 Dec '14, 11:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="39757"></span>
<div id="comment-39757" class="comment">
<div id="post-39757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: that probably won't work with overpass, as there's no instance pointing to the dev server I'm aware of. However, that's not a big issue. Just add [date:"2014-12-21T00:00:00Z"] to the top of the query to always reference that point in time.</p>
</div>
<div id="comment-39757-info" class="comment-info">
<span class="comment-age">(21 Dec '14, 12:02)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="39762"></span>
<div id="comment-39762" class="comment">
<div id="post-39762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. <a href="http://level0.osmz.ru/?url=%2F%2Foverpass-api.de%2Fapi%2Finterpreter%3Fdata%3D%255Bdate%253A%25222014-12-21T00%253A00%253A00Z%2522%255D%250A%255Bbbox%253A45.01922299382942%252C39.02108520269394%252C45.02009039433733%252C39.02220368385315%255D%253B%250Anode%253B%250Aforeach-%253E.a%28%250A%2520%2520%2520%2520node%28around.a%253A0%29-%253E.b%253B%250A%2520%2520%2520%2520%28.b%253B%2520-%2520.a%29%253B%250A%2520%2520%2520%2520out%2520meta%253B%250A%29%253B">Here's a permanent link</a> to this place based on the due date.</p>
</div>
<div id="comment-39762-info" class="comment-info">
<span class="comment-age">(21 Dec '14, 20:06)</span> <span class="comment-user userinfo">chilin</span>
</div>
</div>
</div>
<div id="comment-tools-39745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39745-form-container" class="comment-form-container">
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

<span id="39746"></span>

<div id="answer-container-39746" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39746-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-39746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chilin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Overpass API is not the most common tool for this task, I will also mention a few more mainstream alternatives.</p>
<p><strong>Option 1:</strong> Overpass API</p>
<p>This query will first determine all nodes in the current bounding box. For each node found, we will then start looking for some nodes at exactly the same location. The result will return all pairs of duplicate nodes found in the current bbox.</p>
<pre><code>[bbox:{{bbox}}];
node;
foreach-&gt;.a(
    node(around.a:0)-&gt;.b;
    (.b; - .a);
    out meta;
);</code></pre>
<p>Unfortunately, this approach is extremely slow with <code>out meta;</code> (NB: this seems to be a bug, I've created a <a href="https://github.com/drolbr/Overpass-API/issues/165">Github issue for this</a>). If you don't need metadata information, just replace <code>out meta;</code> by <code>out;</code> and you will get the response almost instantly.</p>
<p>Try it on overpass turbo: <a href="http://overpass-turbo.eu/s/6C7">very slow (with metadata</a>) and <a href="http://overpass-turbo.eu/s/6Cy">fast (without metadata)</a></p>
<p><img src="/upfiles/duplicates.png" alt="alt text" /></p>
<p><strong>Option 2:</strong></p>
<p>I'd really recommend to also look at <strong>keep right!</strong> (analysis data is a few weeks old): see <a href="http://keepright.at/report_map.php?lang=en&amp;ch30=1&amp;ch40=1&amp;ch50=1&amp;ch70=1&amp;ch90=1&amp;ch100=1&amp;ch110=1&amp;ch120=1&amp;ch130=1&amp;ch150=1&amp;ch160=1&amp;ch170=1&amp;ch180=1&amp;ch191=1&amp;ch192=1&amp;ch193=1&amp;ch194=1&amp;ch195=1&amp;ch196=1&amp;ch197=1&amp;ch198=1&amp;ch201=1&amp;ch202=1&amp;ch203=1&amp;ch204=1&amp;ch205=1&amp;ch206=1&amp;ch207=1&amp;ch208=1&amp;ch210=1&amp;ch220=1&amp;ch231=1&amp;ch232=1&amp;ch270=1&amp;ch281=1&amp;ch282=1&amp;ch283=1&amp;ch284=1&amp;ch285=1&amp;ch291=1&amp;ch292=1&amp;ch293=1&amp;ch294=1&amp;ch295=1&amp;ch296=1&amp;ch297=1&amp;ch298=1&amp;ch311=1&amp;ch312=1&amp;ch313=1&amp;ch320=1&amp;ch350=1&amp;ch370=1&amp;ch380=1&amp;ch401=1&amp;ch402=1&amp;ch411=1&amp;ch412=1&amp;ch413=1&amp;number_of_tristate_checkboxes=8&amp;highlight_error_id=0&amp;highlight_schema=0&amp;lat=45.01903&amp;lon=39.02266&amp;zoom=17&amp;show_ign=1&amp;show_tmpign=1&amp;layers=B0T&amp;ch=0%2C20">this example for a layer with multiple nodes on the same spot</a></p>
<p><strong>Option 3:</strong></p>
<p>In addition to that, <strong>JOSM validator</strong> will warn you regarding many unconnected nodes without physical characteristics in that area - and even fix them! That's probably the best way to go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '14, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '14, 11:11</strong> </span></p>
</div>
</div>
<div id="comments-container-39746" class="comments-container">
<span id="39747"></span>
<div id="comment-39747" class="comment">
<div id="post-39747-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for such a detailed answer.</p>
</div>
<div id="comment-39747-info" class="comment-info">
<span class="comment-age">(20 Dec '14, 22:54)</span> <span class="comment-user userinfo">chilin</span>
</div>
</div>
<span id="39755"></span>
<div id="comment-39755" class="comment">
<div id="post-39755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It should also be noted that multiple nodes on the same spot are not necessarily an error, and sometimes even required (e.g. in multi-level buildings).</p>
</div>
<div id="comment-39755-info" class="comment-info">
<span class="comment-age">(21 Dec '14, 11:37)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="64077"></span>
<div id="comment-64077" class="comment">
<div id="post-64077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For those coming here via a search, the above Overpass query requires an extra ';' after the '.a' variable:</p>
<p>(.b; - .a;);</p>
</div>
<div id="comment-64077-info" class="comment-info">
<span class="comment-age">(07 Jun '18, 12:47)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-39746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39746-form-container" class="comment-form-container">
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

