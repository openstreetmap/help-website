+++
type = "question"
title = "Should the edges of landuse=* or boundary=* areas share points with streets that form their borders?"
description = '''... especially the when street is a multi-lane divided road? The alternative is, of course, to have the run parallel at the edge of the road. I can see both sides of it. The ways are naturally aligned and in a way are the same, but the trees don&#x27;t extend into the middle of the street.'''
date = "2011-05-24T21:48:00Z"
lastmod = "2021-04-02T03:44:00Z"
weight = 5352
keywords = [ "shared", "boundary", "landuse", "nodes" ]
aliases = [ "/questions/5352" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Should the edges of landuse=\* or boundary=\* areas share points with streets that form their borders?](/questions/5352/should-the-edges-of-landuse-or-boundary-areas-share-points-with-streets-that-form-their-borders)

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
<span id="post-5352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5352-score" class="post-score" title="current number of votes">
14
</div>
<span id="post-5352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>... especially the when street is a multi-lane divided road?</p>
<p>The alternative is, of course, to have the run parallel at the edge of the road. I can see both sides of it. The ways are naturally aligned and in a way are the same, but the trees don't extend into the middle of the street.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shared" rel="tag" title="see questions tagged &#39;shared&#39;">shared</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '11, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/aae1c9884f315f4fc84f7eb02b594a1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Larry%20Butler&#39;s gravatar image" />
<p><span>Larry Butler</span><br />
<span class="score" title="265 reputation points">265</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Larry Butler has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '13, 23:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-5352" class="comments-container">
&#10;</div>
<div id="comment-tools-5352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5352-form-container" class="comment-form-container">
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

<span id="5360"></span>

<div id="answer-container-5360" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5360-score" class="post-score" title="current number of votes">
18
</div>
<span id="post-5360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In short: no. While landuse areas can (and probably should) share nodes with other areas they are touching like the boundary of next landuse area or the riverbank way they should not share nodes with a street. The reason is - as you correctely stated - that the trees don't extend into the middle of the street. Once we start to map streets the same way as rivers that is with a centerline way for routing and and closed boundary way to record extend then landuse areas should probably share nodes with that outer way.</p>
<p>Note however that you should not needlessly change the mapping if a user mapped an area using shared nodes between landuse areas and roads. It's a lot of work which doesn't help much but can introduce a lot of subtile problems.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '11, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-5360" class="comments-container">
<span id="5368"></span>
<div id="comment-5368" class="comment">
<div id="post-5368-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't think you can just answer this with "no"; as Gnonthgol's answer explains, there are pros and cons for both approaches. Still, +1 for a well-reasoned explanation of the possible problems.</p>
</div>
<div id="comment-5368-info" class="comment-info">
<span class="comment-age">(25 May '11, 10:26)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="5369"></span>
<div id="comment-5369" class="comment">
<div id="post-5369-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>yes best to keep nodes separate as changes will mess up other stuff when editing. common nodes can save a little time but can be a real pain later</p>
</div>
<div id="comment-5369-info" class="comment-info">
<span class="comment-age">(25 May '11, 10:27)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5360-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5354"></span>

<div id="answer-container-5354" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5354-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-5354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are different opinions on this, and both methods have advantages and disadvantages. Both methods are "correct", none is "wrong".</p>
<p>A good rule of thumb is:</p>
<ul>
<li>If you know the precice boundaries of the object you are mapping then try to include this in the data.</li>
<li>If you are uncertain of the exact boundary of the object do not make up some arbitrary data.</li>
<li>Respect the work of others.</li>
</ul>
<p>That means that if you for instance are mapping a forest from good arial photos, let the boundary go parallel to the road where you see the forest ending and the road area starting. If you for instance have surveyed the area and know that the forest runs up to the road then let the forest and the road share ways.</p>
<p>If someone else has mapped something using one method, do not switch to the other method unless you are actually editing the are and feel you make the switch in order to carry on with your work.</p>
<p>You should not let several ways share too many nodes as this may become hard to edit; if a long road forms the edge of a forest and you want to re-use the road geometry, create a multipolygon relation for the forest and make the road one of the "outer" members of that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '11, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '11, 22:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-5354" class="comments-container">
<span id="12577"></span>
<div id="comment-12577" class="comment">
<div id="post-12577-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>With the acquired experience, I share the view that shapes should not share other shapes' nodes for further selecting and editing.</p>
<p>Let me share with you my technique: - I first create an area which shares nodes thanks to the Potlach2 "F" shortcut to follow the node. - When I have closed the area, I create a parallel way with the "P" shortcut and move slightly the mouse to get a way very close to the first one - I tag the second area as wanted - I select again the first created area and then delete it - I save the work</p>
<p>Any comment on this?</p>
</div>
<div id="comment-12577-info" class="comment-info">
<span class="comment-age">(06 May '12, 11:01)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
<span id="20924"></span>
<div id="comment-20924" class="comment">
<div id="post-20924-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Excellent procedure for P2 mappers</p>
</div>
<div id="comment-20924-info" class="comment-info">
<span class="comment-age">(22 Mar '13, 23:29)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5354-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20913"></span>

<div id="answer-container-20913" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20913-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, the meadow starts beside the road and not in the middle of it.<br />
In general, the limits of a country do not grow or shrink with the forest.<br />
Etc.<br />
Furthermore people tracing roads and boundaries usually work with a higher degree of precision than landuse which they often meet as long straight lines. No blame but it is unpleasant to have to detach the landuse from everywhere when improving roads.<br />
So, please attach landuse only to landuse and the person who will rework the road will feel like improving your landuse instead of pushing it aside.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '13, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '13, 17:55</strong> </span></p>
</div>
</div>
<div id="comments-container-20913" class="comments-container">
&#10;</div>
<div id="comment-tools-20913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20913-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79412"></span>

<div id="answer-container-79412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79412-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question still seems to be referred to despite its age. The main principle in this matter is to respect the mapping of other users, and that there are numerous different opinions about the correct way of mapping these adjacent features.<br />
In March 2021 the subject of how to map land cover &amp; land use features, in relation to adjacent highways was discussed on talk-gb[<a href="https://lists.openstreetmap.org/pipermail/talk-gb/2021-March/026507.html%5D.">https://lists.openstreetmap.org/pipermail/talk-gb/2021-March/026507.html].</a> There was a wide ranging discussion, but no clear consensus about how the features should be mapped. Where those features border with a highway, the mapper should avoid using shared nodes if possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '21, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5c1291c3e71c45b6c423613714d3eec4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tallguy&#39;s gravatar image" />
<p><span>Tallguy</span><br />
<span class="score" title="96 reputation points">96</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tallguy has one accepted answer">50%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '21, 00:26</strong> </span></p>
</div>
</div>
<div id="comments-container-79412" class="comments-container">
<span id="79488"></span>
<div id="comment-79488" class="comment">
<div id="post-79488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that you can add a road width. That solves the void issue and allows us to map landuse as it actually exists on the ground. Point certainly taken about undoing others' work.</p>
</div>
<div id="comment-79488-info" class="comment-info">
<span class="comment-age">(02 Apr '21, 03:44)</span> <span class="comment-user userinfo">Joel Amos</span>
</div>
</div>
</div>
<div id="comment-tools-79412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21392"></span>

<div id="answer-container-21392" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21392-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-21392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unlike boundaries, landuse should shared nodes with roads.</p>
<p>Boundaries are administrative data, they cannot be surveyed. Both landuse and roads are physical data, which can be acquired via aerial imagery or local survey. Boundaries and roads may share roughly the same shape at low resolution. But looking closer, you may notice the road has little curves, and you want this data in OSM, without modifying the administrative straight boundary. They are not the same nature, they come from different data source, that is why they should not share their nodes.</p>
<p>Now landuse is a physical property that is heavily influenced by roads (in modern countries), because farm tractors and cows will avoid to cross roads, water cannot flow across a road... Landuse and roads should share nodes if landuse is different on each side of the road, because the road IS the limit of the landuse, and you should not duplicate data. This way, if a road shape is refined or adjusted, the landuse will automatically take advantage of it.</p>
<p>It is true that the trees do not extend into the middle of the road. But roads go on top of landuse. If a road runs in the middle of a single landuse, you will not split the landuse in two different areas. And I doubt we will ever map the roads as areas, because unlike riverbanks, roads have pretty constant width.</p>
<p>Mappers working exclusively on streets and roads may be scared by landuse areas stuck to their roads, because area editing is a significantly more complex task than editing a wired network. Just trust the landuse author: if he/she share nodes with you, he/she wants you to edit the area as you edit your road. However, please note that moving nodes along a straight road segment to the next curve, to improve the curve smoothness without "spending" more nodes, is a dangerous shortcut; you would break the attached landuse. It is better to simply add nodes in curves that need smoothing, and delete useless nodes from straight lines.</p>
<p>Selecting objects sharing the same shape is a bit tricky. If nodes are not shared, you can zoom in as far as necessary until ways separate one from another. This will not work if nodes are shared, but this trick is a bad solution anyway. In JOSM, use the middle mouse button, or ALTGR + left click (Linux), or ALT + left click (Windows), to toggle the object selection between possible ways. In Potlach 2, use the "/" key.</p>
<p>Thanks for reading my point of view. Let me stress that anyway you should respect the work of others. My words do not give you permission to merge roads and landuse anywhere you want. If some mappers want to let the road network float freely over the landuse, let them do it this way, and find another area where nobody is working on the landuse (easy to find!).</p>
<p>Happy mapping!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/4bdd5d454f027ac323ec436ba991441c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Le%20Grand%20Blond&#39;s gravatar image" />
<p><span>Le Grand Blond</span><br />
<span class="score" title="79 reputation points">79</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Le Grand Blond has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '13, 08:42</strong> </span></p>
</div>
</div>
<div id="comments-container-21392" class="comments-container">
<span id="21444"></span>
<div id="comment-21444" class="comment">
<div id="post-21444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, the borders of landuse originate historical close to each other. But at a time the farmers agreed to ride or make a road somewhere in between. That road has widened in time from path to track and road. So at the end the road or ditch (area) could or even should be marked / tagged as an area, labeled as traffic, water area or just a way. Mostly maintained by public services and not by the owners of the land, although sometimes its still a private road or stream. So dont connect landuse over a way to the other side across and keep the borders separated. Greetz</p>
</div>
<div id="comment-21444-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 09:51)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="21447"></span>
<div id="comment-21447" class="comment">
<div id="post-21447-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Hendrik, Please have a look at this : <a href="http://osm.kraluvdvur.cz/osm-zahorany-landuse-residential-mapping.png">http://osm.kraluvdvur.cz/osm-zahorany-landuse-residential-mapping.png</a> Do you really prefer B ? Excluding the roads from the landuse is a lot of effort, a lot of extra data, but are those details useful ? A script could easily split the landuse and widen the roads into areas, from their center to their width. We will not run such script, because it would do nothing good but duplicating data. This was discussed here : <a href="/questions/6508/mapping-landuse-residential-and-overlapping-it-by-other-landuse-on-smaller-areas-in-towns">https://help.openstreetmap.org/questions/6508/mapping-landuse-residential-and-overlapping-it-by-other-landuse-on-smaller-areas-in-towns</a></p>
</div>
<div id="comment-21447-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 10:18)</span> <span class="comment-user userinfo">Le Grand Blond</span>
</div>
</div>
<span id="21450"></span>
<div id="comment-21450" class="comment">
<div id="post-21450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi you’re right; I would make an exception for landuse residential, option A. I’m a geographer and don’t mind the amount of data. It should end up into a readable and logic map. I know OSM is in general a database, but I didn’t start contributing to a database but to a map, without any background, silly maybe. A maps still remains a reflection of the past. Greetz</p>
</div>
<div id="comment-21450-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 11:08)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="21453"></span>
<div id="comment-21453" class="comment">
<div id="post-21453-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is not necessary to exclude all roads from landuse areas. If a residential road has houses on both sides, then it makes sense to draw a single landuse area, including the road.</p>
<p>The issue is when there are different types of landuse on each side of the road. If the landuse shares nodes with the road, then you are saying that half of the road is one landuse, and half another.</p>
</div>
<div id="comment-21453-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 11:21)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="21461"></span>
<div id="comment-21461" class="comment">
<div id="post-21461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Vclaw, if your reacting on my comment, like I explained earlier the neighbors agreed to build a way in between they’re properties. Neither of them grows anything in the middle of the road and they kept the road as narrow as possible. So there’s no landuse in crops. In rural areas where the roads had no borders they widened each year. Like it was discussed recently here, how to tag ? Greetz</p>
</div>
<div id="comment-21461-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 12:28)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-21392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21392-form-container" class="comment-form-container">
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

