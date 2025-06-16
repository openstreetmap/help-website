+++
type = "question"
title = "Bridge vs Tunnel?"
description = '''So, how do you decide if a way is a bridge over another way, or if it has a tunnel going under it? Here are some examples, all involving a railway track that&#x27;s a cutting, with roads going over it at various points: Would this be a bridge? It&#x27;s only the width of the road (which in my mind would be to...'''
date = "2011-06-21T21:28:00Z"
lastmod = "2015-04-29T12:29:00Z"
weight = 5934
keywords = [ "tunnel", "bridge", "layer", "level" ]
aliases = [ "/questions/5934" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [Bridge vs Tunnel?](/questions/5934/bridge-vs-tunnel)

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
<span id="post-5934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5934-score" class="post-score" title="current number of votes">
17
</div>
<span id="post-5934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
4
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, how do you decide if a way is a bridge over another way, or if it has a tunnel going under it?</p>
<p>Here are some examples, all involving a railway track that's a cutting, with roads going over it at various points:</p>
<p>Would this be a bridge? It's only the width of the road (which in my mind would be too short for a tunnel), but the road doesn't raise up to go over the railway, as the track is at a lower level..</p>
<p><img src="http://i.imgur.com/0fiMd.png" alt="alt text" /></p>
<hr />
<p>How about this? I thought this made sense being marked as a tunnel, as it's clearly going under various roads, and it's a relatively long section.</p>
<p><img src="http://i.imgur.com/nwUQu.png" alt="alt text" /></p>
<hr />
<p>This seems borderline again.. bridge or tunnel?</p>
<p><img src="http://i.imgur.com/vovrv.png" alt="alt text" /></p>
<hr />
<p>I suppose layers come into this as well don't they? I assume the track should be marked as <code>cutting=yes</code> and <code>layer=-1</code>. The bridge could be explicitly marked as <code>layer=0</code> to signify that there is no change in level as it crosses the other way. Or would that not make sense to do? Should the track just be marked as having a section of tunnel?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-level" rel="tag" title="see questions tagged &#39;level&#39;">level</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '11, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d35ac2d7ba52cccf2e2e41a5cf87c654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sekai&#39;s gravatar image" />
<p><span>Sekai</span><br />
<span class="score" title="291 reputation points">291</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sekai has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '11, 13:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></p>
</img>
</div>
</div>
<div id="comments-container-5934" class="comments-container">
<span id="5938"></span>
<div id="comment-5938" class="comment">
<div id="post-5938-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I always do it on method of construction; therefore, the above three would likely all be bridges. Definitely, 1 and 3 are.... 2 might be considered a cut-and-cover tunnel.... survey might be needed (o;</p>
</div>
<div id="comment-5938-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 01:17)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="5951"></span>
<div id="comment-5951" class="comment">
<div id="post-5951-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I changed level to layer in your post, because the commonly used tag is layer.</p>
<p>actually layer=0 is default and can be avoided (you might still want to use it to emphasize that you didn't simply forget to put it). Layers in OSM don't actually say if something is below or above ground, they only come to play in relation to other objects crossing them: the higher the layer is the higher is the feature in the order of overlapping features.</p>
</div>
<div id="comment-5951-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 13:04)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="25578"></span>
<div id="comment-25578" class="comment">
<div id="post-25578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using bride or tunnel, you can completely get rid of the layers=* They really only play a role if some features cross WITHOUT a bridge or tunnel or if there is more than one bridge/tunnel crossing at the same point. They are only a hint to the renderer what to draw on top and carry no other meaning in terms of height. But for bridges/tunnels, the renderer already knows what to do.</p>
</div>
<div id="comment-25578-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 16:18)</span> <span class="comment-user userinfo">Chaos99</span>
</div>
</div>
<span id="25588"></span>
<div id="comment-25588" class="comment">
<div id="post-25588-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>youll get a complaint adding a bridge over a way, without a tag layer 1 or -1.</p>
</div>
<div id="comment-25588-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 21:56)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-5934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5934-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="6484"></span>

<div id="answer-container-6484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6484-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-6484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/user/Harry%20Wood/diary/14067">Down the pub one time</a> we suggested the simple rule: <em>"If the road passing under is longer (underneath) than the gap is wide, then it should be a tunnel on the under way, rather than a bridge on the over way."</em> ....But we were all completely drunk at the time :-)</p>
<p>By that rule I'd say your second and third images are both tunnels (and that is how I would map them), but your first one is 50/50. Could be a bridge. See comments on my diary for some further discussion. I've also just added a <a href="https://wiki.openstreetmap.org/wiki/Key:bridge#Bridge_vs_Tunnel">specific section to the wiki</a> where we should one day answer this question.<br />
<strong><em>[update] :</em></strong> The wiki page was modified to carry some more specific advice, which is good I guess. See <a href="https://wiki.openstreetmap.org/wiki/Talk:Key:bridge#Bridge_vs_Tunnels">the discussion here</a></p>
<p>But on the whole I agree with Vincent de Phily. If you have a case where you can't decide between bridge or tunnel... well then it probably doesn't matter too much. Getting levels right matters more (mainly to help the renderers). Avoiding connections where there are none is important (To avoid routing problems)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '11, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '12, 13:51</strong> </span></p>
</div>
</div>
<div id="comments-container-6484" class="comments-container">
&#10;</div>
<div id="comment-tools-6484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5943"></span>

<div id="answer-container-5943" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5943-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-5943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's always going to be a little subjective. To me the presence/absence of a slope on the top/bottom highway doesn't make a difference. The construction type is tempting, but I can see many cases were it will not yield a definite answer. I'd say if the bottom highway crosses a single feature (however broad the feature may be) it's a bridge, otherwise it's a tunnel. So I'd rate your 1&amp;3 as bridges, 2 as tunnel.</p>
<p>YMMV. In the end it's not a big issue, the main thing is to have no connectiing nodes and to have the layers right.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '11, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-5943" class="comments-container">
<span id="5945"></span>
<div id="comment-5945" class="comment">
<div id="post-5945-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>+1 The difference between tunnel and bridge is really somewhat arbitrary, and not really important for most applications. The important thing (especially for routing) is to use <span><code>layer</code></span>s (because that indicates that it's not a level crossing). If it's ambiguous, just choose one; the rule of thumb given looks fine.</p>
</div>
<div id="comment-5945-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 11:29)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="42681"></span>
<div id="comment-42681" class="comment">
<div id="post-42681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, in my comment above "levels" should have been "layers", as that is the right tag to use.</p>
</div>
<div id="comment-42681-info" class="comment-info">
<span class="comment-age">(29 Apr '15, 12:21)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="42683"></span>
<div id="comment-42683" class="comment">
<div id="post-42683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/666/sleske">@sleske</a>: I've edited it – better now? :-) Then please delete your and my (this) comment.</p>
</div>
<div id="comment-42683-info" class="comment-info">
<span class="comment-age">(29 Apr '15, 12:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5943-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5950"></span>

<div id="answer-container-5950" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5950-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-5950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Technically these structures are all bridges (because not dug in the massive earth but constructed openly and then later covered, and not longer then 80 / 160 metres). I would still tag 1 and 3 as bridge and 2 might be better represented as tunnel in osm (because otherwise you would miss the start and end of the covered part of the way, and you might end up with lots of parallel bridges what I would consider a worse representation compared to a simple tunnel for the way below).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '11, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-5950" class="comments-container">
<span id="6183"></span>
<div id="comment-6183" class="comment">
<div id="post-6183-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>+1 good point about the "multiple parallel bridges". That's something that often bothers me with OSM renderings.</p>
</div>
<div id="comment-6183-info" class="comment-info">
<span class="comment-age">(06 Jul '11, 02:10)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="6679"></span>
<div id="comment-6679" class="comment">
<div id="post-6679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd agree they are all bridges. Surely a tunnel implies tunneling through some sort of natural feature?</p>
</div>
<div id="comment-6679-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 00:04)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="32802"></span>
<div id="comment-32802" class="comment">
<div id="post-32802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I solved the paralel bridges with highway areas &amp; railway areas. Then went on to map road widths with areas too. The routeing lines stay to as they are linked and tagged like in comercial products to aid simplifed routing algorithiums.</p>
</div>
<div id="comment-32802-info" class="comment-info">
<span class="comment-age">(01 May '14, 21:50)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-5950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5950-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5939"></span>

<div id="answer-container-5939" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5939-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Imagery is not the main way data should ideally be collected for OSM, ground surveying is.</p>
<p>The best way to get data into OSM is to go to the place and check it out. Take your GPS with you, collect tracks, make observations.</p>
<p>If you want to know if it's a bridge or a tunnel, head over there and check it out.</p>
<p>If it's not near you, then focus on what is! You should be mapping what's local to you, what you can observe yourself, and use the imagery as a backup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '11, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-5939" class="comments-container">
<span id="5944"></span>
<div id="comment-5944" class="comment">
<div id="post-5944-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>While what you say is true, it's offtopic I think. Going on-site probably won't make things clearer in this case. For all we know, the OP might have been on-site and know the area well, but used aerial imagery to illustrate his question.</p>
</div>
<div id="comment-5944-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 10:58)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="5948"></span>
<div id="comment-5948" class="comment">
<div id="post-5948-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You hit the nail on the head Vincent. Thanks for the advice though emacsen!</p>
</div>
<div id="comment-5948-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 12:03)</span> <span class="comment-user userinfo">Sekai</span>
</div>
</div>
<span id="32799"></span>
<div id="comment-32799" class="comment">
<div id="post-32799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I try to to do this mostly seeing the site and possibly taking down notes before using the corrected offset satelight/arial pics to line things up at a drawing out stage. Sometimes when I try using JOSM with no internet and no imagry my attempts are delibratly errored to make it more obvious that the fetures like building outlines still need correction. Still I'd still be pondering after having stared at a long overbridge about this issue.</p>
</div>
<div id="comment-32799-info" class="comment-info">
<span class="comment-age">(01 May '14, 21:20)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-5939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5939-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6488"></span>

<div id="answer-container-6488" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6488-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alas even knowing the structure may still be ambiguous, a cut and cover tunnel is in essence a very wide bridge. Adding to the abiguity are some larger culverts which typically I'd consider a tunnel, but some may consider a bridge</p>
<p><a href="http://www.dot.state.oh.us/Divisions/Communications/BridgingtheGap/PublishingImages/box-culvert.jpg">http://www.dot.state.oh.us/Divisions/Communications/BridgingtheGap/PublishingImages/box-culvert.jpg</a> <a href="http://utca.eng.ua.edu/projects/final_reports/00219report_files/image106.jpg">http://utca.eng.ua.edu/projects/final_reports/00219report_files/image106.jpg</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '11, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/f6827fbcbfc77428dfb7f8743ab775db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sundance&#39;s gravatar image" />
<p><span>Sundance</span><br />
<span class="score" title="467 reputation points">467</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sundance has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-6488" class="comments-container">
<span id="6682"></span>
<div id="comment-6682" class="comment">
<div id="post-6682-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>So you're saying most of the NYC subway isn't really underground, the street above is just a bridge?</p>
</div>
<div id="comment-6682-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 07:18)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="6683"></span>
<div id="comment-6683" class="comment">
<div id="post-6683-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cut and cover constructions are technically considered tunnels if they are very long (e.g. at least 80m in Germany, 160m in the USA). I'd consider the box culvert in your first image a bridge.</p>
</div>
<div id="comment-6683-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 08:44)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="6885"></span>
<div id="comment-6885" class="comment">
<div id="post-6885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No I'm saying the construction techniques for a some cut and cover tunnel can be identical to a bridge. A good example of this would be the Seattle freeway lids on Mercer Island and soon to be on State Route 520.</p>
<p>The longer curved one, okay tunnel, the shorter ones, bridge or tunnel is more ambiguous <a href="https://www.openstreetmap.org/?lat=47.5881&amp;lon=-122.23165&amp;zoom=15&amp;layers=M">https://www.openstreetmap.org/?lat=47.5881&amp;lon=-122.23165&amp;zoom=15&amp;layers=M</a></p>
<p>And yes I would map a cut and cover tunnel as a tunnel. There is some vagueness in some wider bridges as in this example, or in some culverts.</p>
</div>
<div id="comment-6885-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 17:10)</span> <span class="comment-user userinfo">Sundance</span>
</div>
</div>
<span id="32801"></span>
<div id="comment-32801" class="comment">
<div id="post-32801-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cut and covers are very common for underpasses and metros alike seem bottom catch all solution.</p>
</div>
<div id="comment-32801-info" class="comment-info">
<span class="comment-age">(01 May '14, 21:43)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-6488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6477"></span>

<div id="answer-container-6477" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These should all be tagged as bridges, because they are bridges. Don't tag something as a tunnel just because it looks nicer in mapnik.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '11, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0ae71d66eba9ad7437196ee1d689295f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Janjko&#39;s gravatar image" />
<p><span>Janjko</span><br />
<span class="score" title="323 reputation points">323</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Janjko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6477" class="comments-container">
&#10;</div>
<div id="comment-tools-6477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32800"></span>

<div id="answer-container-32800" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32800-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-32800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>if your simply maping a single line for a route then on the over route put a bridge section across all the apans in one (unless a bank (like an earth bank) is used between spans). Then on the other route mark it as a tunnel from the point it passes under to the point it emerges. add appropiate elevation higt and level tags to fit with surounds such as buildings with indor and basement level features etc.</p>
<p>In this way the fact that the tunnel is very short under the bridge is recorded and the systems can easily handle the relationships to their own needs.</p>
<p>The use of level tags is important idealy if the bridge went over flat across a cutting it would fair to say that the level was 0 (or the same as the reast of the line for elevated routes espcially relating to urban buildings with indoor level plans [think more of a ubrban scape with roads raised off the ground and interacting with the upper floors of buildings possibly with entrances or by passing through them entirly enveloped for a stretch).</p>
<p>I'd consider a higher level (and elevation hight) either for midway nodes or bridge line sections if it were hump-backed [a bridge whose over path rises to get above and over a suporting arch] and for simlar varient cases].</p>
<p>Its worth noteing this helps when handleing [automaticly] complex transport junctions with stacked bridges and viaducted canals snd railways passing over and under each other in a small area like in Brimingham Britain.</p>
<hr />
<p><img src="/upfiles/Untitled4.jpg" alt="Spegetti-junction on the M6 at Birmingham, UK, EU." /> This example shows arange of moterways mainroads cyclepths local road and rregional distributer roads Weaving link roads and canals rivers and railway services.</p>
<p>Even before railways birmingham had similar major junctions on the canal system complete with aquduct overpasses and lock-ed link routes to ease the heavy barge traffic!</p>
<p>Sticking to one level may be difficult. Ireality they are built with undulating bridges with some of the older routes in cuttings tunnels and embankments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '14, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '14, 19:16</strong> </span></p>
</div>
</div>
<div id="comments-container-32800" class="comments-container">
<span id="32817"></span>
<div id="comment-32817" class="comment">
<div id="post-32817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li><p>Don't mark both a tunnel and bridge unless there really is a bridge crossing above a tunnel, which would be exceedingly rare. In nearly all cases it's one or the other, but not both.</p></li>
<li><p>Don't tag different parts of a bridge with different layer tags just because it's hump-backed. That isn't what the layer tag is for. It's only for determining the relative position of objects (ie. one object passes above another), not for any kind of elevation change. If one bridge is crossing one other way, the entire bridge should have a layer one step higher than the way underneath.</p></li>
</ol>
</div>
<div id="comment-32817-info" class="comment-info">
<span class="comment-age">(02 May '14, 17:01)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="32880"></span>
<div id="comment-32880" class="comment">
<div id="post-32880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>probably fair enough about a basic humpback and levels but when link road weave up and down as they pass it could be tough to keep to one level. I think I had other cases in mind like elevated and undground service that have connections to buildings at that aren't at ground level like in soul corea.</p>
<p>for isea of the weaveing I'll append an image to the main answer.</p>
</div>
<div id="comment-32880-info" class="comment-info">
<span class="comment-age">(05 May '14, 19:07)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
<span id="32881"></span>
<div id="comment-32881" class="comment">
<div id="post-32881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Govanus</span> please stop reopening extremly old questions</p>
</div>
<div id="comment-32881-info" class="comment-info">
<span class="comment-age">(05 May '14, 19:30)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="32892"></span>
<div id="comment-32892" class="comment">
<div id="post-32892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It doesn't matter if a link road weaves up and down. The physical shape of the road has no relation to the layer tag. The layer tag only indicates the vertical relationship between two crossing ways. That is, it simply indicates one way passes above or under another. Nothing more, nothing less. If you want to represent the changing physical height of a road, the ele=* tag is what you want.</p>
</div>
<div id="comment-32892-info" class="comment-info">
<span class="comment-age">(06 May '14, 00:20)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-32800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32800-form-container" class="comment-form-container">
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

