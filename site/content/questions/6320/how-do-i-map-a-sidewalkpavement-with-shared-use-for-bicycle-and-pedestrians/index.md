+++
type = "question"
title = "How do I map a sidewalk/pavement with shared use for bicycle and pedestrians?"
description = '''I&#x27;m trying to add some detailed mapping along a cycle route (the N72 in Newcastle,UK). This route is largely along peaceful designated bike/hiking paths that are away from the busy roads, but in some areas it briefly travels along the pavement/sidewalk by the side of a road. Ideally I&#x27;d like to capt...'''
date = "2011-07-15T09:56:00Z"
lastmod = "2020-07-07T12:00:00Z"
weight = 6320
keywords = [ "sidewalks", "bicycle", "footway", "tagging", "cycleway" ]
aliases = [ "/questions/6320" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [How do I map a sidewalk/pavement with shared use for bicycle and pedestrians?](/questions/6320/how-do-i-map-a-sidewalkpavement-with-shared-use-for-bicycle-and-pedestrians)

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
<span id="post-6320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6320-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to add some detailed mapping along a cycle route (the N72 in Newcastle,UK). This route is largely along peaceful designated bike/hiking paths that are away from the busy roads, but in some areas it briefly travels along the pavement/sidewalk by the side of a road.</p>
<p>Ideally I'd like to capture this detail in the tagging, preferably in a way that is useful to the various cycle maps. I've had a go at <a href="https://www.openstreetmap.org/?lat=54.96481&amp;lon=-1.65753&amp;zoom=16&amp;layers=M">this section from William Armstrong Drive and along Scotswood Road</a>, which I have currently tagged as follows:</p>
<h2 id="normal-cycle-path">Normal Cycle Path</h2>
<p>The section along the waterfront, away from the road, is simply tagged as most cycle paths are:</p>
<pre><code>highway=cycleway
foot=yes</code></pre>
<h2 id="along-the-pavementsidewalk">Along the Pavement/Sidewalk</h2>
<p>As the route comes up on the pavement alongside William Armstrong Drive and Scotswood Road I've tagged it as:</p>
<pre><code>highway=footway
footway=sidewalk
foot=yes
bicycle=yes</code></pre>
<p>which seems to be about as explicit as I can be.</p>
<h2 id="crossing-the-road">Crossing the Road</h2>
<p>I've also tagged the section where the route crosses the road as:</p>
<pre><code>highway=footway
footway=crossing
cycleway=crossing
foot=yes
bicycle=yes</code></pre>
<p>and drawn that through the <code>highway=crossing</code> node on the road (<a href="https://wiki.openstreetmap.org/wiki/Tag:footway%3Dcrossing">as recommended here</a>)</p>
<p><strong>So does this approach make any sense?</strong><br />
</p>
<p>Logically it seems okay to me, but I'm a bit worried about how it will be interpreted and rendered by existing apps. <em>(Yes I know we should be renderer-agnostic, but I don't want to break a route that used to work correctly)</em>.</p>
<p>Incidentally I can't just add a <code>cycleway=track</code> to the way for the road (as <a href="https://wiki.openstreetmap.org/wiki/Bicycle">suggested in wiki</a>) because unusually the road actually has a cycle lane on it as well (yep, a cycle lane on the road AND a signed shared-use pavement alongside it).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sidewalks" rel="tag" title="see questions tagged &#39;sidewalks&#39;">sidewalks</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '11, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span> </br></p>
</div>
</div>
<div id="comments-container-6320" class="comments-container">
<span id="6324"></span>
<div id="comment-6324" class="comment">
<div id="post-6324-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is likely up for debate, so the wiki or the tagging@ mailing list is probably a better place to ask this.</p>
</div>
<div id="comment-6324-info" class="comment-info">
<span class="comment-age">(15 Jul '11, 13:09)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
<span id="6326"></span>
<div id="comment-6326" class="comment">
<div id="post-6326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <span>@JoshD</span>. I never find anything much gets resolved on the mailing lists :) and I thought if I got some good answers here it might help others in the future (after all how many newbies trawl through all the mailing list archives?)</p>
</div>
<div id="comment-6326-info" class="comment-info">
<span class="comment-age">(15 Jul '11, 14:44)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
</div>
<div id="comment-tools-6320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6320-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="6331"></span>

<div id="answer-container-6331" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6331-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a common problem. I think the consensus is that there is no ideal solution at present, but for those seeking help, rather than discussion, the best compromise is to use a separate way, as you describe. Make sure it is joined to the main way at junctions to aid routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '11, 23:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06004fe865b4475da9d334845acd97ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20reed&#39;s gravatar image" />
<p><span>Peter reed</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter reed has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '11, 00:48</strong> </span></p>
</div>
</div>
<div id="comments-container-6331" class="comments-container">
&#10;</div>
<div id="comment-tools-6331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30562"></span>

<div id="answer-container-30562" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30562-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nowadays, for "along the sidewalk", there is the <a href="https://wiki.openstreetmap.org/wiki/Key:segregated">segregated tag</a>.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '14, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/704f28429974bab1704a7535eb8a5734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgpacker&#39;s gravatar image" />
<p><span>jgpacker</span><br />
<span class="score" title="236 reputation points">236</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgpacker has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-30562" class="comments-container">
&#10;</div>
<div id="comment-tools-30562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30562-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75579"></span>

<div id="answer-container-75579" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75579-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe use semi-colon as the accepted way to add multiple items to a tag and use <code>cycleway=track;lane</code></p>
<p>The Bicycle tagging is mess, it's definitely worth using the wiki or mailing list to find common problems and some way of improving the schema without breaking current contributions.</p>
<p>The wiki list some deviations for UK tagging away from the general cycle tagging, by convention it seems in the UK these shared pavements get mapped as a <code>highway=cycleway, foot=designated, bicycle=designated, segregated=yes</code> despite the wiki saying such a tag is for an off-road cycle-paths, and so in the UK it's (almost) impossible for routing software to tell from tagging if a highway=cyclepath is an off-road cycle path or a roadside pavement. It really feels like there needs to be some sort of tag to indicate it is a pavement but the sidewalk tagging doesn't quite fit right.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Cycling_in_the_United_Kingdom">https://wiki.openstreetmap.org/wiki/Cycling_in_the_United_Kingdom</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '20, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a3b88a2d65ba17d20b29c06c10f0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DevonshireBoy42&#39;s gravatar image" />
<p><span>DevonshireBoy42</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DevonshireBoy42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75579" class="comments-container">
&#10;</div>
<div id="comment-tools-75579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75579-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6353"></span>

<div id="answer-container-6353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6353-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-6353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An alternative way is to have the bike path way merge into the road, then use something like "highway=residential, cycleway=track".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '11, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/75f5707160697b2164444fc3f5054084?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stevage&#39;s gravatar image" />
<p><span>Stevage</span><br />
<span class="score" title="254 reputation points">254</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stevage has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6353" class="comments-container">
<span id="6380"></span>
<div id="comment-6380" class="comment">
<div id="post-6380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Stevage, but as I said the road also has a bike lane, so it already has <code>cycleway=lane</code> on the way for the road.</p>
</div>
<div id="comment-6380-info" class="comment-info">
<span class="comment-age">(17 Jul '11, 22:45)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
</div>
<div id="comment-tools-6353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6353-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6322"></span>

<div id="answer-container-6322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6322-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-6322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This forum is not meant for discussion. So I am tempted to close this question.</p>
<p>However, to give you a short answer I would like to point out that</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Bicycle">https://wiki.openstreetmap.org/wiki/Bicycle</a></p>
<p>covers most options were sidewalks and bicycle lanes meet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '11, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-6322" class="comments-container">
<span id="6325"></span>
<div id="comment-6325" class="comment">
<div id="post-6325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cited that page in the question, but there are problems with the tagging it suggests in this situation. Ref S3 is the closest match, but I can't add <code>cycleway=track</code> to the road as it already has a <code>cycleway=lane</code>. The S3 alternative with multiple ways is good, but it doesn't indicate that these ways are sidewalks which is what I'm trying to achieve.</p>
</div>
<div id="comment-6325-info" class="comment-info">
<span class="comment-age">(15 Jul '11, 14:42)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
<span id="6327"></span>
<div id="comment-6327" class="comment">
<div id="post-6327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I said before: this is a help forum and not a forum for discussion. Please use the wiki or the mailing list instead.</p>
</div>
<div id="comment-6327-info" class="comment-info">
<span class="comment-age">(15 Jul '11, 17:24)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
</div>
<div id="comment-tools-6322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6322-form-container" class="comment-form-container">
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

