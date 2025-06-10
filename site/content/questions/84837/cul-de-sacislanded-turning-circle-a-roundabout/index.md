+++
type = "question"
title = "Cul de sac/islanded turning circle a &quot;roundabout&quot;?"
description = '''I&#x27;ve been seeing people adding junction=roundabout for fully drawn cul-de-sac / turning circles that have a nontraversible island in it. It&#x27;s not clear of the oneway direction mainly because it&#x27;s only one road connecting to it and it was meant for local traffic only. No other roads are connected, ex...'''
date = "2022-06-21T18:21:00Z"
lastmod = "2022-06-22T19:31:00Z"
weight = 84837
keywords = [ "culdesac", "roundabout" ]
aliases = [ "/questions/84837" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Cul de sac/islanded turning circle a "roundabout"?](/questions/84837/cul-de-sacislanded-turning-circle-a-roundabout)

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
<span id="post-84837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84837-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been seeing people adding junction=roundabout for fully drawn cul-de-sac / turning circles that have a nontraversible island in it. It's not clear of the oneway direction mainly because it's only one road connecting to it and it was meant for local traffic only. No other roads are connected, except house driveways.</p>
<p>Should these be tagged with junction=roundabout?</p>
<p>In my preference I do not want to hear "enter roundabout" on GPS software when I approach the end of a residential street that has one of these islanded turning circles and the only way out is back the way one came?</p>
<p>BTW another problem I've seen is that people have been adding junction=roundabout without checking direction of traffic flow. This would make router tools instruct people turn left on drive-on-right areas which is wrong...so a fix is needed on many of these anyway.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-culdesac" rel="tag" title="see questions tagged &#39;culdesac&#39;">culdesac</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '22, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c86f4c99960b2c3ffdeb1698ba833b52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpserror&#39;s gravatar image" />
<p><span>gpserror</span><br />
<span class="score" title="171 reputation points">171</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpserror has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84837" class="comments-container">
&#10;</div>
<div id="comment-tools-84837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84837-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="84851"></span>

<div id="answer-container-84851" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84851-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-84851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gpserror has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd like to combine the answers from andy mackey and Mike N into a unified response.</p>
<p>If the end of the road has a cul-de-sac with no island, or a traversable island, you can tag the end node with <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dturning_circle">highway=turning_circle</a>.</p>
<p>If the end of the road has a cul-de-sac with a non-traverable island, you can tag the end node with <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dturning_loop">highway=turning_loop</a>. If the loop and island are large enough - or if you just want to map things in more detail - the loop can instead be mapped with a closed way running around the loop. This is NOT a roundabout and should not be tagged with junction=roundabout. This is simply a circular piece of road and it doesn't need any additional tagging (other than oneway=yes if that's relevant).</p>
<p>Tagging a cul-de-sac as a roundabout is objectively wrong. It is not a junction. If you see the tags <code>junction=roundabout</code> or <code>highway=mini_roundabout</code> on a cul-de-sac, they should be removed and replaced with one of the more appropriate tags from above (<code>highway=turning_circle</code> or <code>highway=turning_loop</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '22, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-84851" class="comments-container">
<span id="84852"></span>
<div id="comment-84852" class="comment">
<div id="post-84852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>user:alester wrote: "Tagging a cul-de-sac as a roundabout is objectively wrong. It is not a junction. If you see the tags junction=roundabout or highway=mini_roundabout on a cul-de-sac, they should be removed and replaced with one of the more appropriate tags from above (highway=turning_circle or highway=turning_loop)."</p>
<p>I agree entirely.</p>
</div>
<div id="comment-84852-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 17:25)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="84854"></span>
<div id="comment-84854" class="comment">
<div id="post-84854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this clarifies things and I shall zap all these roundabouts people are putting in on cul-de-sacs whether or not it has an island or not. I was just worried there was some other rule I was not aware of and ripping up other peoples' work for no reason. Perhaps an explicit "cul-de-sacs" are not roundabouts is needed in the wiki...</p>
</div>
<div id="comment-84854-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 19:23)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
</div>
<div id="comment-tools-84851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84839"></span>

<div id="answer-container-84839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84839-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think highway=turning circle is all that's needed. I'm not sure how most sat navs treat just highway=turning circle. In addition. I use Potlatch for 99.9% of my edits and highway=turning circle is the offered option. I would think you need two ways for a junction, which would be the result if a roundabout is mapped as a roundabout. ONLY If the turning circle is large and has a traffic island I would map a roundabout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '22, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '22, 06:53</strong> </span></p>
</div>
</div>
<div id="comments-container-84839" class="comments-container">
<span id="84841"></span>
<div id="comment-84841" class="comment">
<div id="post-84841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, and I don't even think that's absolutely necessary either...</p>
<p>What I'm wondering is if it's wrong to have junction=roundabout on this circular road. My opinion is yes it's "wrong" but people keep on adding it and the wiki isn't too clear about this situation. (I think people in general call any circular road a "roundabout" but computers can tell this...but it cannot tell whether the drivers in this circular road has right of way - and this, IMHO, is the more important piece of data.</p>
</div>
<div id="comment-84841-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 02:57)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="84842"></span>
<div id="comment-84842" class="comment">
<div id="post-84842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have added a little to my answer.</p>
</div>
<div id="comment-84842-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 06:55)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-84839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84839-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84843"></span>

<div id="answer-container-84843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a cul-de-sac, this could be described by <code>highway=turning_loop</code>. <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dturning_loop">turning loop</a> However when the non-traversible island becomes large enough, it may be better modeled with the road centerline around the turning loop so that driveway entrances match the physical layout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '22, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '22, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-84843" class="comments-container">
<span id="84845"></span>
<div id="comment-84845" class="comment">
<div id="post-84845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So if this island becomes big enough, the turning loop becomes a roundabout for these cul-de-sacs? Again I do not think roundabout is appropriate, but I see people doing it and causing validation issues (specifically, one way issues), and I wonder if these should be fixed even if the 1-way happens to be correct for the locale.</p>
<p>I'm not sure if people are considering the highway=service service=driveway ways (which usually are NOT even drawn!) as "other roads" that contribute to an actual "junction" between "roads".</p>
</div>
<div id="comment-84845-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 14:31)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="84848"></span>
<div id="comment-84848" class="comment">
<div id="post-84848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Turning loops do not fit the definition of a roundabout. For a large turning loop, the road just loops back on itself - often with a teardrop shape, and it's not clear that it would be marked as one-way unless there is a sign. Adding driveways to a small turning loop are a less common form of micro mapping. Driveways can be useful for navigation when there is a large turning loop and houses are set far back from the turning loop on hilly terrain. The driveway <em>should</em> be marked with the house number, but they may be obscured by foliage.</p>
</div>
<div id="comment-84848-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 15:32)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="84855"></span>
<div id="comment-84855" class="comment">
<div id="post-84855-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. Will zap the junction=roundabout in things like (currently version 3) of <a href="http://www.openstreetmap.org/way/191085659">http://www.openstreetmap.org/way/191085659</a> because this is not a roundabout as I thought. I constantly see these being put in when they put the (implicit/explicit) oneway direction in wrong, and just wanted to make sure I was aware of all the rules for these because they keep popping up. Perhaps the wiki needs an explicit "cul-de-sacs are not roundabouts" :)</p>
</div>
<div id="comment-84855-info" class="comment-info">
<span class="comment-age">(22 Jun '22, 19:31)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
</div>
<div id="comment-tools-84843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84843-form-container" class="comment-form-container">
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

