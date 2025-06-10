+++
type = "question"
title = "[closed] Part/whole confusion with Wikidata tag... Need for enveloping parts into a whole"
description = '''Wikidata tag is a kind of Persistent Place Identifier, associating the &quot;specific place concept&quot; (defined in Wikidata) with the correspondent &quot;map of the place&quot;... So must be associated to a geometry that reflects the same concept: a railway is not a point, a street is not only a line-fragment of the...'''
date = "2018-08-06T15:11:00Z"
lastmod = "2018-08-09T19:11:00Z"
weight = 65163
keywords = [ "wikidata" ]
aliases = [ "/questions/65163" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Part/whole confusion with Wikidata tag... Need for enveloping parts into a whole](/questions/65163/partwhole-confusion-with-wikidata-tag-need-for-enveloping-parts-into-a-whole)

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
<span id="post-65163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Wikidata tag is a kind of <a href="https://wiki.openstreetmap.org/wiki/Persistent_Place_Identifier">Persistent Place Identifier</a>, associating the "specific place concept" (defined in Wikidata) with the correspondent "map of the place"... So must be associated to a geometry that reflects the same concept: a railway is not a point, a street is not only a line-fragment of the whole street.</p>
<p>Seems a commom quality problem of part/whole confusion in the Wikidata attribution or OSM's POI reference... And where there are a need for enveloping parts into a whole.</p>
<p>But somebody (or some software) must to edit "enveloping parts" into a relation. So:</p>
<ol>
<li>Can I edit and do it?</li>
<li>Can I delete the wrong Wikidata-tags (many parts) to preserve only the wikidata tag of the envelop element?</li>
</ol>
<hr />
<h2 id="examples">Examples:</h2>
<p><strong>1. Is it the envelope?</strong></p>
<p>Example 1.1: <a href="https://www.wikidata.org/wiki/Q315548">Sieg Railway</a> seems a <strong>good envelope relation</strong> because it is the whole... but it need a Wikidata ID. There are 33 geometry members of this whole with the Wikidata Q315548, but all 33 are parts.</p>
<p>Example 1.2: <a href="https://www.wikidata.org/wiki/Q896564">Eifel Railway (Q896564)</a> simlar case, with 56 parts with same Wikidata-ID. <a href="https://www.openstreetmap.org/relation/1717088">Relation/1717088 with no Wikidata</a> will be a good envelope for the concept Q896564.</p>
<p><strong>2. Can I build an envelope?</strong></p>
<p>Exempl 2.1: <a href="https://www.wikidata.org/wiki/Q319837">Anhalt Railway (Q319837)</a> seems to have no whole, but have 197 parts with the Q319837 tag, like <a href="https://www.openstreetmap.org/way/539934418">this fragment</a>... So is interesting to create a relation to envelope all 197 parts.</p>
<p>Exempl 2.2: <a href="https://www.wikidata.org/wiki/Q30158648">Rottnebyskogen nature reserve in Dalarna, Sweden (Q30158648)</a> have a <a href="https://www.openstreetmap.org/way/43190037">good way (43190037) representing it</a>... But, in nowadays we can't use way-ID at Wikidata, only relation-ID... to solve the problem some people do a workaround enveloping it... Is a hack, not a real solution.</p>
<p><strong>3. Can I delete?</strong></p>
<p>Example 3.1: <a href="https://www.openstreetmap.org/relation/7902731">Jacaré river <em>relation</em></a> is perhaps <strong>good envelope</strong>, a composition of many member-_way_s, and a whole concept with the Wikidata tag <a href="https://tools.wmflabs.org/reasonator/?lang=pt&amp;q=Q6110511">Q6110511</a>. Lets check a sample of member-ways: <a href="https://www.openstreetmap.org/way/553605376">way1</a>, <a href="https://www.openstreetmap.org/way/553778296">way2</a> or <a href="https://www.openstreetmap.org/way/553583596">way3</a>. Why only <em>way3</em> have also the Wikidata tag, and all other ~50 members of the same river have no Wikidata tag?<br />
Can I delete the Wikitag from <em>way3</em>?</p>
<p>Example 3.2: The <a href="https://tools.wmflabs.org/reasonator/?lang=pt&amp;q=Q41986">Mosa river (Q41986)</a>, is a whole represented by the <a href="https://www.openstreetmap.org/relation/1075197">relation (envelope) 1075197</a>, is perhaps a <strong>good envelope</strong>... There are many other relations, ways and nodes that are parts of relation 1075197. Can they use the Wikidata tag Q41986?   Lets check by <a href="https://overpass-turbo.eu/s/AM5">Overpass/AM5</a>... Hum, all are with the tag Q41986... So, <em>in strict sense</em> <strong>all are wrong</strong>, can I delete Wikitag from there?</p>
<hr />
<p>PS: I say "perhaps a good envelope" because other (subtle) problem is to decide when merge into a big envelope all points as in <a href="https://wiki.openstreetmap.org/wiki/Relation:street#Members">Relation:street#Members</a>, or "river as area vs river as line" perspectives.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '18, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>06 Aug '18, 21:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-65163" class="comments-container">
<span id="65239"></span>
<div id="comment-65239" class="comment">
<div id="post-65239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How to delete my question? On Stackoverflow I have delete option... Here I not see.</p>
</div>
<div id="comment-65239-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 19:11)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65163-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a question" by SimonPoole 06 Aug '18, 21:01

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="65170"></span>

<div id="answer-container-65170" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is clearly the wrong place for these, not really, questions. If you want to have a discussion on tagging best practices you should raise the issue on the tagging mailing list <a href="https://lists.openstreetmap.org/listinfo/tagging">https://lists.openstreetmap.org/listinfo/tagging</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '18, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '18, 21:04</strong> </span></p>
</div>
</div>
<div id="comments-container-65170" class="comments-container">
<span id="65195"></span>
<div id="comment-65195" class="comment">
<div id="post-65195-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Simon, the mailling list is working fine (!), <a href="https://lists.openstreetmap.org/pipermail/tagging/2018-August/038250.html">there are a first reply</a>. Can I delete the question? PS: I have a <a href="https://wiki.openstreetmap.org/wiki/User:Krauss/Wikidata-question1"><code>pandoc</code> copy</a>.</p>
</div>
<div id="comment-65195-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 14:07)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65170-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

