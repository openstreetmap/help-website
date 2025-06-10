+++
type = "question"
title = "Get bus stops by given area and relation."
description = '''Wondering how to write an Overpass query to get only nodes with bus_stops from this query: [out:json][timeout:25]; area[name=&quot;Radom&quot;]-&amp;gt;.searchArea; (   relation[&quot;name&quot;=&quot;8: Os. Wośniki =&amp;gt; Kierzków&quot;](area.searchArea); ); out body; &amp;gt;; out skel qt;  in shortcut get bus stops by given area and r...'''
date = "2020-06-08T09:46:00Z"
lastmod = "2020-12-12T11:27:00Z"
weight = 75196
keywords = [ "bus", "stop", "relation", "overpass" ]
aliases = [ "/questions/75196" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get bus stops by given area and relation.](/questions/75196/get-bus-stops-by-given-area-and-relation)

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
<span id="post-75196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Wondering how to write an Overpass query to get only nodes with bus_stops from this query:</p>
<pre><code>[out:json][timeout:25];
area[name=&quot;Radom&quot;]-&gt;.searchArea;
( 
  relation[&quot;name&quot;=&quot;8: Os. Wośniki =&gt; Kierzków&quot;](area.searchArea);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>in shortcut get bus stops by given area and relation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '20, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/20a6e9808fa4fa75b537e684bb8a9030?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="macik1423&#39;s gravatar image" />
<p><span>macik1423</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="macik1423 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '20, 10:14</strong> </span></p>
</div>
</div>
<div id="comments-container-75196" class="comments-container">
<span id="75201"></span>
<div id="comment-75201" class="comment">
<div id="post-75201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't know much about Overpass QL, but if the relation is according to PTv2 it <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dbus">should have</a> a role of <code>platform</code>, <code>platform_exit_only</code> or <code>platform_entry_only</code>. In the more traditional tagging they would have no role and you would have to look for nodes nodes in the relation that have the <code>highway=bus_stop</code> tag.</p>
</div>
<div id="comment-75201-info" class="comment-info">
<span class="comment-age">(08 Jun '20, 13:29)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-75196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75196-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="75247"></span>

<div id="answer-container-75247" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75247-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="macik1423 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK. We should get only the nodes belonging to the relation. I think it should be better like this :</p>
<pre><code>[out:json][timeout:25];
area[name=&quot;Radom&quot;]-&gt;.searchArea;
&#10;relation[&quot;name&quot;=&quot;8: Os. Wośniki =&gt; Kierzków&quot;](area.searchArea);
node(r)[highway=bus_stop];
out body qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '20, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a588fbc312ece948db9faa4cc02b40de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorglubu&#39;s gravatar image" />
<p><span>zorglubu</span><br />
<span class="score" title="324 reputation points">324</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorglubu has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-75247" class="comments-container">
<span id="75257"></span>
<div id="comment-75257" class="comment">
<div id="post-75257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! This is what I have been looking for. :D</p>
</div>
<div id="comment-75257-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 21:29)</span> <span class="comment-user userinfo">macik1423</span>
</div>
</div>
<span id="77904"></span>
<div id="comment-77904" class="comment">
<div id="post-77904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have another question, is it possible to get order of nodes in data as same as relation in map? For example in this query</p>
<p><code>[out:json][timeout:25]; area[name="Radom"]-&gt;.searchArea; ( relation(5347191)(area.searchArea); node(r)[highway=bus_stop]; ); out geom;</code></p>
<p>order is random, not fit to relation on map.</p>
</div>
<div id="comment-77904-info" class="comment-info">
<span class="comment-age">(12 Dec '20, 11:03)</span> <span class="comment-user userinfo">macik1423</span>
</div>
</div>
<span id="77905"></span>
<div id="comment-77905" class="comment">
<div id="post-77905-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am not sure, but I think that it is not possible directly with overpass. In my mind, the order is the one of the BDD. I am interested if somebody else has a better answer :-)</p>
<p>I have checked this request : [out:json][timeout:25]; relation(5347191); out meta;</p>
<p>The order seems to be the one shown in JOSM. Then you will need a post processing treatment.</p>
</div>
<div id="comment-77905-info" class="comment-info">
<span class="comment-age">(12 Dec '20, 11:27)</span> <span class="comment-user userinfo">zorglubu</span>
</div>
</div>
</div>
<div id="comment-tools-75247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75247-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75209"></span>

<div id="answer-container-75209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, Could you try :</p>
<pre><code>[out:json][timeout:25];
area[name=&quot;Radom&quot;]-&gt;.searchArea;
&#10;relation[&quot;name&quot;=&quot;8: Os. Wośniki =&gt; Kierzków&quot;](area.searchArea);
&#10;&gt; -&gt; .a;
node.a[highway=bus_stop];
&#10;out body qt;</code></pre>
<p>This should extract the elements of the relation, and then only the nodes with the good tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '20, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a588fbc312ece948db9faa4cc02b40de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorglubu&#39;s gravatar image" />
<p><span>zorglubu</span><br />
<span class="score" title="324 reputation points">324</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorglubu has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-75209" class="comments-container">
<span id="75235"></span>
<div id="comment-75235" class="comment">
<div id="post-75235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for respond! It's not quite what I expect. Query returns all bus stops (relation "8: Os. Wośniki =&gt; Kierzków" and reverse relation "8: Kierzków =&gt; Os. Wośniki"), I wanna bus stops from one direction.</p>
</div>
<div id="comment-75235-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 10:14)</span> <span class="comment-user userinfo">macik1423</span>
</div>
</div>
</div>
<div id="comment-tools-75209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75209-form-container" class="comment-form-container">
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

