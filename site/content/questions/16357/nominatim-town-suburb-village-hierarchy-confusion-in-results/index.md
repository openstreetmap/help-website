+++
type = "question"
title = "Nominatim town, suburb, village hierarchy confusion in results"
description = '''Hi, I&#x27;m seeking some clarification of Nominatim&#x27;s behaviour. I have a TOWN, down the road is a SUBURB, and down the road is a VILLAGE. The three places are separate entities. If I search for X street in TOWN, Nominatim returns: &quot;X street, SUBURB, TOWN, Country&quot; - where SUBURB is a smaller locality o...'''
date = "2012-09-22T22:31:00Z"
lastmod = "2012-10-09T17:05:00Z"
weight = 16357
keywords = [ "town", "suburb", "nominatim", "hierarchy", "village" ]
aliases = [ "/questions/16357" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim town, suburb, village hierarchy confusion in results](/questions/16357/nominatim-town-suburb-village-hierarchy-confusion-in-results)

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
<span id="post-16357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16357-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm seeking some clarification of Nominatim's behaviour. I have a TOWN, down the road is a SUBURB, and down the road is a VILLAGE. The three places are separate entities.</p>
<p>If I search for X street in TOWN, Nominatim returns: "X street, SUBURB, TOWN, Country" - where SUBURB is a smaller locality outside of the town which should not be any part of the search result.</p>
<p>Likewise, if I search for Y Street in SUBURB, Nominatim returns Y street, VILLAGE, SUBURB, Country - and again, VILLAGE is a separate and smaller locality outside of suburb, and it should not be part of the result.</p>
<p>I understand it can be helpful for a nearby (larger) population centre to be mentioned as part of the results when searching a smaller locality, but it seems to make no sense to mention a smaller completely-unrelated locality when searching in a larger town. Perhaps there's something I'm missing?</p>
<p>The specific examples use Forster (Town), Forster Keys (Suburb), and Green Point (Village). <a href="http://www.openstreetmap.org/?lat=-32.2061&amp;lon=152.5205&amp;zoom=13&amp;layers=M">http://www.openstreetmap.org/?lat=-32.2061&amp;lon=152.5205&amp;zoom=13&amp;layers=M</a></p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-village" rel="tag" title="see questions tagged &#39;village&#39;">village</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '12, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/4200f1aaa4fa9ccd4d02db2e8e670de1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolftracker&#39;s gravatar image" />
<p><span>wolftracker</span><br />
<span class="score" title="475 reputation points">475</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolftracker has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-16357" class="comments-container">
&#10;</div>
<div id="comment-tools-16357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16357-form-container" class="comment-form-container">
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

<span id="16364"></span>

<div id="answer-container-16364" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16364-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-16364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wolftracker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the <a href="http://wiki.openstreetmap.org/wiki/Place">place</a> and <a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Dsuburb">suburb</a> wiki pages. A <em>suburb</em> is defined as an area inside a <em>town</em> or <em>city</em>. So there is not a clear hierarchy as long as suburbs are tagged as <em>nodes</em>. Every address search engine has to know the exact boundary of a suburb to be able to decide which other map feature belongs to this suburb. If there is just a node Nominatim tries to estimates the outline of the suburb.</p>
<p>From your explanations I chose <a href="http://nominatim.openstreetmap.org/search.php?q=Wallis+Street%2C+Forster&amp;viewbox=152.5%2C-32.17%2C152.53%2C-32.19">this example search</a> (next time clearly tell us a search example or even better a link!). As you can see, Nominatim thinks <a href="http://nominatim.openstreetmap.org/details.php?place_id=119779940">Wallis Street</a> belongs to the suburb <a href="http://www.openstreetmap.org/browse/node/114994001">Forster Keys</a> which is only tagged as a <em>node</em> and therefore has no clear outline. If you think this is wrong then try to replace the Forster Keys suburb node with an <em>area</em>. It doesn't have to be exact and can be improved later either by you or by others.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '12, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16364" class="comments-container">
&#10;</div>
<div id="comment-tools-16364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16360"></span>

<div id="answer-container-16360" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think it's simply because the Green Point dot happens to be (at a glance, although it's a bit hard to judge) slightly closer than the Forster one, and place=village ranks higher than place=suburb. If Green Point were a place=hamlet or Piper Points and Foster Keys had is_in tags (which nominatim apparently takes into account), the problem would solve itself.</p>
<p>In theory, the most surefire way, though (as Scai points out) would be to make sure there is a boundary relation but I'm not sure that would alter the Forster Keys -&gt; Green Point -&gt;Forster hierarchy as it looks like all would fall within the same boundary and put it back to square one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '12, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '12, 19:36</strong> </span></p>
</div>
</div>
<div id="comments-container-16360" class="comments-container">
<span id="16759"></span>
<div id="comment-16759" class="comment">
<div id="post-16759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Our community is undergoing discussion about importing suburb boundaries, so I think I'm going to leave any arbitrary boundary work out for now, but that's a great reminder about the is_in tag which might be a suitable work-around, I'll try it and see how it goes, otherwise will wait for a decision about our boundaries. Cheers, and i appreciate both good answers on this one.</p>
</div>
<div id="comment-16759-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 17:05)</span> <span class="comment-user userinfo">wolftracker</span>
</div>
</div>
</div>
<div id="comment-tools-16360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16360-form-container" class="comment-form-container">
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

